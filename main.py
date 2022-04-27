import backend as backend
from flask import Flask, render_template, request, redirect, url_for




app = Flask(__name__)


@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/interest', methods=['POST', 'GET'])
def main():
    userSelection = request.form.getlist('nm')
    userLocation = request.form.getlist('location')
    if request.method == 'POST':
        selectedData = backend.selected(userSelection, userLocation)

        results1 = selectedData[0]
        results2 = selectedData[1]
        results3 = selectedData[2]
        results4 = selectedData[3]
        results5 = selectedData[4]
        results6 = selectedData[5]
        results7 = selectedData[6]
        results8 = selectedData[7]
        results9 = selectedData[8]
        results10 = selectedData[9]
        results11 = selectedData[10]
        results12 = selectedData[11]

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

        openNow4 = results4["openNow"]
        address4 = results4["address"]
        placeName4 = results4["placeName"]
        photoLink4 = results4["photoLink"]
        webLink4 = results4["webLink"]

        openNow5 = results5["openNow"]
        address5 = results5["address"]
        placeName5 = results5["placeName"]
        photoLink5 = results5["photoLink"]
        webLink5 = results5["webLink"]

        openNow6 = results6["openNow"]
        address6 = results6["address"]
        placeName6 = results6["placeName"]
        photoLink6 = results6["photoLink"]
        webLink6 = results6["webLink"]

        openNow7 = results7["openNow"]
        address7 = results7["address"]
        placeName7 = results7["placeName"]
        photoLink7 = results7["photoLink"]
        webLink7 = results7["webLink"]

        openNow8 = results8["openNow"]
        address8 = results8["address"]
        placeName8 = results8["placeName"]
        photoLink8 = results8["photoLink"]
        webLink8 = results8["webLink"]

        openNow9 = results9["openNow"]
        address9 = results9["address"]
        placeName9 = results9["placeName"]
        photoLink9 = results9["photoLink"]
        webLink9 = results9["webLink"]

        openNow10 = results10["openNow"]
        address10 = results10["address"]
        placeName10 = results10["placeName"]
        photoLink10 = results10["photoLink"]
        webLink10 = results10["webLink"]

        openNow11 = results11["openNow"]
        address11 = results11["address"]
        placeName11 = results11["placeName"]
        photoLink11 = results11["photoLink"]
        webLink11 = results11["webLink"]

        openNow12 = results12["openNow"]
        address12 = results12["address"]
        placeName12 = results12["placeName"]
        photoLink12 = results12["photoLink"]
        webLink12 = results12["webLink"]
        

        return render_template('Results.html', 
        openNow3=openNow3, openNow2=openNow2, openNow1=openNow1, openNow4=openNow4, openNow5=openNow5, openNow6=openNow6, openNow7=openNow7, openNow8=openNow8, openNow9=openNow9, openNow10=openNow10, openNow11=openNow11, openNow12=openNow12,
        placeName1=placeName1, placeName2=placeName2, placeName3=placeName3, placeName4=placeName4, placeName5=placeName5, placeName6=placeName6, placeName7=placeName7, placeName8=placeName8, placeName9=placeName9, placeName10=placeName10, placeName11=placeName11, placeName12=placeName12,
        address1=address1, address2=address2, address3=address3, address4=address4, address5=address5, address6=address6, address7=address7, address8=address8, address9=address9, address10=address10, address11=address11, address12=address12, 
        photoLink1=photoLink1, photoLink3=photoLink3,  photoLink2=photoLink2, photoLink4=photoLink4,  photoLink5=photoLink5, photoLink6=photoLink6, photoLink7=photoLink7,  photoLink8=photoLink8, photoLink9=photoLink9,photoLink10=photoLink10, photoLink11=photoLink11,photoLink12=photoLink12,
        webLink2=webLink2, webLink1=webLink1, webLink3=webLink3, webLink4=webLink4, webLink5=webLink5, webLink6=webLink6, webLink7=webLink7, webLink8=webLink8, webLink9=webLink9,  webLink10=webLink10, webLink11=webLink11, webLink12=webLink12, 
        userSelection=userSelection, userLocation=userLocation)
        
    else:
        return render_template("Interest-page.html")
    
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

        return render_template('Experience-Description-page.html', finalselect=finalselect, name=nameF, photo=photoF, openNow=openNowF, hoursOp=hoursOpF, website=websiteF, address=addressF, userSelection=userSelection, userLocation=userLocation)

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

@app.route('/thankyou', methods = ["POST", "GET"])
def thankyou():

    return render_template("Thank-You-Page.html")
     
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
