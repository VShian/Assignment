class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack=[]
        for ele in A:
            # print(stack)
            if ele==')':
                count=0
                while stack[-1]!='(':
                    stack=stack[:-1]
                    count+=1
                stack=stack[:-1]
                if count==0:
                    return 1
            else:
                stack+=[ele]
        return 0