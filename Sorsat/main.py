import SpeechToText as stt
import TextClassification as textClassify
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


def main():

    # This Uses SpeechRecoModule to yield spoken sentences.
    speech = stt.speechToText()
    
    action = textClassify.classifySpeech(speech)
	
    for ac in action:
		print ac
		tts = gTTS(ac.answer, lang='fi')
		tts.save('testi.mp3')
		
		
		sound = AudioSegment.from_mp3("testi.mp3")
		sound.export("testi.wav", format="wav")
		a = AudioFile("testi.wav")
		a.play()
		a.close()
		
if __name__ == '__main__':
    main()
