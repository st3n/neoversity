from pymongo import MongoClient
from bson.objectid import ObjectId

# Підключення до MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["db"]
collection = db["cats"]


# Створення (Create)
def create_cat(name, age, features):
    cat = {"name": name, "age": age, "features": features}
    result = collection.insert_one(cat)
    return result.inserted_id


# Читання (Read)
def get_all_cats():
    return list(collection.find())


def get_cat_by_name(name):
    return collection.find_one({"name": name})


# Оновлення (Update)
def update_cat_age_by_name(name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    return result.modified_count


def add_feature_by_name(name, feature):
    result = collection.update_one({"name": name}, {"$addToSet": {"features": feature}})
    return result.modified_count


# Видалення (Delete)
def delete_cat_by_name(name):
    result = collection.delete_one({"name": name})
    return result.deleted_count


def delete_all_cats():
    result = collection.delete_many({})
    return result.deleted_count


# Основна функція для демонстрації
if __name__ == "__main__":
    # Створення кота
    cat_id = create_cat("manny", 3, ["ходить в окулярах", "дає себе гладити", "рудий"])
    print(f"Inserted cat with ID: {cat_id}")

    # Отримання всіх котів
    print("All cats:")
    for cat in get_all_cats():
        print(cat)

    # Отримання кота за ім'ям
    name = "manny"
    cat = get_cat_by_name(name)
    if cat:
        print(f"Cat found: {cat}")
    else:
        print(f"Cat with name {name} not found")

    # Оновлення віку кота за ім'ям
    new_age = 4
    modified_count = update_cat_age_by_name(name, new_age)
    print(f"Updated age for {name}, modified count: {modified_count}")

    # Додавання нової характеристики до списку features
    new_feature = "любить молодих кішечок"
    modified_count = add_feature_by_name(name, new_feature)
    print(f"Added feature for {name}, modified count: {modified_count}")

    # Видалення кота за ім'ям
    deleted_count = delete_cat_by_name(name)
    print(f"Deleted count for {name}: {deleted_count}")

    # Видалення всіх котів
    deleted_count = delete_all_cats()
    print(f"Deleted all cats, count: {deleted_count}")

"""
❯ /opt/anaconda3/envs/goit-algo/bin/python /Users/igor.gala/neoversity/goit-cs-hw/hw/db/task2/main.py
Inserted cat with ID: 669cb6ce61a8d98c1d2a24d1
All cats:
{'_id': ObjectId('669cb3113461c0d31583266d'), 'name': 'Lama', 'age': 2, 'features': ['ходить в лоток', 'не дає себе гладити', 'сірий']}
{'_id': ObjectId('669cb3113461c0d31583266e'), 'name': 'Liza', 'age': 4, 'features': ['ходить в лоток', 'дає себе гладити', 'білий']}
{'_id': ObjectId('669cb3113461c0d31583266f'), 'name': 'Boris', 'age': 12, 'features': ['ходить в лоток', 'не дає себе гладити', 'сірий']}
{'_id': ObjectId('669cb3113461c0d315832670'), 'name': 'Murzik', 'age': 1, 'features': ['ходить в лоток', 'дає себе гладити', 'чорний']}
{'_id': ObjectId('669cb31d3461c0d315832671'), 'name': 'barsik', 'age': 3, 'features': ['ходить в капці', 'дає себе гладити', 'рудий']}
{'_id': ObjectId('669cb6ce61a8d98c1d2a24d1'), 'name': 'manny', 'age': 3, 'features': ['ходить в окулярах', 'дає себе гладити', 'рудий']}
Cat found: {'_id': ObjectId('669cb6ce61a8d98c1d2a24d1'), 'name': 'manny', 'age': 3, 'features': ['ходить в окулярах', 'дає себе гладити', 'рудий']}
Updated age for manny, modified count: 1
Added feature for manny, modified count: 1
Deleted count for manny: 1
Deleted all cats, count: 5
"""
