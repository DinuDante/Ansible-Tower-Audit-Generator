import os
import glob
import pandas as pd
import openpyxl as pxl
from datetime import datetime

time = str(datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p"))

#Declaration of Lists

ip = []
created_by = []
inventory_id = []
inventory_name = []
inventory_pool = []
org_id = []
hosts_count = []
last_date_modified = []

#Path to the Executing Directory

path = r'/root/inv_audit_generator/'


os.chdir(path)
myFiles = glob.glob('*.json')


for file in myFiles:
	print(file)
	if file.endswith(".json"):
		df = pd.read_json(file)
		print (df)


#Loop to traverse through Json-Inner

		for index, row in df.iterrows():
			print (row['results']['name'])
			ip.append(row['results']['name'])

			print ("Created By")
			try: print (row['results']['summary_fields']['created_by']['username'])
			except: print ("NaN")
			try: created_by.append(row['results']['summary_fields']['created_by']['username'])
			except: created_by.append("NAN")

			print ("Inventory ID")

			try: print (row['results']['summary_fields']['inventory']['id'])
			except: print ("NaN")
			try: inventory_id.append(row['results']['summary_fields']['inventory']['id'])
			except: inventory_id.append("NAN")

			print ("Organization ID")

			try: print (row['results']['summary_fields']['inventory']['organization_id'])
			except: print ("NaN")
			try: org_id.append(row['results']['summary_fields']['inventory']['organization_id'])
			except: org_id.append("NAN")

			print ("Inventory Name")

			try: print (row['results']['summary_fields']['inventory']['name'])
			except: print ("NaN")
			try: inventory_name.append(row['results']['summary_fields']['inventory']['name'])
			except: inventory_name.append("NAN")

			print ("Inventory Total Hosts")
			try: print (row['results']['summary_fields']['inventory']['total_hosts'])
			except: print ("NaN")
			try: hosts_count.append(row['results']['summary_fields']['inventory']['total_hosts'])
			except: hosts_count.append("NAN")

			print ("Last Date Modified")

			try: print (row['results']['modified'])
			except: print ("NaN")
			try: last_date_modified.append(row['results']['modified'])
			except: last_date_modified.append("NAN")

			print ("\n")

			print ("*********************************\n")


#Getting Head Count
print("Creating dfs...")
tip = str(len(ip))
unique_lst = list(set(ip))
uip = str(len(unique_lst))

x=0

#print(len(ip))
#print(len(unique_lst))

for i in unique_lst:
  st = ""
  for j in range(len(ip)):
    if i == ip[j]:
      st = st + "\n" + str(inventory_name[j])
    else:
      x=x+1
  inventory_pool.append(st)


#Column Head Count String

uni_ip = "Unique IPs " + "(" + uip + ")"
t_ip = "All IPs " + "(" + tip + ")"


#Creating DataFrames

df1 = pd.DataFrame({"Organization ID" : org_id})

df2 = pd.DataFrame({"Inventory ID" : inventory_id})

df3 = pd.DataFrame({"Inventory Name" : inventory_name})

df4 = pd.DataFrame({"Created By" : created_by})

df5 = pd.DataFrame({"Host/IP" : ip})

df6 = pd.DataFrame({"Last Date Modified" : last_date_modified})

df8 = pd.DataFrame({t_ip : ip})

df9 = pd.DataFrame({uni_ip : unique_lst})

df10 = pd.DataFrame({"Inventory Pool" : inventory_pool})

#Concating DataFrames

df = pd.concat([df1, df2, df3, df4, df5, df6], axis=1)
df2 = pd.concat([df8, df9], axis=1)
df3 = pd.concat([df9,df10], axis=1)

#Exporting Filename with TimeStamp
filename = 'PRODUCTION_Inv_Details_'+time+'.xlsx'

#Creating Sheets and Exporting
print("Generating Report...")
df.to_excel(filename, 'Inv Details', index=False)
excel_book = pxl.load_workbook(filename)
with pd.ExcelWriter(filename, engine='openpyxl') as writer:
  writer.book = excel_book
  writer.sheets = {
  worksheet.title: worksheet
  for worksheet in excel_book.worksheets}
  df2.to_excel(writer, 'IP Details', index=False)
  df3.to_excel(writer, 'IP vs Inventory', index=False)
  writer.save()