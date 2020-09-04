#  Hint:  You may not need all of these.  Remove the unused functions.
import random
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length,):
    """
    YOUR CODE HERE
    """
    # Your code here
    # loop through the list of tickedts
    # count keep track of the amount of items in the history
    # iniriate the cache 
    cache = {}
    used=[]
    history = []
    count = 0
    while len(cache) <= length :
        try:
            cache[tickets[count].source] = tickets[count].destination
            count+=1
        except:
            print(count)
            break
        continue
    print(cache)
    history.append('NONE')
    while len(history) <= length:
                
        x = history[-1]
        print(x)
        y = cache[x]
        history.append(y)
        count += 1
        continue
    
    return(history[1:])
    # reconstruct_trip(tickets,length,cache,history,count)
    
        
    
        
ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]


reconstruct_trip(tickets,3)
