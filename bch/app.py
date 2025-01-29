from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Sample data
items = [
    {"name": "Item A", "price": 10.99},
    {"name": "Item B", "price": 23.49},
    {"name": "Item C", "price": 5.99},
    {"name": "Item D", "price": 15.75},
]

@app.route('/')  # Root route
def home():
    return render_template('index.html')

@app.route('/get_price', methods=['GET'])
def get_items():
    print(jsonify(items))
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True, port = 5500)
