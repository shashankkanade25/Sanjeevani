def pod_status_detected(pod):
    """
    Detect unhealthy pod phases.
    """

    unhealthy_phases = [
        "Pending",
        "Failed",
        "Unknown",
    ]

    phase = pod.status.phase

    if phase in unhealthy_phases:

        return True, phase

    return False, phase
