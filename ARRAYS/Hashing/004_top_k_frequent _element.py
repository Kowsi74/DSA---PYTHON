"""
    this problem is asked about to return a top k frequent elements in tha array . so it has the key work frequency
    we have to think about hashing.so frst we have to create a dic and iterate the num .
    if the num is already there we will increase a count else we add on it. after this 
    we using sorting using keys bcaz we need key as a output so but based on values(frequency) so
    we will use lambda function here we make reverse = true which arrange this in desc order.
    finally we return using slice the array with k value. it takes o(n log n ) in time and o(n) in space.
"""

def top_frequency(nums,k):
    seen = {}
    for num in nums:
        if num in seen :   
            seen[num] += 1 
        else:
            seen[num] = 1
    frequency_element = sorted(seen.keys() , key=lambda x : seen[x] , reverse = True)
    return frequency_element[:k]

"""
    now we are optimize it using bucket sort . so bucket sort is the algorithm which works like
    sperating everything in buckets and sort them and give back that . actually think about exam 
    paper distribtion in classroom . okay so frat we create dic and store those index with frequency
    after this we create a bucket for storing . and we append it. then we iterate through bucket
    from last(reverse) we can append those things while checking if the particular list is equal to
    the result we will return res it take o(n) in time and o(n)  in space
"""

def frequency(nums,k):
    seen = {}
    for num in nums:
        if num in seen:
            seen[num] += 1   # seen[num] = seen.get(num,0) + 1
        else:
            seen[num] = 1
    buckets = [[] for i in range(len(nums) + 1)]
    
    for num, freq in seen.items():
        buckets[freq].append(num)
        
    res = []
    for i in range(len(buckets)-1,0,-1):
        for n in buckets[i]:
            res.append(n)
            if len(res) == k:
                return res
            
            
            
