from detectors.restart_detector import restart_detected
from detectors.pod_detector import pod_status_detected
from detectors.container_detector import container_state_detected
from detectors.event_detector import event_detected
from k8s.client import get_pod_events

def detect_incidents(
    pod,
    known_restarts,
):
    """
    Execute all detection logic and return
    the detected incidents.
    """

    incidents = []

    if not pod.status.container_statuses:
        return incidents

    status = pod.status.container_statuses[0]
    incidents.extend(
       container_state_detected(
            status
        )
    )

    pod_name = pod.metadata.name
    
    # =====================================
    # Kubernetes Events
    # =====================================

    events = get_pod_events(
        pod_name
    )

    incidents.extend(

        event_detected(
            events
        )

    )   

    restart_count = status.restart_count

    # Restart Detection

    if restart_detected(
        known_restarts,
        pod_name,
        restart_count,
    ):

        incidents.append(
            {
                "type": "Pod Restart",
                "reason": "Restart Count Increased",
            }
        )

    # Pod Phase Detection

    unhealthy, phase = pod_status_detected(
        pod
    )

    if unhealthy:

        incidents.append(
            {
                "type": "Pod Status",
                "reason": phase,
            }
        )

    return incidents
