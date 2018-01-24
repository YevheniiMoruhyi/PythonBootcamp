#!/usr/bin/env python
import re
ip_address_pattern = re.compile('^((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$')
sub_mask_pattern = re.compile('^(3[0-2]|[1-2]\d|\d)$')

ip_address = raw_input('Enter Ip address:')
while ip_address_pattern.search(ip_address)==None:
	print('Invalid IP address format')
	ip_address = raw_input('Enter Ip address:')

sub_mask = raw_input('Enter subnet mask in decimal format:')
while sub_mask_pattern.search(sub_mask)==None:
	print('Subnet mask is invalid')
	sub_mask = raw_input('Enter subnet mask in decimal format:')

ip_octet_list = []
for obj in ip_address.split('.'):
	ip_octet_list.append(int(obj))
print('{:>8} {:>8} {:>8} {:>8}'.format(ip_octet_list[0],ip_octet_list[1],ip_octet_list[2],ip_octet_list[3]))
print('{:>08b} {:>08b} {:>08b} {:>08b}'.format(ip_octet_list[0],ip_octet_list[1],ip_octet_list[2],ip_octet_list[3]))

f = lambda x: str(1) if (x<int(sub_mask)) else str(0)
mask_digits_list = [f(obj) for obj in range(32)]
mask_digits_str = ''.join(mask_digits_list)
mask_octet_list = [int(mask_digits_str[:8],2),int(mask_digits_str[8:16],2),int(mask_digits_str[16:24],2),int(mask_digits_str[24:32],2)]
netaddr_octet_list = [str(ip_octet_list[i]&mask_octet_list[i]) for i in range(4)]
print('Network address is:{}.{}.{}.{}/{}'.format(netaddr_octet_list[0],netaddr_octet_list[1],netaddr_octet_list[2],netaddr_octet_list[3],sub_mask))


ip_bin_list = [x for x in '{:>08b}{:>08b}{:>08b}{:>08b}'.format(ip_octet_list[0],ip_octet_list[1],ip_octet_list[2],ip_octet_list[3])]
for i in range(int(sub_mask),32):
	ip_bin_list[i] = str(1)

br_addr_bin = ''.join(ip_bin_list)
br_addr_list = [int(br_addr_bin[:8],2),int(br_addr_bin[8:16],2),int(br_addr_bin[16:24],2),int(br_addr_bin[24:32],2)]
print('Broadcast address is:{}.{}.{}.{}/{}'.format(br_addr_list[0],br_addr_list[1],br_addr_list[2],br_addr_list[3],sub_mask))