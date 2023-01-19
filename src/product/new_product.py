from fake_db import record_data
from app import jsonify

class NewProduct:
    def __init__(self, name, susep, seller_expiration, min_value, min_value_extra, age_min, age_final, initial_Redemption, grace_period_between_redemptions):
        self.name = name
        self.susep = susep
        self.seller_expiration = seller_expiration
        self.min_value = int(min_value)
        self.min_value_extra = int(min_value_extra)
        self.age_min = int(age_min)
        self.age_final = int(age_final)
        self.initial_Redemption = int(initial_Redemption)
        self.grace_period_between_redemptions = int(grace_period_between_redemptions)

    def new_product(self):

        if self.min_value < 1000:
            return jsonify({"message": "Minimum contribution amount at the time of hiring is 1000"}) 

        if self.min_value_extra < 100:
            return jsonify({"message": "Minimum contribution amount at the time of hiring is 100"}) 

        if self.age_min < 18:
            return jsonify({"message": "Minimum age to purchase the product is 18 years old"}) 

        if self.age_final > 60:
            return jsonify({"message": "Maximum age to start enjoying the benefit is 60 years old"})  

        if self.initial_Redemption < 60:                           
            return jsonify({"message": "The grace period for making the first redemption is at least 60 days"})
        
        if self.grace_period_between_redemptions < 30:
            return jsonify({"message": "Grace period to carry out another redemption after a redemption carried out is at least 30 days"})
                
        product = {
            'id': 1,
            'name': self.name,
            'susep': self.susep,
            'expiracaoDeVenda': self.seller_expiration,
            'valorMinimoAporteInicial': self.min_value,
            'valorMinimoAporteExtra': self.min_value_extra,
            'idadeDeEntrada': self.age_min,
            'idadeDeSaida': self.age_final,
            'carenciaInicialDeResgate': self.initial_Redemption,
            'carenciaEntreResgates': self.grace_period_between_redemptions
        }

        return record_data('product', 'newProduct', product)