class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #start with having num open, and num close == n
        #in the recursive function:
            #if num open and num close == 0, we have finished adding all parens, return
            #first we always start with adding a open paren, so if open > 0 
                #append to buff
                #recurse by decrementing open by 1
            #then we always wrap the open with a close so add a close paren, so if close > 0 
                #append to buff
                #recurse by decrementing close by 1
        def solve(op, cl, buff, res):
            if op == 0 and cl == 0:
                res.append(buff)
                return
            if op > 0:
                buff= buff + "("
                solve(op - 1, cl, buff, res)
                buff=buff[:-1]
            if cl > op:
                buff= buff + ")"
                solve(op, cl - 1, buff, res)
                buff=buff[:-1]
        res=[]
        solve(n,n,"", res)
        print(res)
        return res