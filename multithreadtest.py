#Python script for comparing performance (exec time) between two elasticsearch queries
import datetime
from threading import Thread
import time

def baseline_method():
    time.sleep(2)
    return

def baseline(iterations):

    total_time = 0

    for i in range(iterations):
        print('Testing: {} without  threading'.format(i))
        start = datetime.datetime.now()
        baseline_method()
        end = datetime.datetime.now()
        timespan = (end-start).microseconds/1000
        total_time =+ timespan
        print('Singlethread test of {} complete in {} milliseconds\n'.format(timespan))

    return total_time


def multithreading(iterations):

    threads = 10
    total_time = 0

    threadlist = list()
    for i in range(threads):
        threadlist.append(Thread(target=baseline_method()))

    for i in range(iterations):
        print('Testing: {} with multithreading'.format(i))



        start = datetime.datetime.now()
        baseline_method()
        end = datetime.datetime.now()
        timespan = (end - start).microseconds / 1000
        total_time = + timespan



        print('Multithread test of {} complete in {} milliseconds\n'.format(timespan))

    return total_time

def main():

    iterations = int(input('How many times do you want to iterate and test threading performance?:\n'))

    print('Starting synchronous baseline test...\n')
    results = baseline(iterations)



    print('The time_delta between queries were of: {} miliseconds\n{}/{} queries showed better performance'.format(results.get('total_delta'),results.get('number_of_improoved'), iterations))
    print('THE END!')

    return

########## ENTRY POINT ##########
main()
########## ENTRY POINT ##########