from project.models import ShortUrl
# Class replaceUrl


class ReplaceUrl:
    """
        We will take a long url and return a short url.
        Then, users can use the short url to take them to the long url.
    """
    base_reduce_url = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k',
                       11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u',
                       21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z', 26: 'A', 27: 'B', 28: 'C', 29: 'D', 30: 'E',
                       31: 'F', 32: 'G', 33: 'H', 34: 'I', 35: 'J', 36: 'K', 37: 'L', 38: 'M', 39: 'N', 40: 'O',
                       41: 'P', 42: 'Q', 43: 'R', 44: 'S', 45: 'T', 46: 'U', 47: 'V', 48: 'W', 49: 'X', 50: 'Y',
                       51: 'Z', 52: '0', 53: '1', 54: '2', 55: '3', 56: '4', 57: '5', 58: '6', 59: '7', 60: '8',
                       61: '9'}
    BASE = 62
    # our url
    URL_TEMPLATE = "http://www.uRshort.us/"

    # function to convert long url to short url
    @staticmethod
    def convert_long_to_short(large_url: str):
        # Check if the large url is in the dict
        temp_list = ShortUrl.objects
        for i in temp_list:
            if large_url == i["long_url"]:
                return {"short_url_obj": i.return_dict(), "already_exist": True}

        # get the count and convert it to the reduced url
        tiny_url = ReplaceUrl.URL_TEMPLATE + ReplaceUrl.convert_count_to_reduced_url(len(temp_list))
        db_object = ShortUrl(long_url=large_url, short_url=tiny_url, id=len(ShortUrl.objects))
        db_object.save()

        return {"short_url_obj": db_object.return_dict(), "already_exist": False}
    # function to convert a short url to a large url

    @staticmethod
    def convert_short_to_long(reduced_url: str):
        # when the short url start with http://www.uRshort.us/, do this
        if reduced_url.startswith(ReplaceUrl.URL_TEMPLATE):
            # convert the short url to number
            cnt = ReplaceUrl.convert_reduced_url_to_number(reduced_url)
            # if the number matches the value
            for i in ShortUrl.objects:
                if i["id"] == cnt:
                    return i["long_url"]
        # if the number doesn't match the value
        return False

    # function to convert count to reduced url
    @staticmethod
    def convert_count_to_reduced_url(count: int):
        values = []
        # if count = 0, match it with the position 0 from base reduce url
        if count == 0:
            return ReplaceUrl.base_reduce_url.get(count)
        # if count > 0
        while count > 0:
            # insert the reminder value to the first position of values
            values.insert(0, count % ReplaceUrl.BASE)
            # get the whole number of count
            count = count // ReplaceUrl.BASE
        return ReplaceUrl.read_the_list(values)
    # function to read through the list

    @staticmethod
    def read_the_list(values: list):
        short_url = ""
        # for loop
        for i in values:
            # get the value from values and match it with the value from base reduce url, then add it to string short url
            short_url += (ReplaceUrl.base_reduce_url.get(i))
        return short_url

    # function to convert reduced url to number
    @staticmethod
    def convert_reduced_url_to_number(reduced_url: str) -> int:
        # get the full short url and only take the shorten url part
        reduced_url_1 = ReplaceUrl.get_short_url(reduced_url)
        # the sum
        count = 0
        # start from the position next to the last
        temp_len = len(reduced_url_1) - 1
        # create a new dictionary but flip key with value
        temp_dict = ReplaceUrl.flip_dict(ReplaceUrl.base_reduce_url)
        # for loop
        for i in reduced_url_1:
            # set the value to i position in temp dictionary
            value = temp_dict.get(i)
            # add the value to the sum
            count += value * (ReplaceUrl.BASE**temp_len)
            # decrement the temp length
            temp_len -= 1
        return count

    # function to flip the dictionary
    @staticmethod
    def flip_dict(new_list: dict):
        # create a new dictionary
        new_dict = {}
        # From key and value from the dictionary, we create a new dictionary but flip key with value.
        for k, v in new_list.items():
            new_dict[v] = k
        return new_dict
    # function to get the url and return the short url

    @staticmethod
    def get_short_url(new_url: str):
        # we shorten the url by taking the part after http://www.uRshort.us/
        short_url = new_url[len(ReplaceUrl.URL_TEMPLATE):]
        return short_url

# http://www.uRshort.us/aaaaa
# 5 characters/digits to make 916,132,832 url
# we will use a-z, A-Z, and 0-9
# we expect to generate 1 million url in 6 months.
