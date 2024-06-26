from datetime import timedelta

# 可以随便写 越长越安全解密越慢
SECRET_KEY = 'Flat-White'

# 访问令牌的过期时间为60分钟
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=60)
# 刷新令牌的过期时间为30天
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

# 数据库配置
# HOSTNAME = '127.0.0.1'
HOSTNAME = '10.129.86.238'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'
DATABASE = 'poetry_learning_platform'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
# 未配置邮箱账号以及授权码 如需使用请自行更改
MAIL_SERVER = 'smtp.qq.com'
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = '1608079002@qq.com'
MAIL_PASSWORD = 'aiwflpoglrexgeic'
MAIL_DEFAULT_SENDER = ("基于文生图大模型的古诗词学习平台", "1608079002@qq.com")

# 有道翻译API配置
APP_KEY = '00a1628544ff1cc0'
APP_SECRET = 'EhbsXAgBYRUPXt1FZ6APQKyXg4crVkIA'

# 百度AI配置
API_KEY = "XiyzILmvNdOVvpr9GqhQjJVb"
SECRET_KEY = "uW4G7oAV3QqcZRdRnfsW7xQ1t8rOwfPo"

# OpenAI API
OPENAI_API_KEY = ""

# 英译中
APP_KEY_C = '60fe49c5bcafe171'
APP_SECRET_C = 'IVnUAPXjj63Z4qBWU4gmCr2fUZyNZ59K'
