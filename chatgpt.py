# import openai
# import json
# from flask import Flask,render_template,request,redirect,session,jsonify

# app = Flask(__name__)

# @app.route('/rest/webhook', methods=['POST', 'GET'])
# def gram():
    
    # if request.method == 'POST':
        # openai.api_key = "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"
        # obj = request.get_json(force=True, silent=False, cache=True)
        # text = obj["response"]
        # response = openai.Completion.create(
            # engine = "text-davinci-003",
            # max_tokens = 80,
            # temperature = 0.7,
            # prompt = text,
            # frequency_penalty = 0,
            # presence_penalty = 0)
        # obj["bot"] = response.choices[0].text
        # json_object = json.dumps(obj, indent = 4)
        # return json_object 
    
    # elif request.method == 'GET':
        # return "Grammar app running successfully"

# if __name__ == "__main__":
     # app.run(host = '0.0.0.0', debug = True, port =5000)


import openai

openai.api_key = "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"
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": "Tell me a funny biology story that I can tell my friends"}]
)

print(completion)