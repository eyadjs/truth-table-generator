from flask import Flask, render_template, request
from main import *
from calculators import *
from formats import *
from parentheses import *


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])

def calculate():
    output = ""
    if request.method =="POST" and "statement" in request.form:
        input = request.form.get("statement")
        output = compute(input)
        input_formatted = output[1][1] # eg. a V b
        variables = output[1][0] # eg. a | b
        headings = (variables, input_formatted)
        preset_combos = [] # eg. [T|T, T|F, etc..]
        truth_values = [] # eg. [T, F , etc..]
        for i in range(len(output[0])):
            preset_combos.append(output[0][i][0])
            truth_values.append(output[0][i][1])
        data = []
        for i in range(len(preset_combos)):
            data.append((preset_combos[i], truth_values[i]))
        
        return render_template("index.html", data=data, tl = variables, tr = input_formatted, headings=headings)
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()