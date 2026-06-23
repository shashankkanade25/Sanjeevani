import os
import time
import datetime

from dotenv import load_dotenv

from kubernetes import client, config

import google.generativeai as genai

# =====================================
# Gemini Setup
# =====================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# =====================================
# Kubernetes Setup
# =====================================

config.load_incluster_config()

v1 = client.CoreV1Api()

apps_v1 = client.AppsV1Api()

print(
    "AI Analyzer Started",
    flush=True
)

# =====================================
# Track Restart Counts
# =====================================

known_restarts = {}

# =====================================
# Save Report
# =====================================

def save_report(
    pod_name,
    incident_type,
    report_text
):

    timestamp = (
        datetime.datetime.now()
        .strftime("%Y%m%d-%H%M%S")
    )

    filename = (
        f"/reports/incident-{timestamp}.txt"
    )

    with open(
        filename,
        "w"
    ) as report:

        report.write(
            "AI INCIDENT REPORT\n\n"
        )

        report.write(
            f"Timestamp: {timestamp}\n"
        )

        report.write(
            f"Pod: {pod_name}\n"
        )

        report.write(
            f"Incident Type: {incident_type}\n\n"
        )

        report.write(
            report_text
        )

    print(
        f"\nIncident saved: {filename}",
        flush=True
    )

# =====================================
# Self-Healing Action
# =====================================

def restart_application():

    try:

        apps_v1.patch_namespaced_deployment(

            name="self-healing-app",

            namespace="self-healing",

            body={
                "spec": {
                    "template": {
                        "metadata": {
                            "annotations": {
                                "restarted-at": str(
                                    time.time()
                                )
                            }
                        }
                    }
                }
            }
        )

        print(
            "\nSELF-HEALING ACTION EXECUTED",
            flush=True
        )

        print(
            "Deployment restarted successfully",
            flush=True
        )

    except Exception as e:

        print(
            f"Restart Failed: {e}",
            flush=True
        )

# =====================================
# Gemini Analysis
# =====================================

def analyze_logs(
    pod_name,
    incident_type,
    logs
):

    print(
        "\nAnalyzing logs with Gemini...",
        flush=True
    )

    prompt = f"""
You are a Senior Site Reliability Engineer.

Incident Type:
{incident_type}

Analyze the Kubernetes logs below.

Provide:

1. Root Cause
2. Severity
3. Impact
4. Recommended Fix
5. Confidence Score
6. Recommended Kubernetes Action

Logs:

{logs}
"""

    response = model.generate_content(
        prompt
    )

    print("\n")
    print("=" * 80)
    print("AI INCIDENT REPORT")
    print("=" * 80)
    print(response.text)

    save_report(
        pod_name,
        incident_type,
        response.text
    )

# =====================================
# Main Loop
# =====================================

while True:

    try:

        pods = v1.list_namespaced_pod(
            namespace="self-healing"
        )

        print(
            "\nChecking Pods...",
            flush=True
        )

        for pod in pods.items:

            if not pod.status.container_statuses:
                continue

            pod_name = (
                pod.metadata.name
            )

            status = (
                pod.status.container_statuses[0]
            )

            restart_count = (
                status.restart_count
            )

            old_count = (
                known_restarts.get(
                    pod_name,
                    restart_count
                )
            )

            print(
                f"{pod_name} restarts={restart_count}",
                flush=True
            )

            # =====================================
            # CrashLoopBackOff Detection
            # =====================================

            try:

                state = status.state

                if (
                    state.waiting
                    and state.waiting.reason
                    == "CrashLoopBackOff"
                ):

                    print(
                        f"\nCRASHLOOPBACKOFF DETECTED: {pod_name}",
                        flush=True
                    )

            except:
                pass

            # =====================================
            # Restart Detection
            # =====================================

            if restart_count > old_count:

                print(
                    f"\nNEW RESTART DETECTED: {pod_name}",
                    flush=True
                )

                try:

                    logs = (
                        v1.read_namespaced_pod_log(
                            name=pod_name,
                            namespace="self-healing",
                            previous=True,
                            tail_lines=50
                        )
                    )

                    analyze_logs(
                        pod_name,
                        "Pod Restart",
                        logs
                    )

                    restart_application()

                except Exception as e:

                    print(
                        f"\nAnalysis Failed: {e}",
                        flush=True
                    )

            known_restarts[
                pod_name
            ] = restart_count

        time.sleep(30)

    except Exception as e:

        print(
            f"Loop Error: {e}",
            flush=True
        )

        time.sleep(30)
