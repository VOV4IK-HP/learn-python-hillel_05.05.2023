import csv
import json


class Metrics:
    def __init__(self):
        self.data = []
        self.sku_index = {}
        self.warehouse_index = {}
        self.operation_index = {}

    def read_csv(self, file):
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.data.append(row)

    def read_json(self, file):
        with open(file, 'r') as f:
            data = json.load(f)
            for row in data:
                self.data.append(row)

    def build_indexes(self):
        for d in self.data:
            sku = d['sku']
            warehouse = d['warehouse']
            operation = d['operation']

            if sku not in self.sku_index:
                self.sku_index[sku] = []
            self.sku_index[sku].append(d)

            if warehouse not in self.warehouse_index:
                self.warehouse_index[warehouse] = []
            self.warehouse_index[warehouse].append(d)

            if operation not in self.operation_index:
                self.operation_index[operation] = []
            self.operation_index[operation].append(d)

    def calculate_profit(self):
        return sum(float(d['operation_cost']) for d in self.data if d['operation'] == 'sale')

    def calculate_lost_sku(self):
        lost_sku = set()
        for d in self.data:
            if d['operation'] == 'dispose' and d['expiration_date'] != '' and d['sku'] not in lost_sku:
                lost_sku.add(d['sku'])
        return len(lost_sku)

    def calculate_goods_through_warehouse(self):
        goods_through_warehouse = {}
        for d in self.data:
            warehouse = d['warehouse']
            if warehouse not in goods_through_warehouse:
                goods_through_warehouse[warehouse] = 0
            goods_through_warehouse[warehouse] += 1
        return goods_through_warehouse

    def calculate_sold_goods(self):
        sold_goods = {}
        for d in self.data:
            if d['operation'] == 'sale':
                warehouse = d['warehouse']
                if warehouse not in sold_goods:
                    sold_goods[warehouse] = 0
                sold_goods[warehouse] += 1
        return sold_goods

    def calculate_utilized_goods(self):
        utilized_goods = {}
        for d in self.data:
            if d['operation'] == 'dispose':
                warehouse = d['warehouse']
                if warehouse not in utilized_goods:
                    utilized_goods[warehouse] = 0
                utilized_goods[warehouse] += 1
        return utilized_goods
