"""
Translation module
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv('machinetranslation/keys.env')
url_lt = os.getenv('URL')
apikey_lt = os.getenv('API_KEY')
VERSION_LT = '2018-05-01'
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=VERSION_LT, authenticator=authenticator)
language_translator.set_service_url(url_lt)


def eng_to_french(text_translate):
    """Converts Eng to French."""
    translation_response = language_translator.translate(text=text_translate, model_id='en-fr')
    translation = {}
    translation = translation_response.get_result()
    french_translation = translation['translations'][0]['translation']
    return french_translation


def french_to_eng(text_translate):
    """Converts French to Eng."""
    translation_response = language_translator.translate(text=text_translate, model_id='fr-en')
    translation = {}
    translation = translation_response.get_result()
    english_translation = translation['translations'][0]['translation']
    return english_translation
