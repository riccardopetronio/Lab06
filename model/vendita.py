from dataclasses import dataclass

@dataclass
class Vendita:
    data: str
    ricavo: int
    retailer_code: int
    product_number: int

    def __hash__(self):
        return hash((self.data, self.product_number, self.product_number))

    def __eq__(self, other):
        return self.data == other.data and self.product_number == other.product_number and self.ricavo == other.ricavo and self.retailer_code == other.retailer_code

    def __str__(self):
        return f"Data: {self.data}, Ricavo:{self.ricavo}, Retailer:{self.retailer_code}, Product:{self.product_number}"