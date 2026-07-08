from k8s.client import restart_deployment


def restart_application():
    """
    Execute the current Version 1 remediation:
    Restart the Kubernetes Deployment.
    """

    try:

        restart_deployment()

        print(
            "\nSELF-HEALING ACTION EXECUTED",
            flush=True,
        )

        print(
            "Deployment restarted successfully",
            flush=True,
        )

    except Exception as e:

        print(
            f"Restart Failed: {e}",
            flush=True,
        )
