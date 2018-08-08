
"""
This purpose of this project is 
- to read some given text and extract simplified relations from them
- to read some given text and produce a knowledge graph of
  learned entities and their relations to each other.
"""

# sense2vec==0.6.0
# spacy==2.0.11

import pandas as pd
import numpy as np
from tools import debugger
from tools import corpus
from pipeline_creator import nlp

debugger.print_log(nlp.pipeline, 'overview')

def learn_from_document(doc):
  analyzed_doc = nlp(doc)
  for ent in analyzed_doc._.graph_entities:
    debugger.print_log(ent, 'temp')

  # for sent in analyzed_doc.sents:
  #   if sent._.has_fact:
  #     debugger.print_log(sent, 'temp')
  #     debugger.print_log(sent._.fact, 'temp')
  #     debugger.print_log('-----------', 'temp')
  #
  # started = False
  # tokens = []
  # for token in analyzed_doc:
  #   if token.ent_type_ in ['PERSON', 'ORG']:
  #     if (started):
  #       tokens[-1] = tokens[-1] + ' ' + str(token)
  #     else:
  #       tokens.append(str(token))
  #     started = True
  #     debugger.print_log(token.ent_type_, 'temp')
  #     debugger.print_log(token.pos_, 'temp')
  #     debugger.print_log(token, 'temp')
  #     debugger.print_log('-----------', 'temp')
  #   else:
  #     started = False
  # print(set(tokens))

if __name__ == "__main__":
  docs = corpus.load_files()
  doc = docs[1]
  print(doc)
  learn_from_document(doc)
