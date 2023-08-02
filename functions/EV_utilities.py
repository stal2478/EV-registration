import matplotlib.pyplot as plt
import numpy as np

def plot_loss(history):
  plt.plot(history.history['loss'], label='loss')
  plt.plot(history.history['val_loss'], label='val_loss')
  plt.plot(np.array(history.history['loss']) - np.array(history.history['val_loss']), label='difference')  
  plt.xlabel('Epoch')
  plt.ylabel('Error [EVs Registered]')
  plt.legend()
  plt.grid(True)