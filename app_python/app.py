from datetime import datetime
import pytz
from flask import Flask, render_template


app = Flask(__name__)


def get_moscow_time():
    time_zone = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(time_zone)
    return moscow_time

def write_to_file(filename, content):
    f = open(filename, "a")
    f.write(content)
    f.close()

def read_from_file(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    return content

@app.route("/")
def index():
    app.logger.warning("It is a test warning!")
    time = get_moscow_time().strftime("%H:%M:%S")
    content = "accessed at " + time + "\n"
    write_to_file("files/file.txt", content)
    return render_template("template.html", time=time)

@app.route("/visits")
def visits():
    content = read_from_file("files/file.txt")
    return render_template("visits.html", time=content)

if __name__ == "__main__":
    app.run("localhost", 5000)
