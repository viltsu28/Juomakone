import SpeechToText as stt
import TextClassification as textClassify
import PlayAudio


		
		
		
def main():

    # This Uses SpeechRecoModule to yield spoken sentences.
    speech = stt.speechToText()
    
    action = textClassify.classifySpeech(speech)
	
    for ac in action:
		print ac
		PlayAudio.sayAnswer(ac.answer)
		
if __name__ == '__main__':
    main()
