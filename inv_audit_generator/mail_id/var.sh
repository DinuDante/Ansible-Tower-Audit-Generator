awk '{printf "    - "; print}' mail.yml >> /root/inv_audit_generator/mail_id/Release_Automation_check/mail_var.yml
sed -i '1i ---' /root/inv_audit_generator/mail_id/Release_Automation_check/mail_var.yml
sed -i '2i - mail_address:' /root/inv_audit_generator/mail_id/Release_Automation_check/mail_var.yml
cd /root/inv_audit_generator/mail_id/Release_Automation_check/
git add .
git commit -m "mail ids"
git push 
