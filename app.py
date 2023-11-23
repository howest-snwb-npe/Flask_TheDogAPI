from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/search")
def search():
    breed = request.args.get("breed")
    
    # call dog api
    r = requests.get(f"https://api.thedogapi.com/v1/breeds/search?q={breed}")
    print(r.json())   
    
    for dog in r.json():
        print(dog)
           
    return render_template("search.html", breed=breed, output=r.json())

if __name__ == "__main__":
    app.run()