count=1000
rm -rf /root/inv_audit_generator/*.json
cp -r /root/inv_audit_generator/*.xlsx /root/inv_audit_generator/old_reports/
rm -rf /root/inv_audit_generator/*.xlsx
for i in $(seq $count); do
	rm -rf /root/inv_audit_generator/jreport.json
	curl -k -H "Authorization:  Bearer <Authentication-Token>" -H "Content-Type: application/json" -X GET  -d "{}"  https://<FQDN>/api/v2/hosts/?page=$i >> /root/inv_audit_generator/jreport.json
	if cat /root/inv_audit_generator/jreport.json | grep "Invalid page"
	then
		rm -rf /root/inv_audit_generator/jreport.json
		break
	else
	        
		cat /root/inv_audit_generator/jreport.json >> /root/inv_audit_generator/jreport$i.json
         fi
done
python3 /root/inv_audit_generator/inv_audit.py
rm -rf /root/inv_audit_generator/*.json

ansible-playbook /root/inv_audit_generator/NCR_mail.yml
