def event_detected(events):
    """
    Detect important Kubernetes events.
    """

    incidents = []

    interesting_events = {

        "BackOff",

        "Failed",

        "FailedScheduling",

        "ImagePullBackOff",

        "ErrImagePull",

        "OOMKilled",

        "Evicted",

    }

    for event in events.items:

        reason = event.reason

        if reason in interesting_events:

            incidents.append(

                {
                    "type": "Kubernetes Event",
                    "reason": reason,
                }

            )

    return incidents
