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

    def __init__(self):
        self.count = 0
        self.urls = {}
        pass

    # function to convert long url to short url
    def convert_large_to_short(self, largeUrl: str):
        # Check if the large url is in the dict
        if largeUrl in self.urls:
            # if it already exists, do sth
            return self.convert_count_to_reduceurl(self.urls.get(largeUrl))

        self.urls[largeUrl] = self.count

        # get the count and convert it to the reduceurl
        reduceurl = self.convert_count_to_reduceurl(self.count)

        # increment
        self.count = self.count + 1

        # return the url
        return reduceurl
    # function to convert a short url to a large url
    def convert_short_to_large(self, reduceurl: str):
        cnt = self.convert_reduceurl_to_number(reduceurl)
        for k,v in self.urls.items():
            if self.v == cnt:
                return k
        return "It is not in the database"

    # function to convert count to reduceurl
    def convert_count_to_reduceurl(self, count: int):
        values = []
        if count == 0:
            return ReplaceUrl.base_reduce_url.get(count)
        while count > 0:
            values.insert(0, count % ReplaceUrl.BASE)
            count = count // ReplaceUrl.BASE
        return self.read_the_list(values)
    # function to read through the list
    def read_the_list(self, values: list):
        tinyurl = ""
        for i in values:
            tinyurl +=(ReplaceUrl.base_reduce_url.get(i))
        return tinyurl

    # function to convert reduceurl to number
    def convert_reduceurl_to_number(self, reduceurl: str):
        count = 0
        temp_len = len(reduceurl) - 1
        temp_dict = ReplaceUrl.flip_dict(ReplaceUrl.base_reduce_url)
        for i in reduceurl:
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
# reduceurl.com/aaaaa

# 5 characters/digits to make 916,132,832 url

# we will use a-z, A-Z, and 0-9

# we expect to generate 1 million url in 6 months.

yo = ReplaceUrl()

print(yo.convert_large_to_short('fakfoakfaofka'))
print(yo.convert_large_to_short('face'))
print(yo.convert_large_to_short('face'))
print(yo.convert_large_to_short('face'))
print(yo.convert_large_to_short('face'))
