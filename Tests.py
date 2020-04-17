import requests
import xmltodict as xtd


# Add number of reviews to weight the ratings

key: str = "FtnOigZcvTP66VcQtByXA"  # Private Key for accessing GoodReads API
url = "https://www.goodreads.com/search.xml"
path = "text_files/"
write_file = "dictionary"
read_file = "title_list"
titles = open(path + read_file)  # Text file with titles stored in it
f = open(path + write_file, "w+")  # File to write ratings on

ratings = ""
for pair in titles:

    pair = pair.split('\t')
    title = pair[0]
    author = pair[1]
    params = (
        ('key', key),
        ('q', title),
    )

    r = requests.get(url, params=params)
    doc = xtd.parse(r.content)

    results_dict = doc['GoodreadsResponse']['search']['results']['work']
    for item in results_dict:
        print(str(item))
    break

