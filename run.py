from datetime import datetime
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def current_time():
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    return str(time)

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
