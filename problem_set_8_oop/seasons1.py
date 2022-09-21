from datetime import date
import sys

def main():
    try:
        year, month, day = input("Date of Birth: ").split("-")
    except ValueError:
        sys.exit("Invalid Date")

    minutes_lived(year, month, day)

def minutes_lived(year, month, day):
    try:
        birthday = date(int(year), int(month), int(day))
    except ValueError:
        print("Invalid Date")
    date_today = date.today()
    time_elapsed = date_today - birthday
    print(time_elapsed)


if __name__ == "__main__":
    main()