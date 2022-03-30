import bert
from flask import Flask, render_template, request, redirect, url_for
from pprint import pp, pprint
import googlemaps



app = Flask(__name__)


@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/interest', methods=['POST', 'GET'])
def main():
    userSelection = ' and '.join(map(str, request.form.getlist('nm')))
    userLocation =  ''.join(map(str, request.form.getlist('location')))
    if request.method == 'POST':
        selectedData = bert.selected(userSelection, userLocation)

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
        

        return render_template('3-results.html', openNow3=openNow3, openNow2=openNow2, openNow1=openNow1, placeName1=placeName1, placeName2=placeName2,
         placeName3=placeName3, address1=address1, address2=address2, address3=address3, photoLink1=photoLink1, webLink1=webLink1, photoLink2=photoLink2, webLink2=webLink2, photoLink3=photoLink3, webLink3=webLink3)
        
    else:
        return render_template("Interest-page.html")
    
@app.route('/results', methods = ["POST", "GET"])
def inte():
    if request.method == "POST":
        finalselect = request.form.getlist('selected')
        userSelection = request.form.get('userSelection')
        
        nameF = (finalselect[0])
        openNowF = (finalselect[1])
        photoF = (finalselect[2])
        hoursOpF = (finalselect[3])
        websiteF = (finalselect[4])
        addressF = (finalselect[5])

        return render_template('Result-page.html', finalselect=finalselect, name=nameF, photo=photoF, openNow=openNowF, hoursOp=hoursOpF, website=websiteF, address=addressF, userSelection=userSelection)

@app.route('/survey', methods = ["POST", "GET"])
def sur():
    if request.method == "POST":
        finalselect = request.form.getlist('selected')

        
        nameF = (finalselect[0])
        photoF = (finalselect[1])
        websiteF = (finalselect[2])
        addressF = (finalselect[3])
        userSelection =  request.form.get('userSelection')


        return render_template('survey.html', nameF=nameF, photoF=photoF, websiteF=websiteF, addressF=addressF, userSelection=userSelection)
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
