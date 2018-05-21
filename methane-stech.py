import cantera as ct
import numpy as np
import matplotlib.pyplot as plt

gas = ct.Solution('gri30.xml')
initial_state = 1200, 5 * ct.one_atm, 'CH4:0.5, O2:1.0, N2:3.76'

# Run a simulation with the full mechanism
gas.TPX = initial_state
r = ct.IdealGasConstPressureReactor(gas)
sim = ct.ReactorNet([r])

tt = []
TT = []
t = 0.0
# Rmax is the maximum relative reaction rate at any timestep
Rmax = np.zeros(gas.n_reactions)
while t < 0.02:
    t = sim.step()
    tt.append(1000 * t)
    TT.append(r.T)
    rnet = abs(gas.net_rates_of_progress)
    rnet /= max(rnet)
    Rmax = np.maximum(Rmax, rnet)

plt.plot(tt, TT, color='k', lw=3, zorder=100)
plt.xlabel('Time (ms)')
plt.ylabel('Temperature (K)')
plt.title('Ignition delay time for stechiometric methane-air mixture\n')

plt.show()
