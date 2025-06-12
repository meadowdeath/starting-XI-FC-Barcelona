# Starting XI Lineup Generator for FC Barcelona

## **Project Description**
This project is a lineup generator for FC Barcelona, designed to create optimal 4-3-3 football lineups based on player performance, injury history, minutes played, and age-related risks. The system uses the **Hungarian Algorithm** to solve the assignment problem in a bipartite graph, ensuring the best possible player-to-position assignments.

---

## **Features**
- **Optimal Lineup Generation**: Creates a 4-3-3 lineup by minimizing costs based on player metrics.
- **Injury Management**: Tracks and excludes injured players from the lineup.
- **Risk Calculation**: Computes injury and age-related risks for each player.
- **Minutes Tracking**: Updates and tracks minutes played by each player after matches.
- **Data Persistence**: Saves and retrieves lineups, player data, and match statistics from text files.

---

## **System Requirements**
- **Python 3.8 or higher**
- Required libraries:
  - `numpy`
  - `scipy`

Install dependencies using:
```bash
pip install numpy scipy
```

---

## **Project Structure**
```
starting_XI/
│
├── data/                     # Data files
│   ├── players.txt           # Player information
│   ├── played_minutes.txt    # Minutes played by each player
│   ├── injury_history.txt    # Injury history of players
│   ├── player_performance.txt # Player performance scores
│   └── lineups.txt           # Saved lineups
│
├── functions/                # Core functions
│   ├── generate_lineup.py    # Lineup generation logic
│   ├── calculate_age_risk.py # Age risk calculation
│   ├── save_lineup.py        # Save lineups to file
│   ├── hungarian_algorithm.py # Hungarian Algorithm implementation
│   └── injuries/             # Injury management
│       ├── register_injury.py
│       └── calculate_coeficient_risk.py
│
├── read_files/               # File reading utilities
│   ├── read_players.py
│   ├── read_played_minutes.py
│   ├── read_injury_history.py
│   ├── read_player_performance.py
│   └── read_lineups.py
│
└── main.py                   # Main program entry point
```

---

## **How to Use**
1. **Run the Program**:
   Execute the `main.py` file:
   ```bash
   python main.py
   ```

2. **Input Current Date**:
   Enter the current date in `YYYY-MM-DD` format to filter out injured players.

3. **View Existing Lineups**:
   The program will display previously saved lineups if available.

4. **Generate a New Lineup**:
   - The system reads player data, calculates risks, and generates an optimal lineup.
   - The lineup is displayed and saved to `lineups.txt`.

5. **Register Injuries**:
   If there are injured players, you can register their injuries, which will update the `injury_history.txt` file.

6. **Update Played Minutes**:
   After generating a lineup, the program allows you to update the minutes played by each player during the match.

---

## **Data Files**
- **`players.txt`**: Contains player details such as name, number, age, and positions.
- **`played_minutes.txt`**: Tracks the total minutes played by each player.
- **`injury_history.txt`**: Stores injury details for each player.
- **`player_performance.txt`**: Contains performance scores for players (1.0-10.0).
- **`lineups.txt`**: Stores previously generated lineups.

---

## **Example Workflow**
1. **Generate a Lineup**:
   The system generates a lineup like this:
   ```
   Lineup 1:
   Goalkeeper: Marc-André ter Stegen
   Centre-back: Ronald Araujo
   Centre-back: Andreas Christensen
   Right-back: Jules Koundé
   Left-back: Alejandro Balde
   Pivot: Frenkie de Jong
   Attacking-midfielder: Pedri
   Midfielder: Gavi
   Right-winger: Raphinha
   Left-winger: Ansu Fati
   Striker: Robert Lewandowski
   ```

2. **Save the Lineup**:
   The lineup is saved to `lineups.txt` for future reference.

3. **Update Match Data**:
   After the match, update played minutes and register any injuries.

---

## **Notes**
- Ensure all data files in the `data/` folder are properly formatted.
- The program handles missing or incomplete data gracefully by assigning default values.

---

## **Contributing**
Contributions are welcome! Please open an issue or submit a pull request.

If you'd like to contribute:
1. Fork the repository.
2. Make your changes.
3. Submit a pull request with a detailed description of your updates.

---

## **License**
This project is for academic purposes and is not intended for commercial use.
