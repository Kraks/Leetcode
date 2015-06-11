#!/usr/bin/env pyhton
#coding=utf8
class Solution:
    def __init__(self):
        self.shortest = 99999999999
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dicts):
        solution = []
        matrix = self.gen_matrix0(list(dicts))
        def findLaddersHelp(start, end, possible, tdict):
            possible.append(start)
            if len(possible) > self.shortest-1:
                return
            if matrix[start][end] == 1:
                possible.append(end)
                if len(possible) < self.shortest:
                    solution[:] = []
                    solution.append(possible)
                    self.shortest = len(possible)
                if len(possible) == self.shortest:
                    solution.append(possible)
                return 
            #startNext = filter(lambda x: self.diff(x, start) == 1, tdict)
            for s in tdict:
                if matrix[s][start] == 1:
                    newdict = tdict[:]
                    newdict.remove(s)
                    findLaddersHelp(s, end, possible[:], newdict)
            
        findLaddersHelp(start, end, [], list(dicts))
        return solution

    def diff(self, a, b):
        diff_count = 0
        for i in range(0, len(a)):
            if not a[i] == b[i]:
                diff_count += 1
        return diff_count
    
    def gen_matrix0(self, dicts):
        d = {}
        for s1 in dicts:
            d[s1] = {}
            for s2 in dicts:
                d[s1][s2] = self.diff(s1, s2)
        return d
