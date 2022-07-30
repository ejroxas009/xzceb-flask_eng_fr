"""Uses IBM Language Translator service to translate english to french and vice-versa"""

import json

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

def translator_instance():
    """Function to create tranlator instance"""
    load_dotenv()
    apikey = os.environ['apikey']
    url = os.environ['url']
    version = '2018-05-01'
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version=version,
        authenticator=authenticator
    )

    language_translator.set_service_url(url)
    return language_translator

def englishToFrench(englishText):
    """Function to convert english to french"""
    e2f_translator = translator_instance()
    frenchText = e2f_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    return frenchText["translations"][0]["translation"]

def frenchToEnglish(frenchText):
    """Function to convert french to english"""
    f2e_translator = translator_instance()
    englishText = f2e_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    return englishText["translations"][0]["translation"]