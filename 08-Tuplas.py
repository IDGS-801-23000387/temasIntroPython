"""sumary_line

las tuplas son inmutables,se declaran con ()
"""
tupla=("uno","dos","tres")
print(tupla)

tuplavariosDatos=(12,True,23.5,"El gato",12+4j)
print(tuplavariosDatos)


tuplasConTuplas=(1,2,3,4,(1,2,3))
print(tuplasConTuplas)

print(tuplasConTuplas[3])
print(tuplasConTuplas[-2])
print(tuplasConTuplas[0:2])

a,b,c=tupla
print(a,b,c)