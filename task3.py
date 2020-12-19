# 241 - потому что число 240 не попало бы в интервал :)
my_result = [item for item in range(20, 241) if item % 20 == 0 or item % 21 == 0]
print(my_result)
