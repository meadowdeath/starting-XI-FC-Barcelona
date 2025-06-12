import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Solve the assignment problem using the Hungarian algorithm (custom implementation).

    Parameters:
        cost_matrix (ndarray): A 2D numpy array representing the cost matrix.

    Returns:
        tuple: Two lists representing the row indices and column indices of the optimal assignments.
    """
    # Step 1: Subtract the row minimum from each row
    cost_matrix = cost_matrix.copy()
    for i in range(cost_matrix.shape[0]):
        row_min = np.min(cost_matrix[i, :])
        cost_matrix[i, :] -= row_min

    # Step 2: Subtract the column minimum from each column
    for j in range(cost_matrix.shape[1]):
        col_min = np.min(cost_matrix[:, j])
        cost_matrix[:, j] -= col_min


    # Step 3: Cover all zeros with a minimum number of lines
    def cover_zeros(matrix):
        """Cover zeros in the matrix using a minimum number of lines."""
        covered_rows = set()
        covered_cols = set()
        while True:
            # Find uncovered zeros
            uncovered_zeros = [(i, j) for i in range(matrix.shape[0]) for j in range(matrix.shape[1])
                               if matrix[i, j] == 0 and i not in covered_rows and j not in covered_cols]

            if not uncovered_zeros:
                break

            # Choose a zero and cover its row or column
            zero = uncovered_zeros[0]
            if sum(matrix[zero[0], :] == 0) <= sum(matrix[:, zero[1]] == 0):
                covered_rows.add(zero[0])
            else:
                covered_cols.add(zero[1])

        return covered_rows, covered_cols

    covered_rows, covered_cols = cover_zeros(cost_matrix)

    while len(covered_rows) + len(covered_cols) < cost_matrix.shape[0]:
        # Step 4: Adjust the matrix
        uncovered_vals = [cost_matrix[i, j] for i in range(cost_matrix.shape[0]) for j in range(cost_matrix.shape[1])
                           if i not in covered_rows and j not in covered_cols]
        min_uncovered = min(uncovered_vals)

        for i in range(cost_matrix.shape[0]):
            for j in range(cost_matrix.shape[1]):
                if i not in covered_rows and j not in covered_cols:
                    cost_matrix[i, j] -= min_uncovered
                elif i in covered_rows and j in covered_cols:
                    cost_matrix[i, j] += min_uncovered

        covered_rows, covered_cols = cover_zeros(cost_matrix)

    # Step 5: Find an optimal assignment
    row_ind = []
    col_ind = []
    assigned_rows = set()
    assigned_cols = set()

    for i in range(cost_matrix.shape[0]):
        for j in range(cost_matrix.shape[1]):
            if cost_matrix[i, j] == 0 and i not in assigned_rows and j not in assigned_cols:
                row_ind.append(i)
                col_ind.append(j)
                assigned_rows.add(i)
                assigned_cols.add(j)

    return row_ind, col_ind

def find_best_players(cost_matrix, positions, players):
    """
    Encuentra al mejor jugador para cada posición basándose en la matriz de costos.

    Parameters:
        cost_matrix (numpy.ndarray): Matriz de costos (filas = jugadores, columnas = posiciones).
        positions (list): Lista de posiciones (columnas de la matriz de costos).
        players (list): Lista de nombres de jugadores (filas de la matriz de costos).

    Returns:
        list: Lista de tuplas (posición, jugador) con la asignación óptima.
    """
    num_players, num_positions = cost_matrix.shape
    assigned_players = set()  # Para evitar asignar un jugador a múltiples posiciones
    lineup = []

    for j, position in enumerate(positions):
        # Encuentra el índice del jugador con el menor costo en la columna j
        min_cost = np.inf
        best_player = None

        for i in range(num_players):
            if i not in assigned_players and cost_matrix[i, j] < min_cost:
                min_cost = cost_matrix[i, j]
                best_player = i

        if best_player is not None:
            lineup.append((position, players[best_player]))
            assigned_players.add(best_player)

    return lineup