from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

def tuplify(d):
    result = []
    for key in d:
        result.append((key, d[key]))
    return result

clues = {
1: """
Where the cars are straight ahead,
<br/>
<br/>
To the left direct your tread.
<br/>
<br/>
Through the gate is where you're headed,
<br/>
<br/>
To find where eggs are first embedded.
""",
2: """
Stand and look out on the view,
<br/>
<br/>
And I will give your second clue.
<br/>
<br/>
Look about for somewhere round,
<br/>
<br/>
As that's the place more eggs are found.
""",
3: """
Down the hill is where you 'ort a
<br/>
<br/>
Look towards a stretch of water.
<br/>
<br/>
Best foot forward therefore measure.
<br/>
<br/>
No trolls patrol where lies your treasure.
""",
4: """
Up the path direct your feet,
<br/>
<br/>
Look for signs of a covered seat.
<br/>
<br/>
Set above the lake in shade,
<br/>
<br/>
Your fourth discovery is made.
""",
5: """
Take the steps behind you now,
<br/>
<br/>
And head towards your final bow.
<br/>
<br/>
Where the fruit and veg are grown,
<br/>
<br/>
Today some chocolate is sewn!
""",
6: """
There's only one more place to see:
<br/>
<br/>
In glass, above, you need to be.
<br/>
<br/>
A place of total Easter pleasure,
<br/>
<br/>
It's where you'll find your final treasure.
"""
}

code_to_id = {
        "k9jyka5oyl": 1,
        "lane9yo82v": 2,
        "shzvxs7v92": 3,
        "fwlivo9c8u": 4,
        "2357y77rk2": 5,
        "t52p3uauad": 6
        }

@app.route("/css/<path:filename>")
def css(filename):
    return send_from_directory("static/css", filename)

@app.route("/img/<path:filename>")
def img(filename):
    return send_from_directory("static/img", filename)

@app.route("/<string:code>")
def home(code):
    return render_template("home.html", content=clues[code_to_id[code]])

@app.route("/secret")
def secret():
    return """
<html>
<body>
%s
</body>
</html>
""" % "".join(["<h1><a href='/%s'>%d</a></h1><br/>" % (code, number) for code, number in sorted(tuplify(code_to_id), key=lambda x:x[1])])

if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0")
