# Policies

Keep research steps away, try just finish the overall picture of a knowledge graph to avoid wasting time on research that may or may not go somewhere.

As far as accuracy is concerned, we'd rather miss facts than pick up things that aren't facts, that way quantity can make up for it hopefully to some extent.

# STORIES =====================================

A way of breaking tasks down.

## In Progress
- [EPIC] Create a spacy pipeline to create and store data according to the schema.

- organize things into folders

- [LEXICAL] make a graph entity object

- Make a git repo

- [SYNTACTIC] Run DEP parser and extract "facts" by regexps (Xsub ... ROOT ... Xobj). Make this component more versatile. Patterns can be defined multiple ways
  - existing regexp methods
  - custom regexp parser using spacy id numbers or strings
  - a function for each match rule

- [LEXICAL] Make a Fact Normalizer to look for other facts on that entity with synonym/same base/same concept root words and combine multiple sentences to be under one ACTION word (first ROOT verb found).

- [OTHER] Set up and experiment with what the data from the neural co ref library looks like

- extend debugger

- clean up code

- test all code written so far

- create neo4j basic schema
- [SEMANTIC] set up mysql or nosql schema for word profiles DB.

## Icebox
- Get text database to work on
- Get facts out in a modularized fashion to be passed in to knowledge graph creator.
- [Neo4j] Integrate Neo4J to take extracted facts and create graph and add to graph in a simple manner.
- [Neo4j] Set up Neo4J to be queried to.
- Set up a system that allows certain fact extraction rules to use semantic web on certain words in the pattern to make inferences.
- Use Pronoun entity coreferencing from Stanford NLP to enhance finding more facts.
- Consider how you can use conceptnet.io web api or personal build (needs 30GB RAM) (https://github.com/commonsense/conceptnet5/wiki/API)

## Completed
- Set up basic pipeline system to build on.
- Read this 2012 thesis: https://digitalcommons.trinity.edu/cgi/viewcontent.cgi?article=1028&context=compsci_honors
- Decided to stick to spacy since stanford semantic graph is really just dependency graphs and I need to get something done.
- Get some documents to work on and create a class to read them in.
- Load in docs
- created debugger
- Run NER and store entities if an entity is a
    PERSON
    NORP
    FACILITY
    ORG
    GPE
    LOC 
  and is also has atleast one proper noun? Make a separate pipeline component for this. Can you create a span around these?
