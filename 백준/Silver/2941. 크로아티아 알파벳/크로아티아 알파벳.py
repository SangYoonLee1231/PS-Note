croaita_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

string = input()

for elem in croaita_alphabet:
    string = string.replace(elem, '*')

print(len(string))