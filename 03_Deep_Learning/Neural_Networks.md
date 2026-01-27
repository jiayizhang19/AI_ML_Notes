### Traditional ML V.S. Deep Learning
| Traditional ML | Deep Learning|
|---|---|
|Relies on hand-crafted features. Feature engineering is slow, expensive, and requires deep domain knowledge | Automatically learns rich, meaningful feature representations from the raw data.|
|Assumes that features are independent of each other. This simplifies computations but loss content.|Better context-modelling due to less independence assumptions.|

### Neural Network Architecture
- Neuron: A neuron refers to a single computational unit in a layer.
- Layers:
    - Input Layer: Receives the raw data and passes this to the hidden layers.
    - Hidden Layer: Performs most of the computations and complex feature extraction. It is usually better to add more layers than neurons per layer.
    - Output Layer: Produces the final prediction of the network. The size of the output layer is determined by the number of predictions required.
- Activation Function: Introduces non-linearity to allow the network to lean complex, curved boundaries.
- Loss Function: 
    - Regression: MSE
    - Classification: Cross-entropy
- Hyperparameters:
    - Batch Size: Start with a low batch size and increase.
    - Epoch: Start with large epochs and use early stopping when performance stops improving.
    - Learning Rate: Start very low and multiply it by a constant until it reaches a high value
    - Early Stopping: Regularization techniques to reduce overfitting and improving generalization during training.
    - Dropout: Large models with many parameters are more prone to overfitting, which benefits more from dropout.
- Training / Optimization:
    - Cost / Loss function: Forward pass
    - Gradient Descent (Derivative of Loss): Backward pass (backpropagration)

- Feedforward Neural Networks (FNN) / MultiLayer Perceptron (MLP)