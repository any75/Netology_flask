from flask import Flask, jsonify, request
app = Flask(__name__)
adv = []
adv_id = 1
@app.route('/adv', methods = ['POST'])
def create_ad():
    global adv_id
    ad = request.json
    ad['id'] = adv_id
    adv_id += 1
    return jsonify(ad), 201
@app.route('/adv', methods = ['GET'])
def get_adv():
    return jsonify(adv), 200
@app.route('/adv/<int:id_ad>', methods = ['DELETE'])
def delete_ad(id_ad):
    global adv
    adv = [ad for ad in adv if ad['id'] != id_ad]
    return jsonify({'message':'Объявление удалено'}), 200




app.run()