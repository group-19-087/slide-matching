# from tts_watson.TtsWatson import TtsWatson
#
# ttsWatson = TtsWatson('watson_user', 'watson_password', 'en-US_AllisonVoice') # en-US_AllisonVoice is a voice from watson you can found more to: https://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/doc/text-to-speech/using.shtml#voices
# ttsWatson.play("The text which i want to be a sound")


import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)

import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Hello World')
engine.runAndWait()

# import pyttsx3
#
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#     print (voice)
#     # if voice.languages[0] == u'en_US':
#     #     engine.setProperty('voice', voice.id)
#     #     break
#     engine.say('Hello World')
#
# engine.runAndWait()