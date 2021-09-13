from collections import Counter, defaultdict

#o(n) t
#o(n) s
def groupAnagrams(words):
  anagrams = defaultdict(list)
  for word in words:
    #turn word into hashable bag
    word_bag = Counter(word)
    grouping = frozenset(word_bag.items())

    #add this word to our grouping
    anagrams[grouping].append(word)

  return list(anagrams.values())
