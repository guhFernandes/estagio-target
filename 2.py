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
