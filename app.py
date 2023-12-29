from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.j2')


@app.route('/about')
def about():
    return render_template('about.j2')

@app.route('/warum')
def warum():
    param1 = request.args.get('param1', default = 'default_value1', type = str)
    param2 = request.args.get('param2', default = 'default_value2', type = str)
    # Use the parameters in your function as needed
    return render_template('warum.jinja', param1=param1, param2=param2)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)