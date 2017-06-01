import sys
import urllib

argLen = len(sys.argv)
baseURL = ""
if (argLen == 3) : baseURL=sys.argv[2]

downloadListFile = sys.argv[1]
f = open(downloadListFile)
download = f.readline()

if (download) : print "starting the download..."

while download:
	urllib.urlretrieve(baseURL+download, 'download/'+download)
	print "downloaded: " + baseURL+download +"..."
	download = f.readline()
f.close()

print "download complete"
	
