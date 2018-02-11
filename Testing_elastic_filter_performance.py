#Python script for comparing performance (exec time) between two elasticsearch queries
import datetime
import statistics
import requests


elastichosturl = 'http://localhost:9200/'

old_query =
'''

'''

new_query =
'''
{
	"query":
	{
		"bool":{
			"filter"
		}
	}
}
'''


def query(query):

    initial_timestamp = datetime.datetime.now()



    final_timestamp = datetime.datetime.now()


    return



def test_both(iterations):

    total_time_old = 0
    average_time_old = 0
    total_time_new = 0
    average_time_new = 0

    for i in range(iterations):

        # old_query testing
        timespan_old = query(old_query)
        total_time_old += timespan_old
        average_time_old = statistics.mean(average_time_old,timespan_old)


        # new_query testing
        timespan_new = query(new_query)
        total_time_old += timespan_new
        average_time_old = statistics.mean(average_time_old,timespan_new)


    results = {
            "total_time_old": total_time_old,
            "average_time_old":average_time_old,
            "total_time_new": total_time_new,
            "average_time_new": average_time_new,
            "average_delta": average_time_new-average_time_old,
            "total_delta": total_time_new-total_time_old
        }

    return results



def main():
    print('How many times do you want to query_test?:\n')

    iterations = #input







########## ENTRY POINT ##########
main()
########## ENTRY POINT ##########