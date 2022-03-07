from flask import Flask, render_template, request, redirect, url_for, session, flash
import random
app = Flask(__name__)
app.config['SECRET_KEY'] = 'guessthisanduragenius'

# rock is 0
# paper is 1
# scissors is 2
# lizard is 3
# spock is 4

# winning cases:
# 0 beats 3, 0 beats 2
# 1 beats 0, 1 beats 4
# 2 beats 1, 2 beats 3
# 3 beats 1, 3 beats 4
# 4 beats 0, 4 beats 2

# results:
# 1 is draw
# 2 is win
# 3 is lose


def check_for_winner(player, computer):
    computer_pick = computer
    player_pick = player
    result = 0
    if player_pick == computer_pick:
        result = 1

    # if computer picks rock
    if computer_pick == 0:
        if player_pick == 1:
            result = 2
        elif player_pick == 2:
            result = 3
        elif player_pick == 3:
            result = 3
        elif player_pick == 4:
            result = 2

    # if computer picks paper
    if computer_pick == 1:
        if player_pick == 0:
            result = 3
        elif player_pick == 2:
            result = 2
        elif player_pick == 3:
            result = 2
        elif player_pick == 4:
            result = 3

    # if computer picks scissors
    if computer_pick == 2:
        if player_pick == 1:
            result = 3
        elif player_pick == 0:
            result = 2
        elif player_pick == 3:
            result = 2
        elif player_pick == 4:
            result = 3

    # if computer picks lizard
    if computer_pick == 3:
        if player_pick == 1:
            result = 3
        elif player_pick == 0:
            result = 2
        elif player_pick == 2:
            result = 2
        elif player_pick == 4:
            result = 3

    # if computer picks spock
    if computer_pick == 4:
        if player_pick == 1:
            result = 2
        elif player_pick == 0:
            result = 3
        elif player_pick == 2:
            result = 3
        elif player_pick == 3:
            result = 2

    return result


@app.route("/")
def index():
    name_list = ['Rock','Paper','Scissors','Lizard','Spock']
    computer_pick = random.randint(0, 4)

    if not request.args.get('c'):
        session['player_score'] = 0
        session['computer_score'] = 0

    if request.args.get('c'):
        playerpick = int(request.args.get('c'))
        if check_for_winner(playerpick, computer_pick) == 1:
            flash('DRAW!')
        elif check_for_winner(playerpick, computer_pick) == 2:
            flash('WINNER!')
            session['player_score'] += 1
        elif check_for_winner(playerpick, computer_pick) == 3:
            session['computer_score'] += 1
            flash('LOSER!')

    if request.args.get('restart'):
        session['player_score'] = 0
        session['computer_score'] = 0

    return render_template('rpslshtml.html', name_list=name_list, computerscore=session['computer_score'], playerscore=session['player_score'])


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    app.run(host, port, debug=True)