import sys
import os
import re
import csv
from datetime import datetime

with open(sys.argv[1], 'r', encoding='latin-1') as file:
	csv_writer = csv.writer(sys.stdout, delimiter=',')
	for line in file:
	
		match_joined = re.match(r'^(\d{2}/\d{2} \d{2}:\d{2}:\d{2} UTC) \*\*\* (\w+) \((\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\) joined$', line.strip())
		if match_joined:
			time = match_joined.group(1)
			username = match_joined.group(2)
			ip_address = match_joined.group(3)
			date_obj = datetime.strptime(time + ' 2023', '%m/%d %H:%M:%S %Z %Y')
			time_str = date_obj.strftime('%H:%M:%S')
			date_str = date_obj.strftime('%d/%m/%Y')
			csv_writer.writerow([date_str, time_str, username, ip_address, 'joined'])
			
		match_quit = re.match(r'^(\d{2}/\d{2} \d{2}:\d{2}:\d{2} UTC) \*\*\* (\w+) quit$', line.strip())
		if match_quit:
			time = match_quit.group(1)
			username = match_quit.group(2)
			date_obj = datetime.strptime(time + ' 2023', '%m/%d %H:%M:%S %Z %Y')
			time_str = date_obj.strftime('%H:%M:%S')
			date_str = date_obj.strftime('%d/%m/%Y')
			csv_writer.writerow([date_str, time_str, username, '', 'quit'])
			
		match_command = re.match(r'^(\d{2}/\d{2} \d{2}:\d{2}:\d{2} UTC) \[input\] \<(\w+)\> (.+)', line.strip())
		if match_command:
			time = match_command.group(1)
			username = match_command.group(2)
			date_obj = datetime.strptime(time + ' 2023', '%m/%d %H:%M:%S %Z %Y')
			time_str = date_obj.strftime('%H:%M:%S')
			date_str = date_obj.strftime('%d/%m/%Y')
			csv_writer.writerow([date_str, time_str, username, '', 'command'])
