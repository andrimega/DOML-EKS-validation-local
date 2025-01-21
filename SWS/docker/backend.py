from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 100)
    return f"""
    <!DOCTYPE html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Scalable Web Server</title>
    </head>
    <body>
        <h1>This is a sample application. Meant to simulate a simple static page</h1>
        <h2>The generated number is:</h2>
        <p>{random_number}</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)