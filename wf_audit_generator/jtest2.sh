count=1000
for i in $(seq $count); do
	rm -rf /root/wf_audit_generator/jreport.json
	curl -k -H "Authorization:  Bearer Wk06jHIbMhOfnfRP53Y63qN4LQvJEx" -H "Content-Type: application/json" -X GET  -d "{}"  https://10.226.73.29/api/v2/workflow_job_templates/?page=$i >> /root/wf_audit_generator/jreport.json
	if cat /root/wf_audit_generator/jreport.json | grep "Invalid page"
	then
		rm -rf /root/wf_audit_generator/jreport.json
		break
	else
	        
		cat /root/wf_audit_generator/jreport.json >> /root/wf_audit_generator/j2report$i.json
         fi
done

