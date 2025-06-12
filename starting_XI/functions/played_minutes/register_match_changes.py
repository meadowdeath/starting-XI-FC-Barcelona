from functions.played_minutes.update_played_minutes_file import update_played_minutes_file

def register_match_changes(lineup, players, played_minutes, played_minutes_file):
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
        Robert Lewandowski,180
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
        Robert Lewandowski,180
        Ferran Torres,30
        ```

    Notes:
        - The function assumes that the file is properly formatted, with each line containing a player's name and their played minutes, separated by a comma.
        - If the file does not exist, it creates a new file and writes the played minutes.
        - The function overwrites the file with the updated content.
    """
    # Ask for additional time
    print("Registering changes during the match:")
    first_half_extra = int(input("Enter additional time for the first half (in minutes): "))
    second_half_extra = int(input("Enter additional time for the second half (in minutes): "))
    total_match_time = 45 + first_half_extra + 45 + second_half_extra

    print(f"\nTotal match duration: {total_match_time} minutes.")

    # Register substitutions
    while True:
        substitution = input("\nWere there any substitutions during the match? (y/n): ").strip().lower()
        if substitution != "y":
            break

        # Show the current lineup
        print("\nPlayers in the current lineup:")
        for position, player in lineup:
            print(f"{player} ({players[player]['number']}) - {position}")

        # Ask for the player who was substituted
        substituted_number = int(input("\nEnter the number of the player who left: "))
        substituted_player = None
        substituted_position = None
        for position, player in lineup:
            if players[player]['number'] == substituted_number:
                substituted_player = player
                substituted_position = position
                break

        if not substituted_player:
            print("Player number not found in the lineup.")
            continue

        # Show available players for the substitution
        print("\nAvailable players for substitution:")
        available_players = [
            (player, attributes['number']) for player, attributes in players.items()
            if substituted_position in attributes['positions'] and player not in [p for _, p in lineup]
        ]
        for player, number in available_players:
            print(f"{player} ({number})")

        # Ask for the player who entered
        entering_number = int(input("\nEnter the number of the player who entered: "))
        entering_player = None
        for player, attributes in players.items():
            if attributes['number'] == entering_number:
                entering_player = player
                break

        if not entering_player:
            print("Player number not found in the player list.")
            continue

        # Validate positions
        if substituted_position not in players[entering_player]['positions']:
            print(f"Player {entering_player} cannot play in the position {substituted_position}.")
            continue

        # Ask for the minute of the substitution
        substitution_minute = int(input("\nEnter the minute of the substitution: "))
        if substitution_minute < 0 or substitution_minute > total_match_time:
            print("Invalid minute.")
            continue
            continue

        # Update played minutes
        if entering_player not in played_minutes:
            played_minutes[entering_player] = 0  # Initialize if the player is not already in played_minutes
        played_minutes[substituted_player] += substitution_minute
        played_minutes[entering_player] += total_match_time - substitution_minute

        # Update the lineup
        lineup = [(position, entering_player if player == substituted_player else player) for position, player in lineup]

    # Assign full match time to players who were not substituted
    for _, player in lineup:
        if played_minutes[player] == 0:
            played_minutes[player] = total_match_time

    # Update the played_minutes.txt file
    update_played_minutes_file(played_minutes_file, played_minutes)

    return played_minutes