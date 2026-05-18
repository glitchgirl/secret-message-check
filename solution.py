import requests

# takes in the URL
# check URL is valid 

link = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
test = requests.get(link)
print(test.text)

# retrieve the data
# don't have to do too much checking here, we can assume the data is formatted correctly based on the instructions

# parse the data
# data starts at zero and can get infinitely large

# print the secret 
# basically, each row is 3 values: x,y and what char to print, and when printed together it'll print a letter 
