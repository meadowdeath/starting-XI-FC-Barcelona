def calculate_age_risk(players):
    """
    Name:
        calculate_age_risk

    Parameters:
        players (dict): A dictionary where each key is a player's name (str) and the value is another dictionary
                        containing the player's attributes:
                        {
                            'number': int,
                            'age': int,
                            'positions': list
                        }

    Description:
        Calculates an age-based risk coefficient for each player based on their age group. The risk values are:
            - Age < 20: Risk = 1.5
            - 20 <= Age <= 25: Risk = 1.2
            - 26 <= Age <= 30: Risk = 1.0
            - 31 <= Age <= 35: Risk = 1.3
            - Age > 35: Risk = 1.7

    Expected Output:
        dict: A dictionary where each key is a player's name (str) and the value is their calculated age risk coefficient (float).

    Example Output:
        {
            'Marc-André ter Stegen': 1.3,
            'Iñaki Peña': 1.2,
            ...
        }
    """
    # Define age risk values
    age_risk_values = {
        "under_20": 1.5,
        "20_to_25": 1.2,
        "26_to_30": 1.0,
        "31_to_35": 1.3,
        "over_35": 1.7
    }

    age_risks = {}

    for player, attributes in players.items():
        age = attributes['age']

        # Determine the risk value based on age
        if age < 20:
            risk = age_risk_values["under_20"]
        elif 20 <= age <= 25:
            risk = age_risk_values["20_to_25"]
        elif 26 <= age <= 30:
            risk = age_risk_values["26_to_30"]
        elif 31 <= age <= 35:
            risk = age_risk_values["31_to_35"]
        else:  # age > 35
            risk = age_risk_values["over_35"]

        # Store the player's name and their age risk coefficient in the dictionary
        age_risks[player] = risk

    return age_risks