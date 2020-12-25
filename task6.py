data = {}
with open("task6.txt", "r") as user_file:
    for user_line in user_file.readlines():
        lesion_and_hours = user_line.split(": ")
        lesion = lesion_and_hours[0]
        hours = lesion_and_hours[1]
        hours_types = hours.split(" ")
        lesion_hours = 0
        for h_iter in hours_types:
            if h_iter != '-' and h_iter != "-\n":
                h_iter_nums = h_iter.split("(")
                num = int(h_iter_nums[0])
                lesion_hours += num
        data[lesion] = lesion_hours
print(data)
