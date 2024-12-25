# Generator expression, Interables e Iterators em python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) #tem __iter__ e __next__
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# quando chegar ao fim do meu interator ele gera uma excessão