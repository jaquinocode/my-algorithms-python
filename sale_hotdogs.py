def sale_hotdogs(customers):
    # price changes depending on customers val
    price = 100 if customers < 5 else 95 if 5 <= customers < 10 else 90

    return customers * price


input_num = int(input())  # do a thing
result = sale_hotdogs(input_num)  # do another thing
print(result)  # do it
