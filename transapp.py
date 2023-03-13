import requests
import json

def main():
    corr = "Correct this to standard English: \n"
    bot_ans=""
    while True:
        sent = ' ನಾನು ವಿದ್ಯಾರ್ಥಿ' #input("Enter your sentence: ")
        payload = {"response":sent,"source":'kn'}
        json_object = json.dumps(payload, indent = 4)
        response_API = requests.post("http://13.234.202.158:4000/rest/webhook",data=json_object)
        res_dic = response_API.json()
        print(res_dic["bot"])
    
main()