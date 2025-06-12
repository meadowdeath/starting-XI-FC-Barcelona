def read_players(file_path):
    """
    Name:
        read_players

    Parameters:
        file_path (str): Path to the text file containing player information.

    Description:
        Reads a text file containing football player information,
        processes each line to extract the data (name, number, age, positions)
        and stores each player as a dictionary within a main dictionary.

    Expected Output:
        dict: A dictionary where each key is the player's name (str) and the value is another dictionary
              containing the player's attributes:
              {
                  'name': str,
                  'number': int,
                  'age': int,
                  'positions': list
              }

    Example Output:
        {
            'Marc-André ter Stegen': {'number': 1, 'age': 33, 'positions': ['Goalkeeper']},
            'Iñaki Peña': {'number': 13, 'age': 26, 'positions': ['Goalkeeper']},
            ...
        }
    """
    players = {}
    with open(file_path, 'r', encoding='utf-8') as file:

        print("Loading players from file...\n")

        for line in file:
            line = line.strip()
            # Ignore empty lines or comments
            if not line or line.startswith('#') or line.startswith('//'):
                continue

            # Split player data
            try:
                name, number, age, positions = line.split(',', maxsplit=3)
                number = int(number.strip())
                age = int(age.strip())
                # Manually process positions to convert them into a list of strings
                positions = positions.strip()[1:-1].split(',')  # Remove brackets and split by commas
                positions = [pos.strip() for pos in positions]  # Remove extra spaces
                # Add player to the dictionary
                players[name.strip()] = {
                    'number': number,
                    'age': age,
                    'positions': positions
                }
            except (ValueError, SyntaxError):
                print(f"Error processing line: {line}")

    return players