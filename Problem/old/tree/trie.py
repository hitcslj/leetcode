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