def container_state_detected(status):
    """
    Detect unhealthy container states.
    Returns a list of detected incidents.
    """

    incidents = []

    state = status.state

    # Waiting State
    if state.waiting:

        incidents.append(
            {
                "type": "Container Waiting",
                "reason": state.waiting.reason,
            }
        )

    # Terminated State
    if state.terminated:

        incidents.append(
            {
                "type": "Container Terminated",
                "reason": state.terminated.reason,
            }
        )

    return incidents
