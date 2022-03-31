import bert
from flask import Flask, render_template, request, redirect, url_for
from pprint import pp, pprint
import googlemaps

app = Flask(__name__)


<<<<<<< HEAD

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





=======
>>>>>>> 3df1ef90554033c8a5fbdf8bf48ef10d17ae6ca3
@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/interest', methods=['POST', 'GET'])
<<<<<<< HEAD
def login():
    userSelection = ' and '.join(map(str, request.form.getlist('nm')))
    userLocation =  (''.join(map(str, request.form.getlist('location'))))
    if request.method == 'POST':
        selectedData = selected(userSelection, userLocation)
=======
def main():
    userSelection = ' and '.join(map(str, request.form.getlist('nm')))
    userLocation =  (''.join(map(str, request.form.getlist('location'))))
    if request.method == 'POST':
        selectedData = bert.selected(userSelection, userLocation)
>>>>>>> 3df1ef90554033c8a5fbdf8bf48ef10d17ae6ca3

        results1 = selectedData[0]
        results2 = selectedData[1]
        results3 = selectedData[2]

        openNow1 = results1["openNow"]
        address1 = results1["address"]
        placeName1 = results1["placeName"]
        photoLink1 = results1["photoLink"]
        webLink1 = results1["webLink"]

        openNow2 = results2["openNow"]
        address2 = results2["address"]
        placeName2 = results2["placeName"]
        photoLink2 = results2["photoLink"]
        webLink2 = results2["webLink"]

        openNow3 = results3["openNow"]
        address3 = results3["address"]
        placeName3 = results3["placeName"]
        photoLink3 = results3["photoLink"]
        webLink3 = results3["webLink"]
        

        return render_template('3-results.html', openNow3=openNow3, openNow2=openNow2, openNow1=openNow1, placeName1=placeName1, placeName2=placeName2, userLocation=userLocation,
         placeName3=placeName3, address1=address1, address2=address2, address3=address3, photoLink1=photoLink1, webLink1=webLink1, photoLink2=photoLink2, webLink2=webLink2, photoLink3=photoLink3, webLink3=webLink3, userSelection=userSelection)
        
    else:
        return render_template("Interest-page.html")
<<<<<<< HEAD


=======
    
>>>>>>> 3df1ef90554033c8a5fbdf8bf48ef10d17ae6ca3
@app.route('/results', methods = ["POST", "GET"])
def inte():
    if request.method == "POST":
        finalselect = request.form.getlist('selected')
        userSelection = request.form.get('userSelection')
        userLocation=  request.form.get('userLocation')
        
        nameF = (finalselect[0])
        openNowF = (finalselect[1])
        photoF = (finalselect[2])
        hoursOpF = (finalselect[3])
        websiteF = (finalselect[4])
        addressF = (finalselect[5])

        return render_template('Result-page.html', finalselect=finalselect, name=nameF, photo=photoF, openNow=openNowF, hoursOp=hoursOpF, website=websiteF, address=addressF, userSelection=userSelection, userLocation=userLocation)

@app.route('/survey', methods = ["POST", "GET"])
def sur():
    if request.method == "POST":
        finalselect = request.form.getlist('selected')

        
        nameF = (finalselect[0])
        photoF = (finalselect[1])
        websiteF = (finalselect[2])
        addressF = (finalselect[3])
        userSelection =  request.form.get('userSelection')
        userLocation=  request.form.get('userLocation')
        



        return render_template('Survey.html', nameF=nameF, photoF=photoF, websiteF=websiteF, addressF=addressF, userSelection=userSelection, userLocation=userLocation)
<<<<<<< HEAD
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)



#         userDataCon = request.form.getlist('nm')
#         userlocation = request.form.getlist('location')
#         user = ' and '.join(map(str, userDataCon))
#         userlocation = ''.join(map(str, userlocation))
#         user = unmasker(f"I love {user} and [MASK].")

            



#         one = (user[0]['token_str'] + ' things in ' + userlocation)
#         two = (user[1]['token_str'] + ' things in ' + userlocation)
#         three = (user[2]['token_str'] + ' things in ' + userlocation)

#         query1 = map_client.places(query=one)
#         query2 = map_client.places(query=two)
#         query3 = map_client.places(query=three)

#         results1 = query1.get('results')
#         results2 = query2.get('results')
#         results3 = query3.get('results')



#         resultsname1 = (results1[0]['name'])
#         resultsname2 = (results2[1]['name'])
#         resultsname3 = (results3[2]['name'])



#         placeQ1 = map_client.places(query=resultsname1)
#         placeQ2 = map_client.places(query=resultsname2)
#         placeQ3 = map_client.places(query=resultsname3)


#         placeId1 = placeQ1.get('results')
#         placeId1 = (placeId1[0]["place_id"])

#         placeId2 = placeQ2.get('results')
#         placeId2 = (placeId2[0]["place_id"])

#         placeId3 = placeQ3.get('results')
#         placeId3 = (placeId3[0]["place_id"])


#         placeIdUrl1 = "https://maps.googleapis.com/maps/api/place/details/json?place_id=" + placeId1 + "&key=" + api_key
#         placeIdUrl2 = "https://maps.googleapis.com/maps/api/place/details/json?place_id=" + placeId2 + "&key=" + api_key
#         placeIdUrl3 = "https://maps.googleapis.com/maps/api/place/details/json?place_id=" + placeId3 + "&key=" + api_key

