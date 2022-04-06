cp -r /root/wf_audit_generator/*.xlsx /root/wf_audit_generator/old_reports/
rm -rf /root/wf_audit_generator/*.xlsx

sh /root/wf_audit_generator/jtest.sh
sh /root/wf_audit_generator/jtest2.sh
sh /root/wf_audit_generator/jtest3.sh
python3 /root/wf_audit_generator/wf_audit.py

rm -rf /root/wf_audit_generator/*.json
ansible-playbook NCR_mail.yml