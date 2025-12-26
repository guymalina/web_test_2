from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

@app.route('/')
def index():
    # Initialize counter to 0 if not set
    if 'counter' not in session:
        session['counter'] = 0
    return render_template('index.html', counter=session['counter'])

@app.route('/increment')
def increment():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return redirect(url_for('index'))

@app.route('/decrement')
def decrement():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] -= 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

