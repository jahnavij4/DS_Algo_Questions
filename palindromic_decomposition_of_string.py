def generate_palindromic_decompositions(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    def palindrome(p):
        if len(p)>0:
            return p==p[::-1]
        return False
        
    def recursive(index,partial_sol):
        nonlocal res
        if index==len(s):
            sub=""
            check=True
            for ele in partial_sol:
                if palindrome(ele):
                    sub+="|"+ele
                else:
                    check=False
                    break
            if check:
                res.append(sub[1:])
                    
            return
        
        # include individual elements
        partial_sol.append(s[index])
        recursive(index+1,partial_sol)
        partial_sol.pop()
        
        # join prev elements
        value= partial_sol[-1]+s[index] 
        partial_sol[-1]=value
        recursive(index+1,partial_sol)
    res=[]
    recursive(1,[s[0]])
    print(res)
    return res
