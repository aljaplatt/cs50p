# def main():
#     height = int(input("Height: "))
#     pyramid(height)

# def pyramid(num):
#     for i in range(num):
#         print("#" * i)


# if __name__ == "__main__":
#     main()

'''
input 5 = 4
#
##
###
####
'''

#* refactor after print debugging

# def main():
#     height = int(input("Height: "))
#     pyramid(height)

# def pyramid(num):
#     for i in range(num):
#         print(i, end=" ")
#         print("#" * i)


# if __name__ == "__main__":
#     main()

'''
0 
1 #
2 ##
3 ###
4 ####
'''

# def main():
#     height = int(input("Height: "))
#     pyramid(height)

# def pyramid(num):
#     for i in range(num):
#         # print(i, end=" ") - first i = 0
#         print("#" * (i + 1))


# if __name__ == "__main__":
#     main()

#! using debugger
# set breakpoint
# set into - step into a specific function - usually the ones yo'u've made
#  step over built in functions, probably not the problem

def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(num):
    for i in range(num):
        print("#" * i)


if __name__ == "__main__":
    main()