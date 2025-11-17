from flask import Flask

app = Flask(__name__)

@app.route('/prime_number/<number1>')
def PNumber(number1):
    number = int(number1)
    Remainders = []
    if number > 1:
        for a in range(number):
            Remainder = number % (a + 1)
            if Remainder == 0:
                Remainders.append(Remainder)

        if len(Remainders) == 2:
            response = "This is a prime number."
        else:
            response = "This is not a prime number."
    else:
        response = "This is not a prime number."

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)