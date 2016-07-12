import web
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['dota2stats']

class PicksAndBansEndpoint:
    def GET(self):
        return 'test'


urls = (
    '/', 'PicksAndBansEndpoint'
)

if __name__ == "__main__":
    print web
    app = web.application(urls, globals())
    print app
    app.run()
