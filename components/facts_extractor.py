
from spacy.tokens import Token, Span
from spacy.matcher import Matcher
from components import fact_matcher_rules

class FactsExtractor(object):
  name = 'facts'

  # make sure the token matches all requirements set by identifier object
  # search up if there's a dynamic way to do this.
  # pos_, _.is_graph_entity, dep_
  # and, or
  # lemma_, optional etc.
  # this should probably be it's own class
  # identifier is a dictionary e.g. { 'DEP_': '', 'AND': [IDENTIFIERS]}
  # ROUGHLY WRITTEN, WONT WORK
  def token_matches(self, token, identifier):
    matching = True
    for spec_key, spec_val in identifier.items():
      if spec_key == 'DEP_':
        matching = matching and token.dep_ == spec_val
      if spec_key == 'POS_':
        matching = matching and token.pos_ == spec_val
      if spec_key == 'is_graph_entity':
        matching = matching and token._.is_graph_entity == spec_val
      if spec_key == 'AND':
        bools_arr = [token_matches(token, next_id) for next_id in spec_val]
        matching = matching and all(bools_arr)
      if spec_key == 'OR':
        bools_arr = [token_matches(token, next_id) for next_id in spec_val]
        matching = matching and any(bools_arr)
    return matching

  def sentence_matches(self, sentence, pattern):
    pattern_index = 0
    match_start = -1
    match_end = -1
    pattern_len = len(pattern)
    for i, token in enumerate(sentence):
      if self.token_matches(token, pattern[pattern_index]):
        if pattern_index == 0:
          match_start = i
        pattern_index += 1

      if pattern_index >= pattern_len:
        match_end = i+1
        return sentence[match_start:match_end]
    return None


# nsubj:NER nsubj:NER verb,ROOT dobj pobj:NER
  # layer on top of matcher to find if matcher matched a "fact" by more complex rules
  def check_if_has_fact(self, sent):
    patterns = fact_matcher_rules.rules
    for pattern in patterns:
      fact_span = self.sentence_matches(sent, pattern)
      if fact_span is not None:
        sent._.set('has_fact', True)
        sent._.set('fact', fact_span)
        return True
    return False

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
      has_fact = self.check_if_has_fact(sent)
      # if has_fact:
      #   sent._.set('has_fact', True)
        # MAIN POINT OF IMPROVEMENT: get the "fact" better
        # sent._.set('fact', sent[?:?])
    return doc
