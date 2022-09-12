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
# convert valid user date to output
try:
    month, day, year = input("Date: ").split("/")

    if int(month) < 10:
        month = f"0{month}"

    if int(day) < 10:
        day = f"0{day}"

    # split on /
    print(f"{year}-{month}-{day}")
except:
    str_date = input("Date: ")
    print(str_date)