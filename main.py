import traceback

from Data_extraction.get_rr_list import get_rr_list
from HRV.metrics import BPMfunction, IBIfunction, SDNNfunction, SDSDfunction, sympatho_vagal_balancefunction
from HRV.graphics import display_signal, display_fourier, display_tachogramme,display_tachogramme_freq
import pandas as pd
import numpy as np


def main():
    try:
        data = pd.read_csv('cardiac_signal.csv')
        x = get_rr_list(data)
        BPMfunction(x)
        IBIfunction(x)
        SDNNfunction(x)
        print("SDSD: ", np.std(SDSDfunction(x)))
        print("RMSD: ", np.sqrt(np.mean(SDSDfunction(x))))
        print("Sympatho-vagal balance: ", np.sqrt(np.mean(sympatho_vagal_balancefunction(x))))

        I = input("Afficher signal y/n? ")
        if (I.lower() == "y"):
            display_signal(data)
    except Exception as error:
        print(traceback.format_exc())

if __name__ == "__main__":
    main()
