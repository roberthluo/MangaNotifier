import re
from pymongo import MongoClient
from HTMLParser import HTMLParser


class MangaDAO:

    def __init__(self):
        client = MongoClient()
        self.db = client['manganotifier']

    def add_manga(self, manga):
        self.db.manga.insert_one(manga)

    def get_all_manga(self):
        result = list(self.db.manga.find())
        return result

    def update_manga(self, manga):
        result = self.db.manga.update_many(
            {'name': manga['name']},
            {'$set': {
                    'release': manga['release'],
                    'link': manga['link']
                }
            }
        )

    def check_if_exist(self, manga):

        exist = self.db.manga.find_one({"name" : manga['name'],
            "link" : manga['link'], "release" : manga['release']})

        if exist == None:
            return False
        else:
            return True


if __name__ == '__main__':
    manga_dao = MangaDAO()

    html_parser = HTMLParser()
    mangaelem = {"name" : 'Vinland Saga',
        "link" :'http://readms.com/r/vinland_saga/127/3377/1',
         "release" : '127 - The Baltic Sea War 3'}
    mangaelem1 = {"name" : 'Vinland Saga',
        "link" :'http://readms.com/r/vinland_saga/127/3377/1',
        "release" : '1272 - The Baltic Sea War 3'}
    #print(html_parser.parse_mangastream())
    print(html_parser.list_size)
    print(manga_dao.check_if_exist(mangaelem))
    print(manga_dao.check_if_exist(mangaelem1))

    line = html_parser.parse_mangastream()
