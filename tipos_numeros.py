#!/usr/bin/env python
# coding: utf-8

# In[1]:


def numero_primo(n):
    z=0
    for i in range(2,n+1):
        if n%i ==0:
            z+=1
    if z==1:
        return True
    else:
        return False


# In[2]:


def varios_primos(x):
    l=[]
    for e in range(1,x+1):
        if numero_primo(e) ==True:
            l.append(e)
    return l
            


# In[3]:


def numero_perfecto(n):
    vacia=[]
    suma=0
    for i in range(1,n):
        a=n%i
        if a==0:
            vacia.append(i)
    for j in vacia:
        suma=suma+j
    if suma==n:
        return True
    else:
        return False


# In[4]:


def varios_perfectos(z):
    l1=[]
    for j in range(1,z+1):
        if numero_perfecto(j) == True:
            l1.append(j)
    return l1


# In[5]:


def repetidos(a):
    b=set(a)
    if len(a) is len(b):
        r=False
    else:
        r=True
    return r
def cuadrado(n):
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
    vacia=[]
    for i in range(1,x+1):
        if numero_feliz(i) is True:
            vacia.append(i)
    return vacia


# In[14]:


#A=(220,284) #amigos


# In[8]:


def numero_deficiente(n):
    vacia=[]
    suma=0
    for i in range(1,n):
        a=n%i
        if a==0:
            vacia.append(i)
    for j in vacia:
        suma=suma+j
    if suma<n:
        return True
    else:
        return False


# In[9]:


def numero_abundante(n):
    vacia=[]
    suma=0
    for i in range(1,n):
        a=n%i
        if a==0:
            vacia.append(i)
    for j in vacia:
        suma=suma+j
    if suma>n:
        return True
    else:
        return False


# In[ ]:


numero_primo(2**2**769-1)


# In[ ]:




