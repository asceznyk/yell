import pyaudio
import threading
import time
import argparse
import wave
import torchaudio
import torch
import sys
import numpy as np
from threading import Event

class Listener:
    def __init__(self, sample_rate=8000, record_seconds=2):
        self.chunk = 1024
        self.sample_rate = sample_rate
        self.record_seconds = record_seconds
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=self.sample_rate,
                        input=True,
                        output=True,
                        frames_per_buffer=self.chunk)

    def listen(self, queue):
        while True:
            data = self.stream.read(self.chunk , exception_on_overflow=False)
            queue.append(data)
            time.sleep(0.01)
            print(len(queue))

    def run(self, queue):
        thread = threading.Thread(target=self.listen, args=(queue,), daemon=True)
        thread.start()
        print("\Speech Recognition engine is now listening... \n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="demoing the speech recognition engine in terminal.")
    parser.add_argument('--model_file', type=str, default=None, required=True,
                        help='optimized file to load. use optimize_graph.py')

    listener = Listener(sample_rate=8000)
    listener.run([])
    threading.Event().wait()
    # activate speech recognition engine




