import numpy as np
import matplotlib.pyplot as plt

from Data_extraction.detect_peaks import detect_peaks
from Data_extraction.get_rr_list import get_rr_list


def display_signal(data):
    X = data['amplitude']
    plt.title("Detected peaks in signal")
    plt.xlim(0, 2500)
    plt.plot(data.amplitude, alpha=0.5, color='blue')
    plt.scatter(detect_peaks(X, mpd=100), X[detect_peaks(X, mpd=100)], color='red')
    plt.show()


def display_fourier(data):
    f = 200
    n = len(data["amplitude"])
    frq = np.fft.fftfreq(n, d=(1. / f))
    frq = frq[range(n // 2)]
    Y = np.fft.fft(data["amplitude"]) / n
    Y = Y[range(n // 2)]
    plt.figure(figsize=(10, 10))
    plt.title("Frequency spectrum")
    plt.xlim(0, 1.5)
    plt.plot(frq, abs(Y))


def display_tachogramme(data):
    plt.title("Tachogramme")
    plt.plot(get_rr_list(data))


def display_tachogramme_freq(data):
    f = 200
    n = len(get_rr_list(data))
    frq = np.fft.fftfreq(n, d=(1. / f))
    frq = frq[range(n // 2)]
    Y = np.fft.fft(get_rr_list(data)) / n
    Y = Y[range(n // 2)]
    plt.figure(figsize=(10, 10))
    plt.title("Tachogramme Frequency spectrum")
    plt.xlim(0, 1.5)
    plt.plot(frq, abs(Y))
