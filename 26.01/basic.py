# numbers
x = 12
y = 2.4


# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x ** y)
# print(x % y)


# strings
s1 = 'ana are mere'
s2 = 'don\'t'
# niciodata ghilimele, doar apostrof


# string formatting
var_ana = 'ana'
var_mere = 'mere'
ss = '{} are {}'.format(var_ana, var_mere)
# print(ss)


# lists
l = [1, 2, 3, 4, 5, 6, 7]
# print(l)
# print([1, 2.3, 'bau', [1, 2, 4]])


# tuples
t = (1, 2, 3, 4, 5, 6, 7)
# print(t)


# sets
s = {1, 2, 3, 4, 5, 6, 7}
# print(s)


# indexing
# print('list', l[0])
# print('tuplu', t[0])
# # nu se poate indexa un set, pentru ca nu are ordine
# print('invers', l[-1]) # e echivalent cu l[len(l - 1)]


# slicing
# print('string slice', s1[4:7])
# print(s1[4:])
# print(t[:5])
# print(l[:])
# print(l[0:5:2])
# print(l[::2])
# print(l[5:0]) # atentie ca nu da eroare
# print(l[::-1]) # pas negativ


# len
# print(len(s1))
# print(len(l))
# print(len(t))
# print(len(s))


# mutability - proprietatea cuiva de a putea fi modificat
# s1[0] = 'A' - string-urile sunt imutabile
s1_modificat = s1.upper()
# print(s1, s1_modificat)

l[0] = -1  # listele sunt mutabile
# print(l)

# t[0] = -1 - tuplurile NU sunt mutabile

'Listele sunt multimi omogene, dar tuplurile sunt neomogene.'
nume = ['Claudia', 'Franci', 'Eric']
locatie = (12.12345, 98.34567, 24)  # latitudine, longitudine si orientare


# unicitate
set_nou = {1, 1, 1, 2, 2, 2, 3, 3, 3}  # elementele set-urilor sunt unice
# print(set_nou)


# exemple de metode
l.append(4)
l.extend([1, 2, 3])
l.pop(5)
# print(l)

lista_naspa = [1, 2, 3, 2, 1, 4, 1, 2, 4]
lista_misto = list(set(lista_naspa))
# print(lista_misto)

lista_multe_randuri = [
    'primul',
    'al doilea',
    'al treilea',
]
# print(lista_multe_randuri)


# dicts
d = {  # cheile trebuie sa fie imutabile
    1: 'bau',
    2: 'miau',
    'cheia3': 'sarpili',
    'cheia4': 69,
    (1, 'unu'): [1, 2, 3],
}
# print(d)

d.pop(1)
# d[0] referentierea directa da eroaore
ceva = d.get(0, 'altceva')
# print(list(d.keys()))
# print(d.values())
# print(ceva)
#
# del d[2]

# print(d)

a = 2
b = 3
# print(a < b)
# print(a <= b)
# print(a > b)
# print(a >= b)
# print(a == b)
# print(a != b)
#
# print(1 != '1')
# print(1 == int('1'))
# print(str(1) == '1')
# print(type(1), type('1'))
# print(isinstance(1, int))  # int, str, list, tuple, set, dict, bool

# print(True and False)
# print(True or False)
# print(1 in [1, 2, 3])  # true
# print(0 in [1, 2, 3])  # false
#
# if a < b:
#     print('da')
# elif a > b:
#     print('nu')
# else:
#     print('poate')

# if (
#     a > b
#     and x > y
# ):
#     pass

# i = 0
# while i < 5:
#     print(i ** 2)
#     i += 1

# for elem in [1, 2, 3]:
#     print(elem)
#     if elem == 2:
#         break
# else:  # se apeleaza doar daca se itereaza toate numerele
#     print('gata')
#
# tuple_ex = [(12, 43), (69, 420), (27, 45), (15, 39)]  # produsul cartezian al unor multimi
#
# for x1, x2 in tuple_ex:  # tuple unpacking
#     print('elem1:', x1)
#     print('elem2:', x2)
#
#
# tuple_ex = [(12, 43, 1), (69, 420, 3), (27, 45, 2), (15, 39, 4)]
#
# for x1, x2, _ in tuple_ex:  # tine cont doar de primele 2 elemente ale tuplului
#     print('elem1:', x1)
#     print('elem2:', x2)
#
# print(range(5))
# print(list(range(5)))
#
# for i in range(len(tuple_ex)):
#     print(i, tuple_ex[i])

list1 = [1, 2, 3, 4, 5, 6]
list2 = []
for elem in list1:
    list2.append(elem ** elem)

print(list2)

print([elem ** elem for elem in list1])  #list comprehension
# [operatie for var_de_nume_pentru_elem in numele_structurii_ordonate]




