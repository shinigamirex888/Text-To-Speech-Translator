from gtts import gTTS
import base64
from ibm_watson import SpeechToTextV1, LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

ltapikey = 'OZmPVJ_4X70AzVgC5OtKU-36Rk5ErjZw-cCJaifRlhKF'
lturl = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/1cd1e936-c1f3-4451-80dc-5de9c7be086a'

ltauthenticator = IAMAuthenticator(ltapikey)
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=ltauthenticator)
lt.set_service_url(lturl)

def text2Speech(data):
    my_text = data
    greek = 'en-el'
    chinese = 'en-zh'
    hindi = 'en-hi'
    translation = lt.translate(text=my_text, model_id=hindi).get_result()
    translatedtext = translation['translations'][0]['translation']

    tts = gTTS(text=translatedtext, lang='en', slow=False)
    tts.save('converted-file.mp3')  # save file as ... (here saving as mp3)
    with open("converted-file.mp3", "rb") as file:
        my_string = base64.b64encode(file.read())
    return my_string
