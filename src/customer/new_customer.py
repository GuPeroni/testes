from fake_db import record_data
from app import jsonify

class Customer:
    def __init__(self, cpf, name, email, birthdate, genre, valueMonthly):
        self.cpf = cpf
        self.name = name
        self.email = email
        self.birthDate = birthdate
        self.genre = genre
        self.valueMonthly = valueMonthly 

    def new_customer(self):

        if len(self.cpf) < 11:
            return jsonify({"message": "Invalid cpf"})

        customer = {
            'id': 1,
            'cpf': self.cpf,
            'name': self.name,
            'email': self.email,
            'birthdate': self.birthDate,
            'genre': self.genre,
            'value_monthly': self.valueMonthly
        }

        return record_data('customer', 'newCustomer', customer)

