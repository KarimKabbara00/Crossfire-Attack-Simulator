import math

with open(r"/Users/username/Desktop/out.tr") as f:
	lines = f.readlines()

trace_line = {}
count = 0
#  total pid
for line in lines:
	extracted = line.split()
	stime=extracted[1]
	sip = extracted[2]
	pid = extracted[11]
	act = extracted[0]
	if pid not in list(trace_line.keys()):
		stime=int(math.ceil(float(stime)))
		trace_line[pid] = {'source_ip':sip, 'start_time':stime,'action':act}
		count += 1
		#print("new pid: {}".format(pid))
	elif pid in  list(trace_line.keys()):
		#print("pid exists so update")
		#trace_line[pid]['source_ip'] = sip
		#trace_line[pid]['start_time']=stime
		if act == 'd':
			#print("dropped packet")
			trace_line[pid]['action']=act
print("Total Packets: {}".format(count))

packets_node1_t1 = 0
packets_node1_t2 = 0
packets_node1_t3 = 0
packets_node1_t4 = 0
packets_node1_t5 = 0
packets_node1_t6 = 0
packets_node1_t7 = 0
packets_node1_t8 = 0
packets_node1_t9 = 0
packets_node1_t10 = 0

sent_packets_node1_t1 = 0
sent_packets_node1_t2 = 0
sent_packets_node1_t3 = 0
sent_packets_node1_t4 = 0
sent_packets_node1_t5 = 0
sent_packets_node1_t6 = 0
sent_packets_node1_t7 = 0
sent_packets_node1_t8 = 0
sent_packets_node1_t9 = 0
sent_packets_node1_t10 = 0

packets_node2_t1 = 0
packets_node2_t2 = 0
packets_node2_t3 = 0
packets_node2_t4 = 0
packets_node2_t5 = 0
packets_node2_t6 = 0
packets_node2_t7 = 0
packets_node2_t8 = 0
packets_node2_t9 = 0
packets_node2_t10 = 0

sent_packets_node2_t1 = 0
sent_packets_node2_t2 = 0
sent_packets_node2_t3 = 0
sent_packets_node2_t4 = 0
sent_packets_node2_t5 = 0
sent_packets_node2_t6 = 0
sent_packets_node2_t7 = 0
sent_packets_node2_t8 = 0
sent_packets_node2_t9 = 0
sent_packets_node2_t10 = 0

packets_node3_t1 = 0
packets_node3_t2 = 0
packets_node3_t3 = 0
packets_node3_t4 = 0
packets_node3_t5 = 0
packets_node3_t6 = 0
packets_node3_t7 = 0
packets_node3_t8 = 0
packets_node3_t9 = 0
packets_node3_t10 = 0

sent_packets_node3_t1 = 0
sent_packets_node3_t2 = 0
sent_packets_node3_t3 = 0
sent_packets_node3_t4 = 0
sent_packets_node3_t5 = 0
sent_packets_node3_t6 = 0
sent_packets_node3_t7 = 0
sent_packets_node3_t8 = 0
sent_packets_node3_t9 = 0
sent_packets_node3_t10 = 0

packets_node4_t1 = 0
packets_node4_t2 = 0
packets_node4_t3 = 0
packets_node4_t4 = 0
packets_node4_t5 = 0
packets_node4_t6 = 0
packets_node4_t7 = 0
packets_node4_t8 = 0
packets_node4_t9 = 0
packets_node4_t10 = 0

sent_packets_node4_t1 = 0
sent_packets_node4_t2 = 0
sent_packets_node4_t3 = 0
sent_packets_node4_t4 = 0
sent_packets_node4_t5 = 0
sent_packets_node4_t6 = 0
sent_packets_node4_t7 = 0
sent_packets_node4_t8 = 0
sent_packets_node4_t9 = 0
sent_packets_node4_t10 = 0

total_packets_node1 = 0
total_packets_node2 = 0
total_packets_node3 = 0
total_packets_node4 = 0


time = ''
dropped = False

