import csv
import random


def read_csv(file):
    data = []
    with open(file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)
    return data


def generate_id():
    return random.randint(1, 1000)


def create_id_index(data):
    id_index = {}
    for item in data:
        item_id = generate_id()
        item['id'] = item_id
        id_index[item_id] = item
    return id_index


def create_category_index(data):
    category_index = {}
    for item in data:
        category = item['category']
        if category not in category_index:
            category_index[category] = []
        category_index[category].append(item['id'])
    return category_index


def create_brand_index(data):
    brand_index = {}
    for item in data:
        brand = item['brand']
        if brand not in brand_index:
            brand_index[brand] = []
        brand_index[brand].append(item['id'])
    return brand_index


def print_brand_stats(brand_index):
    for brand, ids in brand_index.items():
        print(f"{brand}: {len(ids)} товаров")


def print_category_stats(category_index):
    for category, ids in category_index.items():
        print(f"{category}: {len(ids)} товаров")


def print_items_by_brand_and_category(data, brand, category):
    items = [item for item in data if item['brand'] == brand and item['category'] == category]
    for item in items:
        print(f"Товар #{item['id']}:")
        print(f"Модель: {item['модель']}")
        print(f"Категория: {item['category']}")
        print(f"Бренд: {item['brand']}")
        print(f"Цена: {item['price']}")
        print()


def print_brand_distribution_by_category(data):
    brand_distribution = {}
    for item in data:
        category = item['category']
        brand = item['brand']
        if category not in brand_distribution:
            brand_distribution[category] = {}
        if brand not in brand_distribution[category]:
            brand_distribution[category][brand] = 0
        brand_distribution[category][brand] += 1

    for category, brands in brand_distribution.items():
        print(f"Категория: {category}")
        for brand, count in brands.items():
            print(f"{count} товаров от {brand}")
        print()


data = read_csv('tech_inventory.csv')
id_index = create_id_index(data)
category_index = create_category_index(data)
brand_index = create_brand_index(data)

print("Статистика по брендам:")
print_brand_stats(brand_index)
print()

print("Статистика по категориям:")
print_category_stats(category_index)
print()

print("Товары выбранного бренда и категории:")
print_items_by_brand_and_category(data, 'Apple', 'Смартфоны')
print()

print("Распределение товаров по брендам для каждой категории:")
print_brand_distribution_by_category(data)
