from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return "Hi!"

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html', phone = 22937291)
if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 5232, threaded = True, debug = True)