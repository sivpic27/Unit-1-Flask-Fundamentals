from flask import Flask
app = Flask(__name__)

@app.route('/') # Front Door (Home Page)
def home():
    return "Home Page!"

@app.route('/about')
def about():
    return """<h1>Welcome</h1>
    <p>This is my first website<p>
    """

@app.route('/contact')
def contact():
    return "Contact Page!"

app.run(debug=True)