from flask import Flask, render_template
from app import app
app = Flask(__name__,template_folder="app/templates")          
                                                          
@app.route("/")
def hello():
    return render_template('index.html') 

if __name__ == "__main__":
     app.run()