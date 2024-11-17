from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids SQLAlchemy warnings
db = SQLAlchemy(app)


# ORM Model
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return f"{self.name} - {self.description}"

    def to_dict(self):
        """Helper method to convert object to dictionary."""
        return {"id": self.id, "name": self.name, "description": self.description}


# Routes
@app.route('/')
def index():
    return "Welcome to the Drinks API!"


@app.route('/drinks')
def get_drinks():
    """Fetch all drinks from the database."""
    drinks = Drink.query.all()
    return jsonify([drink.to_dict() for drink in drinks])


# Ensure database is initialized
with app.app_context():
    db.create_all()  # Create database tables
    # Add a sample drink if the table is empty
    if not Drink.query.first():
        drink = Drink(name="Grape", description="Tastes like grapes")
        
        db.session.add(drink)
        db.session.commit()
        print("Sample drink added successfully!")


if __name__ == '__main__':
    app.run(debug=True)
