def filtration(items):
    average_price = sum(item['цена'] for item in items) / len(items)
    max_price = [item for item in items if item['цена'] > average_price]
    print(max_price)

items = [
    {"название": "Ноутбук", "цена": 30000},
    {"название": "Телевизор", "цена": 20000},
    {"название": "Кофеварка", "цена": 5000},
    {"название": "Смартфон", "цена": 25000}]

filtration(items)