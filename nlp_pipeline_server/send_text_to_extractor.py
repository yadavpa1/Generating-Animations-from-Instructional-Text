from multiprocessing.connection import Listener
from multiprocessing.connection import Client

def send_text_to_extractor(text,sendaddr,port):
    addrSendsocket = (sendaddr, port)
    addrBlocksocket = ('0.0.0.0', port+1)

    blockSocket = Listener(addrBlocksocket, authkey='leoleo'.encode())
    sendSocket = Client(addrSendsocket, authkey='leoleo'.encode())
            
    conn=blockSocket.accept()
    
    sendSocket.send(text)
    results = conn.recv()

    conn.close()
    sendSocket.close()
    blockSocket.close()
    return results

if __name__=="__main__":
	text = "Boil rice and add chopped onions to it."
	results = send_text_to_extractor(text,'localhost',10000)
	print(results)
