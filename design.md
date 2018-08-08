
## DESIGN
Create a spacy pipeline to create and store data according to the schema. Then work on increasing quality of data going in.

## SCHEMA

Nodes are entities. They have names, alternate names, and characteristics like gender, age, and job to help associate sentences more strongly with them.


Connections are ACTION verbs, augmented by select parts of the sentence as determined by dependency grammar of sentence relation was found in.

One connection has one ACTION (root) verb and multiple sentences. Each sentence has an article it was extracted from.

Hence we have 4 objects:
- Entities
- Connections
- Sentences - refs
- Articles  - refs

Improvement: ACTION verbs are verbs determined by the root verb, but also grouped together under synonyms. i.e. if two sentences have different root verbs but those root verbs are synonyms, the connection can be joined under one of those words.
