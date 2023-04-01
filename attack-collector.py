import sys
import os
import re
import csv
import requests
import json
from datetime import datetime

with open(sys.argv[1], 'r', encoding='latin-1') as file:
	csv_writer = csv.writer(sys.stdout, delimiter=',')
	for line in file:
		match_init = re.search(r'(\d{2}\/\d{2} \d{2}:\d{2}:\d{2} UTC) \[metadata\] (\d+\.\d+\.\d+\.\d+) <- (\d+\.\d+\.\d+\.\d+); computer: ([\w-]+); user: ([\w\s*]+); process: ([\w\.]+); pid: (\d+); os: (\w+); version: (\d+\.\d+); build: (\d+); beacon arch: (\w+) \((\w+)\)', line.strip())
		if match_init:
			time = match_init.group(1)
			external_ip = match_init.group(2)
			internal_ip = match_init.group(3)
			computer_name = match_init.group(4)
			username = match_init.group(5)
			date_obj = datetime.strptime(time + ' 2023', '%m/%d %H:%M:%S %Z %Y')
			time_str = date_obj.strftime('%H:%M:%S')
			date_str = date_obj.strftime('%d/%m/%Y')
			#url = f'https://api.iplocation.net/?cmd=ip-country&ip={external_ip}'
			#response = requests.get(url)
			#data = json.loads(response.text)
			#country = data['country_name']
			csv_writer.writerow([date_str, time_str, username, external_ip, internal_ip, computer_name])

		match_movement = re.match(r'^(\d{2}/\d{2} \d{2}:\d{2}:\d{2} UTC) \*\*\* initial beacon from (\w+) *@(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) \((.+)\)$', line.strip())
		if match_movement:
			time = match_movement.group(1)
			username = match_movement.group(2)
			internal_ip = match_movement.group(3)
			computer_name = match_movement.group(4)
			date_obj = datetime.strptime(time + ' 2023', '%m/%d %H:%M:%S %Z %Y')
			time_str = date_obj.strftime('%H:%M:%S')
			date_str = date_obj.strftime('%d/%m/%Y')
			csv_writer.writerow([date_str, time_str, username, '', internal_ip, computer_name])
