from googlesearch import search


def search_links(response):

    response = response.split("\n")
    links = []
    for i in range(len(response)):
        response[i] = response[i][3:]
    for i in response:
        query = next(search(f"give 1 link of free resource for each topic to learn {i} CHECK THAT ALL SITES ARE WORKING ", tld="com", num=1, stop=1, pause=2.0), None)
        links.append(query)
        print(links)
    return links



