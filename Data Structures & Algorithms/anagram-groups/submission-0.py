class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map ={}

        for word in strs:
            count =[0] * 26

            for c in word:
                count[ord(c) - ord('a')] +=1
            
            key = tuple(count)

            if key not in freq_map:
                freq_map[key] = []
            
            freq_map[key].append(word)
        
        return list(freq_map.values())
