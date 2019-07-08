# SIMPLE REST API WITH FLASK
# IMPORT
from flask import Flask, jsonify, request , render_template       #jsonify is class in Flask

app2 = Flask(__name__)

stores = [
    {
        'name' : 'MyWonderfulStore',
        'items': [
            {
                'name' : 'MyItems',
                'price': '15.99'
            },
            {
                'name' : 'MyItems2',
                'price': '20.11'
            }
        ] 
    }
]


@app2.route('/')
def home():
    print ("Hello This Is My Second App Using Flask")
    return render_template('index.html')

# INSERT DATA STORE
@app2.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    print(new_store)
    stores.append(new_store)
    return jsonify(new_store)

# GET LIST OF STORE
@app2.route('/store/')
def get_stores():
        return jsonify({'stores' : stores})                      #  example :it will be store to JSON suing dictionary format


# GET SOME DATA FROM THE STORE
@app2.route('/store/<string:name>')
def get_store(name):
    # Iterate over stores 
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message' : 'store not found'})

# UPDATE STORE
@app2.route('/update/store/<string:old_name>',methods=['PUT'])
def update_store(old_name):
    request_data = request.get_json()
    for store in stores:
        if store['name']==old_name:
            store['name']=request_data['name']
            print(request_data['name'])
            print(old_name)
            print("yeeeee")
            return jsonify(store)
    return stores

# DELETE STORE
@app2.route('/remove/store/<string:name>',methods=['DELETE'])
def remove_store(name):
    for store in stores:
        if store['name']==name:
            stores.remove(store)
            return jsonify(stores)
    return stores



### ITEM
# INSERT ITEM
@app2.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name']==name:
            new_item = {
                'name' : request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message' : 'store not found'})

# GET ITEMS FROM THE STORE
@app2.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message' : 'store not found'})

# UPDATE ITEM
@app2.route('/update/store/<string:store_name>/items/<string:old_item_name>',methods=['PUT'])
def update_item_store(store_name,old_item_name):
    request_data = request.get_json()
    for store in stores:
        if store['name']==store_name :
            for item in store['items']:
                if item['name']==old_item_name:
                    item['name']=request_data['name']
                    item['price']=request_data['price']
                    print(request_data['name'])
                    print(request_data['price'])
                    print(old_item_name)
                    print("yeeeee")
                return jsonify(store)
            return jsonify(store)
        return jsonify(store)
    return jsonify(store)
# DELETE ITEM
@app2.route('/remove/store/<string:name>/items/<string:item_name>',methods=['DELETE'])
def remove_item_store(name, item_name):
    for store in stores:
        if store['name']==name:
            itemes= store['items']
            for item in itemes:
                if item['name'] == item_name:
                    itemes.remove(item)
                    return jsonify(stores)
            print(items)
            return items
    return stores


app2.run(port=5000)