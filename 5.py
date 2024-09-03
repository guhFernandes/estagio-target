string_original = "Exemplo de string"
string_invertida = ""

for i in range((len(string_original) - 1), -1, -1):
    string_invertida += string_original[i]

print("String original:", string_original)
print("String invertida:", string_invertida)
