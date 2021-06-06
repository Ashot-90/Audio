import pyaudio
import wave


class Player(object):
    def __init__(self):
        pass

    @staticmethod
    def play(filename='output.wav', chunk=1024, speed=1):
        # Create an interface to PortAudio
        pyaudio_interface = pyaudio.PyAudio()
        # Open the sound file
        wf = wave.open(filename, 'rb')
        # Open a .Stream object to write the WAV file to
        # 'output = True' indicates that the sound will be played rather than recorded
        stream = pyaudio_interface.open(format=pyaudio_interface.get_format_from_width(wf.getsampwidth()),
                                        channels=wf.getnchannels(),
                                        rate=wf.getframerate() * speed,
                                        output=True)
        # Read data in chunks
        data = wf.readframes(chunk)

        # Play the sound by writing the audio data to the stream
        while data != b'':
            stream.write(data)
            data = wf.readframes(chunk)

        # Close and terminate the stream
        stream.close()
        pyaudio_interface.terminate()
