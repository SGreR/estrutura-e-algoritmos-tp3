def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def factorial_iterativa(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursao_cauda(n, acc=1):
    if n == 0:
        return acc
    return factorial_recursao_cauda(n - 1, n * acc)


print(factorial(998)) #999 chamadas causam stack overflow exception
print(factorial_iterativa(1000)) #Não causa stack overflow exception
print(factorial_recursao_cauda(998)) #999 chamadas ainda causam stack overflow dado o fato de que python não possui otimização para tail recursion
