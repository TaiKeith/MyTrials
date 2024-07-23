"""
city_map = {}

cities = ["Nairobi", "Kisumu", "Mombasa", "Nakuru", "Eldoret"]
city_map["Kenya"] = []
city_map["Kenya"] += cities  # city_map["Kenya"].append(cities)
print(city_map)

# OR
from collections import defaultdict
city_map = defaultdict(list)

cities = ["Nairobi", "Kisumu", "Mombasa", "Nakuru", "Eldoret"]
city_map["Kenya"] += cities
"""

"""
# Anagram
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)

        for value in anagram_map.values():
            result.append(value)
        return result

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
print(solution.groupAnagrams(strs))
"""

from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)
    
    for word in strs:
        # Sort the word to use it as a key in the dictionary
        sorted_word = ''.join(sorted(word))
        # Add the word to the corresponding group
        groups[sorted_word].append(word)
    
    # Convert the dictionary values to a list of lists
    return list(groups.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
