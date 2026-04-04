class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=f'{len(strs)}#'
        for i in strs:
            encoded+=f'{len(i)}#'
        for i in strs:
            encoded+=i
        return encoded

    def decode(self, s: str) -> List[str]:
        ans=[]
        n=''
        index=0
        while (s[index]!='#'):
            n+=s[index]
            index+=1
        n=int(n)

        count=0
        lengths=[]
        index2=index+1
        temp=''
        while count<n:
            if s[index2]=='#':
                index2+=1
                lengths.append(int(temp))
                temp=''
                count+=1
                continue
            temp+=s[index2]
            index2+=1

        word= s[index2:]
        index3=0
        for i in lengths:
            ans.append(word[index3:index3+i])
            index3+=i
            
        return ans