import urllib
import urllib.request
!pip install profanity-check
def read_text();
  racial = open("C:/Users/Kittu Vinny/Downloads/racial.txt","r")
  contents_of_file = racial.read()
  Print_contents_of_file
  racial.close()
  check_profanity(contents_of_file)
  
def check_profanity(text_to_check):
  connection = urllib.request.urlopen("http://www.wydlike.appsoft.com/?q="+text_to_check)
  output = connection.read()
  print (output)
 connection.close()
if "true" in output:
  print "Profanity Alert!"
  elif "false" in output:
    print "This document has no racial words!"
  else:
    print "Could not scan the document properly"


  read+text() 