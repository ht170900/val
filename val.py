from flask import Flask, render_template

app = Flask(__name__)

# Days of Valentine's Week
valentines_days = {
    "7": {"name": "Rose Day", "emoji": "🌹"},
    "8": {"name": "Propose Day", "emoji": "💍"},
    "9": {"name": "Chocolate Day", "emoji": "🍫"},
    "10": {"name": "Teddy Day", "emoji": "🧸"},
    "11": {"name": "Promise Day", "emoji": "🤞"},
    "12": {"name": "Hug Day", "emoji": "🤗"},
    "13": {"name": "Kiss Day", "emoji": "💋"},
    "14": {"name": "Valentine's Day", "emoji": "❤️", "special": True}  # Mark Valentine's Day
}

@app.route('/')
def home():
    return render_template('index.html', days=valentines_days)

if __name__ == '__main__':
    app.run(debug=True)
