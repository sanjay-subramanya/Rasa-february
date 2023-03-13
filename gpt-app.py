import requests
import json

def main():
    corr = "Correct this to standard English: \n"
    bot_ans=""
    while True:
        sent = input("Enter your sentence: ")
        res = corr + sent
        payload = {"response":res,"bot":bot_ans}
        json_object = json.dumps(payload, indent = 4)
        response_API = requests.post("http://15.207.20.219:5000/rest/webhook",data=json_object)
        res_dic = response_API.json()
        print(res_dic["bot"])
    
main()