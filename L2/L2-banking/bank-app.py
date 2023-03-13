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
    
    para = "Hi, my name is Jay. I am 36 years old and working as a software engineer in Chennai for a multinational company. I want to open a joint account with my wife for our savings. Does your bank offer any special features for savings account holders? Also, I want to purchase a medical insurance policy for my family. My wife is 32 years old and she is a designer. My daughter is 8 years old and my son is 4 years old. Can you please recommend a good policy which will take care of all our hospitalization needs?. I hope you are ready for the questions."
    print(para)
    
    while i <= thres:
    
        rand = random.randint(0,11)
        
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
                if i == thres+1:
                    break
                print(res_dic["bot"])
                act.append(res_dic["score"])
            
    print(f"Final score: {act.count(1)} / {thres}")
    
notmain()