# coding=utf8

class Box(object):
    def __init__(self, x): self.x = x

class Option(Box): pass
class ZeroMore(Box): pass
class OnceMore(Box): pass
class Or(list): pass
class Seq(list): pass

##################

# is `pat` a substring of string[start:end]
def isSubstring(pat, string, start, end):
    for i, j in zip(xrange(start, end), xrange(0, len(pat))):
        if pat[j] != string[i]: return False
    return True

def match(patterns, string, pos):
    #print "current pattern" + str(patterns)
    if len(patterns) == 0:
        return pos == len(string)

    pat = patterns[0]

    if isinstance(pat, Or):
        rest = patterns[1:]
        if len(pat) > 2:
            return match([pat[0]] + rest, string, pos) \
                or match([Or(pat[1:])] + rest, string, pos)
        elif len(pat) == 2:
            return match([pat[0]] + rest, string, pos) \
                or match([pat[1]] + rest, string, pos)
        else: raise Eexception("Invalid Or pattern")

    if isinstance(pat, ZeroMore):
        return match(patterns[1:], string, pos) \
            or match([pat.x] + patterns, string, pos)

    if isinstance(pat, OnceMore):
        return match([pat.x, ZeroMore(pat.x)] + patterns[1:], string, pos)

    if isinstance(pat, Option):
        return match([Or([pat.x, ""])] + patterns[1:], string, pos)

    if isinstance(pat, str):
        length = len(pat)
        return len(string) >= (pos + length) \
            and isSubstring(pat, string, pos, pos+length) \
            and match(patterns[1:], string, pos+length)

    if isinstance(pat, list):
        return match(pat + patterns[1:], string, pos)

    raise Eexception("Bad patterns")

##################

Dot = "."
Digits = Or(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
E = Or(["e", "E"])
Whitespace = Or([" ", "\t", "\n"])
Whitespaces = ZeroMore(Whitespace)
Signs = Or(["+", "-"])

decimal = [Option(Signs), OnceMore(Digits)]
real = [Option(Signs), Or([[OnceMore(Digits), Option(Dot), ZeroMore(Digits)],
                           [ZeroMore(Digits), Option(Dot), OnceMore(Digits)]])]
sci = [real, E, decimal]

numPattern = [Whitespaces,
              Or([decimal, real, sci]),
              Whitespaces]

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return match(numPattern, s, 0)

if __name__ == "__main__":
    #print isSubstring("abc", "abd", 0, 3)
    #print isSubstring("def", "abcdefg", 3, 5)
    #print isSubstring("def", "abcdefg", 3, 7)

    """
    print match(["abc"], "abc", 0) #t
    print match(["abc"], "ab", 0) #f
    print match(["a", ZeroMore("b")], "abbbb", 0) #t
    print match(["a", OnceMore("b")], "acccc", 0) #f
    print match(["a", OnceMore("b")], "abbb", 0) #t
    print match(["a", Option("c"), OnceMore("c"), "d"], "acccccd", 0) #t
    """

    print match(numPattern, "   3.312 E", 0)

    print match(numPattern, "123", 0)
    print match(numPattern, "   3.312 ", 0)
    print match(numPattern, "   2e10 ", 0)
    #print match(numPattern, "   2E10 ", 0)
    print match(numPattern, ".3 ", 0)
    print match(numPattern, "3.", 0)
    print match(numPattern, "42.e3", 0)
    print match(numPattern, "4.3e01", 0)
    print match(numPattern, ".4e9", 0)

    print match(numPattern, "e", 0)
    print match(numPattern, "e3", 0)
    print match(numPattern, ".e3", 0)
    print match(numPattern, "3e.3", 0)

    print match(numPattern, "439724e2e5", 0)
    print match(numPattern, "851822 f2-", 0)
    print match(numPattern, "9997 3+..6", 0)
