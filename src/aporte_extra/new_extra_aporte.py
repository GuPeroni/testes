from fake_db import record_data
from app import jsonify
from utils import read_json
from utils import return_file_in_path

class NewAporteExtra:
    def __init__(self, id_customer, id_plan, aporte_value):
        self.id_customer = id_customer
        self.id_plan = id_plan
        self.aporte_value = aporte_value

    def verify_valid_aporte(self):

        path_product = 'fake_db\\product\\'
        file_product= return_file_in_path(path_product)
        json_product = read_json(path_product, file_product)

        path_customer = 'fake_db\\customer\\'
        file_customer = return_file_in_path(path_customer)
        json_customer = read_json(path_customer, file_customer)

        if json_customer['id'] != int(self.id_customer.split('|')[0].strip()):
            return jsonify({"message": "Invalid customer"})

        if self.aporte_value < json_product['valorMinimoAporteExtra'] :
            return jsonify({"message": f"Minimum contribution amount at the time of hiring is {json_product['valorMinimoAporteExtra']}"}) 

        else:
            return None

    def new_extra_aporte(self):   

        verify_aporte = self.verify_valid_aporte()
        if not verify_aporte: 
            aporte_extra = {
                'id': 1,
                'idCliente': self.id_customer,
                'idPlano': self.id_plan,
                'valorAporte': self.aporte_value,           
            }

            return record_data('aporte_extra', 'newAporteExtra', aporte_extra)