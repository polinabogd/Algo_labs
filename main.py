def write_to_file(list_of_prices, discount_num):
    file = open("file.txt", 'w')
    for el in list_of_prices:
        file.write(str(el) + " ")
    file.write("\n" + str(discount_num))


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
        list_of_prices.insert((i * 3 + 2), round(max_el_in_end, 2))
    return list_of_prices


def counting_discount():
    input_data_prices = open_and_read_file("file.txt")
    discount_pers = (input_data_prices.pop(-1) / 100)
    sorted_prices_list = sorting_prices(input_data_prices, discount_pers)
    final_sum = sum(sorted_prices_list)
    return round(final_sum, 2)


if __name__ == '__main__':
    write_to_file([1, 2, 3, 4, 5, 6, 7], 100)
    print(counting_discount())
