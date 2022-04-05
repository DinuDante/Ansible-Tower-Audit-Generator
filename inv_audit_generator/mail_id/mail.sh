count=10000
rm -rf mail.yml
rm -rf /root/inv_audit_generator/mail_id/Release_Automation_check/mail_var.yml
rm -rf /root/inv_audit_generator/mail_id/*.json
for i in $(seq $count); do
	rm -rf /root/inv_audit_generator/mail_id/jreport.json
	curl -k -H "Authorization:  Bearer Wk06jHIbMhOfnfRP53Y63qN4LQvJEx" -H "Content-Type: application/json" -X GET  -d "{}"  https://10.226.73.29/api/v2/users/?page=$i >> /root/inv_audit_generator/mail_id/jreport.json
	if cat /root/inv_audit_generator/mail_id/jreport.json | grep "Invalid page"
	then
		rm -rf /root/inv_audit_generator/mail_id/jreport.json
		break
	else
	        
		cat /root/inv_audit_generator/mail_id/jreport.json >> /root/inv_audit_generator/mail_id/jreport$i.json
         fi
done
python3 /root/inv_audit_generator/mail_id/inv_audit.py
sh var.sh
