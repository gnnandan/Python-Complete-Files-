def convert(seconds):
    hours=seconds//3600
    minutes=(seconds-hours*3600)//60
    remaining_seconds=seconds - hours * 3600 - minutes * 60
    return print(hours,minutes,remaining_seconds)

convert(3600)