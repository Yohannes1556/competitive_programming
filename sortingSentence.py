class Solution(object):
    def sortSentence(self, s) :
        """
        :type s: str
        :rtype: str
        """
        s=s.split()
        dic={}
        st=''
        for string in s:
            dic[string[-1]]=string[:-1]
        strings=sorted(dic.items())
        for string in strings:
            st+=string[1]+' '
        return st[:-1]
