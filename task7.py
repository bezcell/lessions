from json import dump

my_list = []
profits = []
company_count = 0


def list_sum(a_list):
    res = 0
    for a_item in a_list:
        res += a_item
    return res


with open("task7.txt", "r") as user_file:
    firms = {}
    for user_line in user_file.readlines():
        words_list = user_line.split(" ")
        company_profit = int(words_list[2]) - int(words_list[3])
        if company_profit > 0:
            profits.append(company_profit)
            company_count += 1
        firms[words_list[0]] = company_profit
    average_profit = {'average_profit': list_sum(profits) / company_count}
    my_list.append(firms)
    my_list.append(average_profit)

with open("debug.txt", "a") as save_file:
    dump(my_list, save_file)
