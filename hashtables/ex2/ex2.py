#  Hint:  You may not need all of these.  Remove the unused functions.
import random
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length,cache=None,history=None,count =None,hash=None):
    """
    YOUR CODE HERE
    """
    # Your code here
    # loop through the list of tickedts
    
    if count is None:
        count = 0
        
    if cache is None:
        cache = {}
        for i in tickets:
            if i['source'] == "NONE":
                cache['start'] = i['destination']
                continue
            if i['destination'] == 'NONE':
                cache[i['source']] = 'end'
                continue
            
            cache[i['source']] = i['destination']
    
    if hash is None:
        hash= set()    
    
    if history is None:
        history = []
    
    if count == length:
        print(history)
    print(count)
    
    t = [i for i in cache.items()]
    
    choice = random.choice(t)
    while choice in hash:
        choice = random.choice(t)
    
    # print(choice)
    
    if len(history) == 0:
        history.append('start')
        print(f"{history} plugged in")
        hash.add('start')
        count +=1
        
        
    if len(history) > 0:
        x = history[-1]
        y = cache[x]
        # print(f'this is my choice {choice[0]}')
        # print(f'this would be the dest {y}')
        # print(f'this would be this is the source {x}')
        if choice[0] == y:
            history.append(choice[0])
            hash.add(choice[0])
            count +=1
        else:
            reconstruct_trip(tickets,length,cache,history,count,hash)


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


reconstruct_trip(tickets,9)
