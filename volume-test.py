import time

import pyaudio
import numpy as np

# 配置录音参数
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

audio = pyaudio.PyAudio()

# 打开音频流
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("listen in...")

try:
    while True:
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        volume = np.sqrt(np.mean(np.square(data)))
        print(f"volume: {volume:.2f}")
        time.sleep(.5)
except KeyboardInterrupt:
    print("listen off.")

# 停止和关闭音频流
stream.stop_stream()
stream.close()
audio.terminate()
