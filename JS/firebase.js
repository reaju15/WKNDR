 
 // Import the functions you need from the SDKs you need
 import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.6/firebase-app.js";
 import { getDatabase, ref, set } from "https://www.gstatic.com/firebasejs/9.6.6/firebase-database.js";

 import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.6.6/firebase-analytics.js";
 // TODO: Add SDKs for Firebase products that you want to use
 // https://firebase.google.com/docs/web/setup#available-libraries

 // Your web app's Firebase configuration
 // For Firebase JS SDK v7.20.0 and later, measurementId is optional
 const firebaseConfig = {
   apiKey: "AIzaSyD5Fz9NuZCNetEg-urRJcAGoUY2maBJtD0",
   authDomain: "wkndr-2b16e.firebaseapp.com",
   projectId: "wkndr-2b16e",
   storageBucket: "wkndr-2b16e.appspot.com",
   messagingSenderId: "360092113935",
   appId: "1:360092113935:web:a2aa812a0a4d5fe538977a",
   measurementId: "G-TM923CGGBG"
 };

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

const database = getDatabase(app);


 addBtn.addEventListener('click', (e) => {
          
  
    const toSendToFirebaseObject = {
      place_name: form.querySelector('#name').value, 
      web: form.querySelector('#web').value, 
      photo_link: form.querySelector('#photo').value, 
      Address: form.querySelector('#address').value, 
      user_selection: form.querySelector('#userSelection').value, 
      howEasy: form.querySelector("#howEasy").value,
      recommend_Wkndr: form.querySelector('#recommend').value,
      resultsSatisfaction: form.querySelector("#resultsSatisfaction").value,
      improvements: form.querySelector('#improvements').value,
      email: form.querySelector("#email").value,
      userLocation: form.querySelector("#userLocation").value
    }



    e.preventDefault();
    var id = "id:" + Math.random().toString(16).slice(2)

    set(ref(database, "NewShortSurvey/" + id ), {
        toSendToFirebaseObject
    })
    .then(() => {
      // Data saved successfully!
      window.location.href= "https://zsyp4s7b3q.us-east-1.awsapprunner.com/thankyou";
        console.log('success');
    })
    .catch((error) => {
      console.log('Data could not be saved.' + error);
      // The write failed...
    });


  });

