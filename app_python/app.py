from datetime import datetime
import pytz
from flask import Flask, render_template

app = Flask(__name__)

def get_moscow_time():
    time_zone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(time_zone)
    return moscow_time

@app.route("/")
def index():
    return render_template("template.html", time=get_moscow_time().strftime("%H:%M:%S"))

if __name__ == '__main__':
    app.run('localhost', 5000)
