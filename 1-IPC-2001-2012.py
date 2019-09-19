# -*- coding: utf-8 -*-
#-----(09-A) data analysis of 1-IPC-2001-2012 -----

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/1-IPC-2001-2012.csv',encoding="cp1252")
print("\n------- output data :-----------\n")
print("1-IPC-2001-2012 data analysis:")
print("\n-----------------------------------\n")


# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

#Question – C : State_Name (using GROUP BY method) and no. of states :

state_names = df.groupby(['STATE_UT'])[['YEAR']].count()
print("---------------------------------")
print("\t states names : ")
print("-------------------------------")
print(state_names)
print("-------------------------------")
count = 0
for row in range(len(state_names)): 
        count = count+1
print("total no. of states = ",count)        
print("-----------------------------\n")

#Question – D : Available year(using GROUP BY method)  :

year = df.groupby(['YEAR'])[['STATE_UT']].count()
print("---------------------------------")
print("\t Year : ")
print("-------------------------------")
print(year)
print("-------------------------------")
count = 0
for row in range(len(year)): 
        count = count+1
print("total no. of available years = ",count)        
print("-----------------------------\n")


#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_total = df[df.DISTRICT == 'TOTAL']

# available data size

print('---------------------------------------------')
print("Dimension of the data frame = ",df_total.shape)
print('---------------------------------------------')

# available column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_total.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

#[df_total] State_Name (using GROUP BY method) and no. of states :

state_names = df_total.groupby(['STATE_UT'])[['YEAR']].count()
print("---------------------------------")
print("\t states names : ")
print("-------------------------------")
print(state_names)
print("-------------------------------")
count = 0
for row in range(len(state_names)): 
        count = count+1
print("total no. of states = ",count)        
print("-----------------------------\n")





