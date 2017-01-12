from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
import sys
import pyperclip

#send files to transfer.sh server
register_openers()
datagen, headers = multipart_encode({"file": open(sys.argv[1], "rb")})
request = urllib2.Request("https://transfer.sh", datagen, headers)

#copy link to clipboard
print urllib2.urlopen(request).read()
pyperclip.copy(urllib2.urlopen(request).read())

print("Copied to your clipboard :)")
k = input("Press Enter to Exit")
