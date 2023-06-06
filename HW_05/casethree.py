from flask import Flask, jsonify, request
from pymongo import MongoClient

# Flask uygulaması
app = Flask(__name__)

# MongoDB bağlantısı
username = "username"
password = "password"
cluster = "cluster_url"

# MongoDB bağlantısı
client = MongoClient(f"mongodb+srv://{username}:{password}@{cluster}/test?retryWrites=true&w=majority")

db = client.flaskmongodb
collection = db.Users


# Kullanıcı ekleme endpoint
@app.route('/adduser', methods=['POST'])
def add_user():
    name = request.json['name']
    age = request.json['age']
    job = request.json['job']
    collection.insert_one({"Name": name, "Age": age, "Job": job, "Description": 1})
    return jsonify({"message": "Kullanıcı başarıyla eklendi."})


# Yaşı 25'ten fazla olan kullanıcıları döndüren endpoint
@app.route('/25', methods=['GET'])
def get_users_above_25():
    users = collection.find({"Age": {"$gt": 25}})
    result = []
    for user in users:
        result.append(user)
    return jsonify(result)


# Tüm kullanıcıları döndüren endpoint
@app.route('/', methods=['GET'])
def get_all_users():
    users = collection.find()
    result = []
    for user in users:
        result.append(user)
    return jsonify(result)


# Verilen id'ye göre kullanıcıyı silen endpoint
@app.route('/deleteuser', methods=['POST', 'DELETE'])
def delete_user():
    user_id = request.json['id']
    collection.delete_one({"_id": user_id})
    return jsonify({"message": "Kullanıcı başarıyla silindi."})


if __name__ == '__main__':
    app.run()
