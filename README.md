<p align="center">
  <a href="" rel="noopener">
 <img height=200px width=200px src="./img/neural_network.svg.png" alt="NeuralNetwork-logo"></a>
</p>
<h1 align="center">XOR-With-Numpy-Neural-Network</h1>

<div align="center">
<img src="https://img.shields.io/github/license/sushantPatrikar/XOR-Gate-With-Neural-Network-Using-Numpy">	
<img src="https://www.codefactor.io/repository/github/sushantpatrikar/xor-gate-with-neural-network-using-numpy/badge/master">
<img src="https://img.shields.io/github/issues-pr/sushantPatrikar/XOR-Gate-With-Neural-Network-Using-Numpy">
<img src="https://img.shields.io/github/stars/sushantPatrikar/XOR-Gate-With-Neural-Network-Using-Numpy">
<img src="https://img.shields.io/github/forks/sushantPatrikar/XOR-Gate-With-Neural-Network-Using-Numpy">
<img src="https://img.shields.io/github/issues/sushantPatrikar/XOR-Gate-With-Neural-Network-Using-Numpy">
<img src="https://img.shields.io/badge/PRs-welcome-informational">
</div>

<h4 align="center">XOR gate which predicts the output using Neural Network.</h4>
<hr>



### Python v3.6.5
## Libraries used:
1. numpy
2. tkinter
3. math
4. random
## Purpose
This project can be used for educational purposes as it gives user the freedom to change learning rate, number of neurons in hidden layer and number of epochs. User can compare the results after changing these values.
## Working
The Neural Network has 3 layers: input layer with 2 neurons, hidden layer, in which user can select the number of neurons according to them, and by default, it's value is 2, and output layer with 1 neuron. The first phase of neural network is training in which the possible values of (X,Y) goes as input [(0,0),(0,1),(1,0),(1,1)] with their respective answers [0,1,1,0]. The neural network modifies it's weights & biases according to the answers. After completion of training the neural network is ready to predict the answers.
## How to use
After executing the program, this window pops up

![image](https://user-images.githubusercontent.com/40419750/51909988-ee16af80-23f3-11e9-87be-cbbb724898db.png)

The user can select learning rate, number of neurons in hidden layer and number of epochs according to him, and then click on 'Set' button which sets the number of neurons in hidden layer, if changed by the user.
After changing them, click on 'Train' button, which trains your neural network to predict the output based on the inputs.

![image](https://user-images.githubusercontent.com/40419750/51910625-c6c0e200-23f5-11e9-824d-4d2cd70430b0.png)

Once the 'Training Complete' comes on the screen, the neural network is ready to predict the results.
Input X & Y, and then click on the 'Predict' button, the predicted result will be shown on the Answer box, which you can compare with the expected answer.

![image](https://user-images.githubusercontent.com/40419750/51912607-c2e38e80-23fa-11e9-9e14-ccf5465b26d3.png)



