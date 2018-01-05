import re
pattern = re.compile('^switchport trunk allowed vlan\s(\d.*)')

with open('./text/commands.txt') as myfile:
	read_data = []
	for line in myfile:
		if pattern.search(line)!=None:
			read_data.append(pattern.search(line).group(1))

l = [obg.split(',') for obg in read_data]
for obj in l:
	for i in range(len(obj)):
		obj[i] = obj[i].strip()

set_list = [set(obj) for obj in l]

res1_set = set_list[0]
res2_set = set_list[0]
all_elems = set()
for i in set_list:
	res1_set = res1_set & i                    #intersection

for i in set_list:
	all_elems = all_elems | i                  #union

for i in range(len(set_list)):                 #find unique elements
	for j in set_list:
		if set_list[i] == j:
			continue                                    
		for obj in set_list[i]:
			if (obj in j) and (obj in all_elems):
				all_elems.remove(obj)

res1_list = list(res1_set)
res1_list = [int(i) for i in res1_list]
res1_list.sort()
res1_list = [str(i) for i in res1_list]
print('List_1={}'.format(res1_list))

all_elems = list(all_elems)
all_elems = [int(i) for i in all_elems]
all_elems.sort()
all_elems = [str(i) for i in all_elems]
print('List_2={}'.format(all_elems))






