import glob
import os

# GIVEN A FOLDER FULL OF TXT FILES
# THIS MODULE LOADS THEM INTO MEMORY

path = 'bbc/business/'

def load_files():
  docs = []
  for filename in os.listdir(path):
    with open(path + filename) as file:
      doc = ''.join(file.readlines())
      docs.append(doc)
  return docs
