### Transformers
- Strengths:
    - Parallelisation:
        - Transformers use self-attention to process a whole sentence in parallel, overcome speed and dependency limitations.
        - RNNs process text sequentially, meaning they analyse words one at a time. 
    - Long-term memory:
        - Transformers have a long-term memory.
        - RNNs suffer from the vanishing gradient problem which leads to long-term memory loss.
- Architecture:
    - Transformer Layers (**For feature extraction**): 
        - Token Embedding: Similar to word embeddings, but 
            - It is learned during model training or fine-tuning.
            - The token "bank" starts with an embedding, but its final representation changes depends on context. (e.g. river bank or financial bank)
        - Positional Encoding: Retains word order to allow parallelisation of training.
        - Attention: Allows the network to learn the interdependencies of words in sentenses and the larger text (long-term memory), so that the network can weigh the importance of all other input tokens when encoding the current one.
        - Residual Connection
        - Layer Normalization
        - MLP
    - Linear & Softmax Layers (**For prediction**):
        - Produce a probability distribution over the next possible output tokens.  

![Transformers Architecture](../Images/Transformers.png)
- Applications:
    - Transformer-based architecture
        - GPT: Decoder-only
        - BERT: Encoder-only
    - Limitations:
        - LLMs reply heavily on pattern matching, instead of genuine logical reasoning in mathematics.
        - Sensitive to small changes in input.
        - Inability to filter noise so that it cannot ignore irrelevant data.


### Recurrent NN
- Embeddings (For feature extraction):
    - A distributed lexical representation to represent words as continuous numerical vectors across many dimensions instead of discrete symbols in single location.
- Simple Recurrent Networks:
    - Processing sequential data word by word.
    - Short-term memory.
    - Dimensionality reduction using PCA.


### Embedding Models (Word2Vec, BERT)
Word Embedding: It is not an end-to-end architecture for sequence processing. They are embedding generator that can be used as input to other models.
    - A numeric vector input that represents a token (word or subword) in a lower-dimensional space.
    - It allows words with similar meanings to have a similar representation.
    - Benefits:
        - Preserve syntactical and semantic information.
        - Helps reduce dimensionality. (Before word embeddings, words were often presented as one-hot vectors.)
