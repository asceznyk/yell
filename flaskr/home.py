from flask import Flask, Blueprint, Response, render_template
import pyaudio

bp = Blueprint('app', __name__, url_prefix='/')

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
 
audio1 = pyaudio.PyAudio()

def gen_header(sample_rate, bit_per_sample, channels):
    datasize = 2000*10**6
    o = bytes("RIFF",'ascii')                                               # (4byte) Marks file as RIFF
    o += (datasize + 36).to_bytes(4,'little')                               # (4byte) File size in bytes excluding this and RIFF marker
    o += bytes("WAVE",'ascii')                                              # (4byte) File type
    o += bytes("fmt ",'ascii')                                              # (4byte) Format Chunk Marker
    o += (16).to_bytes(4,'little')                                          # (4byte) Length of above format data
    o += (1).to_bytes(2,'little')                                           # (2byte) Format type (1 - PCM)
    o += (channels).to_bytes(2,'little')                                    # (2byte)
    o += (sample_rate).to_bytes(4,'little')                                  # (4byte)
    o += (sample_rate * channels * bit_per_sample // 8).to_bytes(4,'little')  # (4byte)
    o += (channels * bit_per_sample // 8).to_bytes(2,'little')               # (2byte)
    o += (bit_per_sample).to_bytes(2,'little')                               # (2byte)
    o += bytes("data",'ascii')                                              # (4byte) Data Chunk Marker
    o += (datasize).to_bytes(4,'little')                                    # (4byte) Data size in bytes
    return o

@bp.route("/")
def audio():
    # start Recording
    def sound():
        CHUNK = 1024
        sample_rate = 44100
        bit_per_sample = 16
        channels = 2
        wav_header = gen_header(sample_rate, bit_per_sample, channels)

        stream = audio1.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,input_device_index=1,
                        frames_per_buffer=CHUNK)
        print("recording...")
        #frames = []
        first_run = True
        while True:
           if first_run:
               data = wav_header + stream.read(CHUNK)
               first_run = False
           else:
               data = stream.read(CHUNK)
           yield(data)

    return Response(sound())

#@bp.route("/")
#def main_page():
#    return render_template('main.html')



