from flask import Flask, request, jsonify

app = Flask(__name__)

# Placeholder data storage (replace with a database in a production environment)
players = []
games = []
studios = []

# Player routes
@app.route('/players', methods=['POST'])
def create_player():
    data = request.get_json()
    player = {
        'pid': len(players) + 1,
        'username': data['username'],
        'email': data['email'],
        'contact':data['contact'],
        'age': data['age'],
        'gender': data['gender'],
        'country': data['country'],
        'password': data['password'],
        'account_status': 'active'
    }
    players.append(player)
    return jsonify(player), 201

@app.route('/players/<int:play_id>', methods=['DELETE'])
def close_player_account(play_id):
    for player in players:
        if player['pid'] == play_id:
            player['account_status'] = 'closed'
            return '', 204
    return jsonify({'error': 'Player not found'}), 404

@app.route('/players/<int:pid>/games/<int:gid>', methods=['DELETE'])
def unregister_player_from_game(pid, gid):
    # Remove the player-game relationship
    player = Player.query.get(pid)
    game = Games.query.get(gid)

    if player and game:
        player.games.remove(game)
        db.session.commit()
        return '', 204

# Publisher routes
@app.route('/publishers/popularity', methods=['GET'])
def get_popularity_report():
    popularity_report = db.session.query(Games.title, func.count(GamePlay.pid)). \
        join(GamePlay).group_by(Games.title).all()

    report = [{'game_title': title, 'player_count': count} for title, count in popularity_report]

    return jsonify({'popularity_report': report})

@app.route('/publishers/studios/<int:studio_id>/players', methods=['GET'])
def get_players_for_studio(studio_id):
    players = Player.query.join(GamePlay).join(Game).join(Studio). \
        filter(Studio.id == studio_id).all()
    player_list = [{'player_id': player.id, 'username': player.username} for player in players]
    return jsonify({'players': player_list})

# Studio routes
@app.route('/studios/<int:studio_id>/popularity', methods=['GET'])
def get_studio_popularity(studio_id):
    popularity_report = db.session.query(Game.title, func.count(GamePlay.player_id)). \
        join(GamePlay).join(Game).join(Studio). \
        filter(Studio.id == studio_id).group_by(Games.title).all()
    report = [{'game_title': title, 'player_count': count} for title, count in popularity_report]
    return jsonify({'popularity_report': report})

@app.route('/studios/<int:studio_id>/players/<int:player_id>/games', methods=['DELETE'])
def unregister_player_from_studio_games(studio_id, player_id):
    GamePlay.query.filter(GamePlay.player_id == player_id, GamePlay.game_id.in_(Games.query.with_entities(Games.id).filter(Games.studio_id == studio_id))).delete()
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
