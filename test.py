"""
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        test = []
        test_2 = []
        for i in nums: 
            test.append(i)
            test_2.append(i)
        
        ans = test + test_2

        print(ans)
        return ans


#test = Solution()
#test.getConcatenation(nums=[1,2,1])



class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""

        leng = word1 + word2
        text_1 = list(word1)
        text_2 = list(word2)

        text_e1 = list(word1)
        text_e2 = list(word2)

        
       

        iterator = 0

        if len(text_1) < len(text_2): 
            iterator = len(text_1)
        elif len(text_1) > len(text_2):
            iterator = len(text_2) 
        else: iterator = len(text_2)



        index = 0
        testarray = []
        print(iterator)
        

        for i in range(iterator): 
                #print("te")
    
                testarray.append(text_1[index])
                testarray.append(text_2[index])

             
                text_e1.pop(0)
                text_e2.pop(0)
                index += 1 
        print("strin_1")
        print(text_e1)
        print("strin_2")
        print(text_e2)

        if len(text_e1) > 0:
            for i in text_e1:
                testarray.append(i)
        else:
            for k in text_e2:
                testarray.append(k)
          
                    

               
            
            
           
                
        
        dick_mit_leerzeichen = "".join(testarray)
        print(dick_mit_leerzeichen)  # Ausgabe: Hallo Welt
        


# der string soll im wechsel durch beide strings erzeugt werden 


test2 = Solution2()
test2.mergeAlternately("ab","pqrs")


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        k = list(t)
        returnchar = ""

        
        for i in s:
            for l in t:
                if l == i:
                    k.remove(l)
            #print(i)
        
        for char in k:
            returnchar = char

        return returnchar


test = Solution()
l = test.findTheDifference(s="",t="abcd")

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        for i in range(len(haystack) - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1


test = Solution()
k = test.strStr(haystack = "tester", needle = "tester")
print(k)    

"""
        haystack = list(haystack)
        needle = list(needle)

        
        counter = 0
        n = 0

        for i in haystack:
            print(haystack[n],needle[n])
          
            if i[n] == needle[n]:
        
                    counter +=1 
            n += 1           
            
            
        print(counter)
        
        if counter == len(needle):
            return 0 
        else: 
            return -1



        for i in needle: 
            for l in haystack:
                if l == i:
                    counter += 1 
                    break

 """       

