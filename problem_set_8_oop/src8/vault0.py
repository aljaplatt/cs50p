class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f" Galleons:{self.galleons}\n Sickles: {self.sickles}\n Knuts:{self.knuts}"

potter = Vault(100, 50, 25)
print(potter) # <__main__.Vault object at 0x1053ea770>

weasley = Vault(25, 50, 100)
print(weasley) # Add __str__ to print out format string 

#? combine 2 vaults?

galleons = potter.galleons + weasley.galleons
# print('GALLEONS: ', galleons)
sickles = potter.sickles + weasley.sickles
# print('SICKLES: ', sickles)
knuts = potter.knuts + weasley.knuts
# print('KNUTS: ', knuts)

total = Vault(galleons, sickles, knuts)
print('TOTAL: ', total)