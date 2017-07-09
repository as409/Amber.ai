# Write or paste code here. You can also use the blueprints as a starting point.
# -*- coding: utf-8 -*-
import requests
from meya import Component


class hotel(Component):

    def start(self):
        url = "http://api-sandbox.grnconnect.com/api/v3/hotels/availability"
        payload = "{\n \"destination_code\": \"C!000555\",\n \"checkin\": \"2017-12-29\",\n \"checkout\": \"2017-12-30\",\n \"client_nationality\": \"IN\",\n \"response\": \"fast\",\n \"currency\": \"INR\",\n \"rates\": \"comprehensive\",\n \"hotel_category\": [2, 6],\n \"rooms\": [\n {\n \"adults\": 1\n },\n {\n \"adults\": 2,\n \"children_ages\": [3]\n }\n ]\n}"
        headers = {
            'api-key': "a39c066189fc089c48908554c59f8c21",
            'content-type': "application/json",
            'accept': "application/json",
            'cache-control': "no-cache",
            'postman-token': "2c0f1442-19fc-2cc3-8bfd-efcb806d23a7"
            }
        response = requests.request("POST", url, data=payload, headers=headers)
        text= response.json()['hotels'][0]['rates'][0]['price']
        message= self.create_message(text=str(text))
        return self.respond(message=message, action='next')
        
        
        
        
        '''text = response.json()['hotels'][0]['rates'][0]['price']
        message = self.create_message(text=text)
        return self.respond(message=message, action="next")
        
        
        #response = requests.get("http://api.icndb.com/jokes/random")
        #text = response.json()['value']['joke']
        #message = self.create_message(text=text)
        #return self.respond(message=message, action="next")'''