
# How to Increase Quality and Quantity of Facts

This is a very large problem that can be taken down to the semantic level.

- Read a few articles, and make note of what nature of information you would like to extract. Most likely, unless you go down to a very very semantic understanding of not just words, but sentences, you will need to focus on extracting certain bits of information. If you wish to think and focus more on sentence semantics, that is probably too ambitious but worth thinking about. Things you can extract however are still
 - quotes (said... or ...said with synonyms)
 - general connections between entities more like the paper you read on World War II articles
 - very specifically syntactically structured facts, i.e. you will miss a lot of information but get some    (very little) concrete information
 - on deep semantics, perhaps a neural net could be made using not only syntactic information but also semantic information, but this relies on being able to find a "neural network output layer" that represents a diverse type of inference, which will also maybe need to be manually created through multiple examples by people. (what about labelled output being triplets like THABO_MBEKI IS SOUTH AFRICAN PRESIDENT)
   - note that context (e.g. news articles in the present) also need to be given to make such inferences, hence limiting the application of the inferences to the source type.
   - how can we handle multiple inferences from the same sentence? (same input two possible outcomes?)
   - inferences also depend largely on correct entity coreference resolution with pronouns, etc.
   - in conclusion, good inferences depend on too much information from unsolved problems. All these things can be put into a neural net and a lot of data for learning, but would still probably take a knowledge base of it's own just to make inferences. This knowledge base might be a neural net or a bit more of a complicated mix of an underlying knowledge graph and a neural net to make the most inferences. Identify parts and work on those.
   - Even entity coreference resolution can be seen to be as a type of inference in itself, which depends on a wide variety of knowledge (e.g. trophy wont fit example) We will need to learn things about the tree structure of a dependency encoded in a neural net and what modifies what, not just order.

Now let's see how we can extract and use information from sentences on different levels to get better and better facts.


## EXISTING TOOLS TO ENHANCE

### Entity Coreference Resolution

Use https://github.com/huggingface/neuralcoref.


## LEXICAL LEVEL
As far as each word is concerned, we may want to try swap words with their synoynms, or other words they have a close sense2vec or word2vec vector with to help group facts together.

For example, if the ROOT VERB in a sentence is "killing" for one sentence and "murdered" for another sentence both conveying the same fact, maybe we can group them together by taking the lemma (murder/kill) and looking if their word vectors are close enough to consider them synonyms. We can also use data from concept.io.

### Graph Entities vs NER
Not everything the NER picks up should be a node in the graph (e.g. currencies shouldn't be but a political figure or country should be).


## SYNTACTIC LEVEL

### Pattern Matching

Create your own mini regexp system with spacy to quickly match sentence patterns .
(e.g. 
NSUBJ+GRAPH-ENTITY ... ROOT+VERB ... DOBJ+GRAPH-ENTITY)


## SEMANTIC LEVEL

### Word Profiles
One thing that could be useful is to create a database of word profiles that contain potential POS options, semantic word vectors, data from concept.io, synoynms, sentiment scores, and all sorts of syntactic information as well.

This information about each word can then be looked up and thrown into a neural networks input with other words of a sentence (e.g. the words: 'a', 'the', 'cat', etc.) and even named entities. The output of the neural network can then be a multitude of things e.g. inference triplets.

This can also include data for word models which may be useful in learning how the word can be used. Perhaps if a word can be used in a certain way, we can affirm something about it.

### The Neural Network

This would take each word in the sentence, look up it's word profile, use all that data in the neural network input and output whatever we plan on wanting to output.