# state-1: A & N ISLANDS 

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_andaman = df_total[df_total.STATE_UT == 'A & N ISLANDS']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_andaman.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_andaman['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_andaman.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_andaman['MURDER']
df_2 = df_andaman['ATTEMPT TO MURDER']
df_3 = df_andaman['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_andaman['RAPE']
df_5 = df_andaman['CUSTODIAL RAPE']
                    
df_6 = df_andaman['OTHER RAPE']
df_7 = df_andaman['KIDNAPPING & ABDUCTION']
df_8 = df_andaman['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_andaman['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_andaman['DACOITY']

df_11 = df_andaman['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_andaman['ROBBERY']
df_13 = df_andaman['BURGLARY']
df_14 = df_andaman['THEFT']
df_15 = df_andaman['AUTO THEFT']

df_16 = df_andaman['OTHER THEFT']
df_17 = df_andaman['RIOTS']
df_18 = df_andaman['CRIMINAL BREACH OF TRUST']
df_19 = df_andaman['CHEATING']
df_20 = df_andaman['COUNTERFIETING']
                    
df_21 = df_andaman['ARSON']
df_22 = df_andaman['HURT/GREVIOUS HURT']
df_23 = df_andaman['DOWRY DEATHS']
df_24 = df_andaman['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_andaman['INSULT TO MODESTY OF WOMEN']

df_26 = df_andaman['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_andaman['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_andaman['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_andaman['OTHER IPC CRIMES']
df_30 = df_andaman['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                                                                              

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
# state-2: ANDHRA PRADESH  

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_andhra = df_total[df_total.STATE_UT == 'ANDHRA PRADESH']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_andhra.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_andhra['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_andhra.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_andhra['MURDER']
df_2 = df_andhra['ATTEMPT TO MURDER']
df_3 = df_andhra['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_andhra['RAPE']
df_5 = df_andhra['CUSTODIAL RAPE']
                    
df_6 = df_andhra['OTHER RAPE']
df_7 = df_andhra['KIDNAPPING & ABDUCTION']
df_8 = df_andhra['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_andhra['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_andhra['DACOITY']

df_11 = df_andhra['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_andhra['ROBBERY']
df_13 = df_andhra['BURGLARY']
df_14 = df_andhra['THEFT']
df_15 = df_andhra['AUTO THEFT']

df_16 = df_andhra['OTHER THEFT']
df_17 = df_andhra['RIOTS']
df_18 = df_andhra['CRIMINAL BREACH OF TRUST']
df_19 = df_andhra['CHEATING']
df_20 = df_andhra['COUNTERFIETING']
                    
df_21 = df_andhra['ARSON']
df_22 = df_andhra['HURT/GREVIOUS HURT']
df_23 = df_andhra['DOWRY DEATHS']
df_24 = df_andhra['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_andhra['INSULT TO MODESTY OF WOMEN']

df_26 = df_andhra['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_andhra['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_andhra['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_andhra['OTHER IPC CRIMES']
df_30 = df_andhra['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                        

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")               
                                             
# state-3: ARUNACHAL PRADESH 

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_arun = df_total[df_total.STATE_UT == 'ARUNACHAL PRADESH']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_arun.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_arun['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_arun.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_arun['MURDER']
df_2 = df_arun['ATTEMPT TO MURDER']
df_3 = df_arun['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_arun['RAPE']
df_5 = df_arun['CUSTODIAL RAPE']
                    
df_6 = df_arun['OTHER RAPE']
df_7 = df_arun['KIDNAPPING & ABDUCTION']
df_8 = df_arun['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_arun['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_arun['DACOITY']

df_11 = df_arun['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_arun['ROBBERY']
df_13 = df_arun['BURGLARY']
df_14 = df_arun['THEFT']
df_15 = df_arun['AUTO THEFT']

df_16 = df_arun['OTHER THEFT']
df_17 = df_arun['RIOTS']
df_18 = df_arun['CRIMINAL BREACH OF TRUST']
df_19 = df_arun['CHEATING']
df_20 = df_arun['COUNTERFIETING']
                    
df_21 = df_arun['ARSON']
df_22 = df_arun['HURT/GREVIOUS HURT']
df_23 = df_arun['DOWRY DEATHS']
df_24 = df_arun['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_arun['INSULT TO MODESTY OF WOMEN']

df_26 = df_arun['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_arun['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_arun['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_arun['OTHER IPC CRIMES']
df_30 = df_arun['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                         

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")

# state-4: ASSAM 

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_assam = df_total[df_total.STATE_UT == 'ASSAM']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_assam.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_assam['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_assam.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_assam['MURDER']
df_2 = df_assam['ATTEMPT TO MURDER']
df_3 = df_assam['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_assam['RAPE']
df_5 = df_assam['CUSTODIAL RAPE']
                    
df_6 = df_assam['OTHER RAPE']
df_7 = df_assam['KIDNAPPING & ABDUCTION']
df_8 = df_assam['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_assam['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_assam['DACOITY']

df_11 = df_assam['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_assam['ROBBERY']
df_13 = df_assam['BURGLARY']
df_14 = df_assam['THEFT']
df_15 = df_assam['AUTO THEFT']

df_16 = df_assam['OTHER THEFT']
df_17 = df_assam['RIOTS']
df_18 = df_assam['CRIMINAL BREACH OF TRUST']
df_19 = df_assam['CHEATING']
df_20 = df_assam['COUNTERFIETING']
                    
df_21 = df_assam['ARSON']
df_22 = df_assam['HURT/GREVIOUS HURT']
df_23 = df_assam['DOWRY DEATHS']
df_24 = df_assam['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_assam['INSULT TO MODESTY OF WOMEN']

df_26 = df_assam['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_assam['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_assam['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_assam['OTHER IPC CRIMES']
df_30 = df_assam['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                   
                              
print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")

# state-5: BIHAR 

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_bihar = df_total[df_total.STATE_UT == 'BIHAR']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_bihar.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_bihar['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_bihar.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_bihar['MURDER']
df_2 = df_bihar['ATTEMPT TO MURDER']
df_3 = df_bihar['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_bihar['RAPE']
df_5 = df_bihar['CUSTODIAL RAPE']
                    
df_6 = df_bihar['OTHER RAPE']
df_7 = df_bihar['KIDNAPPING & ABDUCTION']
df_8 = df_bihar['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_bihar['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_bihar['DACOITY']

df_11 = df_bihar['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_bihar['ROBBERY']
df_13 = df_bihar['BURGLARY']
df_14 = df_bihar['THEFT']
df_15 = df_bihar['AUTO THEFT']

df_16 = df_bihar['OTHER THEFT']
df_17 = df_bihar['RIOTS']
df_18 = df_bihar['CRIMINAL BREACH OF TRUST']
df_19 = df_bihar['CHEATING']
df_20 = df_bihar['COUNTERFIETING']
                    
df_21 = df_bihar['ARSON']
df_22 = df_bihar['HURT/GREVIOUS HURT']
df_23 = df_bihar['DOWRY DEATHS']
df_24 = df_bihar['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_bihar['INSULT TO MODESTY OF WOMEN']

df_26 = df_bihar['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_bihar['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_bihar['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_bihar['OTHER IPC CRIMES']
df_30 = df_bihar['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                   
                              
print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")

# state-6: CHANDIGARH 

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_chandi = df_total[df_total.STATE_UT == 'CHANDIGARH']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_chandi.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_chandi['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_chandi.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_chandi['MURDER']
df_2 = df_chandi['ATTEMPT TO MURDER']
df_3 = df_chandi['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_chandi['RAPE']
df_5 = df_chandi['CUSTODIAL RAPE']
                    
df_6 = df_chandi['OTHER RAPE']
df_7 = df_chandi['KIDNAPPING & ABDUCTION']
df_8 = df_chandi['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_chandi['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_chandi['DACOITY']

df_11 = df_chandi['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_chandi['ROBBERY']
df_13 = df_chandi['BURGLARY']
df_14 = df_chandi['THEFT']
df_15 = df_chandi['AUTO THEFT']

df_16 = df_chandi['OTHER THEFT']
df_17 = df_chandi['RIOTS']
df_18 = df_chandi['CRIMINAL BREACH OF TRUST']
df_19 = df_chandi['CHEATING']
df_20 = df_chandi['COUNTERFIETING']
                    
df_21 = df_chandi['ARSON']
df_22 = df_chandi['HURT/GREVIOUS HURT']
df_23 = df_chandi['DOWRY DEATHS']
df_24 = df_chandi['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_chandi['INSULT TO MODESTY OF WOMEN']

df_26 = df_chandi['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_chandi['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_chandi['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_chandi['OTHER IPC CRIMES']
df_30 = df_chandi['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                             
                              
# state-7: CHHATTISGARH 



#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_chatti = df_total[df_total.STATE_UT == 'CHHATTISGARH']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_chatti.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_chatti['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_chatti.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_chatti['MURDER']
df_2 = df_chatti['ATTEMPT TO MURDER']
df_3 = df_chatti['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_chatti['RAPE']
df_5 = df_chatti['CUSTODIAL RAPE']
                    
df_6 = df_chatti['OTHER RAPE']
df_7 = df_chatti['KIDNAPPING & ABDUCTION']
df_8 = df_chatti['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_chatti['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_chatti['DACOITY']

df_11 = df_chatti['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_chatti['ROBBERY']
df_13 = df_chatti['BURGLARY']
df_14 = df_chatti['THEFT']
df_15 = df_chatti['AUTO THEFT']

df_16 = df_chatti['OTHER THEFT']
df_17 = df_chatti['RIOTS']
df_18 = df_chatti['CRIMINAL BREACH OF TRUST']
df_19 = df_chatti['CHEATING']
df_20 = df_chatti['COUNTERFIETING']
                    
df_21 = df_chatti['ARSON']
df_22 = df_chatti['HURT/GREVIOUS HURT']
df_23 = df_chatti['DOWRY DEATHS']
df_24 = df_chatti['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_chatti['INSULT TO MODESTY OF WOMEN']

df_26 = df_chatti['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_chatti['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_chatti['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_chatti['OTHER IPC CRIMES']
df_30 = df_chatti['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                                   

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                
                                                
# state-8: D & N HAVELI 

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_haveli = df_total[df_total.STATE_UT == 'D & N HAVELI']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_haveli.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_haveli['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_haveli.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_haveli['MURDER']
df_2 = df_haveli['ATTEMPT TO MURDER']
df_3 = df_haveli['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_haveli['RAPE']
df_5 = df_haveli['CUSTODIAL RAPE']
                    
df_6 = df_haveli['OTHER RAPE']
df_7 = df_haveli['KIDNAPPING & ABDUCTION']
df_8 = df_haveli['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_haveli['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_haveli['DACOITY']

df_11 = df_haveli['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_haveli['ROBBERY']
df_13 = df_haveli['BURGLARY']
df_14 = df_haveli['THEFT']
df_15 = df_haveli['AUTO THEFT']

df_16 = df_haveli['OTHER THEFT']
df_17 = df_haveli['RIOTS']
df_18 = df_haveli['CRIMINAL BREACH OF TRUST']
df_19 = df_haveli['CHEATING']
df_20 = df_haveli['COUNTERFIETING']
                    
df_21 = df_haveli['ARSON']
df_22 = df_haveli['HURT/GREVIOUS HURT']
df_23 = df_haveli['DOWRY DEATHS']
df_24 = df_haveli['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_haveli['INSULT TO MODESTY OF WOMEN']

df_26 = df_haveli['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_haveli['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_haveli['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_haveli['OTHER IPC CRIMES']
df_30 = df_haveli['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                           

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                        
                                                                        
# state-9: DAMAN & DIU 

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_daman = df_total[df_total.STATE_UT == 'DAMAN & DIU']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_daman.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_daman['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_daman.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_daman['MURDER']
df_2 = df_daman['ATTEMPT TO MURDER']
df_3 = df_daman['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_daman['RAPE']
df_5 = df_daman['CUSTODIAL RAPE']
                    
df_6 = df_daman['OTHER RAPE']
df_7 = df_daman['KIDNAPPING & ABDUCTION']
df_8 = df_daman['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_daman['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_daman['DACOITY']

df_11 = df_daman['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_daman['ROBBERY']
df_13 = df_daman['BURGLARY']
df_14 = df_daman['THEFT']
df_15 = df_daman['AUTO THEFT']

df_16 = df_daman['OTHER THEFT']
df_17 = df_daman['RIOTS']
df_18 = df_daman['CRIMINAL BREACH OF TRUST']
df_19 = df_daman['CHEATING']
df_20 = df_daman['COUNTERFIETING']
                    
df_21 = df_daman['ARSON']
df_22 = df_daman['HURT/GREVIOUS HURT']
df_23 = df_daman['DOWRY DEATHS']
df_24 = df_daman['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_daman['INSULT TO MODESTY OF WOMEN']

df_26 = df_daman['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_daman['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_daman['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_daman['OTHER IPC CRIMES']
df_30 = df_daman['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                            
                           
print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")

# state-10: GOA

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_goa = df_total[df_total.STATE_UT == 'GOA']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_goa.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_goa['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_goa.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_goa['MURDER']
df_2 = df_goa['ATTEMPT TO MURDER']
df_3 = df_goa['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_goa['RAPE']
df_5 = df_goa['CUSTODIAL RAPE']
                    
df_6 = df_goa['OTHER RAPE']
df_7 = df_goa['KIDNAPPING & ABDUCTION']
df_8 = df_goa['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_goa['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_goa['DACOITY']

df_11 = df_goa['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_goa['ROBBERY']
df_13 = df_goa['BURGLARY']
df_14 = df_goa['THEFT']
df_15 = df_goa['AUTO THEFT']

df_16 = df_goa['OTHER THEFT']
df_17 = df_goa['RIOTS']
df_18 = df_goa['CRIMINAL BREACH OF TRUST']
df_19 = df_goa['CHEATING']
df_20 = df_goa['COUNTERFIETING']
                    
df_21 = df_goa['ARSON']
df_22 = df_goa['HURT/GREVIOUS HURT']
df_23 = df_goa['DOWRY DEATHS']
df_24 = df_goa['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_goa['INSULT TO MODESTY OF WOMEN']

df_26 = df_goa['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_goa['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_goa['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_goa['OTHER IPC CRIMES']
df_30 = df_goa['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                                     
                                                      
print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")

# state-11: GUJARAT 

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_gujrat = df_total[df_total.STATE_UT == 'GUJARAT']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_gujrat.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_gujrat['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_gujrat.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_gujrat['MURDER']
df_2 = df_gujrat['ATTEMPT TO MURDER']
df_3 = df_gujrat['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_gujrat['RAPE']
df_5 = df_gujrat['CUSTODIAL RAPE']
                    
df_6 = df_gujrat['OTHER RAPE']
df_7 = df_gujrat['KIDNAPPING & ABDUCTION']
df_8 = df_gujrat['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_gujrat['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_gujrat['DACOITY']

df_11 = df_gujrat['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_gujrat['ROBBERY']
df_13 = df_gujrat['BURGLARY']
df_14 = df_gujrat['THEFT']
df_15 = df_gujrat['AUTO THEFT']

df_16 = df_gujrat['OTHER THEFT']
df_17 = df_gujrat['RIOTS']
df_18 = df_gujrat['CRIMINAL BREACH OF TRUST']
df_19 = df_gujrat['CHEATING']
df_20 = df_gujrat['COUNTERFIETING']
                    
df_21 = df_gujrat['ARSON']
df_22 = df_gujrat['HURT/GREVIOUS HURT']
df_23 = df_gujrat['DOWRY DEATHS']
df_24 = df_gujrat['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_gujrat['INSULT TO MODESTY OF WOMEN']

df_26 = df_gujrat['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_gujrat['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_gujrat['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_gujrat['OTHER IPC CRIMES']
df_30 = df_gujrat['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                                

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")
                                                                                                                                                            
# state-12: HARYANA

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_haryana = df_total[df_total.STATE_UT == 'HARYANA']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_haryana.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_haryana['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_haryana.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_haryana['MURDER']
df_2 = df_haryana['ATTEMPT TO MURDER']
df_3 = df_haryana['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_haryana['RAPE']
df_5 = df_haryana['CUSTODIAL RAPE']
                    
df_6 = df_haryana['OTHER RAPE']
df_7 = df_haryana['KIDNAPPING & ABDUCTION']
df_8 = df_haryana['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_haryana['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_haryana['DACOITY']

df_11 = df_haryana['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_haryana['ROBBERY']
df_13 = df_haryana['BURGLARY']
df_14 = df_haryana['THEFT']
df_15 = df_haryana['AUTO THEFT']

df_16 = df_haryana['OTHER THEFT']
df_17 = df_haryana['RIOTS']
df_18 = df_haryana['CRIMINAL BREACH OF TRUST']
df_19 = df_haryana['CHEATING']
df_20 = df_haryana['COUNTERFIETING']
                    
df_21 = df_haryana['ARSON']
df_22 = df_haryana['HURT/GREVIOUS HURT']
df_23 = df_haryana['DOWRY DEATHS']
df_24 = df_haryana['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_haryana['INSULT TO MODESTY OF WOMEN']

df_26 = df_haryana['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_haryana['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_haryana['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_haryana['OTHER IPC CRIMES']
df_30 = df_haryana['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                   

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")              
                                          
# state-13: HIMACHAL PRADESH 

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_hima = df_total[df_total.STATE_UT == 'HIMACHAL PRADESH']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_hima.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_hima['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_hima.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_hima['MURDER']
df_2 = df_hima['ATTEMPT TO MURDER']
df_3 = df_hima['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_hima['RAPE']
df_5 = df_hima['CUSTODIAL RAPE']
                    
df_6 = df_hima['OTHER RAPE']
df_7 = df_hima['KIDNAPPING & ABDUCTION']
df_8 = df_hima['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_hima['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_hima['DACOITY']

df_11 = df_hima['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_hima['ROBBERY']
df_13 = df_hima['BURGLARY']
df_14 = df_hima['THEFT']
df_15 = df_hima['AUTO THEFT']

df_16 = df_hima['OTHER THEFT']
df_17 = df_hima['RIOTS']
df_18 = df_hima['CRIMINAL BREACH OF TRUST']
df_19 = df_hima['CHEATING']
df_20 = df_hima['COUNTERFIETING']
                    
df_21 = df_hima['ARSON']
df_22 = df_hima['HURT/GREVIOUS HURT']
df_23 = df_hima['DOWRY DEATHS']
df_24 = df_hima['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_hima['INSULT TO MODESTY OF WOMEN']

df_26 = df_hima['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_hima['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_hima['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_hima['OTHER IPC CRIMES']
df_30 = df_hima['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                       

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")            
                                    
# state-14: JAMMU & KASHMIR 

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_jammu = df_total[df_total.STATE_UT == 'JAMMU & KASHMIR']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_jammu.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_jammu['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_jammu.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_jammu['MURDER']
df_2 = df_jammu['ATTEMPT TO MURDER']
df_3 = df_jammu['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_jammu['RAPE']
df_5 = df_jammu['CUSTODIAL RAPE']
                    
df_6 = df_jammu['OTHER RAPE']
df_7 = df_jammu['KIDNAPPING & ABDUCTION']
df_8 = df_jammu['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_jammu['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_jammu['DACOITY']

df_11 = df_jammu['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_jammu['ROBBERY']
df_13 = df_jammu['BURGLARY']
df_14 = df_jammu['THEFT']
df_15 = df_jammu['AUTO THEFT']

df_16 = df_jammu['OTHER THEFT']
df_17 = df_jammu['RIOTS']
df_18 = df_jammu['CRIMINAL BREACH OF TRUST']
df_19 = df_jammu['CHEATING']
df_20 = df_jammu['COUNTERFIETING']
                    
df_21 = df_jammu['ARSON']
df_22 = df_jammu['HURT/GREVIOUS HURT']
df_23 = df_jammu['DOWRY DEATHS']
df_24 = df_jammu['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_jammu['INSULT TO MODESTY OF WOMEN']

df_26 = df_jammu['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_jammu['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_jammu['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_jammu['OTHER IPC CRIMES']
df_30 = df_jammu['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                       

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")            
                                    
# state-15: JHARKHAND 

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_jhar = df_total[df_total.STATE_UT == 'JHARKHAND']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_jhar.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_jhar['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_jhar.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_jhar['MURDER']
df_2 = df_jhar['ATTEMPT TO MURDER']
df_3 = df_jhar['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_jhar['RAPE']
df_5 = df_jhar['CUSTODIAL RAPE']
                    
df_6 = df_jhar['OTHER RAPE']
df_7 = df_jhar['KIDNAPPING & ABDUCTION']
df_8 = df_jhar['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_jhar['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_jhar['DACOITY']

df_11 = df_jhar['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_jhar['ROBBERY']
df_13 = df_jhar['BURGLARY']
df_14 = df_jhar['THEFT']
df_15 = df_jhar['AUTO THEFT']

df_16 = df_jhar['OTHER THEFT']
df_17 = df_jhar['RIOTS']
df_18 = df_jhar['CRIMINAL BREACH OF TRUST']
df_19 = df_jhar['CHEATING']
df_20 = df_jhar['COUNTERFIETING']
                    
df_21 = df_jhar['ARSON']
df_22 = df_jhar['HURT/GREVIOUS HURT']
df_23 = df_jhar['DOWRY DEATHS']
df_24 = df_jhar['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_jhar['INSULT TO MODESTY OF WOMEN']

df_26 = df_jhar['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_jhar['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_jhar['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_jhar['OTHER IPC CRIMES']
df_30 = df_jhar['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                             

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                              
                                                                                          
# state-16: KARNATAKA

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_kar = df_total[df_total.STATE_UT == 'KARNATAKA']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_kar.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_kar['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_kar.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_kar['MURDER']
df_2 = df_kar['ATTEMPT TO MURDER']
df_3 = df_kar['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_kar['RAPE']
df_5 = df_kar['CUSTODIAL RAPE']
                    
df_6 = df_kar['OTHER RAPE']
df_7 = df_kar['KIDNAPPING & ABDUCTION']
df_8 = df_kar['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_kar['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_kar['DACOITY']

df_11 = df_kar['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_kar['ROBBERY']
df_13 = df_kar['BURGLARY']
df_14 = df_kar['THEFT']
df_15 = df_kar['AUTO THEFT']

df_16 = df_kar['OTHER THEFT']
df_17 = df_kar['RIOTS']
df_18 = df_kar['CRIMINAL BREACH OF TRUST']
df_19 = df_kar['CHEATING']
df_20 = df_kar['COUNTERFIETING']
                    
df_21 = df_kar['ARSON']
df_22 = df_kar['HURT/GREVIOUS HURT']
df_23 = df_kar['DOWRY DEATHS']
df_24 = df_kar['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_kar['INSULT TO MODESTY OF WOMEN']

df_26 = df_kar['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_kar['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_kar['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_kar['OTHER IPC CRIMES']
df_30 = df_kar['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                   

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                        
                                                                        
# state-17: KERALA

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_ker = df_total[df_total.STATE_UT == 'KERALA']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_ker.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_ker['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_ker.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_ker['MURDER']
df_2 = df_ker['ATTEMPT TO MURDER']
df_3 = df_ker['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_ker['RAPE']
df_5 = df_ker['CUSTODIAL RAPE']
                    
df_6 = df_ker['OTHER RAPE']
df_7 = df_ker['KIDNAPPING & ABDUCTION']
df_8 = df_ker['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_ker['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_ker['DACOITY']

df_11 = df_ker['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_ker['ROBBERY']
df_13 = df_ker['BURGLARY']
df_14 = df_ker['THEFT']
df_15 = df_ker['AUTO THEFT']

df_16 = df_ker['OTHER THEFT']
df_17 = df_ker['RIOTS']
df_18 = df_ker['CRIMINAL BREACH OF TRUST']
df_19 = df_ker['CHEATING']
df_20 = df_ker['COUNTERFIETING']
                    
df_21 = df_ker['ARSON']
df_22 = df_ker['HURT/GREVIOUS HURT']
df_23 = df_ker['DOWRY DEATHS']
df_24 = df_ker['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_ker['INSULT TO MODESTY OF WOMEN']

df_26 = df_ker['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_ker['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_ker['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_ker['OTHER IPC CRIMES']
df_30 = df_ker['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                                  

 print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                                            
                                                                                                                                       
# state-18: LAKSHADWEEP 

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_lak = df_total[df_total.STATE_UT == 'LAKSHADWEEP']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_lak.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_lak['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_lak.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_lak['MURDER']
df_2 = df_lak['ATTEMPT TO MURDER']
df_3 = df_lak['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_lak['RAPE']
df_5 = df_lak['CUSTODIAL RAPE']
                    
df_6 = df_lak['OTHER RAPE']
df_7 = df_lak['KIDNAPPING & ABDUCTION']
df_8 = df_lak['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_lak['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_lak['DACOITY']

df_11 = df_lak['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_lak['ROBBERY']
df_13 = df_lak['BURGLARY']
df_14 = df_lak['THEFT']
df_15 = df_lak['AUTO THEFT']

df_16 = df_lak['OTHER THEFT']
df_17 = df_lak['RIOTS']
df_18 = df_lak['CRIMINAL BREACH OF TRUST']
df_19 = df_lak['CHEATING']
df_20 = df_lak['COUNTERFIETING']
                    
df_21 = df_lak['ARSON']
df_22 = df_lak['HURT/GREVIOUS HURT']
df_23 = df_lak['DOWRY DEATHS']
df_24 = df_lak['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_lak['INSULT TO MODESTY OF WOMEN']

df_26 = df_lak['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_lak['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_lak['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_lak['OTHER IPC CRIMES']
df_30 = df_lak['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()                 

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                           
                                                                                 
# state-19: MADHYA PRADESH

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_mad = df_total[df_total.STATE_UT == 'MADHYA PRADESH']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_mad.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_mad['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_mad.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_mad['MURDER']
df_2 = df_mad['ATTEMPT TO MURDER']
df_3 = df_mad['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_mad['RAPE']
df_5 = df_mad['CUSTODIAL RAPE']
                    
df_6 = df_mad['OTHER RAPE']
df_7 = df_mad['KIDNAPPING & ABDUCTION']
df_8 = df_mad['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_mad['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_mad['DACOITY']

df_11 = df_mad['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_mad['ROBBERY']
df_13 = df_mad['BURGLARY']
df_14 = df_mad['THEFT']
df_15 = df_mad['AUTO THEFT']

df_16 = df_mad['OTHER THEFT']
df_17 = df_mad['RIOTS']
df_18 = df_mad['CRIMINAL BREACH OF TRUST']
df_19 = df_mad['CHEATING']
df_20 = df_mad['COUNTERFIETING']
                    
df_21 = df_mad['ARSON']
df_22 = df_mad['HURT/GREVIOUS HURT']
df_23 = df_mad['DOWRY DEATHS']
df_24 = df_mad['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_mad['INSULT TO MODESTY OF WOMEN']

df_26 = df_mad['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_mad['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_mad['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_mad['OTHER IPC CRIMES']
df_30 = df_mad['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()       

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                     
                                                               
# state-20: MAHARASHTRA



#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_maha = df_total[df_total.STATE_UT == 'MAHARASHTRA']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_maha.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_maha['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_maha.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_maha['MURDER']
df_2 = df_maha['ATTEMPT TO MURDER']
df_3 = df_maha['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_maha['RAPE']
df_5 = df_maha['CUSTODIAL RAPE']
                    
df_6 = df_maha['OTHER RAPE']
df_7 = df_maha['KIDNAPPING & ABDUCTION']
df_8 = df_maha['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_maha['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_maha['DACOITY']

df_11 = df_maha['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_maha['ROBBERY']
df_13 = df_maha['BURGLARY']
df_14 = df_maha['THEFT']
df_15 = df_maha['AUTO THEFT']

df_16 = df_maha['OTHER THEFT']
df_17 = df_maha['RIOTS']
df_18 = df_maha['CRIMINAL BREACH OF TRUST']
df_19 = df_maha['CHEATING']
df_20 = df_maha['COUNTERFIETING']
                    
df_21 = df_maha['ARSON']
df_22 = df_maha['HURT/GREVIOUS HURT']
df_23 = df_maha['DOWRY DEATHS']
df_24 = df_maha['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_maha['INSULT TO MODESTY OF WOMEN']

df_26 = df_maha['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_maha['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_maha['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_maha['OTHER IPC CRIMES']
df_30 = df_maha['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()          

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                              
                                                                                          
# state-21: MANIPUR
#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_man = df_total[df_total.STATE_UT == 'MANIPUR']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_man.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_man['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_man.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_man['MURDER']
df_2 = df_man['ATTEMPT TO MURDER']
df_3 = df_man['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_man['RAPE']
df_5 = df_man['CUSTODIAL RAPE']
                    
df_6 = df_man['OTHER RAPE']
df_7 = df_man['KIDNAPPING & ABDUCTION']
df_8 = df_man['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_man['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_man['DACOITY']

df_11 = df_man['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_man['ROBBERY']
df_13 = df_man['BURGLARY']
df_14 = df_man['THEFT']
df_15 = df_man['AUTO THEFT']

df_16 = df_man['OTHER THEFT']
df_17 = df_man['RIOTS']
df_18 = df_man['CRIMINAL BREACH OF TRUST']
df_19 = df_man['CHEATING']
df_20 = df_man['COUNTERFIETING']
                    
df_21 = df_man['ARSON']
df_22 = df_man['HURT/GREVIOUS HURT']
df_23 = df_man['DOWRY DEATHS']
df_24 = df_man['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_man['INSULT TO MODESTY OF WOMEN']

df_26 = df_man['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_man['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_man['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_man['OTHER IPC CRIMES']
df_30 = df_man['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                            
                                                                                    
# state-22: MEGHALAYA

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_megh = df_total[df_total.STATE_UT == 'MEGHALAYA']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_megh.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_megh['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_megh.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_megh['MURDER']
df_2 = df_megh['ATTEMPT TO MURDER']
df_3 = df_megh['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_megh['RAPE']
df_5 = df_megh['CUSTODIAL RAPE']
                    
df_6 = df_megh['OTHER RAPE']
df_7 = df_megh['KIDNAPPING & ABDUCTION']
df_8 = df_megh['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_megh['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_megh['DACOITY']

df_11 = df_megh['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_megh['ROBBERY']
df_13 = df_megh['BURGLARY']
df_14 = df_megh['THEFT']
df_15 = df_megh['AUTO THEFT']

df_16 = df_megh['OTHER THEFT']
df_17 = df_megh['RIOTS']
df_18 = df_megh['CRIMINAL BREACH OF TRUST']
df_19 = df_megh['CHEATING']
df_20 = df_megh['COUNTERFIETING']
                    
df_21 = df_megh['ARSON']
df_22 = df_megh['HURT/GREVIOUS HURT']
df_23 = df_megh['DOWRY DEATHS']
df_24 = df_megh['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_megh['INSULT TO MODESTY OF WOMEN']

df_26 = df_megh['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_megh['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_megh['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_megh['OTHER IPC CRIMES']
df_30 = df_megh['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()            

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                                    
                                                                                                            
# state-23: MIZORAM

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_mizo = df_total[df_total.STATE_UT == 'MIZORAM']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_mizo.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_mizo['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_mizo.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_mizo['MURDER']
df_2 = df_mizo['ATTEMPT TO MURDER']
df_3 = df_mizo['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_mizo['RAPE']
df_5 = df_mizo['CUSTODIAL RAPE']
                    
df_6 = df_mizo['OTHER RAPE']
df_7 = df_mizo['KIDNAPPING & ABDUCTION']
df_8 = df_mizo['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_mizo['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_mizo['DACOITY']

df_11 = df_mizo['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_mizo['ROBBERY']
df_13 = df_mizo['BURGLARY']
df_14 = df_mizo['THEFT']
df_15 = df_mizo['AUTO THEFT']

df_16 = df_mizo['OTHER THEFT']
df_17 = df_mizo['RIOTS']
df_18 = df_mizo['CRIMINAL BREACH OF TRUST']
df_19 = df_mizo['CHEATING']
df_20 = df_mizo['COUNTERFIETING']
                    
df_21 = df_mizo['ARSON']
df_22 = df_mizo['HURT/GREVIOUS HURT']
df_23 = df_mizo['DOWRY DEATHS']
df_24 = df_mizo['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_mizo['INSULT TO MODESTY OF WOMEN']

df_26 = df_mizo['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_mizo['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_mizo['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_mizo['OTHER IPC CRIMES']
df_30 = df_mizo['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()              

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                                          
                                                                                                                              
# state-24: NAGALAND

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_naga = df_total[df_total.STATE_UT == 'NAGALAND']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_naga.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_naga['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_naga.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_naga['MURDER']
df_2 = df_naga['ATTEMPT TO MURDER']
df_3 = df_naga['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_naga['RAPE']
df_5 = df_naga['CUSTODIAL RAPE']
                    
df_6 = df_naga['OTHER RAPE']
df_7 = df_naga['KIDNAPPING & ABDUCTION']
df_8 = df_naga['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_naga['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_naga['DACOITY']

df_11 = df_naga['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_naga['ROBBERY']
df_13 = df_naga['BURGLARY']
df_14 = df_naga['THEFT']
df_15 = df_naga['AUTO THEFT']

df_16 = df_naga['OTHER THEFT']
df_17 = df_naga['RIOTS']
df_18 = df_naga['CRIMINAL BREACH OF TRUST']
df_19 = df_naga['CHEATING']
df_20 = df_naga['COUNTERFIETING']
                    
df_21 = df_naga['ARSON']
df_22 = df_naga['HURT/GREVIOUS HURT']
df_23 = df_naga['DOWRY DEATHS']
df_24 = df_naga['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_naga['INSULT TO MODESTY OF WOMEN']

df_26 = df_naga['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_naga['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_naga['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_naga['OTHER IPC CRIMES']
df_30 = df_naga['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()             

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                                       
                                                                                                                     
# state-25: ODISHA

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_odi = df_total[df_total.STATE_UT == 'ODISHA']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_odi.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_odi['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_odi.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_odi['MURDER']
df_2 = df_odi['ATTEMPT TO MURDER']
df_3 = df_odi['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_odi['RAPE']
df_5 = df_odi['CUSTODIAL RAPE']
                    
df_6 = df_odi['OTHER RAPE']
df_7 = df_odi['KIDNAPPING & ABDUCTION']
df_8 = df_odi['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_odi['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_odi['DACOITY']

df_11 = df_odi['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_odi['ROBBERY']
df_13 = df_odi['BURGLARY']
df_14 = df_odi['THEFT']
df_15 = df_odi['AUTO THEFT']

df_16 = df_odi['OTHER THEFT']
df_17 = df_odi['RIOTS']
df_18 = df_odi['CRIMINAL BREACH OF TRUST']
df_19 = df_odi['CHEATING']
df_20 = df_odi['COUNTERFIETING']
                    
df_21 = df_odi['ARSON']
df_22 = df_odi['HURT/GREVIOUS HURT']
df_23 = df_odi['DOWRY DEATHS']
df_24 = df_odi['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_odi['INSULT TO MODESTY OF WOMEN']

df_26 = df_odi['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_odi['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_odi['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_odi['OTHER IPC CRIMES']
df_30 = df_odi['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()               

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                                             
                                                                                                                                       
# state-26: PUDUCHERRY

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_pudu = df_total[df_total.STATE_UT == 'PUDUCHERRY']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_pudu.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_pudu['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_pudu.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_pudu['MURDER']
df_2 = df_pudu['ATTEMPT TO MURDER']
df_3 = df_pudu['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_pudu['RAPE']
df_5 = df_pudu['CUSTODIAL RAPE']
                    
df_6 = df_pudu['OTHER RAPE']
df_7 = df_pudu['KIDNAPPING & ABDUCTION']
df_8 = df_pudu['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_pudu['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_pudu['DACOITY']

df_11 = df_pudu['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_pudu['ROBBERY']
df_13 = df_pudu['BURGLARY']
df_14 = df_pudu['THEFT']
df_15 = df_pudu['AUTO THEFT']

df_16 = df_pudu['OTHER THEFT']
df_17 = df_pudu['RIOTS']
df_18 = df_pudu['CRIMINAL BREACH OF TRUST']
df_19 = df_pudu['CHEATING']
df_20 = df_pudu['COUNTERFIETING']
                    
df_21 = df_pudu['ARSON']
df_22 = df_pudu['HURT/GREVIOUS HURT']
df_23 = df_pudu['DOWRY DEATHS']
df_24 = df_pudu['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_pudu['INSULT TO MODESTY OF WOMEN']

df_26 = df_pudu['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_pudu['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_pudu['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_pudu['OTHER IPC CRIMES']
df_30 = df_pudu['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()           

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                                 
                                                                                                   
# state-27: PUNJAB 

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_pun = df_total[df_total.STATE_UT == 'PUNJAB']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_pun.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_pun['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_pun.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_pun['MURDER']
df_2 = df_pun['ATTEMPT TO MURDER']
df_3 = df_pun['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_pun['RAPE']
df_5 = df_pun['CUSTODIAL RAPE']
                    
df_6 = df_pun['OTHER RAPE']
df_7 = df_pun['KIDNAPPING & ABDUCTION']
df_8 = df_pun['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_pun['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_pun['DACOITY']

df_11 = df_pun['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_pun['ROBBERY']
df_13 = df_pun['BURGLARY']
df_14 = df_pun['THEFT']
df_15 = df_pun['AUTO THEFT']

df_16 = df_pun['OTHER THEFT']
df_17 = df_pun['RIOTS']
df_18 = df_pun['CRIMINAL BREACH OF TRUST']
df_19 = df_pun['CHEATING']
df_20 = df_pun['COUNTERFIETING']
                    
df_21 = df_pun['ARSON']
df_22 = df_pun['HURT/GREVIOUS HURT']
df_23 = df_pun['DOWRY DEATHS']
df_24 = df_pun['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_pun['INSULT TO MODESTY OF WOMEN']

df_26 = df_pun['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_pun['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_pun['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_pun['OTHER IPC CRIMES']
df_30 = df_pun['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()              

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                                          
                                                                                                                              
# state-28: RAJASTHAN 
#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_rajas = df_total[df_total.STATE_UT == 'RAJASTHAN']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_rajas.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_rajas['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_rajas.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_rajas['MURDER']
df_2 = df_rajas['ATTEMPT TO MURDER']
df_3 = df_rajas['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_rajas['RAPE']
df_5 = df_rajas['CUSTODIAL RAPE']
                    
df_6 = df_rajas['OTHER RAPE']
df_7 = df_rajas['KIDNAPPING & ABDUCTION']
df_8 = df_rajas['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_rajas['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_rajas['DACOITY']

df_11 = df_rajas['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_rajas['ROBBERY']
df_13 = df_rajas['BURGLARY']
df_14 = df_rajas['THEFT']
df_15 = df_rajas['AUTO THEFT']

df_16 = df_rajas['OTHER THEFT']
df_17 = df_rajas['RIOTS']
df_18 = df_rajas['CRIMINAL BREACH OF TRUST']
df_19 = df_rajas['CHEATING']
df_20 = df_rajas['COUNTERFIETING']
                    
df_21 = df_rajas['ARSON']
df_22 = df_rajas['HURT/GREVIOUS HURT']
df_23 = df_rajas['DOWRY DEATHS']
df_24 = df_rajas['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_rajas['INSULT TO MODESTY OF WOMEN']

df_26 = df_rajas['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_rajas['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_rajas['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_rajas['OTHER IPC CRIMES']
df_30 = df_rajas['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()           

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                                 
                                                                                                   
# state-29: SIKKIM

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_sik = df_total[df_total.STATE_UT == 'SIKKIM']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_sik.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_sik['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_sik.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_sik['MURDER']
df_2 = df_sik['ATTEMPT TO MURDER']
df_3 = df_sik['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_sik['RAPE']
df_5 = df_sik['CUSTODIAL RAPE']
                    
df_6 = df_sik['OTHER RAPE']
df_7 = df_sik['KIDNAPPING & ABDUCTION']
df_8 = df_sik['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_sik['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_sik['DACOITY']

df_11 = df_sik['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_sik['ROBBERY']
df_13 = df_sik['BURGLARY']
df_14 = df_sik['THEFT']
df_15 = df_sik['AUTO THEFT']

df_16 = df_sik['OTHER THEFT']
df_17 = df_sik['RIOTS']
df_18 = df_sik['CRIMINAL BREACH OF TRUST']
df_19 = df_sik['CHEATING']
df_20 = df_sik['COUNTERFIETING']
                    
df_21 = df_sik['ARSON']
df_22 = df_sik['HURT/GREVIOUS HURT']
df_23 = df_sik['DOWRY DEATHS']
df_24 = df_sik['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_sik['INSULT TO MODESTY OF WOMEN']

df_26 = df_sik['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_sik['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_sik['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_sik['OTHER IPC CRIMES']
df_30 = df_sik['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()               

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                                             
                                                                                                                                       
# state-30: TAMIL NADU

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_tamil = df_total[df_total.STATE_UT == 'TAMIL NADU']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_tamil.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_tamil['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_tamil.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_tamil['MURDER']
df_2 = df_tamil['ATTEMPT TO MURDER']
df_3 = df_tamil['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_tamil['RAPE']
df_5 = df_tamil['CUSTODIAL RAPE']
                    
df_6 = df_tamil['OTHER RAPE']
df_7 = df_tamil['KIDNAPPING & ABDUCTION']
df_8 = df_tamil['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_tamil['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_tamil['DACOITY']

df_11 = df_tamil['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_tamil['ROBBERY']
df_13 = df_tamil['BURGLARY']
df_14 = df_tamil['THEFT']
df_15 = df_tamil['AUTO THEFT']

df_16 = df_tamil['OTHER THEFT']
df_17 = df_tamil['RIOTS']
df_18 = df_tamil['CRIMINAL BREACH OF TRUST']
df_19 = df_tamil['CHEATING']
df_20 = df_tamil['COUNTERFIETING']
                    
df_21 = df_tamil['ARSON']
df_22 = df_tamil['HURT/GREVIOUS HURT']
df_23 = df_tamil['DOWRY DEATHS']
df_24 = df_tamil['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_tamil['INSULT TO MODESTY OF WOMEN']

df_26 = df_tamil['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_tamil['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_tamil['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_tamil['OTHER IPC CRIMES']
df_30 = df_tamil['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()           

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                                 
                                                                                                   
# state-31: TRIPURA

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_tri = df_total[df_total.STATE_UT == 'TRIPURA']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_tri.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_tri['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_tri.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_tri['MURDER']
df_2 = df_tri['ATTEMPT TO MURDER']
df_3 = df_tri['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_tri['RAPE']
df_5 = df_tri['CUSTODIAL RAPE']
                    
df_6 = df_tri['OTHER RAPE']
df_7 = df_tri['KIDNAPPING & ABDUCTION']
df_8 = df_tri['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_tri['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_tri['DACOITY']

df_11 = df_tri['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_tri['ROBBERY']
df_13 = df_tri['BURGLARY']
df_14 = df_tri['THEFT']
df_15 = df_tri['AUTO THEFT']

df_16 = df_tri['OTHER THEFT']
df_17 = df_tri['RIOTS']
df_18 = df_tri['CRIMINAL BREACH OF TRUST']
df_19 = df_tri['CHEATING']
df_20 = df_tri['COUNTERFIETING']
                    
df_21 = df_tri['ARSON']
df_22 = df_tri['HURT/GREVIOUS HURT']
df_23 = df_tri['DOWRY DEATHS']
df_24 = df_tri['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_tri['INSULT TO MODESTY OF WOMEN']

df_26 = df_tri['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_tri['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_tri['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_tri['OTHER IPC CRIMES']
df_30 = df_tri['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()              

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                                          
                                                                                                                              
# state-32: UTTAR PRADESH

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_up = df_total[df_total.STATE_UT == 'UTTAR PRADESH']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_up.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_up['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_up.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_up['MURDER']
df_2 = df_up['ATTEMPT TO MURDER']
df_3 = df_up['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_up['RAPE']
df_5 = df_up['CUSTODIAL RAPE']
                    
df_6 = df_up['OTHER RAPE']
df_7 = df_up['KIDNAPPING & ABDUCTION']
df_8 = df_up['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_up['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_up['DACOITY']

df_11 = df_up['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_up['ROBBERY']
df_13 = df_up['BURGLARY']
df_14 = df_up['THEFT']
df_15 = df_up['AUTO THEFT']

df_16 = df_up['OTHER THEFT']
df_17 = df_up['RIOTS']
df_18 = df_up['CRIMINAL BREACH OF TRUST']
df_19 = df_up['CHEATING']
df_20 = df_up['COUNTERFIETING']
                    
df_21 = df_up['ARSON']
df_22 = df_up['HURT/GREVIOUS HURT']
df_23 = df_up['DOWRY DEATHS']
df_24 = df_up['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_up['INSULT TO MODESTY OF WOMEN']

df_26 = df_up['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_up['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_up['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_up['OTHER IPC CRIMES']
df_30 = df_up['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()        

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                        
                                                                        
# state-33: UTTARAKHAND

#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_uk = df_total[df_total.STATE_UT == 'UTTARAKHAND']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_uk.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_uk['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_uk.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_uk['MURDER']
df_2 = df_uk['ATTEMPT TO MURDER']
df_3 = df_uk['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_uk['RAPE']
df_5 = df_uk['CUSTODIAL RAPE']
                    
df_6 = df_uk['OTHER RAPE']
df_7 = df_uk['KIDNAPPING & ABDUCTION']
df_8 = df_uk['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_uk['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_uk['DACOITY']

df_11 = df_uk['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_uk['ROBBERY']
df_13 = df_uk['BURGLARY']
df_14 = df_uk['THEFT']
df_15 = df_uk['AUTO THEFT']

df_16 = df_uk['OTHER THEFT']
df_17 = df_uk['RIOTS']
df_18 = df_uk['CRIMINAL BREACH OF TRUST']
df_19 = df_uk['CHEATING']
df_20 = df_uk['COUNTERFIETING']
                    
df_21 = df_uk['ARSON']
df_22 = df_uk['HURT/GREVIOUS HURT']
df_23 = df_uk['DOWRY DEATHS']
df_24 = df_uk['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_uk['INSULT TO MODESTY OF WOMEN']

df_26 = df_uk['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_uk['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_uk['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_uk['OTHER IPC CRIMES']
df_30 = df_uk['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()          

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")                              
                                                                                          
# state-34: WEST BENGAL
#---: convert to Total operation :------- 

print("\n---: convert to Total operation :-------")
df_wb = df_total[df_total.STATE_UT == 'WEST BENGAL']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_wb.shape)
print('---------------------------------------------')
print('\t Available year\n--------------------------------')       
year=df_wb['YEAR']
print(year)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_wb.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

df_1 = df_wb['MURDER']
df_2 = df_wb['ATTEMPT TO MURDER']
df_3 = df_wb['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER']
df_4 = df_wb['RAPE']
df_5 = df_wb['CUSTODIAL RAPE']
                    
df_6 = df_wb['OTHER RAPE']
df_7 = df_wb['KIDNAPPING & ABDUCTION']
df_8 = df_wb['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS']
df_9 = df_wb['KIDNAPPING AND ABDUCTION OF OTHERS']
df_10 = df_wb['DACOITY']

df_11 = df_wb['PREPARATION AND ASSEMBLY FOR DACOITY']
df_12 = df_wb['ROBBERY']
df_13 = df_wb['BURGLARY']
df_14 = df_wb['THEFT']
df_15 = df_wb['AUTO THEFT']

df_16 = df_wb['OTHER THEFT']
df_17 = df_wb['RIOTS']
df_18 = df_wb['CRIMINAL BREACH OF TRUST']
df_19 = df_wb['CHEATING']
df_20 = df_wb['COUNTERFIETING']
                    
df_21 = df_wb['ARSON']
df_22 = df_wb['HURT/GREVIOUS HURT']
df_23 = df_wb['DOWRY DEATHS']
df_24 = df_wb['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY']
df_25 = df_wb['INSULT TO MODESTY OF WOMEN']

df_26 = df_wb['CRUELTY BY HUSBAND OR HIS RELATIVES']
df_27 = df_wb['IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES']
df_28 = df_wb['CAUSING DEATH BY NEGLIGENCE']
df_29 = df_wb['OTHER IPC CRIMES']
df_30 = df_wb['TOTAL IPC CRIMES'] 

plt.title('plot - 1 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> MURDER")

plt.plot(year,df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> ATTEMPT TO MURDER")

plt.plot(year,df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
            
plt.plot(year,df_4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> RAPE")
            
plt.plot(year,df_5,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> CUSTODIAL RAPE")
            
plt.legend()
plt.show()

#------------ plot-2 -----------------

plt.title('plot - 2:2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_6,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="6 --> OTHER RAPE")

plt.plot(year,df_7,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="7 --> KIDNAPPING & ABDUCTION")

plt.plot(year,df_8,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
            
plt.plot(year,df_9,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
            
plt.plot(year,df_10,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="10 --> DACOITY")
            
plt.legend()
plt.show() 

#------------ plot-3 -----------------

plt.title('plot - 3: 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_11,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="11 --> PREPARATION AND ASSEMBLY FOR DACOITY")

plt.plot(year,df_12,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="12 --> ROBBERY")

plt.plot(year,df_13,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="13 --> BURGLARY")
            
plt.plot(year,df_14,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="14 --> THEFT")
            
plt.plot(year,df_15,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="15 --> AUTO THEFT")
            
plt.legend()
plt.show() 

#------------ plot-4 -----------------

plt.title('plot - 4 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_16,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="16 --> OTHER THEFT")

plt.plot(year,df_17,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="17 --> RIOTS")

plt.plot(year,df_18,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="18 --> CRIMINAL BREACH OF TRUST")
            
plt.plot(year,df_19,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="19 --> CHEATING")
            
plt.plot(year,df_20,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="20 --> COUNTERFIETING")
            
plt.legend()
plt.show() 

#------------ plot-5 -----------------

plt.title('plot - 5 : 2001 - 2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_21,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="21 --> ARSON")

plt.plot(year,df_22,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="22 --> HURT/GREVIOUS HURT")

plt.plot(year,df_23,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="23 --> DOWRY DEATHS")
            
plt.plot(year,df_24,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
            
plt.plot(year,df_25,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="25 --> INSULT TO MODESTY OF WOMEN")
            
plt.legend()
plt.show() 

#------------ plot-6 -----------------

plt.title('plot - 6 : 2001-2012')
plt.xlabel("Year --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(year,df_26,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")

plt.plot(year,df_27,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")

plt.plot(year,df_28,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="28 --> CAUSING DEATH BY NEGLIGENCE")
            
plt.plot(year,df_29,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="29 --> OTHER IPC CRIMES")
            
plt.plot(year,df_30,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="30 --> TOTAL IPC CRIMES")
            
plt.legend()
plt.show()  

print("1 --> MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_1)
print("--------------------------------------------------------------")

print("2 --> ATTEMPT TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_2)
print("--------------------------------------------------------------")
	
print("3 --> CULPABLE HOMICIDE NOT AMOUNTING TO MURDER")
print("\n--------------\nRow No. --> data\n------------------\n")	
print(df_3)
print("--------------------------------------------------------------")

print("4 --> RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_4)
print("--------------------------------------------------------------")

print("5 --> CUSTODIAL RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_5)
print("--------------------------------------------------------------")

print("6 --> OTHER RAPE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_6)
print("--------------------------------------------------------------")

print("7 --> KIDNAPPING & ABDUCTION")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_7)
print("--------------------------------------------------------------")

print("8 --> KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_8)
print("--------------------------------------------------------------")

print("9 --> KIDNAPPING AND ABDUCTION OF OTHERS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_9)
print("--------------------------------------------------------------")

print("10 --> DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_10)
print("--------------------------------------------------------------")

print("11 --> PREPARATION AND ASSEMBLY FOR DACOITY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_11)
print("--------------------------------------------------------------")

print("12 --> ROBBERY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_12)
print("--------------------------------------------------------------")

print("13 --> BURGLARY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_13)
print("--------------------------------------------------------------")

print("14 --> THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_14)
print("--------------------------------------------------------------")

print("15 --> AUTO THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_15)
print("--------------------------------------------------------------")

print("16 --> OTHER THEFT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_16)
print("--------------------------------------------------------------")

print("17 --> RIOTS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_17)
print("--------------------------------------------------------------")

print("18 --> CRIMINAL BREACH OF TRUST")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_18)
print("--------------------------------------------------------------")

print("19 --> CHEATING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_19)
print("--------------------------------------------------------------")
	
print("20 --> COUNTERFIETING")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_20)
print("--------------------------------------------------------------")

print("21 --> ARSON")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_21)
print("--------------------------------------------------------------")

print("22 --> HURT/GREVIOUS HURT")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_22)
print("--------------------------------------------------------------")

print("23 --> DOWRY DEATHS")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_23)
print("--------------------------------------------------------------")

print("24 --> ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_24)
print("--------------------------------------------------------------")

print("25 --> INSULT TO MODESTY OF WOMEN")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_25)
print("--------------------------------------------------------------")

print("26 --> CRUELTY BY HUSBAND OR HIS RELATIVES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_26)
print("--------------------------------------------------------------")

print("27 --> IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_27)
print("--------------------------------------------------------------")

print("28 --> CAUSING DEATH BY NEGLIGENCE")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_28)
print("--------------------------------------------------------------")

print("29 --> OTHER IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_29)
print("--------------------------------------------------------------")

print("30 --> TOTAL IPC CRIMES")
print("\n--------------\nRow No. --> data\n------------------\n")
print(df_30)
print("--------------------------------------------------------------")

