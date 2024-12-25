#Métodos uteis set
s1 = set()
s1.add('Allan')
s1.add(1)
s1.update(('Olá, mundo',2, 3, 4))
s1.discard(4)
print(s1)
#Operadores uteis
#União = | ou (union)
#insersecção = & ou (intersection) itens presentes em ambos
#diferença = - itns presentes apenas no set da esquerda
#diferença simétrica = ^ itens que não estão em ambos
s2 = {1, 2, 3}
s3= {2, 3, 4}
#s4 = s1 | s2 ou
s4 = s2.intersection(s3)
print(s4)
#s4 = s1 & s2 ou
s4 = s2.union(s3)
print(s4)
#s4 = s1 - s2 ou
s4 = s2.difference(s3)
print(s4)
#s4 = s1 ^ s2 ou
s4  = s2.symmetric_difference(s3)
print(s4)