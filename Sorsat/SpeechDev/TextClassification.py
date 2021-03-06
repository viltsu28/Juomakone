# coding=utf-8
import requests
import json
import random

MIN_CONFIDENCE_LVL = 0.8
NOT_UNDERSTOOD_ANSWER = ['Anteeksi en nyt ihan ymmärtänyt.', 'Voisitko toistaa?', 'Nyt en ihan ymmärtänyt mitä sanoit. Voisitko sanoa vielä uudestaan?']

class Action:

	def __init__(self, intent, confidence, entities, answer):
		self.intent = intent
		self.entities = entities
		self.answer = answer
		self.confidence = confidence
		
	def __str__(self):
		return "Entities: [ " + str(self.entities) + " ]\nIntent: [ " + str(self.intent) + " ]\nInt Confidence: [ " + str(self.confidence) + " ]\nAnswer: [ " + str(self.answer) + " ]\n"





		
def getEntities(response):
	entity = response['tracker']['latest_message']['entities']
	userInput = response['tracker']['latest_message']['text']
	
	if entity: #if not empty
		key = str(entity[0]['entity'])
		value = str(entity[0]['value'])
		
		# check if value is drinkki TODO: fix in RASA if time
		if value == 'drinkki':
			start = int(entity[0]['start'])
			end = int(entity[0]['end'])
			value = str(userInput[start:end])
			
		return (key, value)
		
	return entity
	
	
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
		if (say is None): # This usually means that google stt time limit exceeded
			print "\nUser said: " + str(say)
		else:
			print "\nUser said: " + str(say)	
			payload = {'query': say}
			parse_response = requests.post(parse_url, data=json.dumps(payload))
			parse_response = json.loads(parse_response.text)
			
			confidence = getConfidence(parse_response)
			
			if (confidence > MIN_CONFIDENCE_LVL):
				entities = getEntities(parse_response)
				intent = getIntent(parse_response)
				answer = getAnswer(answer_url, payload)
				action = Action(intent, confidence, entities, answer)
				yield action
			else:
				# Handle not understood moments		
				action = Action('not_understood', confidence, '', random.choice(NOT_UNDERSTOOD_ANSWER))
				yield action