for x, y in trace_line.items():
	#print("Packet ID: {}".format(x))
	for val in y:
		#print(val + ':', y[val])
		if(str(val) == 'action' and str(y[val]) == 'd'):
			dropped = True
			continue
		if(str(val) == 'start_time' and str(y[val]) == '1' ):
			time = 't1'
			continue
		elif(str(val) == 'start_time' and str(y[val]) == '2'):
			time = 't2'
			continue
		elif(str(val) == 'start_time' and str(y[val]) == '3'):
			time = 't3'
			continue
		elif(str(val) == 'start_time' and str(y[val]) == '4'):
			time = 't4'
			continue
		elif(str(val) == 'start_time' and str(y[val]) == '5'):
			time = 't5'
			continue
		elif(str(val) == 'start_time' and str(y[val]) == '6' ):
			time = 't6'
			continue
		elif(str(val) == 'start_time' and str(y[val]) == '7'):
			time = 't7'
			continue
		elif(str(val) == 'start_time' and str(y[val]) == '8'):
			time = 't8'
			continue
		elif(str(val) == 'start_time' and str(y[val]) == '9'):
			time = 't9'
			continue
		elif(str(val) == 'start_time' and str(y[val]) == '10'):
			time = 't10'
			continue
		if(str(val) == 'source_ip' and str(y[val]) == '25' and dropped == True):
			#print("Packet ID: {}".format(x))
			#print(val + ':', y[val])
			if(time == 't1'):
				packets_node1_t1 += 1
			if(time == 't2'):
				packets_node1_t2 += 1
			if(time == 't3'):
				packets_node1_t3 += 1
			if(time == 't4'):
				packets_node1_t4 += 1
			if(time == 't5'):
				packets_node1_t5 += 1
			if(time == 't6'):
				packets_node1_t6 += 1
			if(time == 't7'):
				packets_node1_t7 += 1
			if(time == 't8'):
				packets_node1_t8 += 1
			if(time == 't9'):
				packets_node1_t9 += 1	
			if(time == 't10'):
				packets_node1_t10 += 1	
			dropped = False
			continue

		if(str(val) == 'source_ip' and str(y[val]) == '25' and dropped == False):
			#print("Packet ID: {}".format(x))
			#print(val + ':', y[val])
			if(time == 't1'):
				sent_packets_node1_t1 += 1
			if(time == 't2'):
				sent_packets_node1_t2 += 1
			if(time == 't3'):
				sent_packets_node1_t3 += 1
			if(time == 't4'):
				sent_packets_node1_t4 += 1
			if(time == 't5'):
				sent_packets_node1_t5 += 1
			if(time == 't6'):
				sent_packets_node1_t6 += 1
			if(time == 't7'):
				sent_packets_node1_t7 += 1
			if(time == 't8'):
				sent_packets_node1_t8 += 1
			if(time == 't9'):
				sent_packets_node1_t9 += 1	
			if(time == 't10'):
				sent_packets_node1_t10 += 1	
			dropped = False
			continue

		elif(str(val) == 'source_ip' and str(y[val]) == '26' and dropped == True):
			#print("Packet ID: {}".format(x))
			#print(val + ':', y[val])
			if(time == 't1'):
				packets_node2_t1 += 1
			if(time == 't2'):
				packets_node2_t2 += 1
			if(time == 't3'):
				packets_node2_t3 += 1
			if(time == 't4'):
				packets_node2_t4 += 1
			if(time == 't5'):
				packets_node2_t5 += 1
			if(time == 't6'):
				packets_node2_t6 += 1
			if(time == 't7'):
				packets_node2_t7 += 1
			if(time == 't8'):
				packets_node2_t8 += 1
			if(time == 't9'):
				packets_node2_t9 += 1	
			if(time == 't10'):
				packets_node2_t10 += 1	
			dropped = False
			continue

		elif(str(val) == 'source_ip' and str(y[val]) == '26' and dropped == False):
			#print("Packet ID: {}".format(x))
			#print(val + ':', y[val])
			if(time == 't1'):
				sent_packets_node2_t1 += 1
			if(time == 't2'):
				sent_packets_node2_t2 += 1
			if(time == 't3'):
				sent_packets_node2_t3 += 1
			if(time == 't4'):
				sent_packets_node2_t4 += 1
			if(time == 't5'):
				sent_packets_node2_t5 += 1
			if(time == 't6'):
				sent_packets_node2_t6 += 1
			if(time == 't7'):
				sent_packets_node2_t7 += 1
			if(time == 't8'):
				sent_packets_node2_t8 += 1
			if(time == 't9'):
				sent_packets_node2_t9 += 1	
			if(time == 't10'):
				sent_packets_node2_t10 += 1	
			dropped = False
			continue

		elif(str(val) == 'source_ip' and str(y[val]) == '27' and dropped == True):
			#print("Packet ID: {}".format(x))
			#print(val + ':', y[val])
			if(time == 't1'):
				packets_node3_t1 += 1
			if(time == 't2'):
				packets_node3_t2 += 1
			if(time == 't3'):
				packets_node3_t3 += 1
			if(time == 't4'):
				packets_node3_t4 += 1
			if(time == 't5'):
				packets_node3_t5 += 1
			if(time == 't6'):
				packets_node3_t6 += 1
			if(time == 't7'):
				packets_node3_t7 += 1
			if(time == 't8'):
				packets_node3_t8 += 1
			if(time == 't9'):
				packets_node3_t9 += 1	
			if(time == 't10'):
				packets_node3_t10 += 1	
			dropped = False
			continue

		elif(str(val) == 'source_ip' and str(y[val]) == '27' and dropped == False):
			#print("Packet ID: {}".format(x))
			#print(val + ':', y[val])
			if(time == 't1'):
				sent_packets_node3_t1 += 1
			if(time == 't2'):
				sent_packets_node3_t2 += 1
			if(time == 't3'):
				sent_packets_node3_t3 += 1
			if(time == 't4'):
				sent_packets_node3_t4 += 1
			if(time == 't5'):
				sent_packets_node3_t5 += 1
			if(time == 't6'):
				sent_packets_node3_t6 += 1
			if(time == 't7'):
				sent_packets_node3_t7 += 1
			if(time == 't8'):
				sent_packets_node3_t8 += 1
			if(time == 't9'):
				sent_packets_node3_t9 += 1	
			if(time == 't10'):
				sent_packets_node3_t10 += 1	
			dropped = False
			continue
			
		elif(str(val) == 'source_ip' and str(y[val]) == '28' and dropped == True):
			#print("Packet ID: {}".format(x))
			#print(val + ':', y[val])
			if(time == 't1'):
				packets_node4_t1 += 1
			if(time == 't2'):
				packets_node4_t2 += 1
			if(time == 't3'):
				packets_node4_t3 += 1
			if(time == 't4'):
				packets_node4_t4 += 1
			if(time == 't5'):
				packets_node4_t5 += 1
			if(time == 't6'):
				packets_node4_t6 += 1
			if(time == 't7'):
				packets_node4_t7 += 1
			if(time == 't8'):
				packets_node4_t8 += 1
			if(time == 't9'):
				packets_node4_t9 += 1	
			if(time == 't10'):
				packets_node4_t10 += 1	
			dropped = False
			continue

		elif(str(val) == 'source_ip' and str(y[val]) == '28' and dropped == False):
			#print("Packet ID: {}".format(x))
			#print(val + ':', y[val])
			if(time == 't1'):
				sent_packets_node4_t1 += 1
			if(time == 't2'):
				sent_packets_node4_t2 += 1
			if(time == 't3'):
				sent_packets_node4_t3 += 1
			if(time == 't4'):
				sent_packets_node4_t4 += 1
			if(time == 't5'):
				sent_packets_node4_t5 += 1
			if(time == 't6'):
				sent_packets_node4_t6 += 1
			if(time == 't7'):
				sent_packets_node4_t7 += 1
			if(time == 't8'):
				sent_packets_node4_t8 += 1
			if(time == 't9'):
				sent_packets_node4_t9 += 1	
			if(time == 't10'):
				sent_packets_node4_t10 += 1	
			dropped = False
			continue


