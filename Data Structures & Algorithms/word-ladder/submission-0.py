class Node:
    def __init__(self, word, children):
        self.word = word
        self.children = []

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # form a graph or adj list by comparing each word with every other word to find the neighbors
        # once we have adjaceny list, use bfs to traverse the graph 
        if (endWord not in wordList) or beginWord == endWord:
            return 0

        # form adj list
        n, m = len(wordList), len(wordList[0])
        adj = [[] for _ in range(n)]
        word_map = {}
        for i in range(n):
            word_map[wordList[i]] = i

        for i in range(n):
            for j in range(i + 1, n):
                cnt = 0
                for k in range(m):
                    if wordList[i][k] != wordList[j][k]:
                        cnt += 1

                if cnt == 1:
                    adj[i].append(j)
                    adj[j].append(i)

        q = deque()
        visit = set()
        for i in range(m):
            for c in range(97, 123):
                if chr(c) == beginWord[i]:
                    continue
                word = beginWord[:i] + chr(c) + beginWord[i+1:]
                if word in word_map and word_map[word] not in visit:
                    q.append(word_map[word])
                    visit.add(word_map[word])

        dist = 1
        while q:
            dist += 1
            for i in range(len(q)):
                node = q.popleft()
                if wordList[node] == endWord:
                    return dist
                for neighbor in adj[node]:
                    if neighbor not in visit:
                        q.append(neighbor)
                        visit.add(neighbor)

        return 0
        