from flask import Flask,render_template,request

app = Flask(__name__) #the instance of the app we are building

#URL _> endpoint /
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
            print(request.form)
            name=request.form["username"]
            password=request.form["password"]
    
            return f"<p>Welcome {name}!!!</p>"
    else:#get request hai
        return render_template("login.html")

if __name__=='__main__': #it means it will only run when executed via command line interface and not when this file is imported to other file
    app.run(debug=True)