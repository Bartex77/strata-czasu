from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.jinja')

@app.route('/about')
def about():
    return render_template('about.jinja')
  
@app.route('/warum')
def warum():
    return "Warum? Darum! Warum nicht?"

if __name__ == '__main__':
    app.run(debug=Flask, host="0.0.0.0", port=8080)