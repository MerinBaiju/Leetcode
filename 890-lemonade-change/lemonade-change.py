class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a=0
        l5=0
        lt=0
        for i in bills:
            if(i==5):
                a+=1
                l5+=1
            elif(i==10):
               if(l5>=1):
                a+=1
                lt+=1
                l5-=1
            else:
                if(lt>=1 and l5>=1):
                    a+=1
                    lt-=1
                    l5-=1
                elif(l5>=3):
                    a+=1
                    l5-=3
        if(a==len(bills)):
            return True
        else:
            return False

