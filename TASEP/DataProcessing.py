import numpy as np
import matplotlib.pyplot as plt

class DataProcessing():
    
    def __init__(self, result):
        self.density = result[0]
        self.current_particle_flow_density = result[1]
        
    def plot_header(self, xlabel, ylabel):
        '''
        Sets size, labels and font of graph.
        '''
        font = 30
        plt.figure(figsize=(15,10),facecolor='white')
        plt.xlabel(xlabel, fontsize=font, loc='right')
        plt.ylabel(ylabel, fontsize=font, rotation=0, loc='top')
        plt.xticks(fontsize=font)
        plt.yticks(fontsize=font)
        
    def get_moving_averages(self, size):
        '''
        Counts moving averages of particle flow density.
        '''
        aux = 0
        for i in range(size):
            aux += self.current_particle_flow_density[i]
        moving_averages = [aux]
        for i in range(1,len(self.current_particle_flow_density)-size):
            aux += self.current_particle_flow_density[i+size-1] - self.current_particle_flow_density[i-1]
            moving_averages.append(aux)
        return np.array(moving_averages)/size
    
    def plot_decide_start(self, size):
        '''
        Plots density and moving averages of particle flow density from time t = 0.
        '''
        self.plot_header(r'$t\,$[s]', r'$\rho\,$[m$^{-1}$]')
        plt.plot(np.arange(len(self.density)),self.density)
        self.plot_header(r'$t\,$[s]', r'$J^{'+f'{size}'+'}\,$[s$^{-1}$]')
        moving_averages = self.get_moving_averages(size)
        plt.plot(np.arange(size,len(self.current_particle_flow_density)), moving_averages)
        
    def get_result(self, start):
        '''
        Gets density and particle flow density from time = start.
        '''
        density = 0
        particle_flow_density = 0
        for i in range(start,len(self.density)):
            density += self.density[i]
            particle_flow_density += self.current_particle_flow_density[i]
        return density/(len(self.density)-start), particle_flow_density/(len(self.density)-start)
