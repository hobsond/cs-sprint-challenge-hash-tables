# Your code here

cache={}

def reverser(s):
    return s[::-1]

def seeder(files):
    current = ''
# loop through each letter add it to that string
    for i in files:
        
        i.split("/")
    
def finder(files, queries):
    """
    YOUR CODE HERE
    """
    seeder(files)
    x = []
    for i in queries:
        if i  in cache:
            x.append(cache[i][0])
        
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
        '/usr/bin/baz'
    ]
    queries = [
        "foo.txt",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
