from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@db:3306/mydatabase'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Create the database tables within an application context
with app.app_context():
    db.create_all()

@app.route('/xyz/add', methods=['POST'])
def add_item():
    data = request.json
    new_item = Item(name=data['name'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'id': new_item.id}), 201

@app.route('/xyz/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])

@app.route('/add-item', methods=['GET', 'POST'])
def add_item_page():
    if request.method == 'POST':
        name = request.form['name']
        new_item = Item(name=name)
        db.session.add(new_item)
        db.session.commit()
        return f"Item '{name}' added with ID: {new_item.id}"
    return '''
    <form method="POST">
        <input type="text" name="name" placeholder="Enter item name" required>
        <input type="submit" value="Submit">
    </form>
    '''

@app.route('/xyz')
def xyz_index():
    return "Welcome to the XYZ API!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
