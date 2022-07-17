import pandas as pd


df = pd.read_csv('4sem_data.csv')
#print (df.head())

#print (df['Student_Name'])
sname = input ("Enter name :")
name = df.loc[df['Student_Name'].str.contains(sname, case=False)]




print (name)
print ("*********************************")
#print ("Enrollment:\n",name['Roll No'])
#print ("*********************************")
print ("Name:\n",name['Student_Name'])
print ("*********************************")
print ("Student mobile no:\n",name['Student_Mobile No'])
print ("*********************************")
print ('parents no.:\n',name['P_MobileNo'])
print ("*********************************")
print ('Email id:\n',name['Student Email ID'])
