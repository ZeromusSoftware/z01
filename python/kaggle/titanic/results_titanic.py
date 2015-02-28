'''
Autor : Bastien Pederencino <zeromus.software@gmail.com>
Created : 28/02/2015
'''

import numpy as np
import pandas as pd
'''import matplotlib.pyplot as plt
from pylab import *'''
import csv as csv
from sklearn.ensemble import RandomForestClassifier as rfc

data = pd.read_csv('titanic/train.csv', header=0)

''' -------------- DATA WRANGLING ----------------- '''

#print data
## 12 columns
## PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch Ticket Fare, Cabin, Embarked
#print data.describe()
## PassengerId, Survived, Pclass, Age, SibSp, Parch, Fare
#print data.isnull().sum()
## 177 Ages are null, 687 Cabins are null, 2 Embarked data are null
## Age null -> age median
data.loc[(data.Age.isnull()), 'Age'] = data.Age.median()
#print data.Age.isnull().sum()
## Embarked data null -> the most used Embarked data
default_Embarked = data.Embarked.dropna().mode().values
data.loc[(data.Embarked.isnull()), 'Embarked'] = default_Embarked
## Embarked str -> int
e = list(enumerate(np.unique(data['Embarked'])))
eDict = { name : i for i, name in e }
data.Embarked = data.Embarked.map( lambda x : eDict[x] ).astype(int)
#print data.Embarked.isnull().sum()
## Female, Male -> 0, 1
data['Gender'] = data.Sex.map({ 'female':0, 'male':1 }).astype(int)
## To clean useless columns
data = data.drop(['PassengerId', 'Name', 'Sex', 'Ticket', 'Cabin'], axis=1)
#print data.isnull().sum()
## PassengerId, Survived, Pclass, Age, SibSp, Parch, Fare, Embarked, Gender

''' ----------------- DATA ANALYSIS ------------------ '''
'''
#print data.Pclass.describe()
## Pclass = 1, 2 or 3

dPclass1 = data['Pclass'] == 1
dPclass2 = data['Pclass'] == 2
dPclass3 = data['Pclass'] == 3
dPclass1S = data.loc[(dPclass1), 'Survived'].sum()
dPclass2S = data.loc[(dPclass2), 'Survived'].sum()
dPclass3S = data.loc[(dPclass3), 'Survived'].sum()
dPclass1C = data.loc[(dPclass1), 'Survived'].count()
dPclass2C = data.loc[(dPclass2), 'Survived'].count()
dPclass3C = data.loc[(dPclass3), 'Survived'].count()
result1 = (float(dPclass1S)/float(dPclass1C)) * 100
result2 = (float(dPclass2S)/float(dPclass2C)) * 100
result3 = (float(dPclass3S)/float(dPclass3C)) * 100
#print 'Percent of Class 1 people who survived ' +str(result1) + '%'
#print 'Percent of Class 2 people who survived ' +str(result2) + '%'
#print 'Percent of Class 3 people who survived ' +str(result3) + '%'

## Class 1 : 62.96%, Class 2 : 47.28%, Class 3 : 24.24%

## Mosaic plot
plt.subplot(1,2,1)
plt.bar(1, result1, facecolor='red', edgecolor='white')
plt.bar(2, result2, facecolor='orange', edgecolor='white')
plt.bar(3, result3, facecolor='yellow', edgecolor='white')

plt.xlim(0.5,4.25)
plt.ylim(0, 100)

text(1+0.4, result1+0.05, str(result1)+'%', ha='center', va='bottom')
text(2+0.4, result2+0.05, str(result2)+'%', ha='center', va='bottom')
text(3+0.4, result3+0.05, str(result3)+'%', ha='center', va='bottom')

plt.legend(('Class 1', 'Class 2', 'Class 3'))
plt.xlabel('All classes (1, 2 or 3)', fontsize=14)
plt.ylabel('People who survived (%)', fontsize=14)
plt.title('Repartition des survivants selon leurs classes', fontsize=16, fontweight='bold')
plt.grid()

#print data.Gender.describe()
## Gender : 0 or 1
plt.subplot(1,2,2)
men = data.loc[(data['Gender'] == 1), 'Survived']
women = data.loc[(data['Gender'] == 0), 'Survived']
result1 = float(men.sum())/float(men.count()) * 100
result2 = float(women.sum())/float(women.count()) * 100
#print [result1, result2]

plt.bar(0, result2, facecolor='pink', edgecolor='white')
plt.bar(1, result1, facecolor='blue', edgecolor='white')

plt.xlim(-0.5, 2.25)
plt.ylim(0,100)

text(0+0.4, result2+0.05, str(result2)+'%', ha='center', va='bottom')
text(1+0.4, result1+0.05, str(result1)+'%', ha='center', va='bottom')

plt.legend(('Women', 'Men'))
plt.xlabel('Gender', fontsize=14)
plt.ylabel('People who survived (%)', fontsize=14)
plt.title('Repartition des survivants selon leur sex', fontsize=16, fontweight='bold')
plt.grid()
#plt.show()
'''

''' ---------------- DATA TEST --------------------- '''

tdata = pd.read_csv('titanic/test.csv', header=0)

#print tdata.isnull().sum()
## PassengerId, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked
tdata['Gender'] = tdata.Sex.map({ 'female' : 0, 'male' : 1 }).astype(int)
tdata.loc[(tdata.Age.isnull()), 'Age'] = tdata.Age.dropna().median()
#print tdata.loc[(tdata.Fare.isnull()), 'Pclass']
## One missing fare value to a third class person 
median_fare_thirdClass = tdata.loc[(tdata.Pclass == 3), 'Fare'].dropna().mode().values
#print median_fare_thirdClass
## 7.75
tdata.loc[(tdata.Fare.isnull()), 'Fare'] = median_fare_thirdClass
e = list(enumerate(np.unique(tdata['Embarked'])))
edict = { name : i for i, name in e }
tdata.Embarked = tdata.Embarked.map( lambda x : edict[x] ).astype(int)

ids = tdata['PassengerId'].values
#print ids

tdata = tdata.drop(['PassengerId', 'Name', 'Sex', 'Ticket', 'Cabin'], axis=1)

#print tdata.describe()

''' ------------------- MACHING LEARNING -------------------- '''

vdata = data.values
vtdata = tdata.values

print 'Training...'
forest = rfc(n_estimators=100)
forest = forest.fit( vdata[0::,1::], vdata[0::,0] )

print 'Predicting...'
output = forest.predict(vtdata).astype(int)

predictions_file = open('myfirstforest.csv', 'wb')
open_file_object = csv.writer(predictions_file)
open_file_object.writerow(['PassengerId', 'Survived'])
open_file_object.writerows(zip(ids, output))
predictions_file.close()
print 'Done.'

'''
1763ieme : with 0.73206 accurency (1st submission)
'''
'''

