#  Hint:  You may not need all of these.  Remove the unused functions.
import random
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length,cache=None,history=None,count =None,):
    """
    YOUR CODE HERE
    """
    # Your code here
    # loop through the list of tickedts
    # count keep track of the amount of items in the history
    if count is None:
        count = 0
    # iniriate the cache 
    if cache is None:
        cache = {}
        # add the tickets into the cache
        for i in tickets:
            if i['source'] == "NONE":
                cache['start'] = i['destination']
                continue
            if i['destination'] == 'NONE':
                cache[i['source']] = 'end'
                continue
            
            cache[i['source']] = i['destination']
   
    if history is None:
        history = []
    
    if count == length + 1:
        
        history = history[1:-1]
        print(history)
        return
        

    if len(history) == 0:
        history.append('start')
        count +=1
        
            
    if len(history) > 0:
        x = history[-1]
        y = cache[x]
        history.append(y)
        count += 1
        
    reconstruct_trip(tickets,length,cache,history,count)
        
    
        
    
        
        
        
        


tickets = [
    { "source": "PIT", "destination": "ORD" },
    
    { "source": "XNA", "destination": "CID" },
    { "source": "SFO", "destination": "BHM" },
    { "source": "FLG", "destination": "XNA" },
    { "source": "NONE", "destination": "LAX" },
    { "source": "LAX", "destination": "SFO" },
    { "source": "CID", "destination": "SLC" },
    { "source": "ORD", "destination": "NONE" },
    { "source": "SLC", "destination": "PIT" },
    { "source": "BHM", "destination": "FLG" }
]


reconstruct_trip(tickets,len(tickets))
