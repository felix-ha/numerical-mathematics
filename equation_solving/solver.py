import numpy as np
import pickle


class Solver:

    def __init__(self):
        with open('constants.pickle', 'rb') as f:
            save = pickle.load(f)
            self.epsilon_mach = save['epsilon_mach']
            self.step_length_derivatives = save['step_length_derivatives']
