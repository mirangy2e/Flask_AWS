import os

BASE_DIR = os.path.dirname(__file__)

# 데이터베이스 접속 주소
# pybo.db 라는 데이터베이스 파일이 프로젝트 홈 디렉토리 바로 밑에 저장 됨
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
#SQLAlchemy의 이벤트를 처리하는 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev"