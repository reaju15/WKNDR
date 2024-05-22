# WKNDR: Emotion-Based Recommendations

Welcome to WKNDR! Our web application provides personalized recommendations for experiences and activities based on how you're feeling. By leveraging Google Places API and Google Maps API, we offer curated suggestions that align with your current mood, ensuring you find the perfect experience every time.


## About

Experience Finder was created as part of an entrepreneurship program aimed at developing innovative solutions to improve daily life. Our mission is to help users discover activities and places that match their emotional state, making every experience enjoyable and fulfilling.

## Features

- **Emotion-Based Recommendations**: Get suggestions for activities based on your current mood.
- **Google Places Integration**: Access a wide range of places and activities using Google Places API.
- **Interactive Maps**: Visualize recommended places on an interactive map with Google Maps API.
- **User-Friendly Interface**: Easy-to-use interface for a seamless experience.
- **Mood History**: Track your moods and the activities you enjoyed over time.

## Getting Started

### Prerequisites

To run WKNDR locally, you'll need:

- Node.js (v14.0.0 or higher)
- npm (v6.0.0 or higher)
- Google Places API Key
- Google Maps API Key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/reaju15/WKNDR.git
   cd WKNDR
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your Google API keys:
     ```plaintext
     GOOGLE_PLACES_API_KEY=your_google_places_api_key
     GOOGLE_MAPS_API_KEY=your_google_maps_api_key
     ```

4. Run the application:
   ```bash
   npm start
   ```

5. Open your web browser and go to `http://localhost:3000`.

## Usage

1. **Log In**: Create an account or log in using your credentials.
2. **Select Emotion**: Choose your current emotion from the provided options.
3. **Get Recommendations**: Click the "Find Experiences" button to receive a list of recommended activities and places.
4. **View on Map**: See the suggested places on an interactive map.
5. **Save Favorites**: Save your favorite recommendations for future reference.


## Contributing

We welcome contributions to enhance WKNDR. To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add new feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.


For any questions or inquiries, please contact us at reaj@devverse.net or visit our website at [www.devverse.net](https://www.devverse.net).

---

Thank you for using WKNDR! We hope our app helps you discover amazing experiences that perfectly match your mood.
