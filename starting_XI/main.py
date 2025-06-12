# Import necessary functions
from functions.played_minutes.register_match_changes import register_match_changes
from read_files.read_players import read_players
from read_files.read_played_minutes import read_played_minutes
from read_files.read_injury_history import read_injury_history
from read_files.read_player_performance import read_player_performance
from read_files.read_lineups import read_lineups
from functions.save_lineup import save_lineup
from functions.injuries.calculate_coeficient_risk import calculate_coefficient_risk
from functions.calculate_age_risk import calculate_age_risk
from functions.generate_lineup import generate_lineup
from functions.injuries.register_injury import register_injury


def main():
    # File paths
    players_file = r'c:\Users\galgu\Respaldo\CETI\Cuarto Semestre\Algoritmia\Tercer Parcial\starting_XI\data\players.txt'
    played_minutes_file = r'c:\Users\galgu\Respaldo\CETI\Cuarto Semestre\Algoritmia\Tercer Parcial\starting_XI\data\played_minutes.txt'
    injury_history_file = r'c:\Users\galgu\Respaldo\CETI\Cuarto Semestre\Algoritmia\Tercer Parcial\starting_XI\data\injury_history.txt'
    player_performance_file = r'c:\Users\galgu\Respaldo\CETI\Cuarto Semestre\Algoritmia\Tercer Parcial\starting_XI\data\player_performance.txt'
    lineups_file = r'c:\Users\galgu\Respaldo\CETI\Cuarto Semestre\Algoritmia\Tercer Parcial\starting_XI\data\lineups.txt'

    print("Welcome to the Starting XI Lineup Generator for FC Barcelona!\n")

    # Ask for the current date to discard injured players
    current_date = input("Enter the current date (YYYY-MM-DD): ").strip()

    while True:

        # Read existing lineups
        lineups = read_lineups(lineups_file)
        print(f"\nThere are {len(lineups)} lineups already created.\n")
        if lineups:
            view_lineups = input("Do you want to view the existing lineups? (y/n): ").strip().lower()
            if view_lineups == "y":
                for i, lineup in enumerate(lineups, start=1):
                    print(f"\n{lineup}")

        # Ask if a new lineup should be generated
        generate = input("\nGenerate a new lineup? (y/n): ").strip().lower()
        if generate != "y":
            print("Exiting program.")
            break

        # Read data
        print("\nReading data...")
        players = read_players(players_file)
        played_minutes = read_played_minutes(played_minutes_file)
        injury_history = read_injury_history(injury_history_file)
        player_performance = read_player_performance(player_performance_file)

        # Ask if there are injured players
        injured = input("\nAre there injured players? (y/n): ").strip().lower()
        if injured == "y":
            register_injury(players, injury_history_file)

        # Calculate coefficients
        print("\nCalculating coefficients...")
        risk_coefficients = calculate_coefficient_risk(injury_history)
        age_risks = calculate_age_risk(players)

        # Generate lineup
        print("\nGenerating new lineup...")
        lineup = generate_lineup(players, injury_history, current_date, played_minutes, player_performance, risk_coefficients, age_risks)

        # Show generated lineup
        print("\nGenerated Lineup (4-3-3):")
        for position, player in lineup:
            print(f"{position}: {player}")

        # Save the lineup
        lineup_number = len(lineups) + 1
        save_lineup(lineups_file, lineup, lineup_number)
        print(f"\nLineup {lineup_number} saved successfully!\n")

        # Register changes and update played minutes
        played_minutes = register_match_changes(lineup, players, played_minutes, played_minutes_file)

if __name__ == "__main__":
    main()
