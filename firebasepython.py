import os
import firebase_admin
from firebase_admin import credentials, initialize_app

# Streamlit Secrets에서 자격증명 정보 가져오기
cred_obj = {
    "type": os.environ["firebase_type"],
    "project_id": os.environ["firebase_project_id"],
    "private_key_id": os.environ["firebase_private_key_id"],
    "private_key": os.environ["firebase_private_key"].replace('\\n', '\n'),
    "client_email": os.environ["firebase_client_email"],
    "client_id": os.environ["firebase_client_id"],
    "auth_uri": os.environ["firebase_auth_uri"],
    "token_uri": os.environ["firebase_token_uri"],
    "auth_provider_x509_cert_url": os.environ["firebase_auth_provider_x509_cert_url"],
    "client_x509_cert_url": os.environ["firebase_client_x509_cert_url"]
}

# 파이어베이스 초기화
cred = credentials.Certificate(cred_obj)
app = initialize_app(cred)