total_packets_node1=packets_node1_t1+packets_node1_t2+packets_node1_t3+packets_node1_t4+packets_node1_t5+packets_node1_t6+packets_node1_t7+packets_node1_t8+packets_node1_t9+packets_node1_t10
print("User 1 Dropped Packets at sec 1: {}".format(packets_node1_t1))
print("User 1 Dropped Packets at sec 2 #: {}".format(packets_node1_t2))
print("User 1 Dropped Packets at sec 3 #: {}".format(packets_node1_t3))
print("User 1 Dropped Packets at sec 4 #: {}".format(packets_node1_t4))
print("User 1 Dropped Packets at sec 5 #: {}".format(packets_node1_t5))
print("User 1 Dropped Packets at sec 6 #: {}".format(packets_node1_t6))
print("User 1 Dropped Packets at sec 7 #: {}".format(packets_node1_t7))
print("User 1 Dropped Packets at sec 8 #: {}".format(packets_node1_t8))
print("User 1 Dropped Packets at sec 9 #: {}".format(packets_node1_t9))
print("User 1 Dropped Packets at sec 10 #: {}".format(packets_node1_t10))
print("Total User 1 Dropped Packets #: {}".format(total_packets_node1))

sent_total_packets_node1=sent_packets_node1_t1+sent_packets_node1_t2+sent_packets_node1_t3+sent_packets_node1_t4+sent_packets_node1_t5+sent_packets_node1_t6+sent_packets_node1_t7+sent_packets_node1_t8+sent_packets_node1_t9+sent_packets_node1_t10
print("User 1 sent Packets at sec 1: {}".format(sent_packets_node1_t1+packets_node1_t1))
print("User 1 sent Packets at sec 2 #: {}".format(sent_packets_node1_t2+packets_node1_t2))
print("User 1 sent Packets at sec 3 #: {}".format(sent_packets_node1_t3+packets_node1_t3))
print("User 1 sent Packets at sec 4 #: {}".format(sent_packets_node1_t4+packets_node1_t4))
print("User 1 sent Packets at sec 5 #: {}".format(sent_packets_node1_t5+packets_node1_t5))
print("User 1 sent Packets at sec 6 #: {}".format(sent_packets_node1_t6+packets_node1_t6))
print("User 1 sent Packets at sec 7 #: {}".format(sent_packets_node1_t7+packets_node1_t7))
print("User 1 sent Packets at sec 8 #: {}".format(sent_packets_node1_t8+packets_node1_t8))
print("User 1 sent Packets at sec 9 #: {}".format(sent_packets_node1_t9+packets_node1_t9))
print("User 1 sent Packets at sec 10 #: {}".format(sent_packets_node1_t10+packets_node1_t10))
#print("Total User 1 Sent Packets #: {}".format(sent_total_packets_node1))

