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



def selected(userSelection, userLocation):
    api_key= open('apikey.txt').read()
    map_client = googlemaps.Client(api_key)
    payload = {}
    headers = {}
    selected = []
    

    for i in range(3):
        placeName = (map_client.places(query=userSelection[i] + ' things in ' + userLocation).get('results')[0]['name'])        
        placeId = map_client.places(query=placeName).get('results')[0]["place_id"]
        placeIdUrl = "https://maps.googleapis.com/maps/api/place/details/json?place_id=" + placeId + "&key=" + api_key
        response_data = (requests.request("POST", placeIdUrl, headers = headers, data=payload)).json()
        address = (response_data['result']['formatted_address'])
        photoLink = 'static/images/ab839b129f40850982fdbbaf427a77b23013b8f6422d838e23c23870db3c20f175123a9a7ce6f45e1e81f987223d3f9c3174a64c2b17b7c94e365d_1280.jpg'
        webLink = ""
        openNow = ""

        try:
            webLink = (response_data['result']['website'])
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
