import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions


def naturalLanguageUnderstanding(myText):
    authenticator = IAMAuthenticator('key') #insert here the key you get from IBM Cloud at cloud.ibm.com
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2020-08-01',
        authenticator=authenticator
    )

    natural_language_understanding.set_service_url('https://api.eu-de.natural-language-understanding.watson.cloud.ibm.com/instances/38dd91af-7d70-4a5c-bb9b-f3f90c395bde')

    response = natural_language_understanding.analyze(
        text= myText,
        features=Features(keywords=KeywordsOptions(sentiment=True,emotion=True))).get_result()

    print(json.dumps(response, indent=2))
    return response