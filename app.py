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

        # use these for more specific errors later
        error_handling = transform(input) # ([ ['T', 'AND', 'T', ')'], ... , ... , ...], [0]
                                          # ['p', 'and', 'q', ')'], [1]
                                          # ['p','q'] ]) [2]

        if input == "":
            error = "Field is empty."
            return render_template("index.html", error=error)

        error = "Please correctly format your statement. Be sure to correctly place brackets and use 2 or 3 variables."
        
        try:
            output = makeTable(input)
            headings = output[1]
            data = output[0]

        except:
            return render_template("index.html", error=error)

        if (len(error_handling)) not in (2,3): return render_template("index.html", error=error)
        return render_template("index.html", data=data, headings=headings)
    
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run()