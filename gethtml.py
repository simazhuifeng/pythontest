
import urllib2
import lxml.html

tmpURL = 'http://mp.weixin.qq.com/s?__biz=MzA3MzYzNjMyMA==&mid=201772057&idx=3&sn=21ec9d3233ebde60478d45421b51624e&scene=2&from=timeline&isappinstalled=0#rd'

data = urllib2.urlopen(tmpURL).read()
dom = lxml.html.fromstring(data)

tds = dom.xpath("head/title")

print tds[0].text_content()