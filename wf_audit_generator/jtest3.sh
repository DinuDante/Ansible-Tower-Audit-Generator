count=1000
for i in $(seq $count); do
	rm -rf /root/wf_audit_generator/jreport.json
	curl -k -H "Authorization:  Bearer <Authentication-Token>" -H "Content-Type: application/json" -X GET  -d "{}"  https://<FQDN>/api/v2/job_templates/?page=$i >> /root/wf_audit_generator/jreport.json
	if cat /root/wf_audit_generator/jreport.json | grep "Invalid page"
	then
		rm -rf /root/wf_audit_generator/jreport.json
		break
	else
	        
		cat /root/wf_audit_generator/jreport.json >> /root/wf_audit_generator/j3report$i.json
         fi
done