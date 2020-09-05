def has_negatives(a):
    """
    YOUR CODE HERE
    """
    table = set()
    savior = []
    count = 0
    while len(table) <= len(a):
        try:
            
            x = a[count]
            num = x *-1
            if x not in table :
                if x<0 and num in table:
                    savior.append(num)
                elif x>0 and num in table:
                    savior.append(x)   
                table.add(x)
                
        except:
            break
          
        count += 1
        continue
    return savior
        
   


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
