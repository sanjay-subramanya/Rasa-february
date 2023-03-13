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
        ques=["What is the customer’s name?","What package do they want to book ?","How many family members are there?","How old is the daughter?","How old is the son?","Where does the customer live?","Where does the family want to go?","What is the duration of the package they are looking for?","On what dates do they want to travel?","What type of places do they want to visit?","Where do they want to stay?", "Which activity does the family like doing together?", "What is their budget?", "How do they want to travel?"]

        #answers
        ans=[["jay", "jai"],["family tour package", "family" ,"family package"],["4" ,"four"],["4" , "four", "four years old"],["8", "eight"],["chennai"],["mumbai" ,"goa", "bombay or goa", "bombay"],["four nights", "five days", "4 nights", "5 days"],
            ["13 to 20 january", "thirteenth january to twentieth january", "thirteenth to twentieth january", "thirteen", "twenty january"],["children friendly" , "fun activities"],["resorts or homestays" , "resorts" , "resort", "homestay"],["swimming"], 
            ["fifty thousand", "50 thousand"], ["flight", "air", "airplane", "fly"]]

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
     app.run(host = '0.0.0.0', port = 7000)