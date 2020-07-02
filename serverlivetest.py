import socket
import cv2
import hashlib
import operator

randomBits = ""
hashe=""
pixelRow = 0
pixelColumn = 0


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature



a = socket.gethostname()
b = socket.gethostbyname(a)
print ("\nStarting server at "+b+".....\n")

#UDP_IP = "192.168.56.1"
#UDP_PORT = 5005
TCP_IP = '192.168.0.104'
TCP_PORT = 5005
BUFFER_SIZE = 1024*1024

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))
sock.listen(True)
conn, addr = sock.accept()

cap = cv2.VideoCapture(0) 

#data, addr = sock.recvfrom(1024) 
#print ("received message:", data.decode())
g1=""
i=0
while True:
	#g = input("Enter your message: ")
	#g1=g
	#sock.sendto(g.encode(), addr)
	#if g1=="stop":
		#break       

	#cap = cv2.VideoCapture(0) 
	datal = conn.recv(BUFFER_SIZE)

	check=datal.decode()
	if check=="stop":
		break
	newdatal = str(datal.decode())
	print('Your value is: '+newdatal)
	if newdatal.startswith('1'):
		newvalue = newdatal.replace('1','',1)

	
		satal=int(newvalue)
		if i==0:
			print("\nsending "+str(satal)+" hex values \n Sending.....\n")
			i+=1
			#print("sending "+str(satal)+" values \n Sending.....")
		else:
			#print("Sent "+str(datal)+" values sucessfully..!")
			print("Sent "+str(satal)+" values sucessfully..!\n")
			print("********************************************")
			i=0
		#if 

		for inc in range(satal):
			ret,frame = cap.read()
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			ret,bW_Image = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
			while pixelRow < bW_Image.shape[0]:
				while pixelColumn < bW_Image.shape[1]:
					x = bW_Image[pixelRow,pixelColumn]
					if x.any()==0:
						randomBits = randomBits + "0"
					else:
						randomBits = randomBits + "1"
					pixelColumn = pixelColumn + 1
				pixelRow = pixelRow +1
				pixelColumn = 0
			pixelRow=0
			pixelColumn=0
			hashe= encrypt_string(randomBits)
			conn.send(str(hashe).encode())

			#sock.sendto(str(hashe).encode(),addr)
		#print("\nemptying datal!\n")
		i=1
			#cv2.imshow('adeel',bW_Image)
			#if inc==satal-4:
				#break
			#cv2.imshow('Adeel',bW_Image)
		#cap.release()
		#cv2.destroyAllWindows()
		#if satal=="i values":
			#for i in range(6):
				#sock.sendto(str(i).encode(),addr)
		#else:
			#print ("received message:", datal.decode())

	elif newdatal.startswith('2'):
		newvalue = newdatal.replace('2','',1)
		print(newvalue)

		satal=int(newvalue)
		if i==0:
			print("\nsending "+str(satal)+" binary values \n Sending.....\n")
			i+=1
			#print("sending "+str(satal)+" values \n Sending.....")
		else:
			#print("Sent "+str(datal)+" values sucessfully..!")
			print("Sent "+str(satal)+" values sucessfully..!\n")
			print("********************************************")
			i=0
		#if 

		for inc in range(satal):
			ret,frame = cap.read()
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			ret,bW_Image = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
			while pixelRow < bW_Image.shape[0]:
				while pixelColumn < bW_Image.shape[1]:
					x = bW_Image[pixelRow,pixelColumn]
					if x.any()==0:
						randomBits = randomBits + "0"
					else:
						randomBits = randomBits + "1"
					pixelColumn = pixelColumn + 1
				pixelRow = pixelRow +1
				pixelColumn = 0
			pixelRow=0
			pixelColumn=0
			#hashe= encrypt_string(randomBits)
			conn.send(str(randomBits).encode())
			#sock.sendto(str(randomBits).encode(),addr)
		#print("\nemptying datal!\n")
		i=1
			#cv2.imshow('adeel',bW_Image)
			#if inc==satal-4:
				#break
			#cv2.imshow('Adeel',bW_Image)
		#cap.release()
		#cv2.destroyAllWindows()
		#if satal=="i values":
			#for i in range(6):
				#sock.sendto(str(i).encode(),addr)
		#else:
			#print ("received message:", datal.decode())

conn.close()

cap.release()
print("program stopped!")