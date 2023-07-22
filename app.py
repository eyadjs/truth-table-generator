from flask import Flask, render_template, request
from calculators import *
from formats import *
from parentheses import *


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])

def calculate():

    output = ""

    if request.method =="POST" and "statement" in request.form:

        input = request.form.get("statement")

        error_handling = transform(input) # ([ ['T', 'AND', 'T', ')'], ... , ... , ...], [0]
                                          # ['p', 'and', 'q', ')'], [1]
                                          # ['p','q'] ]) [2]

        if input == "":
            error = "Field is empty."
            return render_template("index.html", error=error)

        
        try:
            output = makeTable(input)

            # Seperating table into sections
            input_formatted = output[1][1] # eg. a V b (top right)
            variables = output[1][0] # eg. a | b (top left)
            headings = (variables, input_formatted)

            preset_combos = [] # eg. [T|T, T|F, etc..] (bottom right)
            truth_values = [] # eg. [T, F , etc..] (bottom left)
            for i in range(len(output[0])):
                preset_combos.append(output[0][i][0])
                truth_values.append(output[0][i][1])

            data = []
            for i in range(len(preset_combos)):
                data.append((preset_combos[i], truth_values[i]))
        except:
            error = "Please correctly format your statement. Be sure to correctly place brackets and use 2 or 3 variables."
            return render_template("index.html", error=error)
        
        
        return render_template("index.html", data=data, headings=headings)
    
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run(debug=False, host="0.0.0.0")