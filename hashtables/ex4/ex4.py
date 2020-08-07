def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create a variable for dictionary
    cache={}
    stack=[]
    # loop through the list items
    for i in a:
    # if item is greater than 0 i will check to see if its in the dictionary
        if i > 0:
            if i not in cache:
    # if its not in the dictionary i will add that key and = 0 
                cache[i] = 0
            else:
                cache[i]+=1
    # if its less than 0 i ill take value
        if i < 0:
    # and inverse and if ithe item is in the dictionary
            x = i * -1
            if x in cache:
    # then ill add that key += 1
                cache[x] +=1
            else:
                cache[x]= 0
    # loop through the catch if key value > 0 the n append the key
    # to an array
    # return array
    for i in cache.items():
        if i[1] ==1:
            stack.append(i[0])
    
    
    
    
     
    
    

    return stack


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
