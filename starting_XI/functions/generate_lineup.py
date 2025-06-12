from scipy.optimize import linear_sum_assignment
from functions.hungarian_algorithm import hungarian_algorithm, find_best_players
import numpy as np
from datetime import datetime, timedelta

def generate_lineup(players, injury_history, current_date, played_minutes, player_performance, risk_coefficients, age_risks):
    """
    Name:
        generate_lineup

    Parameters:
        players (dict): Dictionary of players, where each key is the player's name (str) and the value is another dictionary
                        containing the player's attributes:
                        {
                            'number': int,
                            'age': int,
                            'positions': list
                        }
        injury_history (dict): A dictionary where each key is a player's name (str) and the value is a dictionary
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
        played_minutes (dict): Dictionary with player names as keys and minutes played as values.
        risk_coefficients (dict): Dictionary with player names as keys and injury risk coefficients as values.
        age_risks (dict): Dictionary with player names as keys and age risk coefficients as values.
        player_performance (dict): Dictionary with player names as keys and performance scores (1.0-10.0) as values.

    Description:
        Generates an optimal 4-3-3 lineup by solving a bipartite graph matching problem. The weights of the edges
        are calculated based on the given metrics (performance, minutes played, injury risk, and age risk).

    Expected Output:
        list: A list of tuples where each tuple contains a position and the assigned player.
    """
    # Define the required positions for a 4-3-3 lineup
    positions = [
        "Goalkeeper",
        "Centre-back", "Centre-back",
        "Right-back", "Left-back",
        "Pivot", "Attacking-midfielder", "Midfielder",
        "Striker", "Right-winger", "Left-winger"
    ]

    # Convert current_date to a datetime object
    current_date = datetime.strptime(current_date, "%Y-%m-%d")

    # Filter out injured players
    available_players = []
    for player in players:
        is_injured = False
        if player in injury_history and 'injuries' in injury_history[player]:
            for injury in injury_history[player]['injuries']:
                injury_date = datetime.strptime(injury['date'], "%Y-%m-%d")
                recovery_end_date = injury_date + timedelta(days=injury['recovery_time'])
                if injury_date <= current_date <= recovery_end_date:
                    is_injured = True
                    break
        if not is_injured:
            available_players.append(player)

    # Check if there are enough players for each position
    for position in positions:
        compatible_players = [player for player in available_players if position in players[player]['positions']]
        if not compatible_players:
            raise ValueError(f"No players available for position: {position}")


    # Create a cost matrix (rows = players, columns = positions)
    num_players = len(available_players)
    num_positions = len(positions)
    cost_matrix = np.zeros((num_players, num_positions))

    for i, player in enumerate(available_players):
        for j, position in enumerate(positions):
            # Calculate the weight for the edge (player -> position)
            if position in players[player]['positions']:
                cost_matrix[i, j] = (
                    (10 - player_performance.get(player, 0)) * 0.5 +  # Weight for performance (higher is better)
                    played_minutes.get(player, 0) * 0.2 +  # Weight for minutes played
                    risk_coefficients.get(player, 0) * 0.2 +  # Weight for injury risk
                    age_risks.get(player, 0) * 0.1  # Weight for age risk
                )
            else:
                cost_matrix[i, j] = np.inf  # Assign a high cost if the player cannot play this position

    # Ask the user whether to use the optimized (library) version or not
    #use_optimized = input("¿Usar la versión optimizada (librería scipy) para resolver el problema de asignación? (s/n): ").strip().lower()
    
    # Verify that there are enough players for each position
    for position in positions:
        compatible_players = [player for player in players if position in players[player]['positions']]
        if not compatible_players:
            raise ValueError(f"No players available for position: {position}")
        

    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    lineup = [(positions[j], available_players[i]) for i, j in zip(row_ind, col_ind) if cost_matrix[i, j] != np.inf]

    return lineup

"""""
    if use_optimized == 's':
        row_ind, col_ind = linear_sum_assignment(cost_matrix)
        # Generate the lineup
        lineup = [(positions[j], available_players[i]) for i, j in zip(row_ind, col_ind) if cost_matrix[i, j] != np.inf]
    else:
        # Generar la alineación usando la función alternativa
        lineup = find_best_players(cost_matrix, positions, available_players)

    # Return the generated lineup
    return lineup
"""""