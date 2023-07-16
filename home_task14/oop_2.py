import os

from home_task14.Metrics import Metrics

csv_files = []
json_files = []

for file in os.listdir('folder_path'):
    if file.endswith('.csv'):
        csv_files.append(file)
    elif file.endswith('.json'):
        json_files.append(file)

metrics = Metrics()

for file in csv_files:
    metrics.read_csv(file)

for file in json_files:
    metrics.read_json(file)

metrics.build_indexes()

profit = metrics.calculate_profit()
lost_sku = metrics.calculate_lost_sku()
goods_through_warehouse = metrics.calculate_goods_through_warehouse()
sold_goods = metrics.calculate_sold_goods()
utilized_goods = metrics.calculate_utilized_goods()

print('Total profit:', profit)
print('Lost SKU:', lost_sku)
print('Goods through warehouse:', goods_through_warehouse)
print('Sold goods:', sold_goods)
print('Utilized goods:', utilized_goods)

folder_path = 'C:\Users\shali\PycharmProjects\learn-python-hillel_05.05.2023\home_task14\SKU'

csv_files = []
json_files = []

for file in os.listdir(folder_path):
    if file.endswith('.csv'):
        csv_files.append(file)
    elif file.endswith('.json'):
        json_files.append(file)