total_packets_node2=packets_node2_t1+packets_node2_t2+packets_node2_t3+packets_node2_t4+packets_node2_t5+packets_node2_t6+packets_node2_t7+packets_node2_t8+packets_node2_t9+packets_node2_t10
print("User 2 Dropped Packets at sec 1: {}".format(packets_node2_t1))
print("User 2 Dropped Packets at sec 2 #: {}".format(packets_node2_t2))
print("User 2 Dropped Packets at sec 3 #: {}".format(packets_node2_t3))
print("User 2 Dropped Packets at sec 4 #: {}".format(packets_node2_t4))
print("User 2 Dropped Packets at sec 5 #: {}".format(packets_node2_t5))
print("User 2 Dropped Packets at sec 6 #: {}".format(packets_node2_t6))
print("User 2 Dropped Packets at sec 7 #: {}".format(packets_node2_t7))
print("User 2 Dropped Packets at sec 8 #: {}".format(packets_node2_t8))
print("User 2 Dropped Packets at sec 9 #: {}".format(packets_node2_t9))
print("User 2 Dropped Packets at sec 10 #: {}".format(packets_node2_t10))
print("Total User 2 Dropped Packets #: {}".format(total_packets_node2))

sent_total_packets_node2=sent_packets_node2_t1+sent_packets_node2_t2+sent_packets_node2_t3+sent_packets_node2_t4+sent_packets_node2_t5+sent_packets_node2_t6+sent_packets_node2_t7+sent_packets_node2_t8+sent_packets_node2_t9+sent_packets_node2_t10
print("User 2 sent Packets at sec 1: {}".format(sent_packets_node2_t1+packets_node2_t1))
print("User 2 sent Packets at sec 2 #: {}".format(sent_packets_node2_t2+packets_node2_t2))
print("User 2 sent Packets at sec 3 #: {}".format(sent_packets_node2_t3+packets_node2_t3))
print("User 2 sent Packets at sec 4 #: {}".format(sent_packets_node2_t4+packets_node2_t4))
print("User 2 sent Packets at sec 5 #: {}".format(sent_packets_node2_t5+packets_node2_t5))
print("User 2 sent Packets at sec 6 #: {}".format(sent_packets_node2_t6+packets_node2_t6))
print("User 2 sent Packets at sec 7 #: {}".format(sent_packets_node2_t7+packets_node2_t7))
print("User 2 sent Packets at sec 8 #: {}".format(sent_packets_node2_t8+packets_node2_t8))
print("User 2 sent Packets at sec 9 #: {}".format(sent_packets_node2_t9+packets_node2_t9))
print("User 2 sent Packets at sec 10 #: {}".format(sent_packets_node2_t10+packets_node2_t10))
#print("Total User 2 Sent Packets #: {}".format(sent_total_packets_node2))

