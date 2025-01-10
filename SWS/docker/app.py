from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 100)
    return f"<h1>Random Number: {random_number}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
