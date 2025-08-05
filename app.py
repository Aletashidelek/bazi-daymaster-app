from flask import Flask, render_template, request
from lunar_python import Solar
import os

app = Flask(__name__)

def get_day_master(year, month, day, hour):
    solar = Solar.fromYmdHms(year, month, day, hour, 0, 0)
    lunar = solar.getLunar()
    return lunar.getDayGan(), lunar.getDayZhi()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        year = int(request.form['year'])
        month = int(request.form['month'])
        day = int(request.form['day'])
        hour = int(request.form['hour'])
        gan, zhi = get_day_master(year, month, day, hour)
        result = {
            'day_master': gan,
            'day_pillar': gan + zhi
        }
    return render_template('index.html', result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0", port=port)