total_packets_node3=packets_node3_t1+packets_node3_t2+packets_node3_t3+packets_node3_t4+packets_node3_t5+packets_node3_t6+packets_node3_t7+packets_node3_t8+packets_node3_t9+packets_node3_t10
print("User 3 Dropped Packets at sec 1: {}".format(packets_node3_t1))
print("User 3 Dropped Packets at sec 2 #: {}".format(packets_node3_t2))
print("User 3 Dropped Packets at sec 3 #: {}".format(packets_node3_t3))
print("User 3 Dropped Packets at sec 4 #: {}".format(packets_node3_t4))
print("User 3 Dropped Packets at sec 5 #: {}".format(packets_node3_t5))
print("User 3 Dropped Packets at sec 6 #: {}".format(packets_node3_t6))
print("User 3 Dropped Packets at sec 7 #: {}".format(packets_node3_t7))
print("User 3 Dropped Packets at sec 8 #: {}".format(packets_node3_t8))
print("User 3 Dropped Packets at sec 9 #: {}".format(packets_node3_t9))
print("User 3 Dropped Packets at sec 10 #: {}".format(packets_node3_t10))
print("Total User 3 Dropped Packets #: {}".format(total_packets_node3))

sent_total_packets_node3=sent_packets_node3_t1+sent_packets_node3_t2+sent_packets_node3_t3+sent_packets_node3_t4+sent_packets_node3_t5+sent_packets_node3_t6+sent_packets_node3_t7+sent_packets_node3_t8+sent_packets_node3_t9+sent_packets_node3_t10
print("User 3 sent Packets at sec 1: {}".format(sent_packets_node3_t1+packets_node3_t1))
print("User 3 sent Packets at sec 2 #: {}".format(sent_packets_node3_t2+packets_node3_t2))
print("User 3 sent Packets at sec 3 #: {}".format(sent_packets_node3_t3+packets_node3_t3))
print("User 3 sent Packets at sec 4 #: {}".format(sent_packets_node3_t4+packets_node3_t4))
print("User 3 sent Packets at sec 5 #: {}".format(sent_packets_node3_t5+packets_node3_t5))
print("User 3 sent Packets at sec 6 #: {}".format(sent_packets_node3_t6+packets_node3_t6))
print("User 3 sent Packets at sec 7 #: {}".format(sent_packets_node3_t7+packets_node3_t7))
print("User 3 sent Packets at sec 8 #: {}".format(sent_packets_node3_t8+packets_node3_t8))
print("User 3 sent Packets at sec 9 #: {}".format(sent_packets_node3_t9+packets_node3_t9))
print("User 3 sent Packets at sec 10 #: {}".format(sent_packets_node3_t10+packets_node3_t10))
#print("Total User 3 Sent Packets #: {}".format(sent_total_packets_node3))

total_packets_node4=packets_node4_t1+packets_node4_t2+packets_node4_t3+packets_node4_t4+packets_node4_t5+packets_node4_t6+packets_node4_t7+packets_node4_t8+packets_node4_t9+packets_node4_t10
print("User 4 Dropped Packets at sec 1: {}".format(packets_node4_t1))
print("User 4 Dropped Packets at sec 2 #: {}".format(packets_node4_t2))
print("User 4 Dropped Packets at sec 3 #: {}".format(packets_node4_t3))
print("User 4 Dropped Packets at sec 4 #: {}".format(packets_node4_t4))
print("User 4 Dropped Packets at sec 5 #: {}".format(packets_node4_t5))
print("User 4 Dropped Packets at sec 6 #: {}".format(packets_node4_t6))
print("User 4 Dropped Packets at sec 7 #: {}".format(packets_node4_t7))
print("User 4 Dropped Packets at sec 8 #: {}".format(packets_node4_t8))
print("User 4 Dropped Packets at sec 9 #: {}".format(packets_node4_t9))
print("User 4 Dropped Packets at sec 10 #: {}".format(packets_node4_t10))
print("Total User 4 Dropped Packets #: {}".format(total_packets_node4))

