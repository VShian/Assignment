class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        char_list=[]
        for s in A:
            char_list.append(list(s))
            char_list[-1].sort()
        # print(char_list)
        check=[False for i in range(len(A))]
        anag_list=[]
        for i in range(len(char_list)):
            if check[i]==True:
                continue
            # print(i)
            anag_i=[i+1]
            for j in range(i+1,len(char_list)):
                if check[j]==False and char_list[i]==char_list[j]:
                    anag_i+=[j+1]
                    check[j]=True
            # if len(anag_i)!=1:
            anag_list.append(anag_i)
                
            check[i]=True
        return anag_list