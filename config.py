HOSTNAME = 'host.docker.internal'
PORT = '3306'
DATABASE = 'zb_Platform'
USERNAME = 'root'
PASSWORD = '980505'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI  # 配置连接
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "asdsfasdafa1231415"

# 邮箱配置
MAIL_SERVER = "smtp.163.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "zhoubo1035@163.com"
MAIL_PASSWORD = "CWDFMFSTMSUTXKMO"
MAIL_DEFAULT_SENDER = "zhoubo1035@163.com"

