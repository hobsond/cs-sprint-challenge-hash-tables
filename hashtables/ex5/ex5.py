# Your code here

cache={}
def seeder(files):
    for i in files:
        j = i.split("/")
        x = j[-1]
        if x not in cache:
            cache[x] = [i]
        else:
            cache[x].append(i)
        
    
def finder(files, queries):
    """
    YOUR CODE HERE
    """
    seeder(files)
    
    x = []
    for i in queries:
        if i  in cache:
            for h in cache[i]:
                x.append(h)
        
    # Your code here
    # string reversier
# string reversier
# create a variable current that ''
# loop through each letter add it to that string
    return x
# if the item / addit to the cache ass the key 
# save copy as a variable 
# change boolean varaiable to true and loop through the rest 
# ill set the current back to ''
# if the item > len of the string than the coppy of the current key = the now current
    


if __name__ == "__main__":
    files = [
        '/bin/foo.txt',
        '/bin/bar',
        '/bin/foo.txt',
        '/usr/bin/baz'
    ]
    queries = [
        "foo.txt",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
