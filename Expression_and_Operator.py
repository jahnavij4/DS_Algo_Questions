class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.out=[]
        def calculate(arr):
            res=0
            op=None
            for i in arr[::-1]:
                if i.isdigit() and op is None:
                    res=int(i)
                    prev=int(i)
                elif i.isdigit() and op=="+":
                    res+=int(i)
                    prev=int(i)
                elif i.isdigit() and op=="*":
                    res=res-prev+prev*int(i)
                    prev=int(i)*prev
                else:
                    op=i
            return res               

        def recursive(index,partial_sol):
            if index==len(num):
                print("calculation for arr is: ",partial_sol,calculate(partial_sol))

                if calculate(partial_sol)==target:
                    self.out.append("".join(partial_sol[:]))
                return
            prev=partial_sol[-1]
            partial_sol.extend(["+",num[index]])
            recursive(index+1,partial_sol)
            partial_sol.pop()
            partial_sol.pop()
            partial_sol.extend(["*",num[index]])
            recursive(index+1,partial_sol)
            partial_sol.pop()
            partial_sol.pop()
            value=prev+num[index]
            partial_sol[-1]=str(int(value))
            recursive(index+1,partial_sol)

        recursive(1,[num[0]])
        print(self.out)


        return self.out
