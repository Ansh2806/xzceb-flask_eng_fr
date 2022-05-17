import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('bHLEZ5WaZl7QVBgvMU7KAFqL0XfhfUkgEcbsFqN4R2C2')
language_translator = LanguageTranslatorV3(
    version= '2018-05-01', 
    authenticator= authenticator
)
language_translator.set_service_url('https://api.jp-tok.language-translator.watson.cloud.ibm.com/instances/ec596b6d-5e55-4493-bf26-1e7a23e7f6bf')

def english_to_french(english_text):
    """
    This function translates english to french.
    """
    translation= language_translator.translate( text=english_text, model_id="en-fr").get_result()
    french_text=translation["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    """
    This function translates french to english.
    """
    translation= language_translator.translate( text=french_text, model_id="fr-en").get_result()
    english_text=translation["translations"][0]["translation"]
    return english_text