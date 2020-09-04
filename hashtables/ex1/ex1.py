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
    mem = set()
    
    while len(cache) < length* length :
       
        if count >= length:
            count = 0
            if start < length :
                start +=1
        
        try:
            added = weights[start] + weights[count]
            head=weights[start]
            tail=weights[count]
       
            if added not in cache :
                if count == start:
                    count +=1
                    continue
                cache[added] = [[count,start]]
                mem.add((count,start))
            else:
                if (start,count) not in mem:
                    cache[added].append([count,start])
                    mem.add((count,start))
            count +=1
        except IndexError:
            break
        
        continue
            
        
    
    try:
        return cache[limit][0]
    except :
        return None
    


we = [ 4, 6, 10, 15, 16 ]
leng = 5
lim = 21
weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
print(get_indices_of_item_weights(weights_4, 9, 7))

weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
print(answer_2)