def select_action(incident):

    actions = {

        "Pod Restart": "restart",

        "Container Waiting": "restart",

        "Container Terminated": "analyze",

        "Kubernetes Event": "analyze",

        "Pod Status": "monitor",

    }

    return actions.get(
        incident["type"],
        "none",
    )
