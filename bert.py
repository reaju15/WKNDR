import pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from flask import Flask, render_template, request, redirect, url_for
import requests
import googlemaps
from numpy import place
from urllib.parse import unquote
from sqlalchemy import JSON
from transformers import BertTokenizer, BertForNextSentencePrediction, AutoTokenizer, AutoModelForMaskedLM
from transformers import logging
logging.set_verbosity_error()
from transformers import pipeline
from pprint import pprint



app = Flask(__name__)


def selected(userSelection, userLocation):
    api_key= open('apikey.txt').read()
    map_client = googlemaps.Client(api_key)
    unmasker = pipeline('fill-mask', model='bert-base-uncased')
    payload = {}
    headers = {}

    selected = []
    user = unmasker(f"I like {userSelection} and [MASK].")
    # user = unmasker(f"if you like {userSelection} then you should also try [MASK].")
    pprint(user)
    
    for i in range(3):
        placeName = (map_client.places(query=user[i]['token_str'] + ' things in ' + userLocation).get('results')[i]['name'])

        # results = (map_client.places(query=user[i]['token_str'] + ' things to do in ' + userLocation).get('results')[2])
        # pprint(results)
        placeId = map_client.places(query=placeName).get('results')[0]["place_id"]
        placeIdUrl = "https://maps.googleapis.com/maps/api/place/details/json?place_id=" + placeId + "&key=" + api_key
        response_data = (requests.request("POST", placeIdUrl, headers = headers, data=payload)).json()


        address = (response_data['result']['formatted_address'])
        photoLink = ""
        webLink = ""
        openNow = ""
        webLink = (response_data['result']['website'])
        pprint(webLink)

        try:
            webLink = (response_data['result']['website'])
            pprint(webLink)
            photoRef = (response_data['result']['photos'][0]['photo_reference'])
            photoLink = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400' + '&photo_reference=' + photoRef + "&key=" + api_key
            openNow = (response_data['result']['opening_hours']['open_now'])
            if openNow == True:
                openNow = "Open now"
            else:
                openNow = ""
     
        except Exception:
            print('error')

        selected.append({"photoLink":photoLink, "address":address, "webLink":webLink, "openNow":openNow, "placeName":placeName})

    return selected
