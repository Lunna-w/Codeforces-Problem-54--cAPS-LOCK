s = input()

if len(s) == 1:
    if s.isupper():
        print(s.lower())
    else:
        print(s.upper())

elif s.islower():
    print(s)


elif s[0].isupper() and s[1:].islower():
    print(s)


elif s[0].islower() and s[1:].isupper():
    print(s[0].upper() + s[1:].lower())


elif s.isupper():
    print(s.lower())


elif len(s) == 0:
    print("Input is empty.")


else:
    print(s)