# pede ao usuário para informar um número
num = int(input("Informe um número: "))

# define os primeiros dois termos da sequência
a, b = 0, 1

# inicializa a lista com esses dois termos
fib = [a, b]

# calcula os próximos termos da sequência até que o último termo seja maior do que o número informado pelo usuário
while fib[-1] < num:
    next_term = a + b
    fib.append(next_term)
    a, b = b, next_term

# verifica se o número informado pelo usuário pertence ou não à sequência
if num in fib:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
