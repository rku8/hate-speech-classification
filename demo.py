from hate.logger import *
from hate.exception import CustomException
import sys

logging.info("Hi, this is RAVI")

from hate.configuration.gcloud_syncer import GCloudSync

obj=GCloudSync()
obj.sync_folder_from_gcloud("hate-speech-2024", "dataset.zip","download/data.zip")


# from colorama import Fore, Style

# class MyClass:
#     def __init__(self, data):
#         self.data = data
    
#     def __str__(self):
#         return f"""
#                 {Fore.RED}{self.data}
#                 {Fore.BLUE}{self.data}{Style.RESET_ALL}
#                 """  # Returns red colored string

# # Example usage
# obj = MyClass("Hello, world!")
# print(obj)

