import decimal

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


sns.set_theme(style="darkgrid")


def plot_env_history(env):
    columns = [f"T{i+1}" for i in range(env.num_turbines)]
    yaws = np.c_[[[h["yaw"] for h in env.history[agent]["observation"]]for agent in env.possible_agents]].T
    powers = np.c_[[env.history[agent]["power"] for agent in env.possible_agents]].T
    loads = np.c_[[env.history[agent]["load"] for agent in env.possible_agents]].T
    yaws = pd.DataFrame(yaws, columns=columns)
    powers = pd.DataFrame(powers, columns=columns)
    loads = pd.DataFrame(np.abs(loads).sum(0), columns=columns)
    fig, ax = plt.subplots(ncols=3, figsize=(15, 5))
    ax0 = sns.lineplot(yaws, ax=ax[0])
    ax1 = sns.lineplot(powers.sum(1), ax=ax[1])
    ax2 = sns.lineplot(loads.sum(1), ax=ax[2])
    ax0.set(ylabel="Yaw (°)", xlabel="Iterations")
    ax1.set(ylabel="Normalized Power (MW)", xlabel="Iterations")
    ax2.set(ylabel="Loading Indicator", xlabel="Iterations")
    ax0.grid(True)
    ax1.grid(True)
    ax2.grid(True)
    return fig

def less_than_180(angle):
    # modulo for [-180, 180]
    # takes an angle **already** in the [-180, 180] referential
    return -180 + (angle - (-180)) % 360

def get_wake_delays(cx, cy, uref, phiref=0, gamma=4, stab_time = 80, cutoff_x=2000, cutoff_y=400):
    # Store number of decimals
    precision = -decimal.Decimal(cx[0]).as_tuple().exponent
    # Rotate to get downstream coordinates
    # Remove 0 coords to calculate angle 
    cx = np.array(cx)
    cx[cx==0] = 1
    phiref = less_than_180(phiref)

    # Get polar coordinates
    rs = np.sqrt(cx**2 + np.array(cy)**2)
    theta = np.arctan2(cy/rs, cx/rs)
    theta_new = theta + np.radians(phiref)
    cx = np.round(rs * np.cos(theta_new), precision)
    cy = np.round(rs * np.sin(theta_new), precision)

    nturb = len(cx)
    D = np.ones((nturb,nturb)) * stab_time
    for i in range(nturb):
        for j in range(nturb):
            if (cx[j] > cx[i]) and (cx[j] < cx[i] + cutoff_x) and np.abs(cy[j] - cy[i]) < cutoff_y:
                D[i,j] = max(stab_time, gamma * (cx[j] - cx[i]) / uref)
    return D