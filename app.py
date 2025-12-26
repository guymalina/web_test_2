from flask import Flask, render_template, redirect, url_for, session
import os

app = Flask(__name__)

# Secret key from environment variable (Render)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret')

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    return render_template('index.html', counter=session['counter'])

@app.route('/increment')
def increment():
    session['counter'] = session.get('counter', 0) + 1
    return redirect(url_for('index'))

@app.route('/decrement')
def decrement():
    session['counter'] = session.get('counter', 0) - 1
    return redirect(url_for('index'))

# Local development only
if __name__ == '__main__':
    app.run(debug=True)
