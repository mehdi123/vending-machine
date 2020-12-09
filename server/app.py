import os
from flask import Flask, request

from vending_machine import VendingMachine

vm = VendingMachine()

app = Flask(__name__)

@app.route('/api/load_json', methods=['POST'])
def load_json():
    json_data = eval(request.json.get('json_data'))
    if vm.load_stock(json_data):
        return {"result": "success"}
    else:
        return {"result": "failed"}

@app.route('/api/items', methods=['GET'])
def get_items():
    return {"items": vm.get_items()}

@app.route('/api/insert_money', methods=['POST'])
def insert_money():
    print(request.json)
    money = request.json.get('money')
    if vm.insert_money(money):
        return {"result": "success"}
    else:
        return {"result": "failed"}

@app.route('/api/get_item', methods=['POST'])
def get_item():
    item_name = request.json.get('item_name')
    result = vm.get_item(item_name)
    if result[1]:
        return {"result": "success", "name": item_name}
    else:
        return {"result": "failed", "name": item_name}

if __name__ == '__main__':
    app.run(port=8000, debug=True)