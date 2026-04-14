class Solution:
    
    def encode(self, strs: List[str]) -> str:
        # string = ""
        # for s in strs:
        #     string+=str(len(s))+"#"+s
        # return string     

        string_lengths = ""
        strings = ""


        for s in strs:
            string_lengths+=str(len(s))+"#"
            strings+=s

        return string_lengths+"$"+strings    

    def decode(self, s: str) -> List[str]:

        string_ctns = []

        res = []

        i = 0

        while s[i]!="$":
            count = ""

            while s[i]!="#":
                count+=s[i]
                i+=1
            string_ctns.append(int(count))    
            i+=1 # after # start with new digit
        
        i+=1 # after $ we have our all words
        for length in string_ctns:
            res.append(s[i:length+i])
            i+=length # as we want to move forward also

        return res        

        # i = 0
        # res = []
        # while i<len(s):
        #     j = i                 
        #     while s[j]!="#":
        #         j+=1
            

        #     length = int(s[i:j])

        #     i = j+1

        #     string = s[i:length+i]

        #     res.append(string)

        #     i+=length

        # return res    







        # res = []
        # i = 0

        # while i<len(s):
        #     j = i

        #     while s[j]!="#":
        #         j+=1

        #     length = int(s[i:j])

        #     i = j+1

        #     res.append(s[i:length+i])

        #     i = length+i


        # return res        




    # def encode(self, strs: List[str]) -> str:
    #     strings = ""
    #     string_counts = "" 

    #     for s in strs:
    #         string_counts+=str(len(s))
    #         string_counts+="#"
    #         strings+=s
        
    #     return string_counts + "$" + strings

    # def decode(self, s: str) -> List[str]:
    #     i = 0
    #     string_counts = []
        
    #     count = ""
    #     while s[i]!="$":
    #         if s[i]=="#":
    #             string_counts.append(int(count))
    #             count = ""
    #         else:
    #             count+=s[i]

    #         i+=1

    #     i = i+1 #start after $ 
        
    #     res = []

    #     for length in string_counts:
    #         temp_str = ""
    #         for k in range(i,length+i):
    #             temp_str+=s[k]
    #             i+=1
    #         res.append(temp_str)

    #     return res        

        # will try the another way in shortly




        
