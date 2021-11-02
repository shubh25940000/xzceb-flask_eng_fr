from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
url_lt='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/2874ea28-1865-424e-bfa6-1ab723b05603'
apikey_lt='62kSDjd2RlPmNuj8SwzWAV0wCHM_wdE92C5YkKl_pjSH'
version_lt='2018-05-01'
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
text_translate = 'Hello, how are you?'

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
