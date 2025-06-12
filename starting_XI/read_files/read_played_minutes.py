def read_played_minutes(file_path):
    """
    Name:
        read_played_minutes

    Parameters:
        file_path (str): Path to the text file containing played minutes information.

    Description:
        Reads a text file containing the minutes played by each player and stores the data
        in a dictionary where the keys are the player names and the values are the minutes played.

    Expected Output:
        dict: A dictionary where each key is a player's name (str) and the value is the minutes played (int).

    Example Output:
        {
            'Marc-André ter Stegen': 0,
            'Iñaki Peña': 0,
            'Ronald Araujo': 0,
            ...
        }
    """
    played_minutes = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            # Ignore empty lines or comments
            if not line or line.startswith('//'):
                continue

            try:
                # Split the line into player name and minutes played
                name, minutes = line.split(',', maxsplit=1)
                played_minutes[name.strip()] = int(minutes.strip())
            except ValueError:
                print(f"Error processing line: {line}")

    return played_minutes

# Example usage
file_path = r'c:\Users\galgu\Respaldo\CETI\Cuarto Semestre\Algoritmia\Tercer Parcial\starting_XI\data\played_minutes.txt'
played_minutes = read_played_minutes(file_path)