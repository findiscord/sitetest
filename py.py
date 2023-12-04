from flask import Flask

app = Flask(__name__)

@app.route('/')
def work():
    return 'WORK'

if __name__ == '__main__':
    app.run(port=2023)
