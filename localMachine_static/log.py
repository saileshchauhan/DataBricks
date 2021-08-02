import logging
from decouple import config
FILE_PATH=config('log_file_path')
logging.basicConfig(filename=FILE_PATH,level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')