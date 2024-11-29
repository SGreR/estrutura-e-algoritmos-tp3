def inverter_string(s):
    if not s:
        return ""
    return s[-1] + inverter_string(s[:-1])

print(inverter_string("recursao"))
print(inverter_string("algoritmos"))
