import socket
from threading import Thread 
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
import random
ip_adress="127.0.0.1"
port=5000
server.bind((ip_adress,port))
server.listen()
clients=[]
questions=[
    "What is 1+1? /n a)2 /n b)3 c) /n 4 d)5",
    "What is 1+2? /n a)2 /n b)3 /n  c)4  /n d)5",
     "What is 1+3? /n a)2 /n b)3 /n  c)4  /n d)5",
      "What is 1+4? /n a)2 /n b)3 /n  c)4  /n d)5",
]
answers=['a','b','c','d']
def get_random_question():
    random_index=random.randint(0,len(questions)-1)
    radnom_questions=questions[random_index]
    radnom_answers=answers[random_index]

def remove_qeustions(index):
    questions.pop(index)
    answers.pop(index)

def client_thread(con,addr):
    con.send("Welcome to this Chat room".encode("utf-8"))
    while True:
        try:
            message=con.recv(2048).decode("utf-8")
            if message:
                print("<" + addr[0] + ">" + message)
                message_to_send="<" + addr[0] + ">" + message
                broadcast(message_to_send,con)

            else:
                remove(con)

        except:
            continue

def broadcast(message,connection):
    for cli in clients:
        if cli!=connection:
            try:
                cli.send(message.encode("utf-8"))

            except:
                remove(cli)

def remove(connection):
    if connection in clients:
        clients.remove(connection)
    



while True:
    con,addr=server.accept()
    clients.append(con)
    print(addr[0]+"connected")

    new_thread=Thread(target=client_thread,args=(con,addr))
    new_thread.start()


