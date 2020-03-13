#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import platform
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot(se_file_name, moissi_file_name):
    if platform.system() == 'Darwin' or platform.system() == 'Linux':
        input_dir_path = os.getcwd() + '/'
    else:
        input_dir_path = os.getcwd() + '\\'

    se_input_path = input_dir_path + se_file_name
    moissi_input_path = input_dir_path + moissi_file_name

    se_input_df = pd.read_csv(se_input_path)
    moissi_input_df = pd.read_csv(moissi_input_path)
    se_input_df = se_input_df.replace('?', np.nan).dropna()
    moissi_input_df = moissi_input_df.replace('?', np.nan).dropna()

    boxplots = []
    attributes_to_plot = ['Developers','Commit #','Closed Issues','Releases','Tags','Open Issues','Duration','Stars','Forks','Watchers']
    y_max = [150, 45000, 2000, 45, 200, 650, 520, 5000, 1000, 250]
    y_min = [0, 0, 0, 0, 0, 0, 50, 0, 0, 0]

    fig, boxplots = plt.subplots(2, 5, constrained_layout=True)
    bp = [[None for x in range(10)] for y in range(2)]
    plt.rcParams['ytick.labelsize'] = 14

    for i in range(len(attributes_to_plot)):
        attr = attributes_to_plot[i]
        if (i < 5):
            r_coord = 0
            c_coord = 2*i
        else:
            r_coord = 1
            c_coord = 2*(i-5)
        #print(r_coord, c_coord)
        boxplots[r_coord][int(c_coord/2)].set_ylim([y_min[i],y_max[i]])
        #boxplots[r_coord][c_coord+1].set_ylim([y_min[i],y_max[i]])


        bp[r_coord][c_coord] = pd.to_numeric(se_input_df[attr]).plot.box(showfliers=False, positions=[0.25], whis=[5,95], ax=boxplots[r_coord][int(c_coord/2)],
                                                                         patch_artist=True, return_type='dict', widths=[0.25])
        temp = bp[r_coord][c_coord]
        boxes = temp['boxes']
        boxes[0].set_facecolor('c')
        medians = temp['medians']
        medians[0].set_color('black')

        print("%s:\t %s,   %s" % (attr, int(np.median(moissi_input_df[attr].values)), int(np.median(se_input_df[attr].values))))
        bp[r_coord][c_coord+1] = pd.to_numeric(moissi_input_df[attr]).plot.box(showfliers=False, positions=[0.75], whis=[5,95], ax=boxplots[r_coord][int(c_coord/2)],
                                                                                patch_artist=True, return_type='dict', widths=[0.25])
        temp = bp[r_coord][c_coord+1]
        boxes = temp['boxes']
        boxes[0].set_facecolor('m')
        medians = temp['medians']
        medians[0].set_color('black')
        boxplots[r_coord][int(c_coord/2)].set_xticks([0.5])
        boxplots[r_coord][int(c_coord/2)].set_xticklabels([attr.upper()], fontsize=14, fontweight="bold")
        if attr == "Duration":
            attr = "DURATION (weeks)"
        boxplots[r_coord][int(c_coord / 2)].set_xticklabels([attr.upper()], fontsize=14, fontweight="bold")
        boxplots[r_coord][int(c_coord / 2)].tick_params(axis='y', labelsize=14)

    fig.legend((bp[0][0]['boxes'][0], bp[0][1]['boxes'][0]), ('SE', 'CS'), loc='upper center', prop={'size': 14, 'weight': 'bold'})
    plt.show()

def read_csv(file_name1, file_name2):
    df_1 = pd.read_csv(file_name1)
    df_2 = pd.read_csv(file_name2)
    proj_names_1 = list(df_1['Project Name'].values.tolist())
    proj_names_2 = list(df_2['Project Name'].values.tolist())
    print(set(proj_names_1).intersection(set(proj_names_2)))


plot('se_all_projects_with_other_attributes.csv', 'moissi_projects_with_other_attributes.csv')
