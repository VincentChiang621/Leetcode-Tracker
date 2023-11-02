# Time: O(n*m)
# Space: O(n) 
# make a hashmap key: tuple val: list; count number of times each char appears in each string in list
# add the result to a hashmap, then return the values of the hashmap
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) # maps charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a, b,..., z

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            hashmap[tuple(count)].append(s)

        return hashmap.values()