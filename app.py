from flask import Flask


app = Flask(__name__, instance_relative_config=True)

# Load the views
import views

# Load the config file
app.config.from_object('config')

if __name__ == '__main__':
    """starting app"""
    app.run()

