from bs4 import BeautifulSoup
import urllib, urllib2

text_file = open("Output.txt", "w")
for i in range(0,20):	
	req = urllib2.Request('http://www.alexa.com/topsites/countries;%s/KE' %i, headers={ 'User-Agent': 'Mozilla/5.0' })
	httpResponse = urllib2.urlopen(req)
	if httpResponse.code == 200 :
		html = httpResponse.read()
		bs = BeautifulSoup(html,"lxml")
		sites = bs.find_all('div', {"class":"desc-container"})
		for site in sites:
			web = site.find('a')
			print web.text
			text_file.write(web.text + "\n")
	else :
		print "[-] There was an error in downloading the page\n"
text_file.close()
