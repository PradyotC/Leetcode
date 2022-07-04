/*
Submission Detail:{
    Difficulty : Hard
    Acceptance Rate : 29.67 %
    Runtime : 44 ms
    Memory Usage : 13.9 MB
    Testcase : 601 / 601 passed
    Ranking : 
        Your runtime beats 69.06 % of python3 submissions.
        Your memory usage beats 96.78 % of python3 submissions.
}
*/

class Solution:
    def numberToWords(self, num: int) -> str:
        
        def spell(n):
            ntens = {
                0:"",
                1:"One",
                2:"Two",
                3:"Three",
                4:"Four",
                5:"Five",
                6:"Six",
                7:"Seven",
                8:"Eight",
                9:"Nine"
            }
            tens = {
                0:"",
                2:"Twenty ",
                3:"Thirty ",
                4:"Forty ",
                5:"Fifty ",
                6:"Sixty ",
                7:"Seventy ",
                8:"Eighty ",
                9:"Ninety "
            }
            teens = {
                0:"Ten",
                1:"Eleven",
                2:"Twelve",
                3:"Thirteen",
                4:"Fourteen",
                5:"Fifteen",
                6:"Sixteen",
                7:"Seventeen",
                8:"Eighteen",
                9: "Nineteen"
            }
            d1 = [0,0,0]
            i = 0
            while n!=0 or i!=3:
                d1[i]=n%10
                n//=10
                i+=1
            if d1[1]==1:
                return str(ntens[d1[2]]+(bool(d1[2])*" Hundred ")+teens[d1[0]]).rstrip()
            else:
                return str(ntens[d1[2]]+(bool(d1[2])*" Hundred ")+tens[d1[1]]+ntens[d1[0]]).rstrip()
        
        
        ans = num
        data = [0,0,0,0]
        i = 0
        while ans!=0 or i!=4:
            data[i]=ans%1000
            ans=ans//1000
            i+=1
        if data==[0,0,0,0]: return "Zero"    
        return str(spell(data[3])+(bool(data[3])*" Billion ")+spell(data[2])+(bool(data[2])*" Million ")+spell(data[1])+(bool(data[1])*" Thousand ")+spell(data[0])).rstrip()