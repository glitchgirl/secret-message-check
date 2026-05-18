import requests
from html.parser import HTMLParser

#takes a url and displays a graphic based on the table
def display_secret_message(url): 
    
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
    # retrieve the data - decode it it comes in as bytes not str
    # don't have to do too much checking here, we can assume the data is formatted correctly based on the instructions
    
    response = requests.get(url)
    html_content = response.content.decode('utf-8')
     
    
    # parse the data

    
    parser = TableParser()
    parser.feed(html_content)
    
    # print the secret 
    # basically, each row is 3 values: x,y and what char to print, and when printed together it'll print a letter 
    # data starts at zero and can get infinitely large
    # Skip the header row and extract coordinates + characters
    rows = parser.table_data[1:]
    grid = {}
    max_x = 0
    max_y = 0
    
    for row in rows:
        x = int(row[0])
        char = row[1]
        y = int(row[2])
        
        grid[(x, y)] = char
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    
    # Build and print the picture - this has to start from the highest Y co-ord or it will print upside down
    for y in range(max_y, -1, -1):
        line = ""
        for x in range(max_x + 1):
            line += grid.get((x, y), " ")
        print(line)
# Usage:
url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
display_secret_message(url)
