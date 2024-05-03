from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'Hello, World!'

# Define a route for a custom page
@app.route('/about')
def about():
    return 'About Page'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
