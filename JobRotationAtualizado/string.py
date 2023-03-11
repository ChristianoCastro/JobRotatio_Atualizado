string = "Exemplo de string para inverter"

inverted_string = ""

for i in range(len(string)-1, -1, -1):
    inverted_string += string[i]

print(inverted_string)
