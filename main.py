from leaderboard import Leaderboard, Game, Question

def main():
    leaderboard = Leaderboard()

    questions = [
        Question("What is 2 + 2?", "4"),
        Question("Capital of France?", "Paris"),
        Question("Python is a?", "language"),
        Question("The world famous UNESCO Heritage Site Cologne Cathedral is located in which country?", "Germany"),
        Question("What is the product of 47 * 152?", "7,144"),
        Question("Is Australia a continent or a country?", "both")
    ]
    game = Game("Trivia", questions)

    while True:
        print("🏆 LEADERBOARD APP 🏆")  
        print("="*30)
        print("1. Add Player")  
        print("2. Play Game")
        print("3. Update Score Manually")
        print("4. View Leaderboard")
        print("5. Exit")
        print("="*30)  

        try:
            choice = input("Choose an option (1-5): ").strip()
            if not choice:
                print("Please enter a choice.")
                continue

            if choice == "1":
                name = input("Enter player name: ").strip()
                if not name:
                    print("Name cannot be empty.")
                    continue
                leaderboard.add_player(name)
                print(f"Player '{name}' added successfully!")
            elif choice == "2":
                name = input("Enter player name: ").strip()
                if not name:
                    print("Name cannot be empty.")
                    continue
                game.play_game(name, leaderboard)

            elif choice == "3":
                name = input("Enter player name: ").strip()
                if not name:
                    print("Name cannot be empty.")
                    continue
                try:
                    points = int(input("Enter points to add: ").strip())
                    leaderboard.update_score(name, points)
                    print(f"Added {points} points to {name}!")
                except ValueError:
                    print("Please enter a valid number for points.")

            elif choice == "4":
                top = leaderboard.get_top_players()
                if not top:
                    print("No players yet.")
                else:
                    print("\n🏅 TOP PLAYERS 🏅")
                    print("-" * 20)
                    for i, player in enumerate(top, 1):
                        print(f"{i:2d}. {player}")
                    print("-" * 20)

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select 1-5.")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()