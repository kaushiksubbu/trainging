class Solution:
    def reverseVowels(self, s: str) -> str:
        v=["a","e","i","o","u","A","E","I","O","U"]
#        s="Aeiooauaaioueaouuiaeoeiauuooiea"
        in_v=[]
        for i in range(len(s)):
            if s[i] in v:
                print ("location",i,"Val",s[i])
                in_v.append(s[i])
                print("in_v list",in_v)
        pos=len(in_v)-1
        print(pos)
        in_list=list(s)
        for j in range(len(s)):
            if in_list[j] in v:
                print(in_list[j],in_v[int(pos)])
                in_list[j]=in_v[int(pos)]
                pos-=1
        print("".join(in_list))
        return ("".join(in_list))
