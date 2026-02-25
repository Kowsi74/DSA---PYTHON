"""
    first the problem is asking about the product of all elements 
    except that self . at brute force solution we iterate 
    each num and multiply the previous one and after values
    but it takes o(n^2) in time and o(n) in space 
"""

def product_of_element(nums):
    res = []
    n = len(nums)
    
    for i in range(n):
        product = 1
        
        for j in range(0,i):
            product *= nums[j]
        for k in range(i+1,n):
            product *= nums[k]
            
        res.append(product)
    return res

"""
    Now we try to optimize it using prefix suffix pattern 
    there we first calculate for every element the previous 
    values and store it and for every element we calculate the
    next after values and store them too and we use those prefix 
    and suffix values to get final result . so it takes o(n) in time 
    and o(n) in space
"""

def productelement(nums):
    n = len(nums)
    res = [0]*n
    pref = [0]*n
    suf =[0]*n
    
    pref[0] = 1 
    suf[n-1] = 1
    
    for i in range(1,n):
        pref[i] = nums[i-1] * pref[i-1]
        
    for j in range(n-2,-1,-1):
        suf[j] = nums[j+1] * suf[j+1]
    for k in range(n):
        res[k] = pref[k] * suf[k]
        
    return res


    