class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {p: 1, o: 1, t: 1, s: 1}

        # {
        #     0: [{a: 1, c: 1, t: 1}, 3]
        #     1: [{p: 1, o: 1, t: 1, s: 1}, 2, 4]
        #     5: [{h: 1, a: 1, t: 1}]
        # }
        # [0, 3]
        # [1, 2, 4]
        # [5]

        if len(strs) == 1:
            return [[strs[0]]]

        result = []
        anagram_dict = {}
        for i, word in enumerate(strs):
            found = False
            word_dict = {}
            for char in word:
                word_dict[char] = word_dict.get(char, 0) + 1
            for key, value in anagram_dict.items():
                if word_dict == value[0]:
                    curr_list = anagram_dict[key]
                    curr_list.append(i)
                    anagram_dict[key] = curr_list
                    found = True
                    break
            if not found:        
                anagram_dict[i] = [word_dict, i]

        for key, value in anagram_dict.items():
            curr_anagrams = []
            for idx in range(1, len(anagram_dict[key])):
                curr_anagrams.append(strs[anagram_dict[key][idx]])
            result.append(curr_anagrams)

        return result