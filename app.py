from flask import Flask, render_template, request                     
app = Flask(__name__,template_folder="app/templates")          
                                                          
@app.route("/")
def hello():
    return render_template('index.html') 

if __name__ == "__main__":
     app.run(debug=True ,use_reloader=False)