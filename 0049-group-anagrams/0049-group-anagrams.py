class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #creating a dictionary empty
        Dict={}
        for word in strs:
            temp=''.join(sorted(word))
            if temp in Dict:
                Dict[temp].append(word)
            else:
                Dict[temp]=[word]
        return Dict.values()