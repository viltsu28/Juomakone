import SpeechToText as stt
import TextClassification as textClassify
import PlayAudio
import serial

		
		
		
def main():
	# PUT HERE ALL INIT STUFF
	ser = serial.Serial('/dev/ttyACM0', 11025, timeout=1) #timeout?
	
	
	# TODO: implement here loop checker if lpc is ready to operate (send something via usb and wait response)
	
    # This Uses SpeechRecoModule to yield spoken sentences.
	speech = stt.speechToText()
    
	action = textClassify.classifySpeech(speech)
	
	for ac in action:
		print ac
		
		intent = ac.intent
		
		if intent == "not_understood":
			PlayAudio.sayAnswer(ac.answer)
			
		elif intent == "service_tell_drinklist":
			PlayAudio.sayAnswer(ac.answer)
			
		elif intent == "service_price":
			PlayAudio.sayAnswer(ac.answer)
			
		elif intent == "service_order_drink":
			PlayAudio.sayAnswer(ac.answer)
			
		elif intent == "service_order_specific_drink":
			PlayAudio.sayAnswer(ac.answer)
			#PlayAudio.playMusic("elevatorMusic")
			ser.write("moi\n")
			jea = ser.readline()
			print str(jea)
			
		elif intent == "info_help":
			PlayAudio.sayAnswer(ac.answer)
			
		else:
			PlayAudio.sayAnswer(ac.answer)
		
		
		
		
if __name__ == '__main__':
    main()
