
from spacy.tokens import Token, Span
from spacy.matcher import Matcher

class FactsExtractor(object):
  name = 'facts'

# nsubj:NER nsubj:NER verb,ROOT dobj pobj:NER
  # layer on top of matcher to find if matcher matched a "fact" by more complex rules
  def pattern_matcher(sent):
    pass

  # define the matcher rules
  # and set_extensions on Spans (sentences)
  def __init__(self, nlp):
    self.nlp = nlp
    if self.nlp.has_pipe('facts'):
      self.nlp.remove_pipe('facts')
    self.matcher = Matcher(nlp.vocab)
    # MAIN POINT OF IMPROVEMENT: get the "reg exp" better
    self.matcher.add('FACT', None, [{'DEP': 'nsubj'}], [{'DEP': 'ROOT'}], [{'DEP': 'dobj'}])

    Span.set_extension('has_fact', default=False)
    Span.set_extension('fact', default="") # string describing fact

  # modify the span's attributes to hold the relevant info
  # using the matcher defined in init
  def __call__(self, doc):
    doc_facts = []
    for sent in doc.sents:
      matches = self.matcher(sent.as_doc())
      # print([m.dep_ for m in sent])
      # print(matches)
      if len(matches) > 0:
        sent._.set('has_fact', True)
        # MAIN POINT OF IMPROVEMENT: get the "fact" better
        sent._.set('fact', sent[matches[0][1]:matches[-1][2]])
    return doc
