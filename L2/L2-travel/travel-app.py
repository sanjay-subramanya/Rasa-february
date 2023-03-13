import requests
import json
import random

def notmain():
    thres = 6
    bot_ques = ""
    remark = ""
    asked = []
    score = 0
    act = []
    num = []
    i = 0
    
    para = "Hello, my name is Jay. I want to book a family tour package for me, my wife, 8 year old son and 4 year old daughter. We live in Chennai and want to explore Bombay or Goa for 4 nights and 5 days. I have applied for leave between 13th January and 20th January. We want to visit places which are children-friendly with fun activities for them. We want to stay only in resorts or homestays which have a swimming pool, as we all like swimming. Our budget is 50,000 rupees only and we would like to travel only by flight. Can you please suggest a suitable package for us?"
    print(para)
    
    while i <= thres:
    
        rand = random.randint(0,13)
        
        if rand not in asked:        
            if len(num) < 2:
                num.append(rand)
            else:
                num[0], num[1] = num[1], rand
                
            if num[-1] not in asked:
                asked.append(num[-1])
                i += 1           
                ans = input("Answer: ")
                ans = ans.lower()
                payload = {"answer":ans, "ques_no": num, "score": score, "remark": remark, "bot": bot_ques}
                
                json_object = json.dumps(payload, indent = 4)
                response_API = requests.post("http://13.234.202.158:7000/rest/webhook", data=json_object)
                res_dic = response_API.json()
                # if i == thres+1:
                    # break
                print(res_dic["remark"])
                act.append(res_dic["score"])
                if i != thres+1:
                    print(res_dic["bot"])
                
            
    print(f"Final score: {act.count(1)} / {thres}")
    
notmain()