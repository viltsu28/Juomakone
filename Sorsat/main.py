import SpeechToText as stt
import TextClassification as textClassify
import PlayAudio
import serial
import os
		
		
		
def main():
	# PUT HERE ALL INIT STUFF
	ser = serial.Serial('/dev/ttyACM0', 11025, timeout=1) #timeout?
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/SpeechDev/google_creds.json" #export google creds file
	
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
			drinkName = ac.entities 					#here function that check synonyms for drink/or in rasa
			ser.write('{"cmd":"make_drink","value":"' + drinkName + '"}\n')
			jea = ser.readline()
			print str(jea)
			
		elif intent == "info_help":
			PlayAudio.sayAnswer(ac.answer)
			
		else:
			PlayAudio.sayAnswer(ac.answer)
		
		
		
		
if __name__ == '__main__':
    main()
