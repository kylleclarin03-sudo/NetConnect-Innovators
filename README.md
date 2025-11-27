# NetConnect Innovators Team Activity: Leaderboards App
A Python CLI-based Leaderboard app to track player scores for mini-games, built with Object-Oriented Programming. It includes a Flask API for serving data and can be exposed publicly using ngrok.

# Features
- **Object-Oriented Design**: Classes for Player, Leaderboard, Game, and Question management.
- **CLI Interface**: Command-line interface to add players, play games, update scores, and view leaderboards.
- **Flask API**: RESTful API endpoints to interact with the leaderboard programmatically.
- **Mini-Games**: Built-in trivia game with questions and answers.
- **Public Serving**: Use ngrok to expose the API publicly for other teams.

# CLI Mode
We run the CLI application by:
python main.py

The it will shows the Options:
- Add Player
- Play Game (Trivia)
- Update Score Manually
- View Leaderboard
- Exit

# API Mode
Run the Flask API:
python api.py

The API will run on http://localhost:5000

# Endpoints
- `GET /players`: Get all players
- `GET /leaderboard`: Get top players
- `POST /add_player`: Add a new player (JSON: {"name": "PlayerName"})
- `POST /update_score`: Update player score (JSON: {"name": "PlayerName", "points": 10})

# Public Serving with ngrok
1. We start the Flask API using this command:
   python api.py
2. In another terminal, we run ngrok:
   ngrok http 5000
3. Use the provided ngrok URL to access the API publicly.

# Project Structure
- `leaderboard.py`: Core classes (Player, Leaderboard, Game, Question)
- `main.py`: CLI interface
- `api.py`: Flask API server
- `requirements.txt`: Python dependencies
- `README.md`: This documentation

This project is part of NetConnect Innovators Team Activity.
DevNet 11/27/2025