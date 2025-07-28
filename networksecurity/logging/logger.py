import logging
import os
from datetime import datetime
filename=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=f"{os.path.join(os.getcwd(),'logs')}"
os.makedirs(log_path,exist_ok=True)
log_file_path=f"{os.path.join(log_path,filename)}"
logging.basicConfig(
    filename=log_file_path,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.info("This is a file")
