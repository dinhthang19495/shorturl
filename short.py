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

    def __init__(self):
        self.count = 0
        self.urls = {}
        pass

    # function to convert long url to short url
    def convert_large_to_short(self, largeUrl: str):
        # Check if the large url is in the dict
        if largeUrl in self.urls:
            # if it already exists, do sth
            pass
        # get the count and convert it to the reduceurl
        reduceurl = self.convert_count_to_reduceurl(self.count)

        # increment
        self.count = self.count + 1

        # return the url
        self.count = self.count + 1
        pass
    # function to convert a short url to a large url
    def convert_short_to_large(self):
        pass
    # random function generator short url
    def random_generator(self):
        pass
    # function to check if a short url has been created
    def check_duplicate(self):
        pass

    # function to convert count to reduceurl
    def convert_count_to_reduceurl(self, count: int):
        # if count is less than 62, do this
        if count < 62:
            return ReplaceUrl.base_reduce_url.get(count)
        # if count is greater than 62, do this
        else:
            # create a list to contain values
            values = []
            # enter the while loop
            while(count != 0):
                # create a temp_cnt to store the value of count
                temp_cnt = count
                # create a loop count
                loop_cnt = 0
                # enter the inner while loop
                while(temp_cnt > 62):
                    temp_cnt = temp_cnt // 62
                    loop_cnt = loop_cnt + 1
                # add the temp value to the list
                values.append(temp_cnt)
                count = count - (temp_cnt * 62**loop_cnt)
            return (self.read_the_list(values))
    # function to read through the list
    def read_the_list(self, values: list):
        tinyurl = ""
        for i in values:
            tinyurl +=(ReplaceUrl.base_reduce_url.get(i))
        return tinyurl
    # 
# reduceurl.com/aaaaa

# 5 characters/digits to make 916,132,832 url

# we will use a-z, A-Z, and 0-9

# we expect to generate 1 million url in 6 months.

