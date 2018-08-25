
rules = [
  [{'DEP_': 'nsubj'}, {'DEP_': 'ROOT', 'POS_': 'VERB'}, {'DEP_': 'dobj'}],
  [{'is_graph_entity': True}, {'DEP_': 'ROOT', 'POS_': 'VERB'}, {'is_graph_entity': True}],
]

# HOW can you make a rule system that allows for something like:
# if a negation is connected to some sort of DEP type (e.g ROOT or whatever),
# then that is accounted for, otherwise the opposite is taken to be true.
# optional negation matches as seperate patterns
# [{ 'my_ent_type_': 'ValidEntityNode' }, { 'or': [{ 'dep_': 'ROOT', 'pos_': 'VERB' }, { 'dep_': 'pobj' }]}]
# where ValidEntityNode is set for spans of tokens that are noun entities we want in the graph.
