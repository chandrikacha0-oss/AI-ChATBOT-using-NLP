from flask import Flask,render_template,request,jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()
app=Flask('__name__')
CORS(app)

SC_API_KEY ="AIzaSyDLbRod6eIfd-VJIp__rr5m7sFM_jgce-s"
genai.configure(api_key=SC_API_KEY)


model=genai.GenerativeModel("models/gemini-2.5-flash")
chat=model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat',methods=['POST'])
def chat_response():
    userMsg=request.json.get('message',"")

    if not userMsg:
        return jsonify({"bot_reply":"plzz type something"}),400
       
    try:
        response=chat.send_message(userMsg)

        bot_reply=response.text
        return jsonify({"bot_reply":bot_reply})
    
    except Exception as e:
        print(f"Error:{e}")
        return jsonify({"bot_reply":"Error: "+  (str(e))}),500

if __name__=="__main__":
    app.run(debug=True)
