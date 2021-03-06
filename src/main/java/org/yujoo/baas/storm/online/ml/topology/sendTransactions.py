import logging
import random
import sys
import uuid
import json

from kafka.client import KafkaClient, FetchRequest, ProduceRequest

def gen_row ():
    label = 0
    vals = []
    for i in range(0,4):
    	feature = random.randrange(1,1000)
    	vals.append(feature)
    vals.append(str(uuid.uuid1()).split("-")[0])
    return vals	
          
def send_order(kafka, content):
    message = kafka.create_message(json.dumps(content))
    request = ProduceRequest("transactions", -1, [message])
    kafka.send_message_set(request)  
            
if __name__ == '__main__':
    num_row = int(sys.argv[1])
    kafka = KafkaClient("localhost", 9092)
	
    for i in range(0, num_row):
        send_order(kafka, gen_row())