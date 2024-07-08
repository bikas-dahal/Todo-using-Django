import pika 
import json 

def email_sender(message):
    message = json.loads(message)
    email = message.get('email')
    data = message.get('data')
    print(email, data)

def callback(ch, method, properties, body): 
    # print(ch, method, properties, body)
    message = body.decode()
    print(message)

params = pika.URLParameters('amqps://ydboxbsg:1qN22KC977DbRznZLWtS_r5JsJYuhx18@lionfish.rmq.cloudamqp.com/ydboxbsg')
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
