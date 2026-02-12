## Quick Run
1. Boot Metasploitable2 (192.168.1.100).
2. `./scripts/vuln_scan.sh` → Check `deliverables/scan_results/`.
3. Reports in `/reports/` → Convert to PDF: pandoc *.md -o report.pdf.

## Findings Summary
- Critical: SQLi (9.1), Tomcat RCE (9.8).
- Exploits: Metasploit tomcat_mgr_login, sqlmap DVWA.

Screenshots/logs included. Ethical VM-only.[cite:1][web:47]
reports/capstone_ptes_report.md 


