import numpy as np
import matplotlib.pyplot as plt

N = 4
T = 100
j = -0.5

class ising_state:
	def __init__(self):
		self.state  = np.random.randint(0,2,size=N)
		self.energy = 0

	def energy(self):
		for element in self.state:
			self.energy += element
		



A = ising_state()
print("etado    :",A.state)
A.energy()
print("energia  :",A.energy)


 