#         responsegoogle = requests.request("POST", placeIdUrl1, headers = headers, data=payload)
#         response_data = responsegoogle.json()

    
        
#         openNow1 = ""
#         hoursOp1 = "Check the website if available for the lastest hours"
#         address1 = (response_data['result']['formatted_address'])
#         photoLink1 = 'static/images/ab839b129f40850982fdbbaf427a77b23013b8f6422d838e23c23870db3c20f175123a9a7ce6f45e1e81f987223d3f9c3174a64c2b17b7c94e365d_1280.jpg'
#         weblink1 = ""

#         photoRef1 = ""
  

#         try:
#            openNow1 = (response_data['result']['opening_hours']['open_now'])
#            hoursOp1 = (response_data['result']['opening_hours']['weekday_text'])
#            weblink1 = (response_data['result']['website'])
#            photoRef1 = (response_data['result']['photos'][0]['photo_reference'])
#            photoLink1 = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400' + '&photo_reference=' + photoRef1 + "&key=" + api_key
#            if openNow1 == True:
#                openNow1 = "Open now"
#            else:
#                openNow1 = ""
            
           
           
#         except Exception:
#             print('error1')


#         responsegoogle = requests.request("POST", placeIdUrl2, headers = headers, data=payload)
#         response_data = responsegoogle.json()

#         openNow2 = ""
#         hoursOp2 = "Check the website if available for the latest hours"
#         address2 = (response_data['result']['formatted_address'])
#         photoLink2 = 'static/images/ab839b129f40850982fdbbaf427a77b23013b8f6422d838e23c23870db3c20f175123a9a7ce6f45e1e81f987223d3f9c3174a64c2b17b7c94e365d_1280.jpg'
#         weblink2 = ""
  
#         photoRef2 = ""

        

#         try:
           
#            photoRef2 = (response_data['result']['photos'][0]['photo_reference'])
#            photoLink2 = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400' + '&photo_reference=' + photoRef2 + "&key=" + api_key
#            openNow2 = (response_data['result']['opening_hours']['open_now']) 
#            weblink2 = (response_data['result']['website'])
#            if openNow2 == True:
#                openNow2 = "Open now"
#            else:
#                openNow2 = ""
#            weblink2 = (response_data['result']['website'])



#         except Exception:
#             print('error2')


#         responsegoogle = requests.request("POST", placeIdUrl3, headers = headers, data=payload)
#         response_data = responsegoogle.json()

        
        
#         hoursOp3 ="Check website if available for the latest hours"
#         openNow3 = ""
#         address3 = (response_data['result']['formatted_address'])
#         photoLink3 = 'static/images/ab839b129f40850982fdbbaf427a77b23013b8f6422d838e23c23870db3c20f175123a9a7ce6f45e1e81f987223d3f9c3174a64c2b17b7c94e365d_1280.jpg'
#         weblink3 = ""
#         photoRef3 = ""
 
#         try:
#            hoursOp3 = (response_data['result']['opening_hours']['weekday_text'])
#            weblink3 = (response_data['result']['website'])
#            openNow3 = (response_data['result']['opening_hours']['open_now'])
#            photoRef3 = (response_data['result']['photos'][0]['photo_reference'])
#            photoLink3 = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400' + '&photo_reference=' + photoRef3 + "&key=" + api_key
#            if openNow3 == True:
#                openNow3 = "Open now"
#            else:
#                openNow3 = ""
            


#         except Exception:
#             print('error3')



#         return render_template('3-results.html', resultsname1=resultsname1, resultsname2 =resultsname2, resultsname3=resultsname3, usr=user, one=one, two=two, three=three, 
#         photoLink1=photoLink1, openNow1=openNow1, weblink1=weblink1, hoursOp1=hoursOp1,address1=address1,
#         photoLink2=photoLink2, openNow2=openNow2, weblink2=weblink2, hoursOp2=hoursOp2,address2=address2,
#         photoLink3=photoLink3, openNow3=openNow3, weblink3=weblink3, hoursOp3=hoursOp3,address3=address3, userDataCon=userDataCon)
#     else:
#         return render_template("Interest-page.html")
 
# @app.route('/results', methods = ["POST", "GET"])
# def inte():
#     if request.method == "POST":
#         finalselect = request.form.getlist('selected')
#         userSelection = request.form.get('userSelection')

#         name = (finalselect[0])
#         openNow = (finalselect[1])
#         photo = (finalselect[2])
#         website = (finalselect[4])
#         address = (finalselect[5])
        

#         return render_template('Result-page.html', finalselect=finalselect, name=name, photo=photo, openNow=openNow, website=website, address=address, userSelection=userSelection)

# @app.route('/survey', methods = ["POST", "GET"])
# def sur():
#     if request.method == "POST":
#         finalselect = request.form.getlist('selected')


#         pprint("=====")
#         pprint(finalselect)
        
#         nameF = (finalselect[0])
#         photoF = (finalselect[1])
#         websiteF = (finalselect[2])
#         addressF = (finalselect[3])
#         userSelection =  request.form.get('userSelection')

        

#         return render_template('Survey.html', nameF=nameF, photoF=photoF, websiteF=websiteF, addressF=addressF, userSelection=userSelection)
=======
>>>>>>> 3df1ef90554033c8a5fbdf8bf48ef10d17ae6ca3
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
