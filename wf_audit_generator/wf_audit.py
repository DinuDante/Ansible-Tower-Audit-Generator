import os
import glob
import pandas as pd
import openpyxl as pxl
from datetime import datetime

time = str(datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p"))

#Declaration of Lists

wfj_id = []
wfj_name = []
j_created_by = []
j_created_on = []
j_lro = []


wf_id = []
wf_name = []
f_approved_by = []
f_created_by = []
f_created_on = []
f_lro = []

#Path to the Executing Directory

path = r'/root/wf_audit_generator'


os.chdir(path)
myFiles = glob.glob('*.json')


for file in myFiles:
	print(file)
	if file.startswith("jreport"):
		df = pd.read_json(file)
		print (df)


#Loop to traverse through Json-Inner

		for index, row in df.iterrows():

			print ("Workflow Job ID :")

			try: print (row['results']['summary_fields']['workflow_job_template']['id'])
			except: continue
			wfj_id.append(row['results']['summary_fields']['workflow_job_template']['id'])

			print ("Workflow Job Name :")

			print (row['results']['summary_fields']['workflow_job_template']['name'])
			wfj_name.append(row['results']['summary_fields']['workflow_job_template']['name'])
			
			print ("Job Created by :")

			try: print (row['results']['summary_fields']['created_by']['username'])
			except: print ("NaN")
			try: j_created_by.append(row['results']['summary_fields']['created_by']['username'])
			except: j_created_by.append("NaN")

			print ("Job Created On :")

			try: print (row['results']['created'])
			except: print ("NaN")
			try: j_created_on.append(row['results']['created'])
			except: j_created_on.append("NaN")

			print ("Job Last Ran on :")

			try: print (row['results']['started'])
			except: print ("NaN")
			try: j_lro.append(row['results']['started'])
			except: j_lro.append("NaN")

			print ("\n")

			print ("*********************************\n")


for file in myFiles:
	print(file)
	if file.startswith("j2report"):
		df = pd.read_json(file)
		print (df)


#Loop to traverse through Json-Inner

		for index, row in df.iterrows():

			print ("Workflow Job ID :") 
 
			try: print (row['results']['id'])
			except: continue
			wf_id.append(row['results']['id'])

			print ("Workflow Name :")

			print (row['results']['name'])
			wf_name.append(row['results']['name'])

			print ("Created by :")

			try: print (row['results']['summary_fields']['created_by']['username'])
			except: print ("NaN")
			try: f_created_by.append(row['results']['summary_fields']['created_by']['username'])
			except: f_created_by.append("NaN")

			print ("Created On :")

			try: print (row['results']['created'])
			except: print ("NaN")
			try: f_created_on.append(row['results']['created'])
			except: f_created_on.append("NaN")

			print ("Last Ran on :")

			try: print (row['results']['last_job_run'])
			except: print ("NaN")
			try: f_lro.append(row['results']['last_job_run'])
			except: f_lro.append("NaN")
			print ("\n")

			print ("*********************************\n")


#Creating DataFrames

df1 = pd.DataFrame({
"Workflow Job ID" : wfj_id
})

df2 = pd.DataFrame({
"Workflow Job Name" : wfj_name
})

df3 = pd.DataFrame({
"Job Created By" : j_created_by
})

df4 = pd.DataFrame({
"Job Created on" : j_created_on
})

df5 = pd.DataFrame({
"Job Last Ran On" : j_lro
})


df6 = pd.DataFrame({
"Workflow Approval ID" : wf_id
})

df7 = pd.DataFrame({
"Workflow Approval Name" : wf_name
})

df8 = pd.DataFrame({
"Approval Created By" : f_created_by
})

df9 = pd.DataFrame({
"Approval Created on" : f_created_on
})

df10 = pd.DataFrame({
"Approval Last Ran On" : f_lro
})

#Concating DataFrames

df = pd.concat([df1, df2, df3, df4, df5], axis=1)
dfb = pd.concat([df6, df7, df8, df9, df10], axis=1)

#Exporting Filename with TimeStamp
filename = 'PRODUCTION_Workflow_Details_'+time+'.xlsx'

#Creating Sheets and Exporting
print("Generating Report...")
df.to_excel(filename, 'Workflow Job Details', index=False)
excel_book = pxl.load_workbook(filename)
with pd.ExcelWriter(filename, engine='openpyxl') as writer:
	writer.book = excel_book
	writer.sheets = {
	worksheet.title: worksheet
	for worksheet in excel_book.worksheets
	}
	dfb.to_excel(writer, 'Workflow Approval Details', index=False)
	writer.save()
