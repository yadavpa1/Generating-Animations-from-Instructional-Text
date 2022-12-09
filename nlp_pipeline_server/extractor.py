import benepar
from coreference_resolve_spacy import coreference_resolve_spacy
from nltk.tree import Tree
from multiprocessing.connection import Client
from multiprocessing.connection import Listener

def extractor(text):
	parser = benepar.Parser("benepar_en2")
	tree = parser.parse(text)
	parseTree = Tree.fromstring(str(tree)) 
	parseTree.pretty_print()
	result = extract(parseTree)
	for i in result:
		print(i)
	return result
	
def get_np_info(child):
	state = 0
	g_children=[]
	if(child.label()=='NP'):
		for g_child in child:
			if(g_child.label()=='NN' or  g_child.label()=='NNS' or g_child.label()=='NNP'):
				g_children.append(g_child)
	elif(child.label()=='NN' or  child.label()=='NNS' or child.label()=='NNP'):
		g_children.append(child)
	return g_children

def know_childs(parseTree):
	state = 0
	children = []
	for child in parseTree:
		if(type(child) is Tree):
			if(state==0 and (child.label()=='VB' or child.label()=='VBP')):
				state = 1
				children.append(child)
			elif((state==1 or state==4) and child.label()[0]=='N'):
				state = 2
				g_children = get_np_info(child)
				for g_child in g_children:
					children.append(g_child)
				break;
			elif(state==1 and child.label()=='CC'):
				state=3
			elif(state==3 and (child.label()=='VB' or child.label()=='VBP')):
				state=4
				children.append(child)
			else:
				state = 0
				children.clear()
	if(state!=2):
		return None
	else:
		return children

def relate_nounverb(children):
	ans = []
	verbs = []
	nouns=[]
	print(len(children))
	for elem in children:
		if(elem.label()[0]=='V'):
			for i in elem:
				verbs.append(i)
		else:
			break;
	for elem in children:
		if(elem.label()[0]=='N'):
			for i in elem:
				nouns.append(i)
	for i in verbs:
		for j in nouns:
			ans.append(tuple((i,j)))
	return ans
					
def extract(parseTree):
	ans=[]
	if(know_childs(parseTree)!=None):
		children  = know_childs(parseTree)
		ans = relate_nounverb(children)
		return ans
	for child in parseTree:
		if(type(child) is Tree):
			ans.extend(extract(child))
	return ans

#==============================================================================================
def extractor_server(sendaddr,port):
	addrBlocksocket = ('0.0.0.0',port)
	addrSendsocket = (sendaddr,port+1)
	blockSocket = Listener(addrBlocksocket, authkey='leoleo'.encode())
	print("while started")
	while True:
		conn=blockSocket.accept()
		sendSocket = Client(addrSendsocket, authkey='leoleo'.encode())
		text = conn.recv()
		text = coreference_resolve_spacy(text)
		print("Coreference resolved text is:",text)
		print("conn.recv() over")
		result = extractor(text)
		sendSocket.send(result)
		print("sent tuples")
		sendSocket.close()
		conn.close()

if __name__=="__main__":
	extractor_server('localhost',10000)		
