def check(string):
    string =string.lower()

    vowels=set("aeiou")

    s=set({})

    for char in string:

        if char in vowels:
            s.add(char)

        else:
            pass
    if len(s)==len(vowels):
        print("accepted")
    else:
        print("not present")

check("dhbfahfad")