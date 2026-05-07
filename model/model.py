from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def get_anni(self):
        return DAO.get_anni()

    def get_brand(self):
        return DAO.get_brand()

    def get_retailer(self):
        return DAO.get_retailer()

    def get_top_vendite(self):
        return DAO.get_top_vendite()

    def get_codici_prodotto_brand(self, brand):
        return DAO.get_codici_prodotto_brand(brand)