import matplotlib.pyplot as plt
import numpy as np

class Probabilitycalculator:
    def __init__(self):
        pass

    @staticmethod
    def calculate_probability(p, e, i, j):
        if 0<=p and p<=1 and 0<=e and e<=1:
            pSending1 = p
            pSending0 = 1 - p
            pReceiving1Sending0 = e
            pReceiving0Sending1 = e
            pReceiving1Sending1 = 1 - e
            pReceiving0Sending0 = 1 - e
            pReceiving0 = (
                pReceiving0Sending0 * pSending0 +
                pReceiving0Sending1 * pSending1
            )

            pReceiving1 = (
                pReceiving1Sending0 * pSending0 +
                pReceiving1Sending1 * pSending1
            )

            pSending1Receiving0 = (
                pReceiving0Sending1 * pSending1) / pReceiving0
            pSending0Receiving1 = (
                pReceiving1Sending0 * pSending0) / pReceiving1
            pSending0Receiving0 = (
                pReceiving0Sending0 * pSending0) / pReceiving0
            pSending1Receiving1 = (
                pReceiving1Sending1 * pSending1) / pReceiving1

            conditional_prob = [
                [pSending0Receiving0, pSending0Receiving1],
                [pSending1Receiving0, pSending1Receiving1]
            ]

            return conditional_prob[i][j]
        else:
            return "Erorr=> your value is not between 0 and 1"

class Probability_plot:
    @staticmethod
    def create_plot(pSending1, color, i, j):
        pError = np.arange(0.1,1.1,0.1)

        conditional_probability = []
        for error in pError:
            conditional_probability.append(Probabilitycalculator.calculate_probability(p=pSending1,e=error,i=i,j=j))

        plt.plot(pError, conditional_probability,marker='o', color=color)

        plt.legend(["p = 0.1", "p = 0.5", "p = 0.9"])
        plt.xlabel("e")

    @staticmethod
    def figure():
        plt.figure(0)
        plt.title("P[T0|R1]")
        Probability_plot.create_plot(0.1, "#0000ff", i=0, j=1)
        Probability_plot.create_plot(0.5, "#ff0000", i=0, j=1)
        Probability_plot.create_plot(0.9, "#7fff00", i=0, j=1)
        plt.figure(1)
        plt.title("P[T0|R0]")
        Probability_plot.create_plot(0.1, "#0000ff", i=0, j=0)
        Probability_plot.create_plot(0.5, "#ff0000", i=0, j=0)
        Probability_plot.create_plot(0.9, "#7fff00", i=0, j=0)
        plt.figure(2)
        plt.title("P[T1|R0]")
        Probability_plot.create_plot(0.1, "#0000ff", i=1, j=0)
        Probability_plot.create_plot(0.5, "#ff0000", i=1, j=0)
        Probability_plot.create_plot(0.9, "#7fff00", i=1, j=0)
        plt.figure(3)
        plt.title("P[T1|R1]")
        Probability_plot.create_plot(0.1, "#0000ff", i=1, j=1)
        Probability_plot.create_plot(0.5, "#ff0000", i=1, j=1)
        Probability_plot.create_plot(0.9, "#7fff00", i=1, j=1)
        plt.show()

show = Probability_plot()
show.figure()
