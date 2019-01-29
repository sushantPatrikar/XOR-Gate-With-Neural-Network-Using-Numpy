from tkinter import *
import numpy as np
import math
import random

# Author:- Sushant Patrikar
root = Tk()


class Gui:
    # Initialization of weights and variable
    def __init__(self, master):
        self.learningRate = DoubleVar()
        self.learningRate.set(0.1)
        self.lr = DoubleVar()

        self.inputNeurons = 2
        self.outputNeurons = 1
        self.hiddenNeurons = IntVar()
        self.hiddenNeurons.set(2)

        self.entryXVar = IntVar()
        self.entryYVar = IntVar()
        self.ans = IntVar()
        self.epoch = IntVar()

        self.epoch.set(1)
        self.training = StringVar()
        self.training.set('')
        self.expectedAnswer = IntVar()

        # GUI part
        labelX = Label(master, text='X:')
        labelX.grid(row=0, column=0)

        entryX = Entry(master, textvariable=self.entryXVar)
        entryX.grid(row=0, column=1, padx=5)

        labelY = Label(master, text='Y:')
        labelY.grid(row=1, column=0)

        entryY = Entry(master, textvariable=self.entryYVar)
        entryY.grid(row=1, column=1, pady=5, padx=5)

        labelHiddenLayer = Label(master, text='No. of hidden Neurons: ')
        labelHiddenLayer.grid(row=2, column=0)

        entryHiddenLayer = Entry(master, textvariable=self.hiddenNeurons)
        entryHiddenLayer.grid(row=2, column=1)

        buttonSet = Button(master, text='Set', command=self.set)
        buttonSet.grid(row=2, column=2, padx=5)

        labelLearningRate = Label(master, text='Learning Rate: ')
        labelLearningRate.grid(row=3, column=0)

        entryLearningRate = Entry(master, textvariable=self.learningRate)
        entryLearningRate.grid(row=3, column=1)

        labelEpochs = Label(master, text='No. of epochs:')
        labelEpochs.grid(row=4, column=0)

        entryEpochs = Entry(master, textvariable=self.epoch)
        entryEpochs.grid(row=4, column=1)

        buttonTrain = Button(master, text='   Train   ', command=self.train)
        buttonTrain.grid(row=5, column=1, pady=5)

        buttonPredict = Button(master, text='  Predict  ', command=self.predict)
        buttonPredict.grid(row=7, column=1)

        labelAnswer = Label(master, text='Answer:')
        labelAnswer.grid(row=8, column=0)

        entryAnswer = Entry(master, textvariable=self.ans)
        entryAnswer.grid(row=8, column=1, pady=10)

        labelExpectedAnswer = Label(master, text='Expected Answer:')
        labelExpectedAnswer.grid(row=9, column=0, pady=5)

        entryExpectedAnswer = Entry(master, textvariable=self.expectedAnswer)
        entryExpectedAnswer.grid(row=9, column=1)

        # Initialization of weights
        self.inhiW = np.random.random((self.hiddenNeurons.get(), self.inputNeurons))
        self.hioW = np.random.random((self.outputNeurons, self.hiddenNeurons.get()))
        self.inhiB = np.random.random((self.hiddenNeurons.get(), 1))
        self.hioB = np.random.random((self.outputNeurons, 1))
        self.sigmoid_v = np.vectorize(self.sigmoid)  # Vectorization of sigmoid function

    # Sigmoid function as the activation function for neurons
    def sigmoid(self, x):
        return (1 / (1 + math.exp(-x)))

    # Setting the no. of neurons in hidden layer and initializing weights & biases according to it
    def set(self):
        self.inhiW = np.random.random((self.hiddenNeurons.get(), self.inputNeurons))
        self.hioW = np.random.random((self.outputNeurons, self.hiddenNeurons.get()))
        self.inhiB = np.random.random((self.hiddenNeurons.get(), 1))

    # Training
    def backpropagation(self, X, Y):
        if (X == Y):
            target = np.matrix([0])
        else:
            target = np.matrix([1])

        # Feedforward

        self.inputL = np.matrix([X, Y]).T
        self.hiddenL = self.inhiW.dot(self.inputL)
        self.hiddenL = self.sigmoid_v(self.hiddenL + self.inhiB)
        self.outputL = self.hioW.dot(self.hiddenL)
        self.outputL = self.sigmoid_v(self.outputL + self.hioB)

        # Backpropagation

        outputErrors = target - self.outputL
        x = np.multiply(self.outputL, 1 - self.outputL)
        hiddenGradient = np.multiply(self.hiddenL, 1 - self.hiddenL)
        hiddenErrors = (self.hioW.T).dot(outputErrors)
        deltaWho = (self.lr.get() * (np.multiply(outputErrors, x))).dot(self.hiddenL.T)
        deltaWih = (self.lr.get() * (np.multiply(hiddenErrors, hiddenGradient))).dot(self.inputL.T)
        deltaBih = (self.lr.get() * (np.multiply(hiddenErrors, hiddenGradient)))
        deltaBho = (self.lr.get() * (np.multiply(outputErrors, x)))

        # Updating the weights & biases

        self.hioW += deltaWho
        self.inhiW += deltaWih
        self.inhiB += deltaBih
        self.hioB += deltaBho

    # Predicting the answer after training
    def predict(self):
        self.inputL = np.matrix([self.entryXVar.get(), self.entryYVar.get()]).T
        self.hiddenL = self.inhiW.dot(self.inputL)
        self.hiddenL = self.sigmoid_v(self.hiddenL + self.inhiB)
        self.outputL = self.hioW.dot(self.hiddenL)
        self.outputL = self.sigmoid_v(self.outputL + self.hioB)
        # print(self.outputL.item())
        self.ans.set((self.outputL.item()))
        if (self.entryXVar.get() == self.entryYVar.get()):
            target = 0
        else:
            target = 1
        self.expectedAnswer.set(target)

    # Driver function for feedforward & Backpropagation
    def train(self):
        self.lr.set((self.learningRate.get()))
        self.training.set('Training...')
        self.labelTraining = Label(root, textvariable=self.training)
        self.labelTraining.grid(row=6, column=1)
        for _ in range(self.epoch.get()):
            for i in range(100000):
                X = random.randrange(0, 2)
                Y = random.randrange(0, 2)
                self.backpropagation(X, Y)
        self.training.set('Training Complete')
        print('Training complete')


Gui(root)
root.title('XOR')
root.mainloop()
