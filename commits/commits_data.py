#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import division
from pathlib import Path
from git2repo import *
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import random
import networkx as nx
import re
from git2data import *
from os.path import dirname as up
import os
import platform


if platform.system() == 'Darwin' or platform.system() == 'Linux':
    fname = '/' + "project_list_cs.csv"
    source_projects = up(os.getcwd()) + fname
else:
    fname = '\\' + "project_list_cs.csv"
    source_projects = up(os.getcwd()) + fname
project_list = pd.read_csv(source_projects)

for i in range(project_list.shape[0]):
    access_token = project_list.loc[i,'access_token']
    repo_owner = project_list.loc[i,'repo_owner']
    source_type = project_list.loc[i,'source_type']
    git_url = project_list.loc[i,'git_url']
    api_base_url = project_list.loc[i,'api_base_url']
    repo_name = project_list.loc[i,'repo_name']
    if platform.system() == 'Darwin' or platform.system() == 'Linux':
        data_path = up(os.getcwd()) + '/data/' + repo_name + '/'
    else:
        data_path = up(os.getcwd()) + '\\data\\' + repo_name + '\\'
    if not Path(data_path).is_dir():
        os.makedirs(Path(data_path))

    git_data = git2data.git2data(access_token, repo_owner, source_type,
                                 git_url, api_base_url, repo_name)
    git_data.git_repo.repo_remove()
    git_data.get_commit_data(True)
    commit_df = pd.DataFrame(git_data.git_commits, columns=['commit_number', 'message', 'parent', 'time'])
    commit_df.to_csv('../data/%s_commits.csv' % repo_name, index=False)