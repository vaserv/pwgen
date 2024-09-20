from flask import Flask, jsonify
import string
import random

app = Flask(__name__)

def generate_random_string(length=25):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

@app.route('/password')
def password():
    random_string = generate_random_string()
    response = {
        "password": random_string
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
