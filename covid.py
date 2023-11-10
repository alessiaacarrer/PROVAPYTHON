#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 09:27:17 2023

@author: alessiacarrer
"""


import numpy as np
import pandas as pd
import random as ran
import matplotlib.pyplot as mpl

datatot=pd.read_csv('covid.csv')
dataterapia=datatot[['data', 'terapia_intensiva', 'denominazione_regione']]

dataregione=dataterapia.groupby('denominazione_regione')



for intervallo, sottoinsieme in dataregione: 
    
    
    if intervallo == 'Veneto':
        
        
    
        #print(intervallo)
        #print(sottoinsieme)

    
        #print(bin_value)
        mpl.plot(sottoinsieme['data'], sottoinsieme['terapia_intensiva'], '-')
        
     
        
        
dataiso=datatot[['data', 'isolamento_domiciliare', 'denominazione_regione']]

dataregione1=dataiso.groupby('denominazione_regione')



for intervallo, sottoinsieme in dataregione1: 
    
    
    if intervallo == 'Veneto':
        
        
    
        #print(intervallo)
        #print(sottoinsieme)

    
        #print(bin_value)
        mpl.plot(sottoinsieme['data'], sottoinsieme['isolamento_domiciliare'], '-')
       
        mpl.show()
        
        #CON MPL.SHOW ALLA FINE IO GRAFICO TUTTO SULLO STESSO CANVAS
        