import requests
from html.parser import HTMLParser
from html.entities import name2codepoint

# using HTMLPARSER to parse out the table - took out some stuff we didn't need

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

parser = MyHTMLParser()

# takes in the URL
# check URL is valid 

link = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
test = requests.get(link)
linkF = test.content
print(type(str(linkF)))

# retrieve the data
# don't have to do too much checking here, we can assume the data is formatted correctly based on the instructions
parser.feed(linkF)


# parse the data
# data starts at zero and can get infinitely large

# print the secret 
# basically, each row is 3 values: x,y and what char to print, and when printed together it'll print a letter 
