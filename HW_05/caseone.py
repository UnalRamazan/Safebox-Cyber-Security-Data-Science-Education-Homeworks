import random
from pymongo import MongoClient

# MongoDB bağlantısı
username = "username"
password = "password"
cluster = "cluster_url"

# MongoDB bağlantısı
client = MongoClient(f"mongodb+srv://{username}:{password}@{cluster}/test?retryWrites=true&w=majority")

db = client.flaskmongodb
collection = db.Users

# 50 adet random kullanıcı ekleme
for _ in range(50):
    name = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=5))
    age = random.randint(0, 50)
    job = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=7))
    collection.insert_one({"Name": name, "Age": age, "Job": job, "Description": 1})

print("50 adet random kullanıcı eklendi.")
