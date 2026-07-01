class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        licensePlate.lower()
        print(licensePlate)
        licensePlate=str(licensePlate)
        varied=[]
        for i in range(len(licensePlate)):
            ch=licensePlate[i].lower()
            print(ord('a'), ord(ch) ,ch, ord('z'))
            if ord('a')<= ord(ch) <= ord('z'):
                varied+=[ch]
        print(varied)
        d={}
        x=float('inf')
        ans=''
        for  word in words: 
            if len(varied)<= len(word) and x > len(word):
                count=0
                w=list(word)
                for ch in varied:
                    if ch not in word:
                        break
                    try:
                        w.remove(ch)
                        
                    except:
                        print("error")
                        break
                    print(w)
                    
                else:
                    x=len(word)
                    ans=word
                        
        return ans