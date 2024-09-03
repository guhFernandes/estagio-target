# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e
#  o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, 
# informado um número, ele calcule a sequência de Fibonacci 
# e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci(n):
    fib_sequencia = [0, 1]
    
    # Continua gerando a sequência até que o último número seja maior ou igual ao número informado
    while fib_sequencia[-1] < n:
        procimo_valor = fib_sequencia[-1] + fib_sequencia[-2]
        fib_sequencia.append(procimo_valor)
    
    return fib_sequencia

def num_e_fibonacci(num):
    fib_sequencia = fibonacci(num)
    
    if num in fib_sequencia:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
resultado = num_e_fibonacci(numero)
print(resultado)
