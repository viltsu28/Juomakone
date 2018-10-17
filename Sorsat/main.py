import SpeechRecoModule as stt
import requests
import json

def printSpeech(speech):
    for say in speech:
        #print say
        url = 'http://192.168.1.105:5005/conversations/default/respond'
        headers = {"Accept": "application/json", "Accept-Charset": "utf-8"}
        payload = {'query': say}
        response = requests.post(url, data=json.dumps(payload))	
        print response.text
		
def main():

    # This Uses SpeechRecoModule to yield spoken sentences.
    speech = stt.speechToText()
    
    printSpeech(speech)

if __name__ == '__main__':
    main()
