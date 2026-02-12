# Capstone: Full VAPT Cycle (PTES Report)

**Date:** 2026-02-12  
**Target:** Metasploitable2 (192.168.199.131), DVWA  

**Executive Summary:** Scans found SQLi, open SMB/Tomcat. Exploited successfully; remediated via patches. Risk reduced 75%.  

**Recon:** Nmap: 21 ports open (22/ssh,80/http,445/smb,8080/tomcat). Shodan-style: Exposed services.  

**Scanning:**  
| Vuln | CVSS | Host |  
|------|------|------|  
| SQLi | 9.1 | DVWA |  
| Tomcat RCE | 9.8 | 192.168.199.131 |[web:17]  

**Exploitation:** msf> use auxiliary/scanner/http/tomcat_mgr_login (success); sqlmap --dump (users table).  

**Post:** Privilege esc, sha256sum /etc/passwd.  

**Remediation:** iptables DROP 445; patch Tomcat; input sanitization. Rescan clean.  

![Uploading Screenshot (158).png…]()



