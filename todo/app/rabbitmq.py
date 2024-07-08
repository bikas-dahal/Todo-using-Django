import pika 
import json 

def publish_message(message):
    params = pika.URLParameters('amqps://ydboxbsg:1qN22KC977DbRznZLWtS_r5JsJYuhx18@lionfish.rmq.cloudamqp.com/ydboxbsg')
    
    connection = pika.BlockingConnection(params)
    
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    data = {
        'message': message,
        'email': 'your_email@example.com'
    }
    channel.basic_publish(exchange='', routing_key='hello', body=json.dumps(data))
    
    channel.close()
    