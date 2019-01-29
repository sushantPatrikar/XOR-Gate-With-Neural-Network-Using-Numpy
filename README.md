# XOR-With-Numpy-Neural-Network
XOR gate which predicts the output using Neural Network.
### Python v3.6.5
## Libraries used:
1. Numpy
2. Tkinter
3. Math
4. Random
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
![image](https://user-images.githubusercontent.com/40419750/51910961-9f1e4980-23f6-11e9-99c9-be43d6a4db8b.png)

Input X & Y, and then click on the 'Predict' button, the predicted result will be shown on Answer box, which you can compare with the expected answer.

