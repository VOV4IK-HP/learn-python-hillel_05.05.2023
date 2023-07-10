import csv


def read_inventory(file):
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        inventory = []
        for row in reader:
            inventory.append(row)
    return inventory


def generate_id(inventory):
    id_index = {}
    for i, item in enumerate(inventory):
        item['id'] = i + 1
        id_index[i + 1] = item
    return id_index


def generate_category_index(inventory):
    category_index = {}
    for item in inventory:
        category = item['категория']
        id = item['id']
        if category not in category_index:
            category_index[category] = []
        category_index[category].append(id)
    return category_index


def generate_brand_index(inventory):
    brand_index = {}
    for item in inventory:
        brand = item['марка']
        id = item['id']
        if brand not in brand_index:
            brand_index[brand] = []
        brand_index[brand].append(id)
    return brand_index


def print_brand_stats(inventory):
    brand_stats = {}
    for item in inventory:
        brand = item['марка']
        if brand not in brand_stats:
            brand_stats[brand] = 0
        brand_stats[brand] += 1
    print("Статистика товаров по брендам:")
    for brand, count in brand_stats.items():
        print(f"{brand}: {count}")


def print_category_stats(inventory):
    category_stats = {}
    for item in inventory:
        category = item['категория']
        if category not in category_stats:
            category_stats[category] = 0
        category_stats[category] += 1
    print("Статистика товаров по категориям:")
    for category, count in category_stats.items():
        print(f"{category}: {count}")


def print_items_by_brand_and_category(inventory, brand, category):
    print(f"Товары бренда {brand} и категории {category}:")
    for item in inventory:
        if item['марка'] == brand and item['категория'] == category:
            print(item)


def calculate_brand_distribution(inventory):
    brand_distribution = {}
    for item in inventory:
        category = item['категория']
        brand = item['марка']
        if category not in brand_distribution:
            brand_distribution[category] = {}
        if brand not in brand_distribution[category]:
            brand_distribution[category][brand] = 0
        brand_distribution[category][brand] += 1
    return brand_distribution


def print_brand_distribution(brand_distribution):
    print("Распределение товаров по брендам для каждой категории:")
    for category, brands in brand_distribution.items():
        print(f"Категория: {category}")
        for brand, count in brands.items():
            print(f"{brand}: {count} товаров")
        print()


# Чтение файла
inventory = read_inventory('tech_inventory.csv')

# Генерация уникальных айди
id_index = generate_id(inventory)

# Генерация индекса по категориям
category_index = generate_category_index(inventory)

# Генерация индекса по брендам
brand_index = generate_brand_index(inventory)

# Вывод статистики по брендам и категориям
print_brand_stats(inventory)
print_category_stats(inventory)

# Вывод списка товаров выбранного бренда и категории
selected_brand = "Lenovo"
selected_category = "Ноутбуки"
print_items_by_brand_and_category(inventory, selected_brand, selected_category)

# Расчет и вывод распределения товаров по брендам для каждой категории
brand_distribution = calculate_brand_distribution(inventory)
print_brand_distribution(brand_distribution)
