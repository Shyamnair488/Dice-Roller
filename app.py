from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll_dice/<int:num_of_dice>', methods=['GET'])
def roll_dice(num_of_dice):
    dice = [random.randint(1, 6) for _ in range(num_of_dice)]
    total = sum(dice)
    dice_faces = [dice_art[die] for die in dice]
    return jsonify({'dice_faces': dice_faces, 'total': total})

if __name__ == '__main__':
    app.run(debug=True)
