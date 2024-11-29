def contar_repeticoes(s, char):
    if not s:
        return 0
    return (1 if s[0] == char else 0) + contar_repeticoes(s[1:], char)

print(contar_repeticoes("banana", "a"))
print(contar_repeticoes("morango", "o"))
print(contar_repeticoes("abacaxi", "y"))
