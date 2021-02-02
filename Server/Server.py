#import of the necessary modules and the API functions
import socket 
from speechText import speechText as st
from naturalLanguageUnderstanding import naturalLanguageUnderstanding as nlu

#declaration of the port and adress for the communication
PORT = 8080
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

#initiate the TCP-Socket connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#declaration of the start function which is listening for an connection and write received in working file
def start():

    print("[STARTING] Server is starting...")  
    server.listen()  
    print(f"[LISTENING] Server is listening on {ADDR}")   
    conn, addr = server.accept()
    with open('received.ogg','wb') as f:
        print(f"Server is receiving data from {addr}")
        while True:
            l = bytearray(conn.recv(1024))
            f.write(bytes(l))
            if not l: break

#call of the start function
start()

print("Verarbeitung läuft...")

#call of the transcription function of the speechText-API
transcription = st() 
splitedText = transcription.split("\n") #split transcriped text into array
print(splitedText)
myText = str(splitedText[2]) #read text part of array and save as string
print(myText) 

print("Text wird Analysiert") 

#call analysing function of naturalLanguageUnderstanding-API and save result
results = nlu(myText)

#start of an new TCP connection to send the results 
print("[Reconnect] Server is opening ne connection...")  
server.listen()  
print(f"[LISTENING] Server is listening on {ADDR}")   
conn, addr = server.accept()
print(addr)

#declaration of sendAnswer function that sends answer to client and ends the connection
def sendAnswer(myText):
    
    print('Sending answer')
    msg = bytearray(myText, 'utf-8')
    print(msg)
    conn.sendall(msg)
    print('Send completed')
    conn.close()

sendAnswer(myText)
