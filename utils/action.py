import keyboard

def send_key(key):
	keyboard.press_and_release(key)

def jump():
	keyboard.press_and_release('space')
	print('Jump!')

def fishing():
	print('fishing f!')
	send_key('f')
	print('Float is sent, waiting animation')

def snatch():
	print('snatch g!')
	send_key('g')
