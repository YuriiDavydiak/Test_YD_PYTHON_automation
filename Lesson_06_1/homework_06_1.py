string = input("enter value: ")

unique_symbols = set(string)

if len(unique_symbols) > 10:
    print(True)
else:
    print(False)