# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        
        def fetchhostname(url):
            return url.split('/')[2]

        baseurl = fetchhostname(startUrl)
        listofurls = deque()
        listofurls.append(startUrl)  
        visited = set([startUrl])

        while listofurls:
            url = listofurls.popleft()
            for i in htmlParser.getUrls(url):
                if fetchhostname(i) == baseurl and i not in visited:
                    visited.add(i)
                    listofurls.append(i)
        return visited             
        
