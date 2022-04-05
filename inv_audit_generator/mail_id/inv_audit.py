import os
import numpy as np
import glob
import pandas as pd
import openpyxl as pxl
from datetime import datetime

time = str(datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p"))

#Declaration of Lists

usr_name = []
fst_name = []
lst_name = []
email = []
is_super = []
is_sysaudit = []
last_login = []

#Path to the Executing Directory

path = r'/root/inv_audit_generator/mail_id'


os.chdir(path)
myFiles = glob.glob('*.json')


for file in myFiles:
  print(file)
  if file.startswith("jreport"):
    df = pd.read_json(file)
    print (df)


#Loop to traverse through Json-Inner

    for index, row in df.iterrows():
      print ("Username :")

      try: print (row['results']['username'])
      except: continue
      usr_name.append(row['results']['username'])

      print ("First Name :")

      print (row['results']['first_name'])
      fst_name.append(row['results']['first_name'])
			
      print ("Last Name :")

      try: print (row['results']['last_name'])
      except: print ("NaN")
      try: lst_name.append(row['results']['last_name'])
      except: lst_name.append("NaN")

      print ("Email ID :")

      try: print (row['results']['email'])
      except: print ("NaN")
      try: email.append(row['results']['email'])
      except: email.append("NaN")

      print ("Is Superuser :")

      try: print (row['results']['is_superuser'])
      except: print ("NaN")
      try: is_super.append(row['results']['is_superuser'])
      except: is_super.append("NaN")
      
      print ("Is System Auditor :")
      
      try: print (row['results']['is_system_auditor'])
      except: print ("NaN")
      try: is_sysaudit.append(row['results']['is_system_auditor'])
      except: is_sysaudit.append("NaN")

      print ("Last Login :")
      try: print (row['results']['last_login'])
      except: print ("NaN")
      try: last_login.append(row['results']['last_login'])
      except: last_login.append("NaN")

      print ("\n")

      print ("*********************************\n")



#Creating DataFrames

df1 = pd.DataFrame({
"Username" : usr_name
})

df2 = pd.DataFrame({
"First Name" : fst_name
})

df3 = pd.DataFrame({
"Last Name" : lst_name
})

df4 = pd.DataFrame({
"Email" : email
})

df5 = pd.DataFrame({
"Is Superuser" : is_super
})


df6 = pd.DataFrame({
"Is System Auditor" : is_sysaudit
})

df7 = pd.DataFrame({
"Last Login On" : last_login
})

#Concating DataFrames

df = pd.concat([df1, df2, df3, df4, df5, df6, df7], axis=1)

#Exporting Filename with TimeStamp
filename = 'Prod_User_Details_'+time+'.xlsx'

#mail_array = df4.to_numpy()
#np.savetxt(time+"Mail.txt", mail_array)
df4.to_csv(r'mail.yml', header=None, index=None, sep=' ', mode='a')

#Creating Sheets and Exporting
print("Generating Report...")
df.to_excel(filename, 'User Details', index=False)
excel_book = pxl.load_workbook(filename)
