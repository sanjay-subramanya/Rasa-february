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
    
    para = "Hi. 3 of us are veg and 2 non-veg. We would like to order 3 by 5 veg clear soup, 1 veg starter, 1 non-veg starter and 3 veg large pizzas. Please do not put mushrooms and we prefer something spicy. Please bring us soup and starter immediately as we are very hungry."
    print(para)
    
    while i <= thres:
    
        rand = random.randint(0,9)
        
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