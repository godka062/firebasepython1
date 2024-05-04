import os
import firebase_admin
from firebase_admin import credentials, initialize_app

# 환경 변수에서 자격 증명 정보를 읽어옵니다.
firebase_type = os.getenv('firebase_type', 'service_account')
project_id = os.getenv('firebase_project_id', 'your-default-project-id')
private_key_id = os.getenv('firebase_private_key_id', 'your-private-key-id')
private_key = os.getenv('firebase_private_key', 'your-private-key').replace('\\n', '\n')
client_email = os.getenv('firebase_client_email', 'your-client-email')
client_id = os.getenv('firebase_client_id', 'your-client-id')
auth_uri = os.getenv('firebase_auth_uri', 'https://accounts.google.com/o/oauth2/auth')
token_uri = os.getenv('firebase_token_uri', 'https://oauth2.googleapis.com/token')
auth_provider_x509_cert_url = os.getenv('firebase_auth_provider_x509_cert_url', 'https://www.googleapis.com/oauth2/v1/certs')
client_x509_cert_url = os.getenv('firebase_client_x509_cert_url', 'https://www.googleapis.com/robot/v1/metadata/x509/your-client-x509-cert-url')

cred_obj = {
    "type": firebase_type,
    "project_id": project_id,
    "private_key_id": private_key_id,
    "private_key": private_key,
    "client_email": client_email,
    "client_id": client_id,
    "auth_uri": auth_uri,
    "token_uri": token_uri,
    "auth_provider_x509_cert_url": auth_provider_x509_cert_url,
    "client_x509_cert_url": client_x509_cert_url
}

# 파이어베이스 앱을 초기화합니다.
cred = credentials.Certificate(cred_obj)
app = initialize_app(cred)
