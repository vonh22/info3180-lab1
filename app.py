from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'My home page'

'''
# Routing for your application.
# Put your routes below this comment
'''


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
