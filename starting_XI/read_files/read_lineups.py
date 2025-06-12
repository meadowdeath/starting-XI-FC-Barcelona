def read_lineups(file_path):
    """
    Name:
        read_lineups

    Parameters:
        file_path (str): 
            Path to the text file where lineups are stored.

    Description:
        Reads a text file containing previously saved football lineups. Each lineup is separated by a double newline.
        The function processes the file and returns a list of lineups, where each lineup is represented as a string.

        - If the file exists, it reads the content and splits it into individual lineups.
        - If the file does not exist, it returns an empty list, allowing the program to handle the absence of lineups gracefully.

    Expected Output:
        list: A list of strings, where each string represents a lineup.

    Example Output:
        Given the following `lineups.txt` file:
        ```
        Lineup 1:
        Goalkeeper: Marc-André ter Stegen
        Left-back: Alejandro Balde
        Centre-back: Andreas Christensen
        Centre-back: Jules Koundé
        Right-back: Eric García

        Lineup 2:
        Goalkeeper: Iñaki Peña
        Left-back: Jordi Alba
        Centre-back: Ronald Araújo
        Centre-back: Gerard Piqué
        Right-back: Sergi Roberto
        ```

        Calling the function:
        ```
        read_lineups("lineups.txt")
        ```

        Will return:
        ```
        [
            "Lineup 1:\nGoalkeeper: Marc-André ter Stegen\nLeft-back: Alejandro Balde\nCentre-back: Andreas Christensen\nCentre-back: Jules Koundé\nRight-back: Eric García",
            "Lineup 2:\nGoalkeeper: Iñaki Peña\nLeft-back: Jordi Alba\nCentre-back: Ronald Araújo\nCentre-back: Gerard Piqué\nRight-back: Sergi Roberto"
        ]
        ```

    Notes:
        - The function assumes that lineups are separated by double newlines in the file.
        - If the file is empty or does not exist, it returns an empty list.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            lineups = [lineup.strip() for lineup in content.split("\n\n") if lineup.strip()]  # Handle inconsistent spacing
        return lineups
    except FileNotFoundError:
        return []  # If the file doesn't exist, return an empty list