import csv, sys, time, os, urllib2, json

priorityList = ["high", "medium", "low"]

try:
	pagePriorityLevel = sys.argv[1]
	if pagePriorityLevel in priorityList:
		print "Priority level given: " + pagePriorityLevel
	else:
		raise Exception
except:
	print "First command line argument should be priority level [high|medium|low]"
	sys.exit()

try:
	inputFileName = sys.argv[2]
except:
	print "Second command line argument should be the input file i.e \n separated list of URLs"
	sys.exit()

lastmod = time.strftime('%Y-%m-%d')
outputFileName = 'sitemap_' + pagePriorityLevel +'.xml'

sitemap = open(outputFileName, 'w')

sitemap.write('<?xml version="1.0" encoding="UTF-8"?>\n')
sitemap.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

freqMap = {"high" : "hourly", "medium" : "daily", "low" : "weekly"}
priorityMap = {"high" : "0.9", "medium" : "0.8", "low" : "0.7"}

changefreq = freqMap[pagePriorityLevel]
priority = priorityMap[pagePriorityLevel]
urlsCount = 0

try:
	for url in open(inputFileName, 'rb'):
		urlInfo = '\n\t<url>\n'
		urlInfo += '\t\t<loc>%s</loc>\n'
		urlInfo += '\t\t<lastmod>%s</lastmod>\n'
		urlInfo += '\t\t<changefreq>%s</changefreq>\n'
		urlInfo += '\t\t<priority>%s</priority>\n'
		urlInfo += '\t</url>'
		urlInfo = urlInfo % (url.strip(), lastmod, changefreq, priority)
		sitemap.write(urlInfo) 
		urlsCount += 1 

finally:
	print "Total URLs processed: " + str(urlsCount)
	sitemap.write('\n</urlset>')
	sitemap.close()
	os.system("gzip " + outputFileName)