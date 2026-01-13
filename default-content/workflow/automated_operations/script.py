# function to get the initial status of incident
def start():
    return "assigned"


# function to know steps after current status
def workflow():
    return {"assigned": ["ongoing", "Completed"], "ongoing": ["assigned", "Completed"]}


# function to know when the incident is completed
def end():
    return "Completed"