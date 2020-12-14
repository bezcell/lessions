products = []

while True:
    p_name = input("Введите название товара: ")
    p_cost = input("Введите цену товара: ")
    p_count = input("Введите количество товара: ")
    p_it = input("Введите единицу измерения товара: ")
    product = {
        'название': p_name,
        'цена': p_cost,
        'количество': p_count,
        'ед': p_it,
    }
    product_id = len(products) + 1
    product_item = (product_id, product)
    products.append(product_item)
    print(products)

    # аналитика
    a_names = set()
    a_costs = set()
    a_counts = set()
    a_it = set()
    for item in products:
        a_names.add(item[1]['название'])
        a_costs.add(item[1]['цена'])
        a_counts.add(item[1]['количество'])
        a_it.add(item[1]['ед'])

    print(a_names)
    print(a_costs)
    print(a_counts)
    print(a_it)
