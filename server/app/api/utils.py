import jwt
from rest_framework_jwt.utils import jwt_payload_handler

SECRET_KEY = "cnppgwua3!xa$)une9m#l%!_+g_*ec7-c$14*uuh#2322t(62t"


def create_token(user):
	payloads = jwt_payload_handler(user)
	token = jwt.encode(payloads, SECRET_KEY)
	return token.decode("unicode_escape")