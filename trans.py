from googletrans import Translator
import json
from flask import Flask,render_template,request,redirect,session,jsonify

app = Flask(__name__)

@app.route('/rest/webhook', methods=['POST', 'GET'])
def tran():
    if request.method == 'POST':
        obj = request.get_json(force=True, silent=False, cache=True)
        text = obj["response"]
        lang = obj["source"]
        # create an instance of the Translator class
        translator = Translator()

        # translate text from English to Spanish
        result = translator.translate(text, src = lang, dest='en')

        obj["bot"] = result.text
        
        json_object = json.dumps(obj, indent = 4)
        return json_object 
    
    elif request.method == 'GET':
        return "Translation running successfully"
    
    
if __name__ == "__main__":
     app.run(host = '0.0.0.0', debug = True, port= 4000)