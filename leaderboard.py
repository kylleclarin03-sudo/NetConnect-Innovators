import json
import os

class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name}: {self.score}"

    def to_dict(self):
        return {"name": self.name, "score": self.score}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["score"])

class Leaderboard:
    def __init__(self, data_file="data/players.json"):
        self.data_file = data_file
        self.players = {}
        self.load_data()

    def load_data(self):
    # If file exists AND is not empty
        if os.path.exists(self.data_file) and os.path.getsize(self.data_file) > 0:
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)

                # Convert JSON players to Player objects
                for player_data in data:
                    player = Player.from_dict(player_data)
                    self.players[player.name] = player

            except Exception:
                print("WARNING: Corrupted or invalid JSON detected. Resetting data file...")
                self.players = {}
                self.save_data()

        else:
            # File does not exist OR is empty
            print("No valid players.json found — creating a new one.")
            self.players = {}
            self.save_data()

    def save_data(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w') as f:
            json.dump([p.to_dict() for p in self.players.values()], f, indent=4)

    def add_player(self, name):
        if name not in self.players:
            self.players[name] = Player(name)
            self.save_data()

    def update_score(self, name, points):
        if name in self.players:
            self.players[name].score = points
        else:
            self.add_player(name)
            self.players[name].score = points
        self.save_data()

    def get_top_players(self, n=10):
        sorted_players = sorted(self.players.values(), key=lambda p: p.score, reverse=True)
        return sorted_players[:n]

    def get_all_players(self):
        return list(self.players.values())


#basic questions for mini-game
class Question:
    def __init__(self, question, answer, points=10):
        self.question = question
        self.answer = answer
        self.points = points


class Game:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def play_game(self, player_name, leaderboard):
        score = 0
        print(f"\nStarting {self.name} Game for {player_name}!") 
        print("-" * 40)  
        for i, q in enumerate(self.questions, 1):
            try:
                user_answer = input(f"Q{i}: {q.question} ").strip()
                if user_answer.lower() == q.answer.lower():
                    score += q.points
                    print("Correct! +" + str(q.points) + " points")
                else:
                    print(f"Wrong! Correct answer: {q.answer}")
            except KeyboardInterrupt:
                print("\nGame interrupted.")
                break
        
        #after game score, maaadd dito yung score ng player
        if player_name in leaderboard.players:
            leaderboard.players[player_name].score += score
        else:
            leaderboard.add_player(player_name)
            leaderboard.players[player_name].score = score
            
        leaderboard.save_data()
        print(f"\n{player_name} scored {score} points in {self.name}!")