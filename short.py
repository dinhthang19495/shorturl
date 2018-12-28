# Class replaceUrl
class ReplaceUrl:
    """
        We will take a long url and return a short url.
        Then, users can use the short url to take them to the long url.
    """
    base_reduce_url = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',
                       11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',
                       21:'v',22:'w',23:'x',24:'y',25:'z',26:'A',27:'B',28:'C',29:'D',30:'E',
                       31:'F',32:'G',33:'H',34:'I',35:'J',36:'K',37:'L',38:'M',39:'N',40:'O',
                       41:'P',42:'Q',43:'R',44:'S',45:'T',46:'U',47:'V',48:'W',49:'X',50:'Y',
                       51:'Z',52:'0',53:'1',54:'2',55:'3',56:'4',57:'5',58:'6',59:'7',60:'8',
                       61:'9'}
    BASE = 62
    #our url
    URL_TEMPLATE = "http://www.uRshort.us/"
    def __init__(self):
        self.count = 0
        self.urls = {}

    # function to convert long url to short url
    def convert_long_to_short(self, longUrl: str):
        # Check if the large url is in the dict
        if longUrl in self.urls:
            # if it already exists, do sth
            return self.URL_TEMPLATE + self.convert_count_to_reducedurl(self.urls.get(longUrl))

        self.urls[longUrl] = self.count

        # get the count and convert it to the reduceurl
        reducedurl = self.convert_count_to_reducedurl(self.count)

        # increment
        self.count = self.count + 1

        # return the url
        return self.URL_TEMPLATE + reducedurl
    # function to convert a short url to a large url
    def convert_short_to_long(self, reducedurl: str):
        if reducedurl.startswith(ReplaceUrl.URL_TEMPLATE):
            cnt = self.convert_reducedurl_to_number(reducedurl)
            for k,v in self.urls.items():
                if v == cnt:
                    return k
        return "It is not in the database"

    # function to convert count to reduceurl
    def convert_count_to_reducedurl(self, count: int):
        values = []
        if count == 0:
            return ReplaceUrl.base_reduce_url.get(count)
        while count > 0:
            values.insert(0, count % ReplaceUrl.BASE)
            count = count // ReplaceUrl.BASE
        return self.read_the_list(values)
    # function to read through the list
    def read_the_list(self, values: list):
        shorturl = ""
        for i in values:
            shorturl +=(ReplaceUrl.base_reduce_url.get(i))
        return shorturl

    # function to convert reduceurl to number
    def convert_reducedurl_to_number(self, reducedurl: str):
        reducedurl = ReplaceUrl.get_short_url(reducedurl)
        count = 0
        temp_len = len(reducedurl) - 1
        temp_dict = ReplaceUrl.flip_dict(ReplaceUrl.base_reduce_url)
        for i in reducedurl:
            value = temp_dict.get(i)
            count += value * (ReplaceUrl.BASE**temp_len)
            temp_len -= 1
        return count

    # function to flip the dictionary
    def flip_dict(map: dict):
        new_dict = {}
        for k,v in map.items():
            new_dict[v] = k
        return new_dict
    # function to get the url and return the short url
    def get_short_url(url: str):
        shorturl = url[len(ReplaceUrl.URL_TEMPLATE):]
        return shorturl
# reduceurl.com/aaaaa

# 5 characters/digits to make 916,132,832 url

# we will use a-z, A-Z, and 0-9

# we expect to generate 1 million url in 6 months.

yo = ReplaceUrl()

print(yo.convert_long_to_short('fakfoakfaofka'))
print(yo.convert_long_to_short('face'))
print(yo.convert_long_to_short('face'))
print(yo.convert_long_to_short('face'))
print(yo.convert_long_to_short('face'))
print(yo.convert_short_to_long('http://www.uRshort.us/a'))
print(yo.convert_short_to_long('http://www.uRshort.us/u'))
print(yo.convert_short_to_long('u'))
