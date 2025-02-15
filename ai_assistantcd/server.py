from flask import Flask, request, jsonify
import webbrowser
import platform
import os

app = Flask(__name__)

# YouTube Links
YOUTUBE_LINKS = {
    "education": "https://youtu.be/KWSa4gYpDUY?si=GBr0D9xutY2f5STd",
    "banking": "https://youtu.be/eEiTgnA4JuU?si=HF0y-OX4rLgMvGAJ"
}

@app.route('/open_youtube', methods=['GET'])
def open_youtube():
    category = request.args.get("category")
    if category in YOUTUBE_LINKS:
        webbrowser.open(YOUTUBE_LINKS[category])  # Opens the YouTube video in browser
        return jsonify({"message": "YouTube वीडियो खोला गया"})
    else:
        return jsonify({"error": "कोई वीडियो नहीं मिला"})

@app.route('/call_kuldeep', methods=['GET'])
def call_kuldeep():
    phone_number = "+918103281771"  # Replace with actual number
    
    if platform.system() == "Windows":
        os.system(f'start tel:{phone_number}')  # For Windows
    elif platform.system() == "Darwin":  # macOS
        os.system(f'open tel:{phone_number}')
    elif platform.system() == "Linux":
        os.system(f'xdg-open tel:{phone_number}')
    
    return jsonify({"message": "कुलदीप को कॉल किया जा रहा है"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)