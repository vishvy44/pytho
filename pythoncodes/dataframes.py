  
import pandas as pd
print("LIST TO DATAFRAME")
list=[12,13,14,15]


pd0=pd.DataFrame(list)
print(pd0)

print("NESTED LIST TO DATAFRAME")
list=[12,13,14,15]
list2=[2,3,4,5]
list1=[list,list2]
pd1=pd.DataFrame(list1,columns=['ek','do','teen','chaar'])
print(pd1)

print("LIST OF DICTIONARY TO DATAFRAME")
dictList = [ {'1': '2', '2': '3', '3': '4'},{'4': '5', '5': '6', '6': '7'}

]
dictList1 = [ {'4': '5', '5': '6', '6': '7'},{'1': '2', '2': '3', '3': '4'}

]
list=[dictList,dictList1]
pd2=pd.DataFrame(list,columns=['key', 'Value'])
print(pd2)

print("DICTIONARY TO DATAFRAME")
dic1={'1':'2','2':'3'}

pd3=pd.DataFrame(dic1.items(), columns=['key', 'Value'])
print(pd3)

