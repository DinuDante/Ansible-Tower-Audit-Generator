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

jt_id = []
jt_name = []
jt_approved_by = []
jt_created_by = []
jt_created_on = []
jt_lro = []

workflow_job_frequency = []

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
			
			print ("Job Executed by :")

			try: print (row['results']['summary_fields']['created_by']['username'])
			except: print ("NaN")
			try: j_created_by.append(row['results']['summary_fields']['created_by']['username'])
			except: j_created_by.append("NaN")

			print ("Job Executed On :")

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

for file in myFiles:
	print(file)
	if file.startswith("j3report"):
		df = pd.read_json(file)
		print (df)

		for index, row in df.iterrows():
    
			print ("Job Template ID :") 
 
			try: print (row['results']['id'])
			except: continue
			jt_id.append(row['results']['id'])

			print ("Job Template Name :")

			print (row['results']['name'])
			jt_name.append(row['results']['name'])

			print ("Created by :")

			try: print (row['results']['summary_fields']['created_by']['username'])
			except: print ("NaN")
			try: jt_created_by.append(row['results']['summary_fields']['created_by']['username'])
			except: jt_created_by.append("NaN")

			print ("Created On :")

			try: print (row['results']['created'])
			except: print ("NaN")
			try: jt_created_on.append(row['results']['created'])
			except: jt_created_on.append("NaN")

			print ("Last Ran on :")

			try: print (row['results']['last_job_run'])
			except: print ("NaN")
			try: jt_lro.append(row['results']['last_job_run'])
			except: jt_lro.append("NaN")
			print ("\n")

#Calculating the Frequency of Workflow Job
print("Creating dfs...")
tjc = str(len(wf_id))
ujc = str(len(jt_id))


for i in jt_id:
  st=0
  for j in range(len(wf_id)):
    if i == wf_id[j]:
      st = st + 1
workflow_job_frequency.append(st)

#Calculating the Frequency of Job Templates



#Creating DataFrames

df1 = pd.DataFrame({"Workflow Job ID" + str(len(wf_id)) : wfj_id})

df2 = pd.DataFrame({"Workflow Job Name" : wfj_name})

df3 = pd.DataFrame({"Workflow Job Executed By" : j_created_by})

df4 = pd.DataFrame({"Workflow Job Executed On" : j_created_on})

df5 = pd.DataFrame({"Workflow Job Ran On" : j_lro})

df6 = pd.DataFrame({"Workflow Approval ID" : wf_id})

df7 = pd.DataFrame({"Workflow Approval Name" : wf_name})

df8 = pd.DataFrame({"Workflow Approval Created By" : f_created_by})

df9 = pd.DataFrame({"Workflow Approval Created On" : f_created_on})

df10 = pd.DataFrame({"Workflow Approval Last Ran On" : f_lro})

df11 = pd.DataFrame({"Workflow Job ID" + str(len(jt_id)) : jt_id})

df12 = pd.DataFrame({"Workflow Job Name" : jt_name})

df13 = pd.DataFrame({"Workflow Job Created By" : jt_created_by})

df14 = pd.DataFrame({"Workflow Job Created On" : jt_created_on})

df15 = pd.DataFrame({"Workflow Job Last Ran On" : jt_lro})

df16 = pd.DataFrame({"Frequency" : workflow_job_frequency})

#Concating DataFrames

dfa = pd.concat([df1, df2, df3, df4, df5], axis=1)
dfb = pd.concat([df6, df7, df8, df9, df10], axis=1)
dfc = pd.concat([df11, df12, df13, df14, df15, df16], axis=1)

#Exporting Filename with TimeStamp
filename = 'PRODUCTION_Workflow_and_Job_Details_'+time+'.xlsx'

#Creating Sheets and Exporting
print("Generating Report...")
dfa.to_excel(filename, 'Workflow Job Details', index=False)
excel_book = pxl.load_workbook(filename)
with pd.ExcelWriter(filename, engine='openpyxl') as writer:
	writer.book = excel_book
	writer.sheets = {
	worksheet.title: worksheet
	for worksheet in excel_book.worksheets
	}
	dfb.to_excel(writer, 'Workflow Approval Details', index=False)
	dfc.to_excel(writer, 'Job Template Details', index=False)
	writer.save()