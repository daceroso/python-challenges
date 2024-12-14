def calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive):
    suma = 0
    count = 0
    for i in range(1, max_exclusive):
        if i % 2 == 0 or i % 7 == 0:
            count += 1
            suma += i
    return {"sum": suma, "count": count}

