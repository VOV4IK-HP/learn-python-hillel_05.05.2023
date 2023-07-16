import os
import csv
import json


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
        self.operation_cost = float(operation_cost)
        self.comment = comment

    def str(self):
        return f"Event(date={self.date}, time={self.time}, sku={self.sku}, warehouse={self.warehouse}, warehouse_cell_id={self.warehouse_cell_id}, operation={self.operation}, invoice={self.invoice}, expiration_date={self.expiration_date}, operation_cost={self.operation_cost}, comment={self.comment})"


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


# Класс для хранения индексов
class Index:
    def init(self, data, key):
        self.index = {}
        for item in data:
            value = getattr(item, key)
            if value not in self.index:
                self.index[value] = []
            self.index[value].append(item)

    def get_items_by_key(self, value):
        if value in self.index:
            return self.index[value]
        return []


# Класс для вычисления метрик по данным
def metricsCalculator(events, metricsCalculator=None):
    def init(self, events):
        self.events = events

    def calculate_profit(self):
        profit = sum(event.operation_cost for event in self.events if event.operation == "sale")
        return profit

    def calculate_lost_skus(self):
        lost_skus = set()
        for event in self.events:
            if event.expiration_date and event.operation != "sale":
                lost_skus.add(event.sku)
        return len(lost_skus)

    def calculate_items_per_warehouse(self):
        warehouses = set(event.warehouse for event in self.events)
        items_per_warehouse = {warehouse: sum(1 for event in self.events if event.warehouse == warehouse) for warehouse
                               in warehouses}
        return items_per_warehouse

    def calculate_sold_items_per_warehouse(self):
        warehouses = set(event.warehouse for event in self.events)
        sold_items_per_warehouse = {
            warehouse: sum(1 for event in self.events if event.warehouse == warehouse and event.operation == "sale") for
            warehouse in warehouses}
        return sold_items_per_warehouse

    def calculate_utilized_items_per_warehouse(self):
        warehouses = set(event.warehouse for event in self.events)
        utilized_items_per_warehouse = {
            warehouse: sum(1 for event in self.events if event.warehouse == warehouse and event.operation == "dispose")
            for warehouse in warehouses}
        return utilized_items_per_warehouse

    # Чтение и анализ данных
    fileReader = FileReader("home_task14\SKU")
    events = fileReader.read_files()

    index_sku = Index(events, "sku")
    index_warehouse = Index(events, "warehouse")
    index_operation = Index(events, "operation")
    metricsCalculator = metricsCalculator(events)

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
