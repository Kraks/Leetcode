#!/usr/bin/env pyhton
#coding=utf8
from itertools import izip

def getNexts(word, dicts):
    return [w for w in dicts if isDiffOne(word, w)]

def diff(w1, w2):
    return len(set.difference(set(w1), set(w2)))

def isDiffOne(w1, w2):
    diff = 0
    for c1, c2 in izip(w1, w2):
        if c1 != c2: diff += 1
        if diff > 1: return False
    return diff == 1

class Solution:
    """
    :type beginWord: str
    :type endWord: str
    :type wordlist: Set[str]
    :rtype: List[List[int]]
    """
    def findLadders(self, start, end, dicts):
        self.ret = []
        self.shortestLen = None
        self.end = end
        self.aux(start, dicts, [start])
        return self.ret

    def aux(self, current, dicts, path):
        if self.shortestLen != None and len(path) >= self.shortestLen: pass
        elif len(dicts) == 0: pass
        elif isDiffOne(self.end, current):
            newPath = path + [self.end]
            if self.shortestLen == None:
                self.ret.append(newPath)
                self.shortestLen = len(newPath)
            else:
                if len(newPath) < self.shortestLen:
                    self.ret = [newPath]
                    self.shortestLen = len(newPath)
                elif len(newPath) == self.shortestLen:
                    self.ret.append(newPath)
        else:
            nexts = getNexts(current, dicts)
            for n in nexts:
                self.aux(n, [w for w in dicts if w != n], path+[n])

if __name__ == "__main__":
    solution = Solution()
    #print solution.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    print solution.findLadders("cat", "fin", ["ion","rev","che","ind","lie","wis","oct","ham","jag","ray","nun","ref","wig","jul","ken","mit","eel","paw","per","ola","pat","old","maj","ell","irk","ivy","beg","fan","rap","sun","yak","sat","fit","tom","fin","bug","can","hes","col","pep","tug","ump","arc","fee","lee","ohs","eli","nay","raw","lot","mat","egg","cat","pol","fat","joe","pis","dot","jaw","hat","roe","ada","mac"])
    #print solution.findLadders("cet", "ism", ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"])
