import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
import os
from pathlib import Path
import argparse


def main(args: argparse.Namespace) -> None:
    """

    :param args: path/to/data/file.csv with known and predicted values.

    :return: specified plots
    """

    load_file = args.input

    df = pd.read_csv(load_file)

    p = Path(load_file)
    p = p.parent
    p = p.parent

    plots = p / 'plots'
    if not plots.exists():
        plots.mkdir()

    # Linear plot of all predictions
    dims = (7, 7)
    plt.rcParams['figure.figsize'] = dims
    df_preds = df['Pred']
    df_truth = df['Actual']
    linear_a = sns.regplot(x=df_truth, y=df_preds, fit_reg=False)
    linear_a.set_xlim(0, 2000)
    linear_a.set_ylim(0, 2000)
    linear_a.set_xlabel("Actual EFA [eV/atom]$^{-1}$")  # Label for x-axis
    linear_a.set_ylabel("Predicted EFA [eV/atom]$^{-1}$")  # Label for y-axis
    plt.plot([0, 2000], [0, 2000], linewidth=2, color="b")
    # plt.title(file)
    plt.savefig(str(plots) + '/Orig_234_Predicted_EFA_V2_updated_'
                + str(time.strftime("%Y-%m-%d-%I-%M")) + '.png')
    plt.show()

    # Linear plots with different groups/colors for new data
    dims = (7, 7)
    plt.rcParams['figure.figsize'] = dims

    df_preds_orig = df['Pred'].loc[df['Group'] == 1]
    df_truth_orig = df['Actual'].loc[df['Group'] == 1]

    df_preds_new = df['Pred'].loc[df['Group'] == 2]
    df_truth_new = df['Actual'].loc[df['Group'] == 2]

    linear_m = sns.regplot(x=df_truth_orig, y=df_preds_orig, fit_reg=False, color="b", marker='.', label="With manual features")
    linear_m = sns.regplot(x=df_truth_new, y=df_preds_new, fit_reg=False, color="r", marker='.', label="Without manual features")
    linear_m.set_xlim(0, 2000)
    linear_m.set_ylim(0, 2000)
    linear_m.set_xlabel("Actual EFA [eV/atom]$^{-1}$")  # Label for x-axis
    linear_m.set_ylabel("Predicted EFA [eV/atom]$^{-1}$")  # Label for y-axis
    plt.plot([0, 2000], [0, 2000], linewidth=2, color="b")
    plt.legend()
    plt.savefig(str(plots) + '/FILENAME_HERE_' + str(time.strftime("%Y-%m-%d-%I-%M")) + '.png')
    plt.show()


def parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument('input', type=str, help='path/to/data/file.csv')

    return parser.parse_args()


args = parser()
main(args)
