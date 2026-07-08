from kubernetes import client, config

# =====================================
# Kubernetes Client
# =====================================

config.load_incluster_config()

v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()


def list_pods(namespace="self-healing"):
    """
    Return all pods in the namespace.
    """
    return v1.list_namespaced_pod(namespace=namespace)


def get_previous_logs(
    pod_name,
    namespace="self-healing",
    tail_lines=50,
):
    """
    Fetch logs from the previous crashed container.
    """
    return v1.read_namespaced_pod_log(
        name=pod_name,
        namespace=namespace,
        previous=True,
        tail_lines=tail_lines,
    )


def restart_deployment(
    deployment_name="self-healing-app",
    namespace="self-healing",
):
    """
    Trigger a rolling restart by updating a pod template annotation.
    """
    return apps_v1.patch_namespaced_deployment(
        name=deployment_name,
        namespace=namespace,
        body={
            "spec": {
                "template": {
                    "metadata": {
                        "annotations": {
                            "restarted-at": __import__("time").ctime()
                        }
                    }
                }
            }
        },
    )
