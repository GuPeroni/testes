from fake_db import record_data
from app import jsonify
from utils import return_file_in_path
from utils import read_json
from utils import convert_string_to_datetime

class Rescue:
    def __init__(self, id_plan, value_rescue):
        self.id_plan = id_plan
        self.value_rescue = value_rescue    

    def verify_valid_rescue(self):    
        path_plan = 'fake_db\\plans\\'
        file_plan = return_file_in_path(path_plan)
        json_plan = read_json(path_plan, file_plan)

        if self.value_rescue > json_plan['aporte']:
            return jsonify({"message": f"Value above the contracted value, maximum to be redeemed is {json_plan['aporte']}"})

        else:
            return None          

    def new_rescue(self):

        verify = self.verify_valid_rescue()
        if not verify:
                    
            rescue = {
                'id': 1,
                'idPlano': self.id_plan,
                'valorResgate': self.value_rescue               
            }

            return record_data('rescues', 'rescue', rescue)