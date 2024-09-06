import pyaudio
import time
import numpy as np

import random

waitSilent=False

def randomFloatNum (start, end):
	return random.uniform(start, end)

def randomIntNum (start, end):
	return random.randint(start, end)

def randomWait(startNum=1, endNum=5):
	random_num = randomFloatNum(startNum, endNum)
	print(f'wait {random_num}...')
	time.sleep(random_num)
	return


def get_volume(data):
    """计算音频数据的音量"""
    audio_data = np.frombuffer(data, dtype=np.int16)
    return np.max(np.abs(audio_data))

def listen(silentVolume=760,gotVolume=1800):
	global waitSilent
	print('Well, now we are listening for loud sounds...')
	CHUNK = 1024  # CHUNKS of bytes to read each time from mic
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 18000
	# THRESHOLD = 1800  # The threshold intensity that defines silence
	#Open stream
	audio = pyaudio.PyAudio()
	stream = audio.open(
		format=FORMAT,
		channels=CHANNELS,
		rate=RATE,
		input=True,
		frames_per_buffer=CHUNK)
	success = False
	listening_start_time = time.time()
	while True:
		try:
			cur_data = stream.read(CHUNK)
			volume = get_volume(cur_data)
			print(f'cur Volume:{volume}')
			if volume < int(silentVolume):
				waitSilent = False
			if not waitSilent:
				if volume > gotVolume:
					print(f"Sound detected! Volume: {volume}")
					success = True
					waitSilent = True
					break
				else:
					print("No sound detected.")
					time.sleep(0.5)
				if time.time() - listening_start_time > 20:
					print('I don\'t hear anything already 20 seconds!')
					break
			else:
				print("wait to silent")
				time.sleep(0.5)
		except IOError:
			break
	# print "* Done recording: " + str(time.time() - start)
	stream.stop_stream()
	stream.close()
	audio.terminate()
	return success