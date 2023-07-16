import csv
import json
import os


# Создаем класс для представления события
class Event:
    def __init__(self, date, time, sku, warehouse, warehouse_cell_id, operation, invoice, expiration_date,
                 operation_cost, comment):
        self.date = date
        self.time = time
        self.sku = sku
        self.warehouse = warehouse
        self.warehouse_cell_id = warehouse_cell_id
        self.operation = operation
        self.invoice = invoice
        self.expiration_date = expiration_date
        self.operation_cost = operation_cost
        self.comment = comment


# Создаем класс для хранения всех событий и выполнения метрик
class Metrics:
    def __init__(self):
        self.events = []  # список для хранения всех событий
        self.index_sku = {}  # индекс по колонке sku
        self.index_warehouse = {}  # индекс по колонке warehouse
        self.index_operation = {}  # индекс по колонке operation
        self.profit = 0  # прибыль от всех операций типа sale
        self.lost_skus = set()  # уникальные SKU, которые были потеряны
        self.total_products_per_warehouse = {}  # количество товаров в каждом составе (warehouse)
        self.disposed_products_per_warehouse = {}  # количество утилизированных товаров по каждому составу (warehouse)

    def read_data(self):
        directory = '/home_task14/SKU'  # путь к директории с файлами
        for filename in os.listdir(directory):
            if filename.endswith(".csv"):
                filepath = os.path.join(directory, filename)
                self.read_csv(filepath)
            elif filename.endswith(".json"):
                filepath = os.path.join(directory, filename)
                self.read_json(filepath)

    # Чтение данных из CSV файла
    def read_csv(self, filepath):
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # пропускаем заголовок
            for row in reader:
                event = Event(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                self.events.append(event)
                self.update_indexes(event)

    # Чтение данных из JSON файла
    def read_json(self, filepath):
        with open(filepath, 'r') as file:
            data = json.load(file)
            for item in data:
                event = Event(item['date'],
                              item['time'],
                              item['sku'],
                              item['warehouse'],
                              item['warehouse_cell_id'],
                              item['operation'],
                              item['invoice'],
                              item['expiration_date'],
                              item['operation_cost'],
                              item['comment'])
                self.events.append(event)
                self.update_indexes(event)

    # Обновление индексов
    def update_indexes(self, event):
        # Индекс по колонке sku
        if event.sku in self.index_sku:
            self.index_sku[event.sku].append(event)
        else:
            self.index_sku[event.sku] = [event]

        # Индекс по колонке warehouse
        if event.warehouse in self.index_warehouse:
            self.index_warehouse[event.warehouse].append(event)
        else:
            self.index_warehouse[event.warehouse] = [event]

        # Индекс по колонке operation
        if event.operation in self.index_operation:
            self.index_operation[event.operation].append(event)
        else:
            self.index_operation[event.operation] = [event]

    # Вычисление метрик
    def calculate_metrics(self):
        for event in self.events:
            # Вычисление прибыли от всех операций типа sale
            if event.operation == 'sale':
                self.profit += float(event.operation_cost)

            # Проверка, если expiration_date прошло и sale не произошло, добавляем SKU в список потерянных
            if event.operation != 'sale' and event.expiration_date != '' and event.date > event.expiration_date:
                self.lost_skus.add(event.sku)

            # Подсчет количества товаров в каждом составе (warehouse)
            if event.warehouse in self.total_products_per_warehouse:
                self.total_products_per_warehouse[event.warehouse] += 1
            else:
                self.total_products_per_warehouse[event.warehouse] = 1

                # Подсчет количества утилизированных товаров по каждому составу (warehouse)
                if event.operation == 'dispose':
                    if event.warehouse in self.disposed_products_per_warehouse:
                        self.disposed_products_per_warehouse[event.warehouse] += 1
                    else:
                        self.disposed_products_per_warehouse[event.warehouse] = 1

                # Создаем объект класса Metrics
                metrics = Metrics()

                # Чтение данных и вычисление метрик
                metrics.read_data()
                metrics.calculate_metrics()

                # Вывод результатов
                print("Прибыль от всех операций типа sale:", metrics.profit)
                print("Количество уникальных SKU, которые были потеряны:", len(metrics.lost_skus))
                print("Количество товаров в каждом составе (warehouse):", metrics.total_products_per_warehouse)
                print("Количество утилизированных товаров по каждому составу (warehouse):",
                      metrics.disposed_products_per_warehouse)
