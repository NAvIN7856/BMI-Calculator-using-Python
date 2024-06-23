# pip install flask

from flask import Flask, render_template, request

import csv

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ""
    cm = ""
    if request.method == 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        name = str(request.form.get('name'))
        bmi = calc_bmi(weight, height)

        with open('bmi.txt', 'a', newline='') as f:
            b = csv.writer(f, delimiter=',')
            b.writerow(['Name', 'BMI'])
            rec = []
            while True:
                n = str(name)
                d = str(bmi)
                L = [n, d]
                rec.append(L)
                for i in rec:
                    b.writerow(i)
                return render_template("bmi_calc.html", bmi=bmi)

    if request.method == 'POST' and 'foot' in request.form:
        foot = float(request.form.get('foot'))
        inch = float(request.form.get('inch'))
        cm = calc_cm(foot, inch)
    return render_template("bmi_calc.html", bmi=bmi, cm=cm)


def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)


def calc_cm(foot, inch):
    return round(((inch+(foot*12))*2.54), 2)


if __name__ == '__main__':
    app.run(host = '0.0.0.0')