sent_total_packets_node4=sent_packets_node4_t1+sent_packets_node4_t2+sent_packets_node4_t3+sent_packets_node4_t4+sent_packets_node4_t5+sent_packets_node4_t6+sent_packets_node4_t7+sent_packets_node4_t8+sent_packets_node4_t9+sent_packets_node4_t10
print("User 4 sent Packets at sec 1: {}".format(sent_packets_node4_t1+packets_node4_t1))
print("User 4 sent Packets at sec 2 #: {}".format(sent_packets_node4_t2+packets_node4_t2))
print("User 4 sent Packets at sec 3 #: {}".format(sent_packets_node4_t3+packets_node4_t3))
print("User 4 sent Packets at sec 4 #: {}".format(sent_packets_node4_t4+packets_node4_t4))
print("User 4 sent Packets at sec 5 #: {}".format(sent_packets_node4_t5+packets_node4_t5))
print("User 4 sent Packets at sec 6 #: {}".format(sent_packets_node4_t6+packets_node4_t6))
print("User 4 sent Packets at sec 7 #: {}".format(sent_packets_node4_t7+packets_node4_t7))
print("User 4 sent Packets at sec 8 #: {}".format(sent_packets_node4_t8+packets_node4_t8))
print("User 4 sent Packets at sec 9 #: {}".format(sent_packets_node4_t9+packets_node4_t9))
print("User 4 sent Packets at sec 10 #: {}".format(sent_packets_node4_t10+packets_node4_t10))
#print("Total User 4 Sent Packets #: {}".format(sent_total_packets_node4))

nt1 = packets_node1_t1+packets_node2_t1+packets_node3_t1+packets_node4_t1
nt2=packets_node1_t2+packets_node2_t2+packets_node3_t2+packets_node4_t2
nt3=packets_node1_t3+packets_node2_t3+packets_node3_t3+packets_node4_t3
nt4=packets_node1_t4+packets_node2_t4+packets_node3_t4+packets_node4_t4
nt5=packets_node1_t5+packets_node2_t5+packets_node3_t5+packets_node4_t5
nt6=packets_node1_t6+packets_node2_t6+packets_node3_t6+packets_node4_t6
nt7=packets_node1_t7+packets_node2_t7+packets_node3_t7+packets_node4_t7
nt8=packets_node1_t8+packets_node2_t8+packets_node3_t8+packets_node4_t8
nt9=packets_node1_t9+packets_node2_t9+packets_node3_t9+packets_node4_t9
nt10=packets_node1_t10+packets_node2_t10+packets_node3_t10+packets_node4_t10
print("Total Dropped Packets at sec 1: {}".format(nt1))
print("Total Dropped Packets at sec 2 #: {}".format(nt2))
print("Total Dropped Packets at sec 3 #: {}".format(nt3))
print("Total Dropped Packets at sec 4 #: {}".format(nt4))
print("Total Dropped Packets at sec 5 #: {}".format(nt5))
print("Total Dropped Packets at sec 6 #: {}".format(nt6))
print("Total Dropped Packets at sec 7 #: {}".format(nt7))
print("Total Dropped Packets at sec 8 #: {}".format(nt8))
print("Total Dropped Packets at sec 9 #: {}".format(nt9))
print("Total Dropped Packets at sec 10 #: {}".format(nt10))
total_dropped = total_packets_node1+total_packets_node2+total_packets_node3+total_packets_node4
print("Total Dropped Packets #: {}".format(total_dropped))

