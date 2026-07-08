def choose_action(incident):
    """
    Decide how Sanjeevani should respond
    to a detected incident.
    """

    actions = {

        "Pod Restart": {
            "action": "restart_deployment",
            "analyze": True,
        },

        "Pod Status": {
            "action": "monitor",
            "analyze": False,
        },

    }

    return actions.get(

        incident["type"],

        {
            "action": "none",
            "analyze": False,
        },

    )
