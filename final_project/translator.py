from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv('keys.env')
import os
url_lt= os.getenv('URL')
apikey_lt= os.getenv('API_KEY')
version_lt='2018-05-01'
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)

def eng_to_french(text_translate):
    translation_response = language_translator.translate(text=text_translate, model_id='en-fr')
    translation = translation_response.get_result()
    french_translation = translation['translations'][0]['translation']
    return french_translation
def french_to_eng(text_translate):
    translation_response = language_translator.translate(text=text_translate, model_id='fr-en')
    translation = translation_response.get_result()
    english_translation = translation['translations'][0]['translation']
    return english_translation