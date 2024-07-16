from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
  return render_template('home_page.html')

@app.route('/<anyroute>')
def default(anyroute):
  return redirect(url_for('home_page'))

if __name__ == '__main__':
  app.run(debug=True)