import random
import json
from flask import Flask,render_template,request,redirect,session,jsonify
app = Flask(__name__)


@app.route('/rest/webhook',methods=['POST'])
def home():

    # asking the user questions
    if request.method == 'POST':
    
        obj = request.get_json(force=True, silent=False, cache=True)
        text = str(obj["answer"]).lower()
        num = obj["ques_no"]
        
        ques=["What is the customer’s name ?","How old is the customer ? ","Where is the customer working ?","What is his profession ?","What does the customer want to open ?","What features does he want to know about ?","Are they looking to purchase any insurance policy ?","How old is the customers wife ? ","What does the customer's wife do ?","How many children does the customer have ?","How old are the children ?","What recommendation are they looking for ?"]
        
        ans=[["jay"],["36" ,"thirty", "six", "thirtysix"],["chennai" ,"multinational", "mnc"],["software","engineer"],["joint", "account","jointaccount"],["special"],["yes", "yeah", "of course", "yep"],
            ["32","thirty two"],["designer", "design"],["2","two"],["4","8", "four"],["good", "policy","hospitalization","needs"]]
        
        print(num)
        
        flag = 0
        if len(num) == 1:
            obj["remark"] = "Okay, let us begin."
            obj["bot"] = ques[num[0]]
            json_object = json.dumps(obj, indent = 4)
            return json_object
       
        user_ans = text.split()
        
        print(user_ans)
        for k in ans[num[0]]:
            # print(ans[num[0]])
            print(k)
            if k in user_ans:
                flag = 1
                obj["score"] = 1
                #print(obj["score"])
                obj["remark"] = "You got the correct answer!"
                obj["bot"] = ques[num[1]]
                json_object = json.dumps(obj, indent = 4)
                return json_object
      
        if flag == 0:
            obj["remark"] = "Sorry, that is incorrect."
            obj["score"] = 0
            # print(obj["score"])
            obj["bot"] = ques[num[1]]
            json_object = json.dumps(obj, indent = 4)
            return json_object                 


if __name__ == "__main__":
     app.run(host = '0.0.0.0', port = 5000)

