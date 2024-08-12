from typing import List

# https://leetcode.cn/problems/longest-common-suffix-queries
class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1


class Trie:
    def __init__(self,wordsContainer):
        self.root = TrieNode()
        self.wordsContainer = wordsContainer

    def insert(self, word, index):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                node = node.children[char]
                node.index = index
            else:
                # 开始进行比较
                node = node.children[char]
                s = self.wordsContainer[node.index]
                if len(word)<len(s):
                    node.index = index

    def find_longest_suffix(self, word):
        node = self.root
        cur = -1
        for char in word:
            if char in node.children:
                node = node.children[char]
                cur = node.index
            else:
                break
        return cur


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        wordsContainer = [word[::-1] for word in wordsContainer]
        wordsQuery = [word[::-1] for word in wordsQuery]
        ans = []

        trie = Trie(wordsContainer)
        for i, word in enumerate(wordsContainer):
            trie.insert(word, i)
        
        def findMin(wordsContainer):
            l = min(len(s) for s in wordsContainer)
            for i,s in enumerate(wordsContainer):
                if len(s)==l:
                    return i
        minIdx = findMin(wordsContainer)
        for query in wordsQuery:
            idx = trie.find_longest_suffix(query)
            if idx == -1:
                ans.append(minIdx)
            else:
                ans.append(idx)
        return ans



# https://leetcode.cn/problems/implement-magic-dictionary
class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.isEnd = True

    def search(self, word, idx, cnt):
        if cnt > 1:
            return False
        if idx == len(word):
            return cnt == 1 and self.isEnd
        for char in self.children:
            if char == word[idx]:
                if self.children[char].search(word, idx + 1, cnt):
                    return True
            else:
                if self.children[char].search(word, idx + 1, cnt + 1):
                    return True
        return False

class MagicDictionary:

    def __init__(self):
        self.trie = Trie()


    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)

    def search(self, searchWord: str) -> bool:
        return self.trie.search(searchWord, 0, 0)



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)