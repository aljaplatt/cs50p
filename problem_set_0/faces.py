# faces

def main():
    user_input = input()
    result = convert(user_input)
    print(result)

def convert(string):

    happy_string = string.replace(':)', "🙂")
    # print(new_string)
    sad_string = happy_string.replace(':(', '🙁')
    # print(sad_string)
    return sad_string

# convert("Hey slippin jimmy, :( what's up? :)")

main()