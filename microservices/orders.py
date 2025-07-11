from flask import Flask, jsonify
import requests

app = Flask(__name__)

orders = {
    100: {"user_id": 1, "product": "Laptop"},
    101: {"user_id": 2, "product": "Smartphone"}
}

@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    
    # Call User Service to get user details
    user_response = requests.get(f"http://localhost:5001/user/{order['user_id']}")
    if user_response.status_code == 200:
        user_data = user_response.json()
        return jsonify({
            "order_id": order_id,
            "product": order["product"],
            "user": user_data
        })
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(port=5002)  # Runs on port 5002
