def main():
    time = input("Please enter what time it is in a 24hr format eg 13:00: ").strip()

    # converted_time = convert(time)
    # print(converted_time)
    # if converted_time >= 7 and converted_time <= 8:
    #     print('breakfast time')
    # elif converted_time >= 12 and converted_time <= 13:
    #     print('lunch time')
    # elif converted_time >= 18 and converted_time <= 19:
    #     print('dinner time')

    converted_time = convert(time)
    # print(converted_time)
    if 7 <= converted_time <= 8:
        print('breakfast time')
    elif 12 <= converted_time <= 13:
        print('lunch time')
    elif 18 <= converted_time <= 19:
        print('dinner time')


def convert(time):
    hours, minutes = time.split(":")
    converted_minutes = float(minutes) / 60

    return float(hours) + converted_minutes

if __name__ == "__main__":
    main()


