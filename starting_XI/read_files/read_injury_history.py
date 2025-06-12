def read_injury_history(file_path):
    """
    Name:
        read_injury_history

    Parameters:
        file_path (str): Path to the text file containing injury history information.

    Description:
        Reads a text file containing football players' injury history,
        processes each player's data to extract their injuries, and stores each player
        as a dictionary. Each player is represented as a key, and the value is another
        dictionary containing a list of injuries. Each injury is represented as a dictionary
        with the following attributes:
            - Date (str)
            - Injury Type (str)
            - Recovery Time (int, in days)
            - Severity (str)
            - Minutes Played Before Injury (int)
            - Recurrent (str: "Yes" or "No")

    Expected Output:
        dict: A dictionary where each key is a player's name (str) and the value is a dictionary
              containing a list of injuries:
              {
                  'player_name': {
                      'injuries': [
                          {
                              'date': str,
                              'injury_type': str,
                              'recovery_time': int,
                              'severity': str,
                              'minutes_played': int,
                              'recurrent': str
                          },
                          ...
                      ]
                  },
                  ...
              }

    Example Output:
        {
            'Marc-André ter Stegen': {
                'injuries': [
                    {'date': '2024-09-23', 'injury_type': 'Patellar Tendon Rupture', 'recovery_time': 214, 'severity': 'Severe', 'minutes_played': 1800, 'recurrent': 'No'},
                    {'date': '2023-11-05', 'injury_type': 'Back Injury', 'recovery_time': 86, 'severity': 'Moderate', 'minutes_played': 2500, 'recurrent': 'No'},
                    ...
                ]
            },
            'Toni Fernández': {
                'injuries': []
            },
            ...
        }
    """
    players = {}
    current_player = None

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            # Ignore empty lines or comments
            if not line or line.startswith('//'):
                continue

            # Detect player name
            if line.startswith("# Player:"):
                current_player = line.replace("# Player:", "").strip()
                players[current_player] = {'injuries': []}
            elif line == "No recorded injuries":
                # Handle players with no injuries
                players[current_player]['injuries'] = []
            elif not line.startswith("#"):
                # Process injury data
                try:
                    date, injury_type, recovery_time, severity, minutes_played, recurrent = line.split(',', maxsplit=5)
                    recovery_time = int(recovery_time.strip())
                    minutes_played = int(minutes_played.strip())
                    players[current_player]['injuries'].append({
                        'date': date.strip(),
                        'injury_type': injury_type.strip(),
                        'recovery_time': recovery_time,
                        'severity': severity.strip(),
                        'minutes_played': minutes_played,
                        'recurrent': recurrent.strip()
                    })
                except ValueError:
                    print(f"Error processing line: {line}")

    return players