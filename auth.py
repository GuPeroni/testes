import jwt 
from functools import wraps
from app import jsonify, current_app, request

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'Authorization' in request.headers:
            token = dict(request.headers)['Authorization']
            if not token:
                return jsonify({'message': 'token is missing', 'data': []}), 401    
                       
            # Aqui ele descriptografa o jwt e verificaria no banco se é um user válido mas como está hardcoded eu só verifico se existe o algo na váriavel "data"
            data = jwt.decode(token.replace('Bearer ', ''), current_app.config['SECRET_KEY'], algorithms=['HS256'])
            if data:
                return current_app.ensure_sync(f)(*args, **kwargs)
            else:
                jsonify({'message': 'User not found'})          
        else:
            return jsonify({'message': 'token is missing', 'data': []}), 401
    return decorated
