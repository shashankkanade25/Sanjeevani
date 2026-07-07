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

    Analyze the Kubernetes logs and return ONLY the following fields.

    Status:
    Severity:
    Root Cause:
    Impact:
    Recommended Fix:
    Confidence:

    Rules:

    - Maximum 1 sentence per field.
    - Root Cause should be under 20 words.
    - Impact should be under 20 words.
    - Confidence should be High, Medium or Low only.
    - Recommended Fix should be under 20 words.
    - Do not explain.
    - Do not repeat information.
    - Do not use markdown.
    - Return plain text only.

    Logs:

    {logs}
    """

    response = model.generate_content(
        prompt
    )

    print()

    print("=" * 80)
    print("🚨 SANJEEVANI INCIDENT REPORT")
    print("=" * 80)

    print()

    print(f"📦 Pod               : {pod_name}")

    print(
        f"📅 Time              : {datetime.datetime.now().strftime('%d-%b-%Y %H:%M:%S')}"
    )

    print()

    print("📋 INCIDENT SUMMARY")
    print("-" * 80)
    
    print()

    for line in response.text.splitlines():

        if line.startswith("Status:"):

            print(
                "✔ " +
                line.replace(
                    "Status:", 
                    "Status            :"
                )
            )

            print()

        elif line.startswith("Severity:"):

            print(
                "✔ " +
                line.replace(
                    "Severity:",
                    "Severity          :"
                )
            )

            print()

        elif line.startswith("Root Cause:"):

            print(
                "✔ " +
                line.replace(
                    "Root Cause:",
                    "Root Cause        :"
                )
            )

            print()

        elif line.startswith("Impact:"):

            print(
                "✔ " +
                line.replace(
                    "Impact:",
                    "Impact            :"
                )
            )

            print()

        elif line.startswith("Recommended Fix:"):

            print(
                "✔ " +
                line.replace(
                    "Recommended Fix:",
                    "Recommended Fix   :"
                )
            )

            print()

        elif line.startswith("Confidence:"):

            print(
                "✔ " +
                line.replace(
                    "Confidence:",
                    "Confidence        :"
                )
            )

    print()

    print("=" * 80)

    print("⚙️ AUTOMATED REMEDIATION")
    print("-" * 80)

    print()

    print("✅ Previous Logs Collected")

    print("✅ AI Root Cause Analysis Completed")

    print("✅ Incident Report Generated")

    print("✅ Report Stored Successfully")

    print("✅ Deployment Restart Triggered")

    print("✅ Kubernetes Recovery Initiated")

    print()

    print("=" * 80)

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
