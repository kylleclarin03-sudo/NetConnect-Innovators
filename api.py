from flask import Flask, request, jsonify
from leaderboard import Leaderboard

app = Flask(__name__)
leaderboard = Leaderboard()

@app.route('/players', methods=['GET'])
def get_players():
    players = leaderboard.get_all_players()
    return jsonify([{'name': p.name, 'score': p.score} for p in players])

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    top = leaderboard.get_top_players()
    return jsonify([{'name': p.name, 'score': p.score} for p in top])

@app.route('/add_player', methods=['POST'])
def add_player():
    data = request.get_json()
    name = data.get('name')
    if name:
        leaderboard.add_player(name)
        return jsonify({'message': f'Player {name} added.'}), 201
    return jsonify({'error': 'Name required'}), 400

@app.route('/update_score', methods=['POST'])
def update_score():
    data = request.get_json()
    name = data.get('name')
    points = data.get('points')
    if name and points is not None:
        leaderboard.update_score(name, points)
        return jsonify({'message': f'Updated {name} by {points} points.'}), 200
    return jsonify({'error': 'Name and points required'}), 400

if __name__ == '__main__':
    app.run(debug=True)