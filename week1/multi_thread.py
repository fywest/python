import threading

def hello(name):
	print('current child thread, thread ID: {}'.format(threading.get_ident()))
	print('Hello '+name)

def main():
	print('current main thread, thread ID: {}'.format(threading.get_ident()))
	print('-------------------------------------------')
	t=threading.Thread(target=hello,args=('shiyanlou',))
	t.start()
	t.join()
	print('------------------------------------')
	print('current main thread, thread ID: {}'.format(threading.get_ident()))

if __name__=='__main__':
	main()		
