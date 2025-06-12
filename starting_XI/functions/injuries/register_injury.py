from functions.injuries.update_injury_history import update_injury_history

def register_injury(players, injury_history_file):
    """
    Name:
        register_injury

    Parameters:
        players (dict): 
            Dictionary containing player information. Each key is the player's name, and the value is a dictionary 
            with attributes such as the player's jersey number.
        injury_history_file (str): 
            Path to the `injury_history.txt` file where the injury data will be stored.

    Description:
        This function allows the user to register a new injury for a specific player. The process includes:
        - Displaying a list of players with their jersey numbers.
        - Allowing the user to select the injured player by entering their jersey number.
        - Prompting the user to input detailed information about the injury, including:
            - Date of the injury (YYYY-MM-DD).
            - Name or description of the injury.
            - Recovery time in days.
            - Severity of the injury (Mild, Moderate, Severe).
            - Minutes played by the player before the injury.
            - Whether the injury is a recurrence (Yes/No).
        - Creating a dictionary with the injury details.
        - Calling the `update_injury_history` function to save the injury data in the `injury_history.txt` file.

    Expected Output:
        None: The function updates the `injury_history.txt` file with the new injury data.

    Example:
        Given the following `players` dictionary:
        ```
        players = {
            "Marc-André ter Stegen": {"number": 1},
            "Lamine Yamal": {"number": 19},
            "Robert Lewandowski": {"number": 9}
        }
        ```

        And the following `injury_history.txt` file:
        ```
        # Player: Marc-André ter Stegen
        # Injury History (Last 5 Years)
        2024-09-23, Patellar Tendon Rupture, 214, Severe, 1800, No
        ```

        Calling the function:
        ```
        register_injury(players, "injury_history.txt")
        ```

        User Input:
        ```
        Enter the jersey number of the injured player: 19
        Injury date (YYYY-MM-DD): 2025-05-15
        Injury name: Muscle Tear
        Recovery days: 30
        Select severity (1-3): 2
        Minutes played before injury: 1200
        Is it a recurrence? (y/n): n
        ```

        Will update the file to:
        ```
        # Player: Marc-André ter Stegen
        # Injury History (Last 5 Years)
        2024-09-23, Patellar Tendon Rupture, 214, Severe, 1800, No

        # Player: Lamine Yamal
        2025-05-15, Muscle Tear, 30, Moderate, 1200, False
        ```

    Notes:
        - The function assumes that the [players] dictionary contains valid player data, including jersey numbers.
        - If the user enters an invalid jersey number, the function will display an error message and terminate.
        - The function validates the severity input to ensure it is one of the predefined options (Mild, Moderate, Severe).
        - The [update_injury_history] function is used to handle the actual file update.
    """
    print("\nPlayer list:")
    for player_name, attributes in players.items():
        print(f"{attributes['number']}: {player_name}")

    # Select the injured player
    jersey_number = int(input("\nEnter the jersey number of the injured player: "))
    player_name = None
    for name, attributes in players.items():
        if attributes['number'] == jersey_number:
            player_name = name
            break

    if not player_name:
        print("Jersey number not found.")
        return

    # Request injury information
    print(f"\nRegistering injury for {player_name}:")
    date = input("Injury date (YYYY-MM-DD): ")
    injury_type = input("Injury name: ")
    recovery_time = int(input("Recovery days: "))
    print("Injury severity:")
    print("1. Mild")
    print("2. Moderate")
    print("3. Severe")
    severity_options = {1: "Mild", 2: "Moderate", 3: "Severe"}
    while True:
        try:
            severity_choice = int(input("Select severity (1-3): "))
            if severity_choice in severity_options:
                severity = severity_options[severity_choice]
                break
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Invalid input. Enter a number from 1 to 3.")
    minutes_played = int(input("Minutes played before injury: "))
    recurrent_input = input("Is it a recurrence? (y/n): ").strip().lower()
    recurrent = 'Yes' if recurrent_input == 'y' else 'No'

    # Create the injury data dictionary
    injury_data = {
        "date": date,
        "injury_type": injury_type,
        "recovery_time": recovery_time,
        "severity": severity,
        "minutes_played": minutes_played,
        "recurrent": recurrent
    }

    # Update the injury_history.txt file
    update_injury_history(injury_history_file, player_name, injury_data)
    print(f"\nInjury registered for {player_name} and saved in {injury_history_file}.")
