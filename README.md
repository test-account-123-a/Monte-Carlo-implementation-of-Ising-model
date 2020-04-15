# Monte-Carlo-implementation-of-Ising-model

This is an instruction for the final project of Physics 77, 2020 Spring

group number: 4

group members: Haiyue Dong, Jose Rodriguez, Jinze Wu (arranged by last name)

The topic of final project is Monte Carlo Implementation on Ising Model

## Project Description

The Monte Carlo Implementation on Ising Model is a computational simulation that uses Metropolis 
Algorithem to effeciently select a finite set of lattice states under Boltzman distribution, and 
using these states to calculate magnitization, specific heat, correlation function of the system.
The project consists of simulation of Ising model using Monte Carlo method and visuliation of the
calculated result. Simulation should also be compare with the analytical solution, namely Onsager
solution.

## Term Explanation

1.**Ising model** is a 2D lattice whose Harmitonian equals to $-\sum_{<i,j>}*J*\sigma_j*\sigma_i$
  where J is a constant, \sum<i,j> denotes the sum over neareat lattice point
  
2.**Lattice** is a periodical structure of points that align one by one. 2D lattice can be plotted as:

    * * * * * * * *   
    * * * * * * * * 
    * * * * * * * *
    * * * * * * * *
    * * * * * * * *
    
  The points in lattice are called **lattice points**, **neareast lattice points** of point ^ are those 
  lattice points denoted by (*) shown in the graph below:
  
    * * * * * * * * 
    * * *(*)* * * *
    * *(*)^(*)* * *
    * * *(*)* * * *
    * * * * * * * *
    
  Each lattice point is denoted by a number i in the Harmitonian written above.
  
    * * * * * * * * 
    * * * * * * * *
    * * * * * * * *<-the i-th lattice point
    * * * * * * * *
    * * * * * * * *
    
  **Periodical strcture** means that lattice point at(1,1) is the same as that at(1,9) if the lattice 
  is 5 by 8. more e.g.(1,1)<=>(6,1), (2,3)<=>(2,11). A 2D lattice can be any Nx by Ny.
  The location (x,y) here is another denotion of lattice point that is fundementally same as i-th 
  lattice point denotation above.
  
    * * * * * * * * 5 
    * * * * * * * * 4
    * * * * * * * * 3
    * * * * * * * * 2
    * * * * * * * * 1
    1 2 3 4 5 6 7 8 
    
   The **state of lattice point**, which is also called **spin**, is +1 or -1, which is denoted by \sigma.
   The **state of lattice** is an array that shows the state of all lattice points points.
   The number of lattice points in our simulation is a finite numebr, Np, 
   
3.**Metropolis Algorithem**: For each step, randomize a new lattice state, use a random number in the 
                         range of (0,1) and compare it to e^(-\Delta H/kT), where \Delta H is the 
                         change of Harmitonian in the process of lattice state change, k is the 
                         Boltzman constant and T is the temperature. Accept or reject the new state 
                         by this comparison. After thousands times of randomization and selection, 
                         we can finally get a finite set of lattice states under Boltzman distribution.

4.**Magnitizaiton** of a lattice state is the average spin of all lattice points times -h\mu
  $M = -h\mu \sum_i \sigma_i$
  Here we only calculate the magnitizaiton of the final state.
  Final state is the last accpted state in the process of Monte Carlo.
  
5.**Specitic heat** of a grid is the variance of energy of all accepted state over T^2.
  $c_v = \frac{1}{T^2}*(<E^2>-<E>^2)$
  where <E> is the sum of energy of all accepted state, <E^2> is the sum of energy^2

6.Coherence function between two spins \simga_i and \sigma_j is the 

## Instruction Detail

The whole project is divided into simulation part and visualization part. First, the 


### Simulation

1.First we need

2.Second we need

3.Third

4.Forth

### Visualization

balabalabala

### Optimization

This part will be done if time perimits.
# test edit
