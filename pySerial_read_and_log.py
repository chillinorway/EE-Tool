# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:56:31 2022

@author: Aleksander
"""

from threading import Thread
from queue import Queue
import keyboard

import datetime
import serial

import csv

time_now = datetime.datetime.now().strftime("%y%m%dT%H%M%S")


# producer task
def producer(queue):
    for i in range(1):
        with serial.Serial('COM4', 115200, timeout=1) as ser:
            ser.flushInput()
            print('Producer: Running')
            while True:
                if keyboard.is_pressed('q'):
                    break   
                # line = ser.read_until(b'\xbb')
                line = ser.read(1000)
                # line = bytes.hex(line, ' ')
                # add to the queue
                queue.put(line)
            # signal that there are no further items
            queue.put(None)
            print('Producer: Done')
 
# consumer task
def consumer(queue):
    for i in range(1):
        with open(f"{time_now}.csv", "a", newline="") as f:
            writer = csv.writer(f, delimiter=" ")
            print('Consumer: Running')
            # consume items
            while True:
                # get a unit of work
                item = queue.get()
                writer.writerow(item)
                # check for stop
                if item is None:
                    break
            # all done
            print('Consumer: Done')
 
# create the shared queue
queue = Queue()
# start the consumer
consumer = Thread(target=consumer, args=(queue,))
consumer.start()
# start the producer
producer = Thread(target=producer, args=(queue,))
producer.start()
# wait for all threads to finish
producer.join()
consumer.join()