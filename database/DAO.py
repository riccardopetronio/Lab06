from database.DB_connect import DBConnect
from model.retailer import Retailer
from model.vendita import Vendita

# ho aggiunto questa riga
class DAO():

    @staticmethod
    def get_anni():
        connection = DBConnect.get_connection()
        cursor = connection.cursor(dictionary=True)

        query = """select distinct YEAR(Date)
                from go_daily_sales gds"""

        cursor.execute(query)
        risultato = []
        for row in cursor:
            risultato.append(row["YEAR(Date)"])

        cursor.close()
        connection.close()
        return risultato


    @staticmethod
    def get_brand():
        connection = DBConnect.get_connection()
        cursor = connection.cursor(dictionary=True)

        query = """select distinct gp.Product_brand 
                from go_products gp"""

        cursor.execute(query)
        risultato = []
        for row in cursor:
            risultato.append(row["Product_brand"])

        cursor.close()
        connection.close()
        return risultato


    @staticmethod
    def get_retailer():
        connection = DBConnect.get_connection()
        cursor = connection.cursor(dictionary=True)

        query = """select * 
                from go_retailers gr"""

        cursor.execute(query)
        risultato = []
        for row in cursor:
            risultato.append(Retailer(**row))

        cursor.close()
        connection.close()
        return risultato

    @staticmethod
    def get_top_vendite():
        connection = DBConnect.get_connection()
        cursor = connection.cursor(dictionary=True)

        query = """select Date as data, (gds.Quantity*gds.Unit_sale_price) as ricavo, gds.Retailer_code as retailer_code, gds.Product_number as product_number
                from go_daily_sales gds
                order by (gds.Quantity*gds.Unit_sale_price) desc"""

        cursor.execute(query)
        risultato = []
        for row in cursor:
            if row['data']:
                row['data'] = str(row['data'])
            risultato.append(Vendita(**row))

        cursor.close()
        connection.close()
        return risultato

    @staticmethod
    def get_codici_prodotto_brand(brand):
        connection = DBConnect.get_connection()
        cursor = connection.cursor(dictionary=True)

        query = """select gp.Product_number
                from go_products gp
                where gp.Product_brand = %s"""

        cursor.execute(query, (brand,))
        risultato = []
        for row in cursor:
            risultato.append(row["Product_number"])

        cursor.close()
        connection.close()
        return risultato
