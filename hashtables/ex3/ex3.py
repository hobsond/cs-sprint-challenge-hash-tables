
def intersection(arrays):
    cache = {}
    result = []
    """
    YOUR CODE HERE
    """
    # Your code here
    # create the dictionary 
    # we loop throuh arrays 
    # which we will h
    start =0
    check = 0 
    height = len(arrays)
    while start <= height:
        try:
            
            number = arrays[start][check] 
            if number not in cache:
                cache[number]= [start]
            else:
                cache[number].append(start)
                if len(cache[number]) == height:
                    result.append(number)
            check += 1 
        except:
            check = 0
            start += 1
        
        continue
    return result
   
   
    

if __name__ == "__main__":
    arrays = [
            [1,2,3],
            [1,4,5,3],
            [1,6,7,3]
        ]

    # arrays.append(list(range(100, 200)) + [1, 2, 3])
    # arrays.append(list(range(200, 300)) + [1, 2, 3])
    # arrays.append(list(range(300, 400)) + [1, 2, 3])
    print(intersection(arrays))
