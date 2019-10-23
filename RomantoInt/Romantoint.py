class RomantoInt:
    def romanToInt(self, s: str) -> int:
        '''
        I V X  L   C   D   M
        
        1 5 10 50 100 500 1000
        
        '''
        rom_dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        result=0
        
        for i in range(len(s)):
            if (i > 0 and rom_dic[s[i]] > rom_dic[s[i-1]]):
                result += rom_dic[s[i]] - 2*rom_dic[s[i-1]]  #Because we already plus the rom_dic[s[i-1]] in the previous loop iteration so we want to minus double the value
            else:
                result += rom_dic[s[i]] 

        return result