import socket

#UDP_IP = "192.168.56.1"
#UDP_PORT = 5005
MESSAGE = "Welcome"

TCP_IP = '192.168.0.104'
TCP_PORT = 5005
BUFFER_SIZE = 1024*1024

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))
g1=""
print('\nWelcome\n**********\n Random Number generator\n**********\nYou have to enter the amount of frames required for the random numbers you want when asked......if you want to stop the program simply write stop\n')


valuetype=input('\n1| Press 1 for hex value \n2| Press 2 for value in decimal \n===>')	
#print('Type of valuetype is: ',type(valuetype))
while valuetype.isdecimal():

	if valuetype=='1':

		print('You are going to recieve the hex values')
		g = input("Enter your the amount of random numbers that you require: ")
		if g.isnumeric():
			g1=g

			if valuetype=='':
				valuetype=valuetype+'1'

			finalvaluetosend = valuetype+g
			#sock.sendto(finalvaluetosend.encode(), (UDP_IP, UDP_PORT))
			sock.send(finalvaluetosend.encode())
		else:
			while g.isnumeric()==False:
				g=input("Please enter a numeric value: ")
			g1=g

			if valuetype=='':
				valuetype=valuetype+'1'
			finalvaluetosend = valuetype+g

			#sock.sendto(finalvaluetosend.encode(), (UDP_IP, UDP_PORT))
			sock.send(finalvaluetosend.encode())
		finalvaluetosend = valuetype+g
		#sock.sendto(finalvaluetosend.encode(), (UDP_IP, UDP_PORT))
		sock.send(finalvaluetosend.encode())
		while True:
			if g1=="stop":
				#sock.sendto(g.encode(), (UDP_IP, UDP_PORT)) 
				sock.send(g.encode())
				break
			for inc in range(int(g)):
				#data, addr = sock.recvfrom(1024)
				data = sock.recv(BUFFER_SIZE)
				print ("received message:", data.decode())
			#sata=data.decode()
			#sprint(sata)
			#if sata=="stop" or g1=="stop":
			#for inc in range(int(g)):
				#print ("received message:", data.decode())

			g = input("Enter the no of values required : ")
			if g=="stop":
				#sock.sendto(g.encode(), (UDP_IP, UDP_PORT)) 
				sock.send(g.encode())
				break
			elif g.isnumeric():
				g1=g
				if valuetype=='':
					valuetype=valuetype+'1'
				finalvaluetosend = valuetype+g
				#sock.sendto(finalvaluetosend.encode(), (UDP_IP, UDP_PORT))
				sock.send(finalvaluetosend.encode())
			else:
				while g.isnumeric()==False:
					g=input("Please enter a numerica value : ")
				g1=g 
				if valuetype=='':
					valuetype=valuetype+'1'
				finalvaluetosend = valuetype+g
				#sock.sendto(finalvaluetosend.encode(),(UDP_IP,UDP_PORT))
				sock.send(finalvaluetosend.encode())
		break
	elif valuetype=='2':

		print('You are getting decimal values')
		g = input("Enter the amount of frames that you require for values: ")
		if g.isnumeric():
			g1=g

			if valuetype=='':
				valuetype=valuetype+'2'

			finalvaluetosend = valuetype+g
			#sock.sendto(finalvaluetosend.encode(), (UDP_IP, UDP_PORT))
			sock.send(finalvaluetosend.encode())
		else:
			while g.isnumeric()==False:
				g=input("Please enter a numeric value: ")
			g1=g

			if valuetype=='':
				valuetype=valuetype+'2'
			finalvaluetosend = valuetype+g

			#sock.sendto(finalvaluetosend.encode(), (UDP_IP, UDP_PORT))
			sock.send(finalvaluetosend.encode())

		#sock.sendto(g.encode(), (UDP_IP, UDP_PORT))
		if valuetype=='':
			valuetype = valuetype+'2'
		finalvaluetosend = valuetype+g
		sock.send(finalvaluetosend.encode())
		while True:
			if g1=="stop":
				#sock.sendto(g.encode(), (UDP_IP, UDP_PORT)) 
				sock.send(g.encode())
				break
			for inc in range(int(g)):
				#data, addr = sock.recvfrom(1024)
				data = sock.recv(BUFFER_SIZE)
				print ("received message:", data.decode())
			#sata=data.decode()
			#sprint(sata)
			#if sata=="stop" or g1=="stop":
			#for inc in range(int(g)):
				#print ("received message:", data.decode())
			g = input("Enter the no of frames required for generating values: ")
			if g=="stop":
				#sock.sendto(g.encode(), (UDP_IP, UDP_PORT)) 
				sock.send(g.encode())
				break
			elif g.isnumeric():
				g1=g

				if valuetype=='':
					valuetype=valuetype+'2'

				finalvaluetosend = valuetype+g
				#sock.sendto(finalvaluetosend.encode(), (UDP_IP, UDP_PORT))
				sock.send(finalvaluetosend.encode())
			else:
				while g.isnumeric()==False:
					g=input("Please enter a numerica value : ")
				g1=g 
				if valuetype=='':
					valuetype=valuetype+'2'
				finalvaluetosend = valuetype+g
				#.sendto(finalvaluetosend.encode(),(UDP_IP,UDP_PORT))
				sock.send(finalvaluetosend.encode())
		break
	else:
		print('Please enter choose either option 1 or 2 \n\n')
		valuetype=input('\n1| Press 1 for hex value \n2| Press 2 for value in decimal')
#else:
	#print('Please enter a numeric value')



#g = input("Enter your the amount of random numbers that you require: ")
#if g.isnumeric():
	#g1=g
	#sock.sendto(g.encode(), (UDP_IP, UDP_PORT)) 
#else:
	#while g.isnumeric()==False:
		#g=input("Please enter a numeric value: ")
	#g1=g
	#sock.sendto(g.encode(), (UDP_IP, UDP_PORT)) 

#sock.sendto(g.encode(), (UDP_IP, UDP_PORT))
#while True:
	#if g1=="stop":
		#sock.sendto(g.encode(), (UDP_IP, UDP_PORT)) 
		#break
	#for inc in range(int(g)):
		#data, addr = sock.recvfrom(1024)
		#print ("received message:", data.decode())
	#sata=data.decode()
	#sprint(sata)
	#if sata=="stop" or g1=="stop":
	#for inc in range(int(g)):
		#print ("received message:", data.decode())
	#g = input("Enter the no of values required : ")
	#if g=="stop":
		#sock.sendto(g.encode(), (UDP_IP, UDP_PORT)) 
		#break
	#elif g.isnumeric():	
		#g1=g
		#sock.sendto(g.encode(), (UDP_IP, UDP_PORT))  
	#else:
		#while g.isnumeric()==False:
			#g=input("Please enter a numerica value : ") 
		#g1=g
		#sock.sendto(g.encode(),(UDP_IP,UDP_PORT))         

sock.close()
print("program stopped!")