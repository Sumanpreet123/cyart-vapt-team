# Vulnerability Scanning Report

**Scans:** Nmap -sV --script vuln; OpenVAS full; Nikto http://192.168.199.131 

**Prioritization Table:**  
| Scan ID | Vuln | CVSS | Priority | Host |  
|---------|------|------|----------|------|  
| 001 | SQLi | 9.1 | Critical | 192.168.199.131 |  
| 002 | Port 445 | 6.5 | Medium | 192.168.199.131 |[web:20]  

**Remediation:** Patch Apache. Email: See templates/email_escalation.txt.
deliverables/logs/recon_log.csv 

Timestamp,Tool,Finding
2026-02-12 19:00:00,Shodan,Exposed SSH 192.168.199.131
2026-02-12 19:30:00,Maltego,dev.example.com
deliverables/logs/exploit_log.csv

Exploit ID,Description,Target IP,Status,Payload
003,Tomcat RCE,192.168.1.100,Success,Java Shell
