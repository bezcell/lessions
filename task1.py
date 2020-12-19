from sys import argv


hours = int(argv[1])
pay_by_hour = int(argv[2])
premium = int(argv[3])


print((hours * pay_by_hour) + premium)
