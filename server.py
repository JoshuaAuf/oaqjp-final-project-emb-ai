"""
This module implements the server-side logic for the Emotion Detector application.
It provides a RESTful API for detecting emotions in text and returns the results
as a JSON response.
Author: Joshua Aufderheide
Date: 03/05/2025
"""
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def sent_detector():
    """
    Handles the /emotionDetector endpoint.
    Retrieves the text to analyze from the request arguments, passes it to the
    emotion_detector function, and returns the response.
    Returns:
        str: The response from the emotion_detector function.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and " 
        f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )
    if dominant_emotion is None:
        return "Invalid text! Please try again."
    return formatted_response
@app.route("/")
def render_index_page():
    """
    Handles the / endpoint.
    Renders the index.html template and returns it as the response.
    Returns:
        str: The rendered index.html template.
    """
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
