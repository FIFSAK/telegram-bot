from googlesearch import search


def search_links(response):
    links = []
    response = response.split("\n")
    for i in range(len(response)):
        response[i] = response[i][3:]
    for i in response:
        query = next(search(i, tld="com", num=1, stop=1, pause=2.0), None)
        links.append(query)
    return links