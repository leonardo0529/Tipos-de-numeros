#!/usr/bin/env python
# coding: utf-8

# In[4]:


def repetidos(a):
    """Funcion que te dice si en una lista  tiene numeros repetidos"""
    b=set(a)
    if len(a) is len(b):
        r=False
    else:
        r=True
    return r


# In[5]:


def cuadrado(n):
    """Funcion que te regresa la suma de cada dijito al cuadrado"""
    lista_numero=list(str(n))
    lista_vacia=[]
    suma=0
    for i in lista_numero:
        numero=int(i)
        lista_vacia.append(numero)
    for j in lista_vacia:
        suma=suma+j**2
    return suma


# In[6]:


def numero_feliz(x):
    """Funcion que te dice si un numero es feliz o no"""
    principal=[]
    auxilar=[]
    principal.append(cuadrado(x))
    if principal[-1]==1:
        final=True
    else:
        while principal[-1]!=1:
            aux=cuadrado(principal[-1])
            auxilar.append(aux)
            for i in auxilar:
                principal.append(i)
            auxilar.pop(0)
            if principal[-1]==1:
                final=True
                break
            if repetidos(principal) is True:
                final=False
                break
    return final


# In[7]:


def varios_felices(x):
    """Funcion que te regresa los numeros felices que estan del 1 al el numero x"""
    vacia=[]
    for i in range(1,x+1):
        if numero_feliz(i) is True:
            vacia.append(i)
    return vacia


# In[ ]:




