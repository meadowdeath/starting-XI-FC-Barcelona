def organize_players(players):
    """
    Name:
        organize_players

    Parameters:
        players (dict): Dictionary of players, where each key is the player's name (str)
                        and the value is another dictionary with the player's attributes:
                        {
                            'number': int,
                            'age': int,
                            'positions': list
                        }

    What it does/usage:
        Organizes players by their main position (the first in the positions list)
        and prints them in the following format:

        FC Barcelona Players (sorted by position)

        Forwards:
        Name, Number, Age, Positions:

        Midfielders:

        Defenders:

        Goalkeepers:

    Expected output:
        None: Prints the players organized by position to the console.

    Example output:
        FC Barcelona Players (sorted by position)

        Forwards:
        Ferran Torres, 7, 25, ['Right Winger', 'Striker']
        Ansu Fati, 10, 22, ['Left Winger', 'Striker']

        Midfielders:
        Gavi, 6, 20, ['Midfielder', 'Attacking Midfielder']
        ...
    """
    positions = {
        "Forwards": [],
        "Midfielders": [],
        "Defenders": [],
        "Goalkeepers": []
    }

    # Classify players by their main position
    for name, attributes in players.items():
        player_positions = attributes['positions']
        main_position = player_positions[0]  # Take the main position
        if "Left-winger" in main_position or "Right-winger" in main_position or "Striker" in main_position:
            positions["Forwards"].append((name, attributes))
        elif "Midfielder" in main_position or "Attacking-Midfielder" in main_position or "Pivot" in main_position:
            positions["Midfielders"].append((name, attributes))
        elif "Centre-back" in main_position or "Right-back" in main_position or "Left-back" in main_position:
            positions["Defenders"].append((name, attributes))
        elif "Goalkeeper" in main_position:
            positions["Goalkeepers"].append((name, attributes))

    # Print organized players
    print("FC Barcelona Players (sorted by position)\n")
    for position, players_list in positions.items():
        print(f"{position}:")
        for name, attributes in players_list:
            print(f"Name: {name}, Number: {attributes['number']}, Age: {attributes['age']}, Positions: {attributes['positions']}")
        print()