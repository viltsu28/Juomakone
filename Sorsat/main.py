import SpeechRecoModule as stt

def printSpeech(speech):
    for say in speech:
        print say

def main():

    # This Uses SpeechRecoModule to yield spoken sentences.
    speech = stt.speechToText()
    
    printSpeech(speech)

if __name__ == '__main__':
    main()
