# Sets - Conjuntos em python (tipo set)
# Conjuntos são ensinados na matemática
# Representados graficamente pelo diagram de venn
# Sets em phyton são mutáveis, porém aceitam apenas tipos imutáveis como valor interno

# Criando um set
# Set(interável) ou {1, 2, 3}

# Stes são eficientes para remover valores duplicados de interáveis
# - eles não tem índexes
# - eles não garantem ordem
# - eles são interáveis (for, in. not in)

# Métodos últeis
# - add, update, clear, discard

s1 = set()
s1 = {1, 2, 3, 3, 3, 3, 3, 3} # um set naturalmente remove valores duplicados
print(s1)