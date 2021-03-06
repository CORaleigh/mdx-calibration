import argparse
import threading
import logging
import time
import json
from kafka import KafkaConsumer, KafkaProducer

class Consumer(threading.Thread):
    daemon = True
    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=["10.160.103.165:9092"],
                                 auto_offset_reset='earliest',
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        consumer.subscribe(['parsed-mdx-raw'])
        for message in consumer:
            print (message)

def main():
    threads = [
        # Producer(),
        Consumer()
    ]
    for t in threads:
        t.start()
    time.sleep(10)
if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:' +
               '%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()
