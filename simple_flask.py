
from flask import Flask

# Create Flask app
app = Flask(__name__)

# Define a route
@app.route('/login')
def home():
    return "Hello, World! This is my first Flask app."

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
