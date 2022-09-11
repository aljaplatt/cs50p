def main():
    fraction = get_fraction()
    if fraction == 0/100 or fraction == 1/100:
        print('E')
        return
    elif fraction == 100/100 or fraction == 99/100:
        print('F')
        return
    percentage = get_percentage(fraction)
    print(f"{percentage}%")


def get_fraction():
    # get fraction from user
    while True:
        try:
            num1, num2 = input('Fraction: ').split('/')
            # convert string fraction to int fraction
            try:
                if float(num2) >= float(num1):
                    try:
                        return int(num1) / int(num2)
                    except ZeroDivisionError:
                        pass
                        # print('You cannot divide zero')
            except ValueError:
                        pass
                        # print('Please use whole numbers')
        except ValueError:
            pass


def get_percentage(fraction):
    # convert fraction to percentage & round
    return round(fraction * 100)


main()


'''
:( input of 3/4 yields output of 75%
    expected "75%", not ""
:( input of 1/3 yields output of 33%
    expected "33%", not ""
:( input of 2/3 yields output of 67%
    expected "67%", not ""
:( input of 0/100 yields output of E
    expected "E", not ""
:( input of 1/100 yields output of E
    expected "E", not ""
:( input of 100/100 yields output of F
    expected "F", not ""
:( input of 99/100 yields output of F
    expected "F", not ""
:( input of 100/0 results in reprompt
    expected program to reject input, but it did not
:( input of 10/3 results in reprompt
    expected program to reject input, but it did not
:( input of three/four results in reprompt
    expected program to reject input, but it did not
:( input of 1.5/4 results in reprompt
    expected program to reject input, but it did not
:( input of 3/5.5 results in reprompt
    expected program to reject input, but it did not
:( input of 5-10 results in reprompt
    expected program to reject input, but it did not
'''