# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    
    return response

@app.route("/")
def render_index_page():
   
    return render_template('index.html')

if __name__ == "__main__":
   
    app.run(host="0.0.0.0", port=5000)