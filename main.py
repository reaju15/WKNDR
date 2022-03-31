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



api_key= open('apikey.txt').read()
map_client = googlemaps.Client(api_key)
unmasker = pipeline('fill-mask', model='bert-base-uncased')
payload = {}
headers = {}
def selected(userSelection, userLocation):
    # api_key= open('apikey.txt').read()
    # map_client = googlemaps.Client(api_key)
    # unmasker = pipeline('fill-mask', model='bert-base-uncased')
    # payload = {}
    # headers = {}

    selected = []
    user = unmasker(f"I like {userSelection} and [MASK].")

    
    for i in range(3):
        placeName = (map_client.places(query=user[i]['token_str'] + ' things in ' + userLocation).get('results')[i]['name'])

        
        placeId = map_client.places(query=placeName).get('results')[0]["place_id"]
        placeIdUrl = "https://maps.googleapis.com/maps/api/place/details/json?place_id=" + placeId + "&key=" + api_key
        response_data = (requests.request("POST", placeIdUrl, headers = headers, data=payload)).json()


        address = (response_data['result']['formatted_address'])
        photoLink = ""
        webLink = ""
        openNow = ""
        webLink = (response_data['result']['website'])


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





@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/interest', methods=['POST', 'GET'])
def login():
    
    if request.method == 'POST':
        userSelection = request.form.getlist('nm')
        userLocation = request.form.getlist('location')
        user = ' and '.join(map(str, userSelection))
        userLocation = ''.join(map(str, userLocation))
        user = unmasker(f"I Love {user} and [MASK].")


        one = (user[0]['token_str'] + ' things in ' + userLocation)
        two = (user[1]['token_str'] + ' things in ' + userLocation)
        three = (user[2]['token_str'] + ' things in ' + userLocation)

        query1 = map_client.places(query=one)
        query2 = map_client.places(query=two)
        query3 = map_client.places(query=three)

        results1 = query1.get('results')
        results2 = query2.get('results')
        results3 = query3.get('results')



        placeName1 = (results1[0]['name'])
        placeName2 = (results2[1]['name'])
        placeName3 = (results3[2]['name'])



        placeQ1 = map_client.places(query=placeName1)
        placeQ2 = map_client.places(query=placeName2)
        placeQ3 = map_client.places(query=placeName3)


        placeId1 = placeQ1.get('results')
        placeId1 = (placeId1[0]["place_id"])

        placeId2 = placeQ2.get('results')
        placeId2 = (placeId2[0]["place_id"])

        placeId3 = placeQ3.get('results')
        placeId3 = (placeId3[0]["place_id"])


        placeIdUrl1 = "https://maps.googleapis.com/maps/api/place/details/json?place_id=" + placeId1 + "&key=" + api_key
        placeIdUrl2 = "https://maps.googleapis.com/maps/api/place/details/json?place_id=" + placeId2 + "&key=" + api_key
        placeIdUrl3 = "https://maps.googleapis.com/maps/api/place/details/json?place_id=" + placeId3 + "&key=" + api_key

        responsegoogle = requests.request("POST", placeIdUrl1, headers = headers, data=payload)
        response_data = responsegoogle.json()

    
        
        openNow1 = ""
        address1 = (response_data['result']['formatted_address'])
        photoLink1 = 'static/images/ab839b129f40850982fdbbaf427a77b23013b8f6422d838e23c23870db3c20f175123a9a7ce6f45e1e81f987223d3f9c3174a64c2b17b7c94e365d_1280.jpg'
        webLink1 = ""
        photoRef1 = ""

        try:
           openNow1 = (response_data['result']['opening_hours']['open_now'])
           webLink1 = (response_data['result']['website'])
           photoRef1 = (response_data['result']['photos'][0]['photo_reference'])
           photoLink1 = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400' + '&photo_reference=' + photoRef1 + "&key=" + api_key
           openNow1 = (response_data['result']['opening_hours']['open_now'])
           if openNow1 == True:
               openNow1 = "Open now"
           else:
               openNow1 = ""
            
           
           
        except Exception:
            print('error1')


        responsegoogle = requests.request("POST", placeIdUrl2, headers = headers, data=payload)
        response_data = responsegoogle.json()

        openNow2 = ""
        address2 = (response_data['result']['formatted_address'])
        photoLink2 = 'static/images/ab839b129f40850982fdbbaf427a77b23013b8f6422d838e23c23870db3c20f175123a9a7ce6f45e1e81f987223d3f9c3174a64c2b17b7c94e365d_1280.jpg'
        webLink2 = ""
        photoRef2 = ""


        try:
           photoRef2 = (response_data['result']['photos'][0]['photo_reference'])
           photoLink2 = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400' + '&photo_reference=' + photoRef2 + "&key=" + api_key
           webLink2 = (response_data['result']['website'])
           openNow2 = (response_data['result']['opening_hours']['open_now']) 
           if openNow2 == True:
               openNow2 = "Open now"
           else:
               openNow2 = ""
           



        except Exception:
            print('error2')


        responsegoogle = requests.request("POST", placeIdUrl3, headers = headers, data=payload)
        response_data = responsegoogle.json()

        
        
        hoursOp3 ="Check website if available for the latest hours"
        openNow3 = ""
        address3 = (response_data['result']['formatted_address'])
        photoLink3 = 'static/images/ab839b129f40850982fdbbaf427a77b23013b8f6422d838e23c23870db3c20f175123a9a7ce6f45e1e81f987223d3f9c3174a64c2b17b7c94e365d_1280.jpg'
        webLink3 = ""

        photoRef3 = ""


        try:
        #    hoursOp3 = (response_data['result']['opening_hours']['weekday_text'])
           webLink3 = (response_data['result']['website'])
           openNow3 = (response_data['result']['opening_hours']['open_now'])
           photoRef3 = (response_data['result']['photos'][0]['photo_reference'])
           photoLink3 = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400' + '&photo_reference=' + photoRef3 + "&key=" + api_key
           openNow3 = (response_data['result']['opening_hours']['open_now'])
           if openNow3 == True:
               openNow3 = "Open now"
           else:
               openNow3 = ""
            


        except Exception:
            print('error3')



        return render_template('3-results.html', placeName1=placeName1, placeName2 =placeName2, placeName3=placeName3, usr=user, one=one, two=two, three=three, 
        photoLink1=photoLink1, openNow1=openNow1, webLink1=webLink1, address1=address1,
        photoLink2=photoLink2, openNow2=openNow2, webLink2=webLink2, address2=address2,
        photoLink3=photoLink3, openNow3=openNow3, webLink3=webLink3, address3=address3, userSelection=userSelection, userLocation=userLocation)
    else:
        return render_template("Interest-page.html")
 
@app.route('/results', methods = ["POST", "GET"])
def inte():
    if request.method == "POST":
        finalselect = request.form.getlist('selected')
        userSelection = request.form.get('userSelection')
        userLocation = request.form.get('userLocation')

        name = (finalselect[0])
        openNow = (finalselect[1])
        photo = (finalselect[2])
        website = (finalselect[4])
        address = (finalselect[5])
        

        return render_template('Result-page.html', finalselect=finalselect, name=name, photo=photo, openNow=openNow, website=website, address=address, userSelection=userSelection, userLocation=userLocation)

@app.route('/survey', methods = ["POST", "GET"])
def sur():
    if request.method == "POST":
        finalselect = request.form.getlist('selected')

        
        nameF = (finalselect[0])
        photoF = (finalselect[1])
        websiteF = (finalselect[2])
        addressF = (finalselect[3])
        userSelection =  request.form.get('userSelection')
        userLocation = request.form.get('userLocation')

        

        return render_template('survey.html', nameF=nameF, photoF=photoF, websiteF=websiteF, addressF=addressF, userSelection=userSelection, userLocation=userLocation)
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
