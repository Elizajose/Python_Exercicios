lista=[]
listb=[]
a='0'
b='0'

def uniao (a,b):
    c=a+b
    c=list(set(c))
    return c 

def interseção (a,b):
    c = list(set(a) & set (b))
    return c

def diferença (a,b):
    c = list(set(a)-set(b))
    return c

print('Digite os elementos da lista A ')
while a!='':
    a=input(': ')
    lista.append(a)
    
print('Digite os elementos da lista B ')
while b!='':
    b=input(': ')
    listb.append(b)

lista.remove('')
listb.remove('')
u = uniao(lista,listb)
i = interseção(lista,listb)
d = diferença(lista,listb)
print('a união é %s'%u)
print('a interseção é %s'%i)
print('a diferença é %s'%d)
