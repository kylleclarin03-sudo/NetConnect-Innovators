from leaderboard import Leaderboard, Game, Question

def main():
    leaderboard = Leaderboard()

    # Sample game
    questions = [
        Question("What is 2 + 2?", "4"),
        Question("Capital of France?", "Paris"),
        Question("Python is a?", "language")
    ]
    game = Game("Trivia", questions)

    while True:
        print("\nLeaderboard App")
        print("1. Add Player")
        print("2. Play Game")
        print("3. Update Score Manually")
        print("4. View Leaderboard")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter player name: ")
            leaderboard.add_player(name)
            print(f"Player {name} added.")

        elif choice == "2":
            name = input("Enter player name: ")
            game.play_game(name, leaderboard)

        elif choice == "3":
            name = input("Enter player name: ")
            points = int(input("Enter points to add: "))
            leaderboard.update_score(name, points)
            print(f"Added {points} points to {name}.")

        elif choice == "4":
            top = leaderboard.get_top_players()
            print("\nTop Players:")
            for i, player in enumerate(top, 1):
                print(f"{i}. {player}")

        elif choice == "5":
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()