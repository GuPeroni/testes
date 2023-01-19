from fake_db import record_data
from utils import return_file_in_path
from utils import read_json
from utils import convert_string_to_datetime
from app import jsonify


class ContractPlan:
    def __init__(self, id_customer, id_product, aporte, birtdate_plan):
        self.id_customer = id_customer
        self.id_product = id_product
        self.aporte = aporte
        self.birtdate_plan = birtdate_plan

    def verify_valid_plan(self):    
        path_product = 'fake_db\\product\\'
        file_product = return_file_in_path(path_product)

        if not file_product:
            return jsonify({"message": "You not have products"})

        path_customer = 'fake_db\\customer\\'
        file_customer = return_file_in_path(path_customer)

        json_product = read_json(path_product, file_product)
        json_customer = read_json(path_customer, file_customer)

        if json_product['id'] != int(self.id_product.split('|')[0].strip()) or json_customer['id'] != int(self.id_customer.split('|')[0].strip()):
            return jsonify({"message": "Invalid product or customer"})
        
        if self.aporte < json_product['valorMinimoAporteInicial']:
            return jsonify({"message": f"Minimum contribution amount at the time of hiring is {json_product['valorMinimoAporteInicial']}"})

        if convert_string_to_datetime(self.birtdate_plan) < convert_string_to_datetime(json_product['expiracaoDeVenda']):
            return jsonify({"message": "Product Expired"})

        else:
            return None
     

    def new_plan(self):

        verify = self.verify_valid_plan()
        if not verify:

            plan = {
                'id': 1,
                'idCliente': self.id_customer,
                'idProduto': self.id_product,
                'aporte': self.aporte,
                'dataDaContratacao': self.birtdate_plan,            
            }

            return record_data('plans', 'newPlans', plan)