
def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n 

    # Step 1: Prefix products, Without any exceptions
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]
        print(f"i: {i}")
        print(f"Output: {output[i]}")
        print(f"Prefix: {prefix}\n")
        
    print(f"Prefix after looping: {prefix}")
    print(f"Output after prefix loop: {output}")
    

    # Step 2: Postfix products (and multiply with existing prefix)
    postfix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= postfix
        postfix *= nums[i]
        print(f"i: {i}")
        print(f"Output: {output[i]}")
        print(f"Postfix: {postfix}\n")
        
    print(f"Postfix after looping: {postfix}")
    print(f"Output after postfix loop: {output}")


    # return output
    
productExceptSelf([1,2,3,4])