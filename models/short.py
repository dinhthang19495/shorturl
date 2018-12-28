from mongoengine import *
connect('databs')

class shorturl(Document):
    long_url = StringField(required=True)
    short_url = StringField(required=True)
    id = IntField(required=True, primary_key=True)


# create
# example = shorturl(long_url = "http://www.google.com", short_url = "http://www.uRshort.us/a", id = 0)
# example.save()

# read
# list_of_urls = shorturl.objects
# x = list_of_urls[0]
# print(f'Long field: {x.long_url}\n Short field: {x.short_url}')

# update
# x.long_url = "http://www.amazon.com"

# delete
# x.delete()
