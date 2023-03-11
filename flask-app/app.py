from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/datetime')
def get_datetime():
    now = datetime.now(pytz.utc)
    return now.strftime('%Y-%m-%d %H:%M:%S')

@app.route('/time/<timezone>')
def get_time(timezone):
    tz = pytz.timezone(timezone)
    now = datetime.now(tz)
    return now.strftime('%Y-%m-%d %H:%M:%S %Z')

if __name__ == '__main__':
    app.run()
