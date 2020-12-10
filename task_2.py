# task 2
seconds_input = int(input('Please, input time in seconds here: '))
hours = seconds_input // 3600

other_seconds = seconds_input - (hours * 3600)
minutes = other_seconds // 60

seconds = seconds_input - ((hours * 3600) + (minutes * 60))

print(f"{hours}:{minutes}:{seconds}")
