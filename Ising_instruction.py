# This is an instruction to the whole project, which shows the basic structure of code and guides the following work.
# for the functions below, we need to write arguments, return variables and a brief description for each of them.
# unfinished yet

import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt
import scipy.special as sc

#Simulation part
def initialize_lattice(N):
    ''' 
    The initialization of lattice should be the first step of simulation. In this function, 
    we give the lattice a random initial state by built-in function, the 
    
    arguments:
    N: the number of lattice points
    
    return values:
    initial_lattice_state: the initial state generalized by this function
                           it a numpy array whose elements equals to +1 or -1
    '''
    return initial_lattice_state


def spin_flip(lattice_state,algorithem):
    '''
    For Metropolis algorithem
    Randomly flip a spin, namely ranmonly choose a lattice point and change the state 
    of it from +1 to -1 or from -1 to +1 once a time to generate a new state of lattice.
    For Wolff algorithem
    Filp spins of a group of lattice points
    
    arguments: 
    lattice_state: the state of lattice that is going to be changed
    algorithem: M or W, where M denotes Metropolis algorithem, W is Wollf algorithem
                we firstly need to finish the Metropolis and then use Wolff to optimize
    
    return values:
    new_state: the state of lattice after spin flipping
    '''
    return new_state


def Monte_Carlo(lattice_state_1,lattice_state_2):
    '''
    If the old state of lattice and a new state of lattice are given, use Metropolis Algorithm to determine whether
    we should accept it or not.
    arguments:
    lattice_state_1: the state of lattice before spin change
    lattice_state_2: the state of lattice after spin change
    
    return values:
    if_accept: whether the new state(state_2) is accepted or not
               if_accept equals to True when it is accepted and it equals to False when it is rejected.
    current_state: if new state is accpeted, then current_state is state 2; otherwise, current_state is state 1
    '''
    return if_accept, current_state



def Ising_simulation(N,N_step,ifcorr,corr):
    '''
    arguments:
    N: the number of lattice points
    N_step: the number of simulation
    ifcorr: whether calculate the correlation function or not
    corr: the distance of two lattice points ??????????
    
    return value:
    final_lattice_state: 
    energy: 
    magenetization: 
    specific_heat: 
    correlation_function: 
    
    '''
    return

def calculate_energy(lattice_state):
    '''
    '''
    return energy

def calculate_magnetization(lattice_state):
    '''
    '''
    return magnetization

#???????maybe this part should be put inside the simulation function?????????
def calculate_specific_heat(all_accepted_energy):
    '''
    '''
    return specific_heat

def calculate_correlation_function(all_accepted_lattice_state):

#Visualization part
def plot_lattice(lattice_state):
    '''
    plot a 2D gird that shows the state of each lattice point
    spin up(+1) is denoted by black cubic
    spin down(-1) is denoted by white cubic
    
    arguments:
    lattice_state
    
    return value:
    none
    '''
    return

def plot_energy(energy_data):
    '''
    '''
    return

def plot_magnetization(magnetization_data):
    '''
    '''
    return

def plot_specific_heat(specific_heat_data):
    '''
    '''
    return

def plot_correlation_function(correlation_function_data):
    '''
    '''
    return
