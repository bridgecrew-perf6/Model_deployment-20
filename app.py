from flask import Flask ,render_template ,request
app=Flask(__name__)
import model

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/",methods=['POST'])
def submit():
    # html -> python file


    if request.method == "POST":
        temperature = request.form["Temperature"]
        humidity = request.form["Humidity"]
        ph = request.form["Ph"]
        rainfall = request.form["Rainfall"]
        ip=[[temperature,humidity,ph,rainfall]]
        pred=model.predictions(ip)[0]


    #python file -> html
    return render_template("index.html",op=pred)

if __name__ == "__main__":
    app.run(debug=True)