print("Total Sent Packets at sec 1: {}".format(sent_packets_node1_t1+sent_packets_node2_t1+sent_packets_node3_t1+sent_packets_node4_t1+nt1))
print("Total Sent Packets at sec 2 #: {}".format(sent_packets_node1_t2+sent_packets_node2_t2+sent_packets_node3_t2+sent_packets_node4_t2+nt2))
print("Total Sent Packets at sec 3 #: {}".format(sent_packets_node1_t3+sent_packets_node2_t3+sent_packets_node3_t3+sent_packets_node4_t3+nt3))
print("Total Sent Packets at sec 4 #: {}".format(sent_packets_node1_t4+sent_packets_node2_t4+sent_packets_node3_t4+sent_packets_node4_t4+nt4))
print("Total Sent Packets at sec 5 #: {}".format(sent_packets_node1_t5+sent_packets_node2_t5+sent_packets_node3_t5+sent_packets_node4_t5+nt5))
print("Total Sent Packets at sec 6 #: {}".format(sent_packets_node1_t6+sent_packets_node2_t6+sent_packets_node3_t6+sent_packets_node4_t6+nt6))
print("Total Sent Packets at sec 7 #: {}".format(sent_packets_node1_t7+sent_packets_node2_t7+sent_packets_node3_t7+sent_packets_node4_t7+nt7))
print("Total Sent Packets at sec 8 #: {}".format(sent_packets_node1_t8+sent_packets_node2_t8+sent_packets_node3_t8+sent_packets_node4_t8+nt8))
print("Total Sent Packets at sec 9 #: {}".format(sent_packets_node1_t9+sent_packets_node2_t9+sent_packets_node3_t9+sent_packets_node4_t9+nt9))
print("Total Sent Packets at sec 10 #: {}".format(sent_packets_node1_t10+sent_packets_node2_t10+sent_packets_node3_t10+sent_packets_node4_t10+nt10))
#total_sent = sent_total_packets_node1+sent_total_packets_node2+sent_total_packets_node3+sent_total_packets_node4
#print("Total Sent Packets #: {}".format(total_sent))
nnt1=sent_packets_node1_t1+sent_packets_node2_t1+sent_packets_node3_t1+sent_packets_node4_t1+nt1
nnt2=sent_packets_node1_t2+sent_packets_node2_t2+sent_packets_node3_t2+sent_packets_node4_t2+nt2
nnt3=sent_packets_node1_t3+sent_packets_node2_t3+sent_packets_node3_t3+sent_packets_node4_t3+nt3
nnt4=sent_packets_node1_t4+sent_packets_node2_t4+sent_packets_node3_t4+sent_packets_node4_t4+nt4
nnt5=sent_packets_node1_t5+sent_packets_node2_t5+sent_packets_node3_t5+sent_packets_node4_t5+nt5
nnt6=sent_packets_node1_t6+sent_packets_node2_t6+sent_packets_node3_t6+sent_packets_node4_t6+nt6
nnt7=sent_packets_node1_t7+sent_packets_node2_t7+sent_packets_node3_t7+sent_packets_node4_t7+nt7
nnt8=sent_packets_node1_t8+sent_packets_node2_t8+sent_packets_node3_t8+sent_packets_node4_t8+nt8
nnt9=sent_packets_node1_t9+sent_packets_node2_t9+sent_packets_node3_t9+sent_packets_node4_t9+nt9
nnt10=sent_packets_node1_t10+sent_packets_node2_t10+sent_packets_node3_t10+sent_packets_node4_t10+nt10

print("Degradation Ratio for Second 1:{}%".format( (float(nt1)/float(nnt1))*100  ))
print("Degradation Ratio for Second 2:{}%".format( (float(nt2)/float(nnt2))*100 ))
print("Degradation Ratio for Second 3:{}%".format( (float(nt3)/float(nnt3))*100 ))
print("Degradation Ratio for Second 4:{}%".format( (float(nt4)/float(nnt4))*100 ))
print("Degradation Ratio for Second 5:{}%".format( (float(nt5)/float(nnt5))*100 ))
print("Degradation Ratio for Second 6:{}%".format( (float(nt6)/float(nnt6))*100 ))
print("Degradation Ratio for Second 7:{}%".format( (float(nt7)/float(nnt7))*100 ))
print("Degradation Ratio for Second 8:{}%".format( (float(nt8)/float(nnt8))*100 ))
print("Degradation Ratio for Second 9:{}%".format( (float(nt9)/float(nnt9))*100 ))
print("Degradation Ratio for Second 10:{}%".format( (float(nt10)/float(nnt10))*100 ))
