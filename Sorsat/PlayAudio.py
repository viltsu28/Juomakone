from gtts import gTTS
from pydub import AudioSegment
import pyaudio
import wave
import sys


class AudioFile:
    chunk = 1024

    def __init__(self, file):
        """ Init audio stream """ 
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True
        )

    def play(self):
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != '':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()


def sayAnswer(answer):
	# check first answer sha1sum and compare if one is found from AnswerBank. If not found make google tts request and save to Audio Bank.
	import hashlib
	import os.path
	shaName = hashlib.sha1(answer).hexdigest()
	fileNameWav = "AnswerBank/" + str(shaName) + ".wav"
	fileNameMp3 = "AnswerBank/" + str(shaName) + ".mp3"
	
	if os.path.isfile(fileNameWav):
		print "play answer from bank!!!"
		audioFile = AudioFile(fileNameWav)
		audioFile.play()
		audioFile.close()
	else:
		print "get answer from google tts!!!"
		tts = gTTS(answer, lang='fi')
		tts.save(fileNameMp3)
		sound = AudioSegment.from_mp3(fileNameMp3)
		sound.export(fileNameWav, format="wav")
		
		#delete mp3 version
		os.remove(fileNameMp3)
		audioFile = AudioFile(fileNameWav)
		audioFile.play()
		audioFile.close()