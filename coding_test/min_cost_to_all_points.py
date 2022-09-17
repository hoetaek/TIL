import heapq
from itertools import combinations
from collections import defaultdict
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        points = [tuple(i) for i in points]
        # for i in range(1, len(points) + 1):
        #     adj[i] = []
        
        nodes = [i for i in combinations(points, 2)]
        for n1, n2 in nodes:
            weight = self.get_distance(n1, n2)
            adj[n1].append([n2, weight])
            adj[n2].append([n1, weight])

        # Initialize the heap by choosing a single node
        # (in this case 1) and pushing all its neighbors.
        minHeap = []
        for neighbor, weight in adj[points[0]]:
            heapq.heappush(minHeap, [weight, points[0], neighbor])

        cost = 0
        visit = set()
        visit.add(points[0])
        while len(visit) < len(points):
            weight, n1, n2 = heapq.heappop(minHeap)
            if n2 in visit:
                continue

            cost += weight
            visit.add(n2)
            for neighbor, weight in adj[n2]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, n2, neighbor])
        return cost

        
        
    def get_distance(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)


import heapq
from itertools import combinations

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = []
        points = [tuple(i) for i in points]
 
        nodes = [i for i in combinations(points, 2)]
        for n1, n2 in nodes:
            weight = self.get_distance(n1, n2)
            heapq.heappush(minHeap, [weight, n1, n2])

        unionFind = UnionFind(points)
        mst = []
        while len(mst) < len(points) - 1:
            # print(minHeap)
            # print(mst)
            weight, n1, n2 = heapq.heappop(minHeap)
            if not unionFind.union(n1, n2):
                continue
            mst.append(weight)
        return sum(mst)

        
    def get_distance(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)
    
class UnionFind:
    def __init__(self, points):
        self.par = defaultdict(tuple)
        self.rank = defaultdict(int)

        for i in range(len(points)):
            self.par[points[i]] = points[i]
            self.rank[i] = 0
    
    # Find parent of n, with path compression.
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        # print("-" * 40, "union")
        # print(p1, p2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True
