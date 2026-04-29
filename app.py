import os
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather
import google.generativeai as genai

# 1. वेब सर्वर चालू करें
app = Flask(__name__)

# 2. Gemini API सेटअप करें (चाबी हम पर्यावरण चर यानी Environment Variables से लेंगे)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """जब भी कोई आपके नंबर पर कॉल करेगा, तो यह कोड चलेगा।"""
    response = VoiceResponse()

    # अगर कॉलर ने कुछ बोला है, तो उसे यहाँ पकड़ें
    if 'SpeechResult' in request.values:
        user_speech = request.values['SpeechResult']
        
        # Gemini को बताएँ कि उसे कैसे व्यवहार करना है
        system_instruction = "तुम मुकेश भाई और KRYA ब्रांड के एक बहुत ही विनम्र और मददगार AI असिस्टेंट हो। तुम फ़ोन कॉल पर बात कर रहे हो। हमेशा हिंदी में छोटे, स्पष्ट और प्राकृतिक (natural) तरीके से जवाब दो।"
        ai_prompt = f"{system_instruction}\nकॉलर का सवाल: {user_speech}"
        
        # Gemini से जवाब लें
        ai_response = model.generate_content(ai_prompt)
        reply_text = ai_response.text

        # जवाब को आवाज़ में बोलें (Aditi एक भारतीय हिंदी आवाज़ है)
        response.say(reply_text, voice='Polly.Aditi')

    # कॉलर की आवाज़ सुनने के लिए 'Gather' का इस्तेमाल करें
    gather = Gather(input='speech', action='/voice', language='hi-IN', speechTimeout='auto')
    
    # अगर यह पहली बार कॉल उठी है, तो आपका Welcome Message बोलें
    if 'SpeechResult' not in request.values:
         gather.say("नमस्ते! मैं मुकेश भाई का एआई असिस्टेंट बोल रहा हूं । मैं आपकी कैसे मदद कर सकता हूँ?", voice='Polly.Aditi')
         
    response.append(gather)

    # अगर कॉलर चुप रहे, तो कॉल कटने न दें, वापस लूप में भेजें
    response.redirect('/voice')

    return str(response)

if __name__ == "__main__":
    # यह सर्वर को लगातार चालू रखेगा
    app.run(host='0.0.0.0', port=8080)
  
