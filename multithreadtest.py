###Practice of 3 new elements:
#Random number generation
#SHA cryptography
#Multithreading

import datetime
from threading import Thread
import time
import random
import hashlib


number_of_threads = 5000
random_list = list()
encrypted_list = list()


def fill_random_list(iterations):

    for i in range(iterations):
        random_list.append(random.randint(1,9999))

    return

def method(inputvalue):

    time.sleep(5)
    encrypted_list.append(hashlib.sha256(str(inputvalue)).hexdigest())

    return

def multithread_method(inputlist, threadno):
    for i in inputlist:
        time.sleep(5)
        encrypted_list.append(hashlib.sha256(str(i)).hexdigest())
        print 'Inserida uma entrada com sucesso!'

    return



def baseline():

    total_time = 0

    for i in random_list:
        print('Testing {} without  threading'.format(random_list.index(i)+1))
        start = datetime.datetime.now()
        method(i)
        end = datetime.datetime.now()
        timespan = (end-start).seconds
        total_time += timespan
        print('Singlethread test of {} complete in {} seconds\n'.format(random_list.index(i)+1, timespan))

    return total_time




def multithreading():

    start = datetime.datetime.now()

    inteiro = len(random_list) // number_of_threads
    resto = len(random_list) % number_of_threads

    threadlist = list()

    for i in range(resto):
        inputlist = list()
        for y in range(inteiro+1):
            inputlist.append(random_list.pop())
        tx = Thread(target=multithread_method, args=(inputlist,i))
        tx.start()
        threadlist.append(tx)
    for i in range(number_of_threads-resto):
        inputlist = list()
        for y in range(inteiro):
            inputlist.append(random_list.pop())
        tx = Thread(target=multithread_method, args=(inputlist, inteiro+i))
        tx.start()
        threadlist.append(tx)

    for tx in threadlist:
        tx.join()

    end = datetime.datetime.now()
    total_time = (end - start).seconds

    return total_time




def main():

    iterations = int(input('How many times do you want to iterate and test threading performance?:\n'))
    # number_of_threads = int(input('And how many threads  do you want to run simultaneously?:\n'))

    fill_random_list(iterations)

    print('Starting synchronous baseline test...\n')
    # baseline_timespan_milliseconds = baseline()
    #print('Finished synchronous baseline test. It took {} seconds\n'.format(baseline_timespan_milliseconds))

    print 'Results from synchronous method:'
    for i in encrypted_list:
        print i

    time.sleep(3)

    print('\n\n\nStarting async test...\n')
    multithread_timespan_milliseconds = multithreading()
    print('Finished async test. It took {} seconds\n'.format(multithread_timespan_milliseconds))


    print 'Results from async method:'
    for i in encrypted_list:
        print i

    print 'THE END!'

    return



########## ENTRY POINT ##########
main()
########## ENTRY POINT ##########