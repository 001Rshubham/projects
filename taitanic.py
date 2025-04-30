"""Titel=Prdicting survival rate
Author=Shubham Landge"""

import pandas as pd  #manuplate and data handling
import seaborn as sns # IN statcal visualisation
import matplotlib.pyplot as plt #in imporove our viuslisation
from  sklearn.model_selection import train_test_split #split dataset in train and test phase
from sklearn.preprocessing import LabelEncoder # this will encode all the catagorial values in dataset
from sklearn.ensemble import RandomForestClassifier #this model will train our module
from sklearn.metrics import classification_report, accuracy_score # this will help us to evaluate our module


df_raw=pd.read_csv("Titanic-Dataset.csv")
df=df_raw.copy()

df.drop(columns=['PassengerID','Name','Ticket','Cabin'],inplace=True)

df['Age'].fillna(df['Age'].median(),inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0],inplace=True)

le=LabelEncoder()
df['Sex']=le.fit_transform(df['Sex'])  #male=1 female=0
df['Embarked']=le.fit_transform(df['Embarked']) #s=2 c=0 q=1

fig1=plt.figure(figsize=(10,5))
survival_counts=df_raw['Survived'].value_counts()
plt.pie(survival_counts,labels=['Survived','Non-Survived'],autopct='1.1f%%',startangle=90, colors=['yello','red'])
plt.title("titanic survival rate")
plt.savefig('fig1.png',dpi=200)
plt.show()