def get_indices_of_item_weights(weights, length, limit,cache=None,count=None,start =None):
    """
    YOUR CODE HERE
    """
    # Your code here
    if cache is None:
        cache={}
    if count is None:
        count = 0
    if start is None:
        start = 0
    
    while len(cache) < length* length :
       
        if count >= length:
            count = 0
            if start < length :
                start +=1
        
        try:
            added = weights[start] + weights[count]
       
            if added not in cache:
                cache[added] = [(weights[start],weights[count])]
            # else:
            #     cache[added].append((weights[start],weights[count]))
            count +=1
        except IndexError:
            break
        
        continue
            
        
    
    print(cache[limit])
    


we = [ 4, 6, 10, 15, 16 ]
leng = 5
lim = 21
get_indices_of_item_weights(we,leng,lim)