from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client.dbhomework


@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    orders = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive,

    }

    db.candleOrders.insert_one(orders)
    return jsonify({'result': 'success'})


@app.route('/order', methods=['GET'])

def view_orders():
    orders = list(db.candleOrders.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)