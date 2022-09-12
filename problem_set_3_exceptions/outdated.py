months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    # check date strings for char that will indicate what format the string is in
    if "/" in date:
        month, day, year = date.split("/")
    elif "," in date:
        # remove comma in string date
        date = date.replace(",", "")
        # split on space
        month, day, year = date.split(" ")
        if month in months:
            # reassign month str to int using month index + 1
            month = months.index(month) + 1
    else:
        continue

    try:
        if int(month) > 12 or int(day) > 31:
            continue
        else:
            break
    except ValueError:
        continue

print(f"{int(year):02}-{int(month):02}-{int(day):02}")