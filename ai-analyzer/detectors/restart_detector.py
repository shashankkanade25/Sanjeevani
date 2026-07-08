def restart_detected(
    known_restarts,
    pod_name,
    restart_count,
):
    """
    Detect whether a pod restart has occurred.
    """

    previous_count = known_restarts.get(
        pod_name,
        restart_count,
    )

    known_restarts[pod_name] = restart_count

    return restart_count > previous_count
