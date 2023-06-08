import audioread
import matplotlib.pyplot as plt
import numpy as np

filename = "1.wav"
with audioread.audio_open(filename) as f:
    print(f.channels, f.samplerate, f.duration)
    for buf_i, buf in enumerate(f):
        if buf_i < 180:
            continue
        data = np.frombuffer(buf, np.int16)
        plt.plot(range(buf_i*len(data)//2, (buf_i+1)*len(data)//2), data[0::2])
        plt.plot(range(buf_i*len(data)//2, (buf_i+1)*len(data)//2), data[1::2])
        if buf_i > 200:
            break
    plt.show()



























