from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    request = request.get('https://torre.bio/api/bios/vimuriel' )
    print(json.loads(request.data)))
    #return render_template("index.html")

@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == "GET":
        return "Please submit de form instead"
    else:    
        name = request.form.get("name")
        return render_template("hello.html", name=name)