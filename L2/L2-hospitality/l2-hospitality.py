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
        ques=["How many customers are at the table","How many are vegetarians?","How many are non-vegetarians?","What is the order for soup?","How many veg starters were ordered?","How many non-veg starters were were ordered?","How many pizzas do they want?","What is the size of the pizzas?","Is there any specific ingredient to avoid on the pizza?","What do they want immediately?"]

    #answers
        ans=[["five", "5"],["3" , "three"],["2" , "two"],["three by five veg clear" , "three veg clear" , "three soups" , "three by five"],["1" , "one"],["1" , "one"],["3" , "three"],
        ["veg large" , "large", "big"],["avoid mushrooms" , "mushrooms"],["soup & starters" , "soups" , "starters" , "soup and starters"]]
        
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
     app.run(host = '0.0.0.0', port = 6000)