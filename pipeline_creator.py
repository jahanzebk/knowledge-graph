import spacy
from sense2vec import Sense2VecComponent
from components.facts_extractor import FactsExtractor
from components.graph_entity_extractor import GraphEntityExtractor

nlp = spacy.load('en')

# s2v = Sense2VecComponent('reddit_vectors-1.1.0/')
# nlp.add_pipe(s2v)

graph_entity_extractor_component = GraphEntityExtractor(nlp)
nlp.add_pipe(graph_entity_extractor_component)

# may eventually rely on sense2vec component
fact_extractor_component = FactsExtractor(nlp)
nlp.add_pipe(fact_extractor_component)
