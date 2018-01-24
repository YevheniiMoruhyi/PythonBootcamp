#!/usr/bin/env python
import re
mode_pattern = re.compile('^(access|trunk)$')
interface_pattern = re.compile('^((([Ff]ast|[Gg]igabit)?[Ee]thernet)|([Ff]a?|[Gg]a?|[Ee]))(\d{1,3}\/\d{1,3}(\/\d{1,3})?)$')
vlan_pattern = re.compile('^(409[0-4]|40[0-8]\d|[123]\d\d\d|[1-9]\d\d|[1-9]\d|[1-9])$')
allow_vl_pattern = re.compile('^((409[0-4]|40[0-8]\d|[123]\d\d\d|[1-9]\d\d|[1-9]\d|[1-9])\,)+(409[0-4]|40[0-8]\d|[123]\d\d\d|[1-9]\d\d|[1-9]\d|[1-9])$')

access_template = ['switchport mode access',

'switchport access vlan {}',

'switchport nonegotiate',

'spanning-tree portfast',

'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',

'switchport mode trunk',

'switchport trunk allowed vlan {}']

mode = raw_input('Enter interface mode(access/trunk):')
while mode_pattern.search(mode)==None:
	print('Invalid mode\n')
	mode = raw_input('Enter interface mode(access/trunk):')

interface = raw_input('Enter interface type and number:')
while interface_pattern.search(interface)==None:
	print('Invalid interface type and number\n')
	interface = raw_input('Enter interface type and number:')

if mode == 'access':
	vlan = raw_input('Enter VLAN number:')
	while vlan_pattern.search(vlan)==None:
		print('VLAN number is invalid\n')
		vlan = raw_input('Enter VLAN number:')
	print('Switch_1#sh run | in {}'.format(interface))
	print('Interface ' + interface)
	print(access_template[0])
	print(access_template[1].format(vlan))
	print(access_template[2])
	print(access_template[3])
	print(access_template[4])
else:
	allow_vl = raw_input('Enter allowed VLANs:')
	while allow_vl_pattern.search(allow_vl)==None:
		print('VLANs are invalid\n')
		allow_vl = raw_input('Enter allowed VLANs:')
	print('Switch_1#sh run | in {}'.format(interface))
	print('Interface ' + interface)
	print(trunk_template[0])
	print(trunk_template[1])
	print(trunk_template[2].format(allow_vl))

