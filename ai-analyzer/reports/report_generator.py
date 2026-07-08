import datetime


def save_report(
    pod_name,
    incident_type,
    report_text,
):
    """
    Save incident report to the mounted PVC.
    """

    timestamp = datetime.datetime.now().strftime(
        "%Y%m%d-%H%M%S"
    )

    filename = (
        f"/reports/incident-{timestamp}.txt"
    )

    with open(
        filename,
        "w",
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
        flush=True,
    )


def print_incident_report(
    pod_name,
    report_text,
):
    """
    Print formatted incident report to stdout.
    """

    print()
    print("=" * 80)
    print("🚨 SANJEEVANI INCIDENT REPORT")
    print("=" * 80)

    print()

    print(f"📦 Pod               : {pod_name}")

    print(
        f"📅 Time              : "
        f"{datetime.datetime.now().strftime('%d-%b-%Y %H:%M:%S')}"
    )

    print()

    print("📋 INCIDENT SUMMARY")
    print("-" * 80)

    print()

    for line in report_text.splitlines():

        if line.startswith("Status:"):

            print(
                "✔ "
                + line.replace(
                    "Status:",
                    "Status            :",
                )
            )
            print()

        elif line.startswith("Severity:"):

            print(
                "✔ "
                + line.replace(
                    "Severity:",
                    "Severity          :",
                )
            )
            print()

        elif line.startswith("Root Cause:"):

            print(
                "✔ "
                + line.replace(
                    "Root Cause:",
                    "Root Cause        :",
                )
            )
            print()

        elif line.startswith("Impact:"):

            print(
                "✔ "
                + line.replace(
                    "Impact:",
                    "Impact            :",
                )
            )
            print()

        elif line.startswith("Recommended Fix:"):

            print(
                "✔ "
                + line.replace(
                    "Recommended Fix:",
                    "Recommended Fix   :",
                )
            )
            print()

        elif line.startswith("Confidence:"):

            print(
                "✔ "
                + line.replace(
                    "Confidence:",
                    "Confidence        :",
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
