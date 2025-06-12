def save_lineup(file_path, lineup, lineup_number):
    """
    Name:
        save_lineup

    Parameters:
        file_path (str): 
            Path to the text file where lineups are stored.
        lineup (list): 
            List of tuples representing the lineup, where each tuple contains:
                - position (str): The position of the player (e.g., "Goalkeeper", "Left-back").
                - player (str): The name of the player assigned to that position.
        lineup_number (int): 
            The number of the lineup being saved (e.g., 1 for "Lineup 1").

    Description:
        Saves the given lineup to the specified file in a structured and readable format.
        - Each lineup is prefixed with its unique identifier (e.g., "Lineup 1").
        - Each player's position and name are written on a new line.
        - Lineups are separated by a blank line for readability.

        If the file does not exist, it is created. If the file already exists, the new lineup is appended to the end.

    Expected Output:
        None: The function writes the lineup directly to the specified file.

    Example Input:
        file_path = "lineups.txt"
        lineup = [
            ("Goalkeeper", "Marc-André ter Stegen"),
            ("Left-back", "Alejandro Balde"),
            ("Centre-back", "Andreas Christensen"),
            ("Centre-back", "Jules Koundé"),
            ("Right-back", "Eric García")
        ]
        lineup_number = 1

    Example Output in File:
        ```
        Lineup 1:
        Goalkeeper: Marc-André ter Stegen
        Left-back: Alejandro Balde
        Centre-back: Andreas Christensen
        Centre-back: Jules Koundé
        Right-back: Eric García
        ```

    Notes:
        - The function assumes that the [lineup](http://_vscodecontentref_/1) parameter is a list of tuples, where each tuple contains a position and a player.
        - Lineups are appended to the file without overwriting existing content.
        - The file is encoded in UTF-8 to support special characters in player names.
    """
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"Lineup {lineup_number}:\n")
        for position, player in lineup:
            file.write(f"{position}: {player}\n")
        file.write("\n")  # Separate lineups with a blank line