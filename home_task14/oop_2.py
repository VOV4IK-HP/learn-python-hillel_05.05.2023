import os
import csv
import json
import datetime


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

    def get_sku(self):
        return self.sku

    def get_warehouse(self):
        return self.warehouse

    def get_operation(self):
        return self.operation

    def get_operation_cost(self):
        return self.operation_cost


class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        pass


class CSVFileReader(FileReader):
    def __init__(self, file_path):
        super().__init__(file_path)

    def read_file(self):
        events = []

        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            for row in reader:
                event = Event(*row)
                events.append(event)

        return events


class JSONFileReader(FileReader):
    def __init__(self, file_path):
        super().__init__(file_path)

    def read_file(self):
        events = []

        with open(self.file_path, 'r') as file:
            data = json.load(file)
            for item in data:
                event = Event(*item.values())
                events.append(event)

        return events


class DataManager:
    def __init__(self, events):
        self.events = events

    def calculate_profit(self):
        sale_costs = [event.get_operation_cost() for event in self.events if event.get_operation() == 'sale']
        total_profit = sum(sale_costs)
        return total_profit

    def calculate_lost_skus(self):
        lost_skus = set()
        for event in self.events:
            if event.get_operation() != 'sale' and event.expiration_date < datetime.date.today():
                lost_skus.add(event.get_sku())
        return len(lost_skus)

    def calculate_products_per_warehouse(self):
        products_per_warehouse = {}
        for event in self.events:
            warehouse = event.get_warehouse()
            if warehouse not in products_per_warehouse:
                products_per_warehouse[warehouse] = 0
            products_per_warehouse[warehouse] += 1
        return products_per_warehouse

    def calculate_sold_products_per_warehouse(self):
        sold_products_per_warehouse = {}
        for event in self.events:
            if event.get_operation() == 'sale':
                warehouse = event.get_warehouse()
                if warehouse not in sold_products_per_warehouse:
                    sold_products_per_warehouse[warehouse] = 0
                sold_products_per_warehouse[warehouse] += 1
        return sold_products_per_warehouse

    def calculate_disposed_products_per_warehouse(self):
        disposed_products_per_warehouse = {}
        for event in self.events:
            if event.get_operation() == 'dispose':
                warehouse = event.get_warehouse()
                if warehouse not in disposed_products_per_warehouse:
                    disposed_products_per_warehouse[warehouse] = 0
                disposed_products_per_warehouse[warehouse] += 1
        return disposed_products_per_warehouse


class DataProcessor:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def process_data(self):
        files = self.get_files_from_directory()

        events = []

        for file in files:
            file_reader = None
            if file.endswith('.csv'):
                file_reader = CSVFileReader(file)
            elif file.endswith('.json'):
                file_reader = JSONFileReader(file)
            events += file_reader.read_file()

        data_manager = DataManager(events)

        profit = data_manager.calculate_profit()
        lost_skus = data_manager.calculate_lost_skus()
        products_per_warehouse = data_manager.calculate_products_per_warehouse()
        sold_products_per_warehouse = data_manager.calculate_sold_products_per_warehouse()
        disposed_products_per_warehouse = data_manager.calculate_disposed_products_per_warehouse()

    def get_files_from_directory(self):
        files = []
        for file in os.listdir(self.directory_path):
            file_path = os.path.join(self.directory_path, file)
            if os.path.isfile(file_path):
                files.append(file_path)
        return files


data_processor = DataProcessor('SKU')
data_processor.process_data()
