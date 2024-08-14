from flask import Flask, render_template

'''
it creates an instance of Flask class
which will be our WSGI application
'''
# WSGI (Web Server Gateway Interface) application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "<htmml><body><h1>Welcome to home page</h1></body></html>"

@app.route('/index')
def index():
    return "<htmml><body><h1>Welcome to index page</h1></body></html>"

@app.route('/about')
def about():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True) # run the flask app and turn on debug mode, save data and relode server