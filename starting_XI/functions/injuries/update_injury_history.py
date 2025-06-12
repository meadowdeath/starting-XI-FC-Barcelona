def update_injury_history(file_path, player_name, injury_data):
    """
    Name:
        update_injury_history

    Parameters:
        file_path (str): 
            Path to the `injury_history.txt` file where the injury data will be updated.
        player_name (str): 
            Name of the injured player whose injury history needs to be updated.
        injury_data (dict): 
            Dictionary containing the details of the injury. The dictionary must include the following keys:
                - 'date' (str): Date of the injury in the format 'YYYY-MM-DD'.
                - 'injury_type' (str): Name or description of the injury.
                - 'recovery_time' (int): Number of days required for recovery.
                - 'severity' (str): Severity of the injury ('Mild', 'Moderate', 'Severe').
                - 'minutes_played' (int): Minutes played by the player before the injury.
                - 'recurrent' (str): Indicates whether the injury is a recurrence ('True' or 'False').

    Description:
        This function updates the `injury_history.txt` file with information about a new injury for a specific player.
        - If the player already exists in the file, the new injury is appended to their section.
        - If the player does not exist in the file, a new section is created for the player, and the injury is added.
        - The function ensures that the injury history is properly formatted and maintains the structure of the file.

    Expected Output:
        None: The function writes the updated injury history directly to the `injury_history.txt` file.

    Example:
        Given the following `injury_history.txt` file:
        ```
        # Player: Marc-André ter Stegen
        # Injury History (Last 5 Years)
        2024-09-23, Patellar Tendon Rupture, 214, Severe, 1800, No
        ```

        Calling the function:
        ```
        update_injury_history(
            file_path="injury_history.txt",
            player_name="Marc-André ter Stegen",
            injury_data={
                "date": "2025-05-15",
                "injury_type": "Back Injury",
                "recovery_time": 86,
                "severity": "Moderate",
                "minutes_played": 2500,
                "recurrent": "No"
            }
        )
        ```

        Will update the file to:
        ```
        # Player: Marc-André ter Stegen
        # Injury History (Last 5 Years)
        2025-05-15, Back Injury, 86, Moderate, 2500, No
        2024-09-23, Patellar Tendon Rupture, 214, Severe, 1800, No
        ```

    Notes:
        - The function assumes that the file is properly formatted and uses `# Player:` to identify player sections.
        - If the player does not exist in the file, a new section is added at the end of the file.
        - The function overwrites the file with the updated content.
    """
    # Read the current contents of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Search for the player's section
    updated_lines = []
    player_found = False
    header_found = False

    for idx, line in enumerate(lines):
        # Add the current line to the updated lines
        updated_lines.append(line)

        # Check if the line matches the player's section
        if line.strip() == f"# Player: {player_name}":
            player_found = True
            # Check if the next line is the injury history header
            next_idx = idx + 1
            if next_idx < len(lines) and lines[next_idx].strip() == "# Injury History (Last 5 Years)":
                header_found = True
                continue  # Skip further processing for this iteration

        # If the header has been found, insert the new injury right after the header (before the current line)
        if header_found and line.strip() != "# Injury History (Last 5 Years)":
            # Insert the new injury at the position before the current line
            updated_lines.insert(len(updated_lines) - 1,
            f"{injury_data['date']}, {injury_data['injury_type']}, {injury_data['recovery_time']}, "
            f"{injury_data['severity']}, {injury_data['minutes_played']}, {injury_data['recurrent']}\n"
            )
            header_found = False  # Reset the flag to avoid adding the injury multiple times

    # If the player is not found, add them at the end
    if not player_found:
        updated_lines.append(f"\n# Player: {player_name}\n")
        updated_lines.append("# Injury History (Last 5 Years)\n")
        updated_lines.append(
            f"{injury_data['date']}, {injury_data['injury_type']}, {injury_data['recovery_time']}, "
            f"{injury_data['severity']}, {injury_data['minutes_played']}, {injury_data['recurrent']}\n"
        )

    # Write the changes to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)
