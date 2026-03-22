# signal_generator.py

import numpy as np
import pandas as pd

def generate_signals(data):
    signals = []
    for i in range(1, len(data)):
        if data['Close'][i] > data['Close'][i-1]:
            signals.append(1)  # Buy signal
        elif data['Close'][i] < data['Close'][i-1]:
            signals.append(-1)  # Sell signal
        else:
            signals.append(0)  # Hold signal
    return np.array(signals)

# Example usage
# data = pd.DataFrame(...)  # Your market data here
# signals = generate_signals(data)