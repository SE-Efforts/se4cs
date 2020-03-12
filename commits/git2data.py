# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:30:28 2018

@author: suvod
"""
from __future__ import division
from main.api import git_access, api_access
from main.git_log import git2repo, buggy_commit
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import os
import re
import networkx as nx
import platform
from os.path import dirname as up


class git2data(object):

    def __init__(self, access_token, repo_owner, source_type, git_url, api_base_url, repo_name):
        self.repo_name = repo_name
        if platform.system() == 'Darwin' or platform.system() == 'Linux':
            self.data_path = up(os.getcwd()) + '/data/'
        else:
            self.data_path = up(os.getcwd()) + '\\data\\'
        #print("git2data", self.data_path)
        print(self.data_path, access_token, repo_owner, source_type,
              git_url, api_base_url, repo_name)
        self.git_client = api_access.git_api_access(access_token, repo_owner, source_type, git_url, api_base_url,
                                                    repo_name)
        self.git_repo = git2repo.git2repo(git_url, repo_name)
        self.repo = self.git_repo.clone_repo()

    def get_commit_data(self, extra_details=False):
        # print("Inside get_commit_data in git2data")
        self.git_commits = self.git_repo.get_commits_updated(extra_details)