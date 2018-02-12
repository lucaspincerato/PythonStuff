#Python script for comparing performance (exec time) between two elasticsearch queries
import datetime
import requests

elastichosturl = 'http://localhost:9200/courses/_search'

old_query = '''
{
  "query": {
    "bool": {
          "must": [
            {"match": {"professor.name": "bill"}},
            {"match": {"name": "accounting"}}
            ]
    }
  }
}
'''

new_query = '''
{
  "query": {
    "bool": {
      "filter": {
        "bool": {
          "must": [
            {"match": {"professor.name": "bill"}},
            {"match": {"name": "accounting"}}
            ]
        }
      }
    }
  }
}
'''


def query(query):

    initial_timestamp = datetime.datetime.now()

    response = requests.get(elastichosturl, query)

    final_timestamp = datetime.datetime.now()

    timespan = (final_timestamp - initial_timestamp)
    miliseconds = timespan.microseconds/1000

    return miliseconds



def test_both(iterations):

    total_time_old = 0
    average_time_old = 0
    total_time_new = 0
    average_time_new = 0
    number_of_improoved = 0

    for i in range(iterations):
        print(i)

        # old_query testing
        timespan_old = query(old_query)
        total_time_old += timespan_old
        average_time_old = (average_time_old+timespan_old)/2


        # new_query testing
        timespan_new = query(new_query)
        total_time_new += timespan_new
        average_time_new = (average_time_new+timespan_new)/2

        result_out = 'Worse'

        if timespan_new < timespan_old:
            number_of_improoved+=1
            result_out = 'Better'

        print('timespan_old: {} miliseconds\ntimespan_new: {} miliseconds\n{}\n\n'.format(timespan_old, timespan_new, result_out))

    results = {
            "total_time_old": total_time_old,
            "average_time_old":average_time_old,
            "total_time_new": total_time_new,
            "average_time_new": average_time_new,
            "average_delta": average_time_new-average_time_old,
            "total_delta": total_time_new-total_time_old,
            "number_of_improoved": number_of_improoved
        }

    return results



def main():

    iterations = int(input('How many times do you want to query_test?:\n'))

    results = test_both(iterations)

    print('The time_delta between queries were of: {} miliseconds\n{}/{} queries showed better performance'.format(results.get('total_delta'),results.get('number_of_improoved'), iterations))
    print('THE END!')

    return

########## ENTRY POINT ##########
main()
########## ENTRY POINT ##########