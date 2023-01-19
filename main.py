import jwt
from datetime import datetime, timedelta
from app import jsonify, request, create_app
from auth import token_required
from src.customer import Customer
from src.product import NewProduct
from src.plan import ContractPlan
from src.aporte_extra import NewAporteExtra
from src.rescue import Rescue

# Carrega os dados do json e cria a instancia do flask
app = create_app()

@app.route('/api/v1/auth', methods=['POST'])
def get_token():

    # Em caso real o jwt iria pegar os dados do usuario no banco e gerar o jwt e dentro do @token_required ele iria verificar se é um usuário válido e validar
    def exp():
        return datetime.utcnow() + timedelta(minutes=1000)

    payload = {
        'email': 'test@test.com',
        'exp':exp()
    }
    user = {        
        'email': 'test@test.com',
        'name': 'test',
    }

    token = jwt.encode(payload, app.config['SECRET_KEY'])

    return jsonify({'status': 200, 'token': f'{token}', 'exp': str(payload['exp'])[0:19], 'user': user})

@app.route('/api/v1/customer', methods=['POST'])
@token_required
def customer():

    body = request.get_json()

    if not 'cpf' in body:
        return jsonify({'status': 400, "message": 'cpf not found'})

    if not 'nome' in body:
        return jsonify({'status': 400, "message": 'nome not found'})

    if not 'email' in body:
        return jsonify({'status': 400, "message": 'email not found'})

    if not 'dataDeNascimento' in body:
        return jsonify({'status': 400, "message": 'dataDeNascimento not found'})

    if not 'sexo' in body:
        return jsonify({'status': 400, "message": 'sexo not found'})

    if not 'rendaMensal' in body:
        return jsonify({'status': 400, "message": 'rendaMensal not found'})

    cpf = body['cpf']
    name = body['nome']
    email = body['email']
    birthdate = body['dataDeNascimento']
    genre = body['sexo']
    valueMonthly = body['rendaMensal']

    return Customer(cpf, name, email, birthdate, genre, valueMonthly).new_customer()

@app.route('/api/v1/product', methods=['POST'])
@token_required
def product():

    body = request.get_json()

    if not 'nome' in body:
        return jsonify({'status': 400, "message": 'name not found'})

    if not 'susep' in body:
        return jsonify({'status': 400, "message": 'susep not found'})

    if not 'expiracaoDeVenda' in body:
        return jsonify({'status': 400, "message": 'expiracaoDeVenda not found'})

    if not 'valorMinimoAporteInicial' in body:
        return jsonify({'status': 400, "message": 'valorMinimoAporteInicial not found'})

    if not 'valorMinimoAporteExtra' in body:
        return jsonify({'status': 400, "message": 'valorMinimoAporteExtra not found'})

    if not 'idadeDeEntrada' in body:
        return jsonify({'status': 400, "message": 'idadeDeEntrada not found'})

    if not 'idadeDeSaida' in body:
        return jsonify({'status': 400, "message": 'idadeDeSaida not found'})

    if not 'carenciaInicialDeResgate' in body:
        return jsonify({'status': 400, "message": 'carenciaInicialDeResgate not found'})

    if not 'carenciaEntreResgates' in body:
        return jsonify({'status': 400, "message": 'carenciaEntreResgates not found'})

    name = body['nome']
    susep = body['susep']
    seller_expiration = body['expiracaoDeVenda']
    min_value = body['valorMinimoAporteInicial']
    min_value_extra = body['valorMinimoAporteExtra']
    age_min = body['idadeDeEntrada']
    age_final = body['idadeDeSaida']      
    initial_Redemption  = body['carenciaInicialDeResgate']   
    grace_period_between_redemptions = body['carenciaEntreResgates']        

    return NewProduct(name, susep, seller_expiration, min_value, min_value_extra, age_min, age_final, initial_Redemption, grace_period_between_redemptions).new_product()

@app.route('/api/v1/contracting-plan', methods=['POST'])
@token_required
def contracting_plan():    

    try:
        body = request.get_json()
    except:
        return jsonify({"message": 'Invalid json requests'})

    if not 'idCliente' in body:
        return jsonify({'status': 400, "message": 'idCliente not found'})

    if not 'idProduto' in body:
        return jsonify({'status': 400, "message": 'idProduto not found'})

    if not 'aporte' in body:
        return jsonify({'status': 400, "message": 'aporte not found'})

    if not 'dataDaContratacao' in body:
        return jsonify({'status': 400, "message": 'dataDaContratacao not found'})
    
    id_customer = body['idCliente']
    id_product = body['idProduto']
    aporte = body['aporte']
    birtdate_plan = body['dataDaContratacao']
    
    return ContractPlan(id_customer, id_product, aporte, birtdate_plan).new_plan()

@app.route('/api/v1/extra-contribution', methods=['POST'])
@token_required
def extra_contribution():

    try:
        body = request.get_json()
    except:
        return jsonify({"message": 'Invalid json requests'})

    if not 'idCliente' in body:
        return jsonify({'status': 400, "message": 'idCliente not found'})

    if not 'idPlano' in body:
        return jsonify({'status': 400, "message": 'idPlano not found'})

    if not 'valorAporte' in body:
        return jsonify({'status': 400, "message": 'valorAporte not found'})
    
    id_customer = body['idCliente']
    id_plan = body['idPlano']
    aporte_value = body['valorAporte']

    return NewAporteExtra(id_customer, id_plan, aporte_value).new_extra_aporte() 

@app.route('/api/v1/plan-rescue', methods=['POST'])
@token_required
def plan_rescue():

    try:
        body = request.get_json()
    except:
        return jsonify({"message": 'Invalid json requests'})

    if not 'idPlano' in body:
        return jsonify({'status': 400, "message": 'idPlano not found'})

    if not 'valorResgate' in body:
        return jsonify({'status': 400, "message": 'valorResgate not found'})
    
    id_plan = body['idPlano']
    rescues_value = body['valorResgate']    

    return Rescue(id_plan, rescues_value).new_rescue()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)