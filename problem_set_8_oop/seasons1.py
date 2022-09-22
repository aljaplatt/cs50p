from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    try:
        year, month, day = input("Date of Birth: ").split("-")

    except ValueError:
        sys.exit("Invalid Date")

    print(minutes_lived(year, month, day))

def minutes_lived(year, month, day):
    try:
        birthday = date(int(year), int(month), int(day))
    except ValueError:
        return "Invalid Date"
    date_today = date.today()
    time_elapsed = date_today - birthday
    # print('TE: ', time_elapsed)
    # print(type(time_elapsed)) # <class 'datetime.timedelta'>
    minutes = int(time_elapsed.total_seconds() / 60)
    # print(minutes)
    # print(p.number_to_words(minutes)) # twenty million, five hundred and forty thousand, one hundred and sixty
    return f'{p.number_to_words(minutes, andword="").capitalize()} minutes'


if __name__ == "__main__":
    main()