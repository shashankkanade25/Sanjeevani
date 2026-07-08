def select_action(incident):

    incident_type = incident["type"]
    reason = incident["reason"]

    # Restart Count
    if incident_type == "Pod Restart":

        return "restart"

    # CrashLoopBackOff
    if (
        incident_type == "Container Waiting"
        and reason == "CrashLoopBackOff"
    ):

        return "restart"

    # OOMKilled
    if (
        incident_type == "Container Terminated"
        and reason == "OOMKilled"
    ):

        return "increase_memory"

    # Image Pull Failure
    if (
        incident_type == "Kubernetes Event"
        and reason == "ImagePullBackOff"
    ):

        return "notify"

    # Pending Pod
    if incident_type == "Pod Status":

        return "monitor"

    return "none"
