import logging
import configparser

# logging.basicConfig(level=logging.INFO)

# logger = logging.getLogger()
# hello_logger = logging.getLogger('Hello')
# recommende_logger = logging.getLogger(__name__)

# logger.error('nanana log')
# hello_logger.critical("nonon log")
# recommende_logger.info('just info log')

# logging.basicConfig()

# logger = logging.getLogger()

# logger.critical("Critical")
# logger.error("Error")
# logger.warning('Warning')
# logger.info('Info')

# logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a')

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

# logger.critical("Critical")
# logger.error("Error")
# logger.warning('Warning')
# logger.info('Info')

# FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

# logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a',\
#                     format=FORMAT)

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

# logger.critical("Critical")
# logger.error("Error")
# logger.warning('Warning')
# logger.info('Info')


config = configparser.ConfigParser()

print(config.read('config.ini'))

print('Sections:', config.sections(), '\n')

print('mariadb section:')
print('Host:', config['mariadb']['name'])
print('Database:', config['mariadb']['Name'])
print('Username:', config['mariadb']['user'])
print('Password:', config['mariadb']['password'], '\n')

print('redis section:')
print('Host:', config['redis']['host'])
print('Port:', int(config['redis']['port']))
print('Dataase number:', int(config['redis']['db']))

# Get method.
print('Host:', config.get('mariadb', 'host'))