#Simple Developer Blog: www.simpledeveloper.wordpress.com
#Python code to make simple Twitter searches using
#user-entered arguments
#2013 - Mozilla P2PU Challenge - Programming with Twitter API

import json
import urllib2

def search_twitter(query):
    #take care of any possible exceptions from bad api calls
    url = 'http://search.twitter.com/search.json?q='+query         #add the query to the url
    try:
        tweets = urllib2.urlopen(url)                              #make the call to twitter
        parsed_data = json.load(tweets)                            #load using JSON
        return print_tweets(parsed_data)
    except urllib2.URLError, e:                                    #catch any errors that might occur
        print e.reason
        raise

#define our print_tweets() function
def print_tweets(data):
    i = 0
    while i < len(data['results']):                                           #use a while loop and a counter
        print '@%s tweeted: %s on %s' % (data['results'][i]['from_user'],     #access ['from_user'] data
                                         data['results'][i]['text'],          #access ['text'] data
                                         data['results'][i]['created_at'])    #access ['created_at'] data
        i += 1                                                                #Increment the counter here

#Call the function and see the results
if __name__ == '__main__':
    while True:
        query = raw_input("Enter a search term:")                  #prompt the user for a search term
        if not query:                                              #if no term, break, else
            break
        search_twitter(query)                                      #call the function and get the result

    
    
