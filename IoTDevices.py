import boto3
import datetime
import random

sqs = boto3.resource('sqs', endpoint_url='http://localhost:4566')

shops = [('Carpisa', 5), ('Adidas', 8), ('Carrefour', 6), ('Sephora', 7), ('Zuiki', 8)]

for shop, max_capacity in shops:
	queue = sqs.get_queue_by_name(QueueName=shop)
	measure_date = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	
	people = random.randint(0, 1000)
	msg_body = '{"shop": "%s","measure_date": "%s","people": "%s","sensor_type": "%s"}' % (shop, measure_date, str(people), "in")
	print(msg_body)
	queue.send_message(MessageBody=msg_body)
	
	people2 = random.randint(people - max_capacity, people)
	msg_body2 = '{"shop": "%s","measure_date": "%s","people": "%s","sensor_type": "%s"}' % (shop, measure_date, str(people2), "out")
	print(msg_body2)
	queue.send_message(MessageBody=msg_body2)