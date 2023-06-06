from pymongo import MongoClient

# MongoDB bağlantısı
username = "username"
password = "password"
cluster = "cluster_url"

# MongoDB bağlantısı
client = MongoClient(f"mongodb+srv://{username}:{password}@{cluster}/test?retryWrites=true&w=majority")

db = client.flaskmongodb
collection = db.Users

# Tüm kullanıcıları getiren sorgu
all_users = collection.find()
for user in all_users:
    print(user)

# İsmi Ahmet olan kullanıcıları getiren sorgu
ahmet_users = collection.find({"Name": "Ahmet"})
for user in ahmet_users:
    print(user)

# Yaşı 20'den fazla olan kullanıcıları getiren sorgu
age_gt_20_users = collection.find({"Age": {"$gt": 20}})
for user in age_gt_20_users:
    print(user)

# Yaşı 25'den fazla olan ve description'ı 0 olan kullanıcıları getiren sorgu
age_gt_25_desc_0_users = collection.find({"$and": [{"Age": {"$gt": 25}}, {"Description": 0}]})
for user in age_gt_25_desc_0_users:
    print(user)

# Yaşı 45-48 arasında olan kullanıcıları silen sorgu
age_range_users = collection.delete_many({"Age": {"$gte": 45, "$lte": 48}})
print(f"{age_range_users.deleted_count} kullanıcı silindi.")
