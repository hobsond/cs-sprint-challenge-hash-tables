# File Finder

Given a list of full paths to files, and a list of filenames to query,
report all the full paths that match that filename.

Example input:

```python
paths = [
    "/usr/local/share/foo.txt",
    "/usr/bin/ls",
    "/home/davidlightman/foo.txt",
    "/bin/su"
]
# string reversier
# create a variable current that ''
# create a variable boolean that says i got my current
# loop through each letter add it to that string
# if the item / addit to the cache ass the key 
# save copy as a variable 
# change boolean varaiable to true and loop through the rest 
# ill set the current back to ''
# if the item > len of the string than the coppy of the current key = the now current

queries = [
    "ls",
    "foo.txt",
    "nosuchfile.txt"
]
```

Example return value:

```
[ "/usr/local/share/foo.txt", "/usr/bin/ls", "/home/davidlightman/foo.txt" ]
```

because that's where the `foo.txt` and `ls` files are. 

The file `"nosuchfile.txt"` is ignored because it's not in the `paths`.

Return list can be in any order.

Limits:

* Up to approximately 1,000,000 paths.
* Up to approximately 1,000,000 queries.
