

amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coins_inserted = int(input("Insert a coin: "))
    if coins_inserted > 25:
        print(f"Amount Due: {amount_due}")
        coins_inserted = int(input("Insert a coin: "))
    else:
        amount_due -= coins_inserted

if amount_due < 0:
    # print(amount_due)
    print(f"Change owed: {str(amount_due)[1:]}")
else:
    print(f"Change owed: {str(amount_due)}")