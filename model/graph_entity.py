
# will import neo4j here

class GraphEntity(object):
  def __init__(self, tokens):
    self.tokens = tokens
    self.entity_text = self.get_entity_text()
    self.alternative_names = []
    self.gender = ''

  def get_entity_text(self):
    return ' '.join([str(token) for token in self.tokens])

