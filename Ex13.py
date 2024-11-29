def eh_palindromo(palavra):
    if len(palavra) <= 1:
        return True
    if palavra[0] != palavra[-1]:
        return False
    return eh_palindromo(palavra[1:-1])

print(eh_palindromo("radar"))
print(eh_palindromo("python"))
