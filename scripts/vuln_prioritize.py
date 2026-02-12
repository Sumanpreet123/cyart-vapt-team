python
import csv
import sys

# Sample data from Sheets
data = [
    ['001', 'SQL Injection', 9.1, 'Critical', '192.168.1.20'],
    ['002', 'Open Port 445', 6.5, 'Medium', '192.168.1.30']
]

with open('deliverables/prioritized_vulns.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Vuln', 'CVSS', 'Priority', 'Host'])
    sorted_data = sorted(data, key=lambda x: float(x[2]), reverse=True)
    writer.writerows(sorted_data)
print("Prioritized CSV created. High CVSS first!")
Run: pip install pandas if needed; python vuln_prioritize.py.
