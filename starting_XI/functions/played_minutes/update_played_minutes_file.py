def update_played_minutes_file(file_path, played_minutes):
    """
    Name:
        update_played_minutes_file

    Parameters:
        file_path (str): 
            Path to the `played_minutes.txt` file where the played minutes data will be updated.
        played_minutes (dict): 
            Dictionary containing the played minutes for players. Each key is the player's name (str), 
            and the value is the total minutes played (int).

    Description:
        This function updates the `played_minutes.txt` file with the new played minutes for players.
        - If the file already exists, it reads the current played minutes and updates the values for existing players.
        - If a player is not already in the file, they are added with their played minutes.
        - The function ensures that the file is properly formatted, with each line containing a player's name and their total played minutes, separated by a comma.

    Expected Output:
        None: The function writes the updated played minutes directly to the `played_minutes.txt` file.

    Example:
        Given the following `played_minutes.txt` file:
        ```
        Marc-André ter Stegen,90
        Robert Lewandowski,80
        ```

        Calling the function:
        ```
        update_played_minutes_file(
            file_path="played_minutes.txt",
            played_minutes={
                "Marc-André ter Stegen": 45,
                "Ferran Torres": 30
            }
        )
        ```

        Will update the file to:
        ```
        Marc-André ter Stegen,135
        Robert Lewandowski,80
        Ferran Torres,30
        ```

    Notes:
        - The function assumes that the file is properly formatted, with each line containing a player's name and their played minutes, separated by a comma.
        - If the file does not exist, it creates a new file and writes the played minutes.
        - The function overwrites the file with the updated content.
    """
    # Read the current played minutes from the file
    current_minutes = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                player, minutes = line.strip().split(',')
                current_minutes[player] = int(minutes)
    except FileNotFoundError:
        pass  # If the file doesn't exist, start with an empty dictionary

    # Update the played minutes
    for player, minutes in played_minutes.items():
        if player in current_minutes:
            current_minutes[player] += minutes
        else:
            current_minutes[player] = minutes

    # Write the updated played minutes back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        for player, minutes in current_minutes.items():
            file.write(f"{player},{minutes}\n")