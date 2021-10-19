def open_and_read_file(url):
    price_data = []
    with open(url) as file:
        for line in file:
            price_data.extend([int(item) for item in line.split()])
    return price_data


def sorting_prices(list_of_prices: list, discount_pers):
    list_of_prices.sort()
    for i in range(len(list_of_prices) // 3):
        max_el_in_end = list_of_prices.pop(-1)
        max_el_in_end = max_el_in_end - (max_el_in_end * discount_pers)
        list_of_prices.insert((i*3+2), round(max_el_in_end, 2))
    return list_of_prices
