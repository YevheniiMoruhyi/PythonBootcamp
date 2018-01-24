#!/usr/bin/env python
import re
ospf_pattern = re.compile('^(O)\s(E1|E2|IA)\s(((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d))\s(\[.*\])\svia\s(((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d))\,\s(\d:\d{2}:\d{2})\,\s(.*)$')
eigrp_pattern = re.compile('^(D|E|R)\s(((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d))\s(\[.*\])\svia\s(((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d))\,\s(\d:\d{2}:\d{2})\,\s(.*)$')
dir_conn_pattern = re.compile('^(C)\s(((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d))\s(((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d))\s(is directly connected)\,\s(.*)$')
isis_pattern = re.compile('^(i)\s(L2|L1)\s(((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d))\s(\[.*\])\svia\s(((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d))\,\s(\d:\d{2}:\d{2})\,\s(.*)$')
nhrp_pattern = re.compile('^(H)\s(((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d))\s(\[.*\])\svia\s(((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d))\,\s(\d{1,2}:\d{2}:\d{2})\,\s(.*)$')

pattern_list = [ospf_pattern,eigrp_pattern,dir_conn_pattern,isis_pattern,nhrp_pattern]

base = {'O':'OSPF', 
		'E1':'external type 1', 
		'E2':'external type 2',
		'IA':'OSPF inter area',
		'D':'EIGRP',
		'EX':'EIGRP external',
		'E':'EGP',
		'C':'Directly connected',
		'S':'Static',
		'R':'RIP',
		'ia':'IS-IS inter area',
		'i':'IS-IS',
		'L1':'level 1',
		'L2':'level 2',
		'H':'NHRP'}

with open('./text/ShowIpRoute.txt') as myfile:
	read_data = myfile.readlines()


for line in read_data:
	for pattern in pattern_list:
		match = pattern.search(line)
		if match:
			if match.group(1)=='O' or match.group(1)=='i':
				print('Protocol:           {} {}'.format(base[match.group(1)],base[match.group(2)]))
				print('Prefix:             {}'.format(match.group(3)))
				print('AD/Metric:          {}'.format(match.group(7)))
				print('Next-Hop:           {}'.format(match.group(8)))
				print('Last update:        {}'.format(match.group(12)))
				print('Outbound interface: {}\n'.format(match.group(13)))
			elif match.group(1)=='D'or match.group(1)=='E' or match.group(1)=='R' or match.group(1)=='H' or match.group(1)=='EX':
				print('Protocol:           {}'.format(base[match.group(1)]))
				print('Prefix:             {}'.format(match.group(2)))
				print('AD/Metric:          {}'.format(match.group(6)))
				print('Next-Hop:           {}'.format(match.group(7)))
				print('Last update:        {}'.format(match.group(11)))
				print('Outbound interface: {}\n'.format(match.group(12)))
			elif match.group(1)=='C':
				print('Protocol:           {}'.format(base[match.group(1)]))
				print('Prefix:             {}'.format(match.group(2)))
				print('AD:                 {}'.format('0'))
				print('Next-Hop:           {}'.format('directly connected'))
				print('Last update:        {}'.format('----'))
				print('Outbound interface: {}\n'.format(match.group(11)))
