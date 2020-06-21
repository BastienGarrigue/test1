import matplotlib.pyplot as plt
from scipy.signal import butter


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq=0.5*fs
    low=lowcut/nyq
    high=highcut/nyq
    b, a = butter(order, [low, high], btype='band')
    return b,a

def butter_bandpass_filter(data,lowcut,highcut,fs,order=5):
    b,a=butter_bandpass(lowcut,highcut,fs,order=order)
    y=filter(b,a,data)
    return y
"""
y = butter_bandpass_filter(data['amplitude'][:1000],0.8, 4, 200, order=5)
plt.plot(y)
"""