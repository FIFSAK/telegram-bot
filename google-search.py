from googlesearch import search

query = "python fastapi"

for i in search(query, tld='com', num=5, stop=5):
    print(i)