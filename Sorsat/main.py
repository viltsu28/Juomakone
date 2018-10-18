import SpeechRecoModule as stt
import requests
import json

MIN_CONFIDENCE_LVL = 0.8

def getEntities(response):
    pass

    
def getIntent(response):
    
    intent = response['tracker']['latest_message']['intent']['name']
    return intent

    
def getAnswer(url, payload):

	response = requests.post(url, data=json.dumps(payload))
	response = json.loads(response.text)
	answer = response[0]['text']
	return answer


def getConfidence(response):

    return response['tracker']['latest_message']['intent']['confidence']

	
def classifySpeech(speech):
    
    base_url = 'http://192.168.1.105:5005/conversations/default/'
    answer_url = base_url + 'respond'
    parse_url = base_url + 'parse'
    headers = {"Accept": "application/json", "Accept-Charset": "utf-8"}
	
    for say in speech:
        print "\nUser said: " + str(say)	
        payload = {'query': say}
        parse_response = requests.post(parse_url, data=json.dumps(payload))
        parse_response = json.loads(parse_response.text)
		
        confidence = getConfidence(parse_response)
		
        if (confidence > MIN_CONFIDENCE_LVL):
		    #entities = getEntities(parse_response)
			entities = 'not implemented'
			intent = getIntent(parse_response)
			answer = getAnswer(answer_url, payload)
			print "Entities: [ " + str(entities) + " ]\nIntent: [ " + str(intent) + " ]\nInt Confidence: [ " + str(confidence) + " ]\nAnswer: [ " + str(answer) + " ]\n"
        else:
            # Handle not understood moments		
            print "Not understood: " #+ parse_response.text
		
def main():

    # This Uses SpeechRecoModule to yield spoken sentences.
    speech = stt.speechToText()
    
    classifySpeech(speech)

if __name__ == '__main__':
    main()
