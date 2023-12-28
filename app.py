from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Czysta Strata Czasu, mon..."
  
@app.route('/warum')
def about():
    return "Warum? Darum! Warum nicht?"

if __name__ == '__main__':
    app.run(debug=Flask, host="0.0.0.0", port=8080)