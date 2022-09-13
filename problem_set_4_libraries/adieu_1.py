import inflect
p = inflect.engine()

# instantiate list with these two items 
text = ["Adieu", "adieu"]
# new_text = p.join(text) # Adieu and adieu
# print(new_text)

# text = ["Adieu", "adieu", "adieu"]
# new_text = p.join(text) # Adieu, adieu, and adieu
# print(new_text)

while True:
    try:
        name = input("Name: ")
    except EOFError:
        print()
        break
    # append input to list
    text.append(name)
# add to before first name
text[2] = f"to {text[2]}"

if len(text) == 3:
    # handles 1 name
    new_text = p.join(text, conj='')
elif len(text) == 4:
    # handles 2 names
    #? final_sep add and / , ?
    new_text = p.join(text, final_sep='')
else:
    # handles more than 2 names
    new_text = p.join(text)
# new_text = p.join(text)
print(new_text)