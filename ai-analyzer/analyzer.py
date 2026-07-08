import time

from engine.detection_engine import detect_incidents

from remediation.remediator import restart_application

from reports.report_generator import (
    print_incident_report,
    save_report,
)

from k8s.client import (
    list_pods,
    get_previous_logs,
)

from ai.gemini import analyze_logs as gemini_analyze


print(
    "AI Analyzer Started",
    flush=True
)

# =====================================
# Track Restart Counts
# =====================================

known_restarts = {}

# =====================================
# Process Incident
# =====================================

def process_incident(
    pod_name,
    incident_type,
    logs,
):

    response_text = gemini_analyze(logs)

    print_incident_report(
        pod_name,
        response_text,
    )

    save_report(
        pod_name,
        incident_type,
        response_text,
    )


# =====================================
# Main Loop
# =====================================

while True:

    try:

        pods = list_pods()

        print(
            "\nChecking Pods...",
            flush=True
        )

        for pod in pods.items:

            pod_name = pod.metadata.name

            incidents = detect_incidents(
                pod,
                known_restarts,
            )

            if not incidents:
                continue

            for incident in incidents:

                print(
                    f"\nINCIDENT DETECTED : {incident['type']}",
                    flush=True,
                )

                print(
                    f"Reason            : {incident['reason']}",
                    flush=True,
                )

                if incident["type"] == "Pod Restart":

                    try:

                        logs = get_previous_logs(
                            pod_name=pod_name,
                        )

                        process_incident(
                            pod_name,
                            incident["type"],
                            logs,
                        )

                        restart_application()

                    except Exception as e:

                        print(
                            f"\nAnalysis Failed: {e}",
                            flush=True,
                        )

        time.sleep(30)

    except Exception as e:

        print(
            f"Loop Error: {e}",
            flush=True,
        )

        time.sleep(30)
