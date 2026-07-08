import time

from k8s.client import list_pods


def verify_recovery(
    deployment_name="self-healing-app",
    namespace="self-healing",
):
    """
    Verify whether the application recovered
    after remediation.
    """

    print(
        "\nVerifying Recovery...",
        flush=True,
    )

    time.sleep(15)

    pods = list_pods(namespace)

    for pod in pods.items:

        if deployment_name in pod.metadata.name:

            phase = pod.status.phase

            if phase == "Running":

                print(
                    "Recovery Successful",
                    flush=True,
                )

                return True

    print(
        "Recovery Failed",
        flush=True,
    )

    return False
