def calculate_coefficient_risk(injury_history):
    """
    Name:
        calculate_coefficient_risk

    Parameters:
        injury_history (dict): A dictionary where each key is a player's name (str) and the value is a dictionary
                               containing a list of injuries. Each injury is represented as a dictionary with the following attributes:
                               - date (str)
                               - injury_type (str)
                               - recovery_time (int, in days)
                               - severity (str)
                               - minutes_played (int)
                               - recurrent (str: "Yes" or "No")

    Description:
        Calculates a risk coefficient for each player based on their injury history. The formula used is:
        Risk Coefficient = (Total Injuries * Severity Weight) + (Recurrent Injuries * Recurrence Weight) + (Average Recovery Time / 10)

    Expected Output:
        dict: A dictionary where each key is a player's name (str) and the value is their calculated risk coefficient (float).

    Example Output:
        {
            'Marc-André ter Stegen': 45.6,
            'Iñaki Peña': 22.3,
            ...
        }
    """
    # Define severity weights
    severity_weights = {
        "Mild": 1,
        "Moderate": 2,
        "Severe": 3
    }
    recurrence_weight = 2  # Weight for recurrent injuries

    risk_coefficients = {}

    for player, data in injury_history.items():
        injuries = data['injuries']
        total_injuries = len(injuries)
        total_severity_weight = 0
        total_recovery_time = 0
        recurrent_injuries = 0

        for injury in injuries:
            severity = injury['severity']
            recovery_time = injury['recovery_time']
            recurrent = injury['recurrent']

            # Add severity weight
            total_severity_weight += severity_weights.get(severity, 0)

            # Add recovery time
            total_recovery_time += recovery_time

            # Count recurrent injuries
            if recurrent == "Yes":
                recurrent_injuries += 1

        # Calculate average recovery time
        average_recovery_time = total_recovery_time / total_injuries if total_injuries > 0 else 0

        # Calculate risk coefficient
        risk_coefficient = (
            (total_injuries * total_severity_weight) +
            (recurrent_injuries * recurrence_weight) +
            (average_recovery_time / 10)
        )

        # Store the result in the dictionary
        risk_coefficients[player] = round(risk_coefficient, 2)

    return risk_coefficients