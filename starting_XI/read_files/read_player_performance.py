def read_player_performance(file_path):
    """
    Name:
        read_player_performance

    Parameters:
        file_path (str): Path to the text file containing player performance information.

    Description:
        Reads a text file containing the performance scores assigned to each player by the coach
        and stores the data in a dictionary where the keys are the player names and the values are the performance scores.

    Expected Output:
        dict: A dictionary where each key is a player's name (str) and the value is the performance score (float).

    Example Output:
        {
            'Marc-André ter Stegen': 5.0,
            'Iñaki Peña': 7.5,
            'Wojciech Szczęsny': 10.0,
            ...
        }
    """
    player_performance = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            # Ignore empty lines or comments
            if not line or line.startswith('//'):
                continue

            try:
                # Split the line into player name and performance score
                name, performance = line.split(',', maxsplit=1)
                player_performance[name.strip()] = float(performance.strip())
            except ValueError:
                print(f"Error processing line: {line}")

    return player_performance

# Example usage
file_path = r'c:\Users\galgu\Respaldo\CETI\Cuarto Semestre\Algoritmia\Tercer Parcial\starting_XI\data\player_performance.txt'
player_performance = read_player_performance(file_path)
