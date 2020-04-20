import requests
import xmltodict as xtd
from collections import OrderedDict


def get_last_name(full_name):
    name_list = full_name.split()
    return name_list[len(name_list) - 1]


# Add number of reviews to weight the ratings

key: str = "FtnOigZcvTP66VcQtByXA"
url = "https://www.goodreads.com/search.xml"
path = "text_files/"
write_file = "title_rating"
read_file = "title_list"
titles = open(path + read_file)  # Text file with titles and authors stored in it
f = open(path + write_file, "w+")  # File to write ratings on

ratings = ""
number = 0
for pair in titles:
    number += 1
    print(pair)
    pair = pair.split('\t')
    title = pair[0]
    author = pair[1]
    params = (
        ('key', key),
        ('q', title + " " + author),
    )

    r = requests.get(url, params=params)
    doc = xtd.parse(r.content)

    # f.write(r.text)   # Only for debugging
    #############
    # check author LAST name match
    # if != , increase work index if none return null

    # if number == 2:
    # f.write(r.text)
    # break
    work_dict = doc['GoodreadsResponse']['search']['results']['work']
    results_dict = doc['GoodreadsResponse']['search']['results']['work']
    found: bool = False
    try:
        if type(results_dict) == OrderedDict:
            auth = results_dict['best_book']['author']['name']
            print(auth + " : " + author)
            if get_last_name(auth).strip() == get_last_name(author).strip():
                rating = str(results_dict['average_rating']) + '\t' + str(results_dict['ratings_count']['#text'])
                print(rating)
                found = True
        else:
            for work in work_dict:
                auth = work['best_book']['author']['name']
                print(auth + " : " + author)
                if get_last_name(auth).strip() == get_last_name(author).strip():
                    rating = str(work['average_rating']) + '\t' + str(work['ratings_count']['#text'])
                    print(rating)
                    found = True
                    break
    except KeyError:
        print("KeyError")
    except TypeError:
        rating = "null"
    if not found:
        rating = "Not Found"
    ratings += rating + '\n'
    print(number)
    if number == 500:
        break

f.write(ratings)
