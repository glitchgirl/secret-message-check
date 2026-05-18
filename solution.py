import requests
from html.parser import HTMLParser
from html.entities import name2codepoint

# using HTMLPARSER to parse out the table 

class TableParser(HTMLParser):
    # defining what the table is
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.in_td = False
        self.in_span = False
        self.table_data = []
        self.current_row = []
        self.current_cell = ""

    # these are based off the default parser from HTMLParser
    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.in_table = True
        elif tag == "tr" and self.in_table:
            self.current_row = []
        elif tag == "td" and self.in_table:
            self.in_td = True
            self.current_cell = ""
        elif tag == "span" and self.in_td:
            self.in_span = True
    
    def handle_endtag(self, tag):
        if tag == "td" and self.in_td:
            self.in_td = False
            self.current_row.append(self.current_cell.strip())
        elif tag == "tr" and self.in_table:
            if self.current_row:  # Only add non-empty rows
                self.table_data.append(self.current_row)
        elif tag == "table":
            self.in_table = False
    
    def handle_data(self, data):
        if self.in_td:
            self.current_cell += data

# takes in the URL
#  TODO check URL is valid 
# retrieve the data
# don't have to do too much checking here, we can assume the data is formatted correctly based on the instructions

link = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
response = requests.get(link)


# DECODE bytes to string 
html_content = response.content.decode('utf-8') 
print(type(html_content))
parser = TableParser()
parser.feed(html_content)



# parse the data
# data starts at zero and can get infinitely large

# print the secret 
# basically, each row is 3 values: x,y and what char to print, and when printed together it'll print a letter 
for row in parser.table_data:
    print(row)
