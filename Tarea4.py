#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np #Importamos las librerías que hemos de utilizar
import pandas as pd


# In[2]:


data = pd.read_csv('exoplanets.csv',low_memory=False)
a = pd.DataFrame(data) #Cargamos los datos en un DF
B = pd.DataFrame([a['NAME'],a['TEFF'],a['MASS'],a['A'],a['DENSITY'],a['R'],a['STAR'],a['MSTAR'],a['RSTAR'],
                 a['BINARY']]) #del DF anterior extraemos las columnas que nos piden
A =pd.DataFrame.transpose(B) #Transponemos los datos con .transpose


# In[3]:


DF = A.dropna(subset=['BINARY']) #Borramos los elementos Nan

for i in range(3263): #Borramos los elementos nulos de BINARY
    if DF['BINARY'][i]==1:
        DF = DF.drop(index=i)


# In[4]:


DF = DF.reset_index() #renombramos los indices
DF = DF.drop(['index'], axis=1) #Borramos las columnas innecesarias
DF


# In[5]:


DF.insert(9,"MASSE",DF["MASS"]*317.8) #La masa de la Júpiter es 317.8 veces la masa de la Tierra
 # Con lo anterior hemos creado la columna que contiene las masas en terminos de masas terrestres


# In[6]:


DF.insert(10,"RE",DF["R"]*11.2) #El radio de Júpiter es 11.2 veces el radio de la Tierra


# In[7]:


DF.insert(11,"LUM",4*np.pi*(DF["RSTAR"]**2)*5.670373*10**(-8)*((6.96*10**8)**2)*DF["TEFF"]**4/(3.828*10**26)) #Aplicamos la ecuación para calcular la
#luminosidad de cada una de estas estrellas


# In[8]:


#
DF.insert(12,"ri",
          (0.72-2.7619*10**(-5)*(DF["TEFF"]-5780)-
           3.8095*10**(-9)*(DF["TEFF"]-5780)**2)*np.sqrt(DF["LUM"].astype(float)))  #.astype(float) convierte a 
                                                                                    #flotante


# In[9]:


DF.insert(13,"r0",
          (1.77-1.3786*10**(-4)*(DF["TEFF"]-5780)-
           1.4286*10**(-9)*(DF["TEFF"]-5780)**2)*np.sqrt(DF["LUM"].astype(float)))


# In[10]:


Densidad = DF.query("DENSITY>=5")
Densidad #Imprimimos la tabla con los valores que cumplen dicha condición


# In[11]:


Densidad.insert(14,"HZD",(2*DF["A"]-DF["r0"]-DF["ri"])/(DF["r0"]-DF["ri"])) #Creamos el intervalo de habitabilidad


# In[12]:


Habitabilidad= Densidad.query("HZD<=1 and HZD>=-1") #Imponemos la condición de habitabilidad
Habitabilidad #Mostramos los planetas que cumplen con dichas condiciones


# In[13]:


#Procedemos a plotear las gráficas pedidas, está de más comentarlas. (Eso supongo)
Habitabilidad.plot(kind='scatter',x="MSTAR",y="A",
                   title="Masa de la estrella Vs Distancia del planeta a su estrella")


# In[17]:


Habitabilidad.plot(kind='hist',x="MASS",y="A",title="Distribución orbital de los planetas")


# In[18]:


Habitabilidad.plot(x="DENSITY",y="MSTAR",title="Densidad Vs Masa de la estrella")


# In[19]:


Habitabilidad.plot(x="A",y="TEFF",title="Distancia a la estrella Vs Temperatura efectiva")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




