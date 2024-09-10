from dotenv import load_dotenv
import os
import logging

logging.basicConfig(filename= 'HWLogs.log',
                    level = logging.DEBUG,
                    format = '%(levelname)s LOG - %(asctime)s - %(message)s')

load_dotenv()

Hello=os.getenv("TASK")

print(Hello)

logging.info('This info log confirms the print of "Hello World!"')
