"""Flask application for CPS3500 Assignment."""

from flask import Flask, render_template

# Create Flask instance
app = Flask(__name__)

# Default route
@app.route('/')
def home():
    """Display the default homepage."""
    return "Hello CPS3500!"

# New route
@app.route('/new_page')
def new_page():
    """Display the new page message."""
    return "This is a New Page!"

# Route with a variable + render template
@app.route('/user/<username>')
def user(username):
    """Render a template and greet the user."""
    return render_template("user.html", username=username)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
