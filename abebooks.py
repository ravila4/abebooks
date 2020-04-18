import requests


class AbeBooks:

    def __get_price(self, payload):
        url = "https://www.abebooks.com/servlet/DWRestService/pricingservice"
        resp = requests.post(url, data=payload)
        resp.raise_for_status()
        return resp.json()

    def __get_recomendations(self, payload):
        url = "https://www.abebooks.com/servlet/RecommendationsApi"
        resp = requests.get(url, params=payload)
        resp.raise_for_status()
        return resp.json()

    def getPriceByISBN(self, isbn):
        """
        Parameters
        ----------
        isbn (int) - a book's ISBN code
        """
        payload = {'action': 'getPricingDataByISBN',
                   'isbn': isbn,
                   'container': 'pricingService-{}'.format(isbn)}
        return self.__get_price(payload)

    def getPriceByAuthorTitle(self, author, title):
        """
        Parameters
        ----------
        author (str) - book author
        title (str) - book title
        """
        payload = {'action': 'getPricingDataForAuthorTitleStandardAddToBasket',
                   'an': author,
                   'tn': title,
                   'container': 'oe-search-all'}
        return self.__get_price(payload)

    def getPriceByAuthorTitleBinding(self, author, title, binding):
        """
        Parameters
        ----------
        author (str) - book author
        title (str) - book title
        binding(str) - one of 'hard', or 'soft'
        """
        if binding == "hard":
            container = "priced-from-hard"
        elif binding == "soft":
            container = "priced-from-soft"
        else:
            raise ValueError(
                    'Invalid parameter. Binding must be "hard" or "soft"')
        payload = {'action': 'getPricingDataForAuthorTitleBindingRefinements',
                   'an': author,
                   'tn': title,
                   'container': container}
        return self.__get_price(payload)

    def getRecommendationsByISBN(self, isbn):
        """
        Parameters
        ----------
        isbn (int) - a book's ISBN code
        """
        payload = {'pageId': 'plp',
                   'itemIsbn13': isbn}
        return self.__get_recomendations(payload)
