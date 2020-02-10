


class OpenFoodFactsClient(object):

    API_URL = 'https://world.openfoodfacts.org'
    
    def product_by_barcode(self, barcode):
        return f'{self.API_URL}/api/v0/product/{barcode}.json'

    def get(self, url):
        pass

