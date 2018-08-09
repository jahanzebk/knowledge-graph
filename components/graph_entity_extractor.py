
from spacy.tokens import Token, Span, Doc
from spacy.matcher import Matcher
from model.graph_entity import GraphEntity

class GraphEntityExtractor(object):
  name = 'graph_entity'

  # given a list of tokens in which the entity is, 
  # returns text for entity and last token index relative to start
  def get_entity_parts(self, ent):
    # only include upto last PROPN
    last_propn_index = 0
    for i, word in enumerate(ent):
      if word.pos_ == 'PROPN':
        last_propn_index = i
    entity_main_parts = ent[:last_propn_index + 1]

    return entity_main_parts

  # set graph entity related extensions
  def __init__(self, nlp):
    self.nlp = nlp
    if self.nlp.has_pipe('graph_entity'):
      self.nlp.remove_pipe('graph_entity')

    Token.set_extension('is_graph_entity', default=True)
    Doc.set_extension('graph_entities', default=[]) # string describing fact

  # find and label entities that qualify as graph entities
  # set an array of these as a Doc property
  def __call__(self, doc):
    doc_graph_entities = []
    current_ent = []
    chain_started = False
    for token in doc:
      if token.ent_type_ in ['ORG', 'PERSON', 'NORP', 'FACILITY', 'GPE', 'LOC']:
        token._.set('is_graph_entity', True)
        if not chain_started:
          current_ent.append(token)
          chain_started = True
        else:
          current_ent.append(token)
      else:
        if chain_started:
          graph_ent_parts = self.get_entity_parts(current_ent)
          graph_ent = GraphEntity(graph_ent_parts)
          if graph_ent.entity_text not in [ent.entity_text for ent in doc_graph_entities]:
            doc_graph_entities.append(graph_ent)
          current_ent = []
        chain_started = False
    doc._.set('graph_entities', doc_graph_entities)
    return doc
