import os
import csv
import json
from datetime import datetime


# Класс для представления события
class Event:
    def init(self, date, time, sku, warehouse, warehouse_cell_id, operation, invoice, expiration_date, operation_cost,
             comment):
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


# Класс для чтения данных из файлов и определения их типа
class FileReader:
    def init(self, directory):
        self.directory = directory

    def read_files(self):
        events = []
        for filename in os.listdir(self.directory):
            filepath = os.path.join(self.directory, filename)
            if filename.endswith(".csv"):
                events += self.read_csv(filepath)
            elif filename.endswith(".json"):
                events += self.read_json(filepath)
        return events

    def read_csv(self, filepath):
        events = []
        with open(filepath, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                event = Event(*row)
                events.append(event)
        return events

    def read_json(self, filepath):
        events = []
        with open(filepath, "r") as file:
            data = json.load(file)
            for item in data:
                event = Event(**item)
                events.append(event)
        return events


# Класс для вычисления метрик по данным
class MetricsCalculator:
    def init(self, events):
        self.events = events

    def calculate_profit(self):
        profit = 0
        for event in self.events:
            if event.operation == "sale":
                profit += event.operation_cost
        return profit

    def calculate_lost_skus(self):
        lost_skus = set()
        for event in self.events:
            if event.expiration_date and event.operation != "sale":
                lost_skus.add(event.sku)
        return len(lost_skus)

    def calculate_items_per_warehouse(self):
        items_per_warehouse = {}
        for event in self.events:
            if event.warehouse not in items_per_warehouse:
                items_per_warehouse[event.warehouse] = 0
            items_per_warehouse[event.warehouse] += 1
        return items_per_warehouse

    def calculate_sold_items_per_warehouse(self):
        sold_items_per_warehouse = {}
        for event in self.events:
            if event.operation == "sale":
                if event.warehouse not in sold_items_per_warehouse:
                    sold_items_per_warehouse[event.warehouse] = 0
                sold_items_per_warehouse[event.warehouse] += 1
        return sold_items_per_warehouse

    def calculate_utilized_items_per_warehouse(self):
        utilized_items_per_warehouse = {}
        for event in self.events:
            if event.operation == "dispose":
                if event.warehouse not in utilized_items_per_warehouse:
                    utilized_items_per_warehouse[event.warehouse] = 0
                utilized_items_per_warehouse[event.warehouse] += 1
        return utilized_items_per_warehouse


# Класс для создания индексов
class IndexBuilder:
    def init(self, events):
        self.events = events
        self.sku_index = {}
        self.warehouse_index = {}
        self.operation_index = {}

    def build_indexes(self):
        for event in self.events:
            if event.sku not in self.sku_index:
                self.sku_index[event.sku] = []
            self.sku_index[event.sku].append(event)

            if event.warehouse not in self.warehouse_index:
                self.warehouse_index[event.warehouse] = []
            self.warehouse_index[event.warehouse].append(event)


    if event.operation not in self.operation_index:
        self.operation_index[event.operation] = []
    self.operation_index[event.operation].append(event)


    def get_events_by_sku(self, sku):
        if sku in self.sku_index:
            return self.sku_index[sku]
        return []


    def get_events_by_warehouse(self, warehouse):
        if warehouse in self.warehouse_index:
            return self.warehouse_index[warehouse]
        return []


    def get_events_by_operation(self, operation):
        if operation in self.operation_index:
            return self.operation_index[operation]
        return []


    # Чтение и анализ данных
    fileReader = FileReader("path/to/directory")
    events = fileReader.read_files()

    indexBuilder = IndexBuilder(events)
    indexBuilder.build_indexes()

    metricsCalculator = MetricsCalculator(events)

    profit = metricsCalculator.calculate_profit()
    print("Total profit: $", profit)

    lost_skus = metricsCalculator.calculate_lost_skus()
    print("Number of lost SKUs:", lost_skus)

    items_per_warehouse = metricsCalculator.calculate_items_per_warehouse()
    for warehouse, count in items_per_warehouse.items():
        print("Items in warehouse", warehouse + ":", count)

    sold_items_per_warehouse = metricsCalculator.calculate_sold_items_per_warehouse()
    for warehouse, count in sold_items_per_warehouse.items():
        print("Sold items from warehouse", warehouse + ":", count)

    utilized_items_per_warehouse = metricsCalculator.calculate_utilized_items_per_warehouse()
    for warehouse, count in utilized_items_per_warehouse.items():
        print("Utilized items from warehouse", warehouse + ":", count)
