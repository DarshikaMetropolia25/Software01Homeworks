from flask import Flask

app = Flask(__name__)

@app.route('/prime_number/<number1>')