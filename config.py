import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'e4bada5e477ce2ce2fa77110e0fca1d8db0793d9'
    SQLALCHEMY_DATABASE_URI = 'postgres://jkaoiknsmntcfp:85a5400e8b8fd6fb9a5b90482d40b68dcaaa' \
                              '938150643f861b1856ce30dd9bc7@ec2-204-236-228-169.' \
                              'compute-1.amazonaws.com:5432/d9ssmlvpnkaomm'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
