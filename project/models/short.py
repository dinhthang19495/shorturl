from project.app import db

URL_TEMPLATE = "http://www.uRshort.us/"


class ShortUrl(db.Document):
    long_url = db.StringField(required=True)
    short_url = db.StringField(required=True)
    id = db.IntField(required=True, primary_key=True)

    def return_dict(self) -> dict:
        temp_dict = dict()
        temp_dict["long_url"] = self.long_url
        temp_dict["short_url"] = self.short_url
        temp_dict["id"] = self.id

        return temp_dict
# create
# example = ShortUrl(long_url = "http://www.google.com", short_url = "http://www.uRshort.us/a", id = 0)
# example.save()

# read
# list_of_urls = ShortUrl.objects
# x = list_of_urls[0]
# print(f'Long field: {x.long_url}\n Short field: {x.short_url}')

# update
# x.long_url = "http://www.amazon.com"

# delete
# x.delete()
