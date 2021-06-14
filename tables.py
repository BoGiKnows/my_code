def restaurant(single_tables: int, double_tables: int, visitors: list) -> int:
    '''
    function takes number of single tables, number of double tables and a list of visitors
    to restaurant. Goal is to sit them at the tables.

    :param single_tables: integer
    :param double_tables: integer
    :param visitors: list
    :return: integer
        number of visitors who was denied to enter, because there were no tables for them
    '''
    dict_of_tables = {1: single_tables, 2: double_tables}
    double_tables_with_one_visitor = 0
    denied = 0

    for visitor in visitors:
        if visitor == 1:
            if dict_of_tables[1]:
                dict_of_tables[1] -= 1
            elif dict_of_tables[2]:
                dict_of_tables[2] -= 1
                double_tables_with_one_visitor += 1
            elif double_tables_with_one_visitor:
                double_tables_with_one_visitor -= 1
            else:
                denied += 1
        else:
            if dict_of_tables[2]:
                dict_of_tables[2] -= 1
            else:
                denied += 2

    return denied

test_data = (63, 40, [2, 2, 1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 2,
                      2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1,
                      1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 2, 1,
                      2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 2, 2,
                      2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 2,
                      2, 1, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 2, 2, 1, 2,
                      2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 1, 2, 2, 1, 2,
                      1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 1, 1,
                      1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2,
                      2, 1, 1, 2])

print(restaurant(*test_data))

