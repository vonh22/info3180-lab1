from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'My home page'

'''
# Routing for your application.
# Put your routes below this comment
'''


@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

