#!/usr/bin/env pyhton
#coding=utf8
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dicts):
        path = [start]
        current = start
        rest = set(dicts)
        while self.diff(current, end) > 0:
            candidates = set(filter(lambda x: self.diff(x, current) == 1, rest))
            print candidates
            rest = candidates.difference(rest)
            print rest
            

    def diff(self, a, b):
        diff_count = 0
        for i in range(0, len(a)):
            if not a[i] == b[i]: diff_count += 1
        return diff_count
    
