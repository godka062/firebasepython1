import os
import firebase_admin
from firebase_admin import credentials, initialize_app

# 환경 변수에서 자격 증명 파일 경로 가져오기
cred_path = os.getenv('FIREBASE_CREDENTIALS')
if cred_path and os.path.exists(cred_path):
    cred = credentials.Certificate(cred_path)
    app = initialize_app(cred)
else:
    raise ValueError("Firebase credentials path is not set or invalid")
