class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphaMap = {}

        for i in range(len(order)):
            alphaMap[order[i]] = i
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            for j in range(min(len(w1), len(w2))):
                if j == min(len(w1), len(w2))-1 and len(w1) > len(w2):
                    return False

                if alphaMap[w1[j]] < alphaMap[w2[j]]:
                    break
                elif alphaMap[w1[j]] > alphaMap[w2[j]]:
                    return False
                else: 
                    continue
                

        return True