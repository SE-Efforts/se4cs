import sys
import os
import subprocess as sp
import pandas as pd
import numpy as np
import shlex
from collections import Counter

filenames = ['ndslabs', 'hoomd', 'psi4', 'elasticsearch', 'trilinos',
             'dealii', 'galaxy', 'qcfractal', 'abinit',
             'quantum_package', 'clowder', 'hubzero', 'ompi',
             'cctools', 'tripal', 'radical_pilot']


def read_csv_file():
    current_dir = os.getcwd()
    results = {}
    for fname in filenames:

        eng_files, sci_files, common_files = None, None, None
        proj_path = "../data/%s" % fname

        bug_file_path = "../data/csv_files/bugfixes/%s.csv" % fname
        bug_df = pd.read_csv(bug_file_path, index_col=False)
        sci_col, eng_col = 'Science Fix', 'Engineering Fix'
        bug_df_filtered = bug_df.loc[(bug_df[sci_col] == 1) | (bug_df[eng_col] == 1)]
        science_df = bug_df_filtered.loc[bug_df_filtered[sci_col] == 1]['commit_number']
        engineering_df = bug_df_filtered.loc[bug_df_filtered[eng_col] == 1]['commit_number']


        everything_file_path = "../data/csv_files/everything/%s.csv" % fname
        everything_df = pd.read_csv(everything_file_path, index_col=False)
        sci_col, eng_col = 'science enhancement', 'engineering enhancement'
        df_filtered = everything_df.loc[(everything_df[sci_col] == 1) | (everything_df[eng_col] == 1)]
        science_commits_df = pd.concat([science_df, df_filtered.loc[df_filtered[sci_col] == 1]['commit_number']])
        engineering_commits_df = pd.concat([engineering_df, df_filtered.loc[df_filtered[eng_col] == 1]['commit_number']])

        os.chdir(proj_path)
        communicate_sp("git reset --hard master")
        ecommits, scommits = engineering_commits_df.values.tolist(), science_commits_df.values.tolist()

        if len(ecommits) < 10 or len(scommits) < 10:
            print(fname, "not have sufficient engineering or scientific development commits")
            print()
            os.chdir(current_dir)
            continue

        eng_files, count_efiles = get_files(ecommits)
        sci_files, count_sfiles = get_files(scommits)
        #common_files = eng_files & sci_files
        #common_files_count = sum(common_files.values())
        common_files = eng_files.intersection(sci_files)
        common_files_count = len(common_files)

        shared_count_ecommit = get_commits(ecommits, common_files)
        shared_count_scommit = get_commits(scommits, common_files)

        results[fname] = {
            "num_eng_files": count_efiles,
            "num_sci_files": count_sfiles,
            "common_files_count": common_files_count,
            "efiles_percentage": common_files_count / (count_efiles + 0.0000001),
            "sfiles_percentage": common_files_count / (count_sfiles + 0.0000001),
            "num_eng_commits": shared_count_ecommit,
            "num_sci_commits": shared_count_scommit,
            "scommits_percentage": shared_count_ecommit / len(ecommits),
            "ecommits_percentage": shared_count_scommit / len(scommits),
        }
        print(fname.upper(), end=", ")
        for m in results[fname].keys():
            print("%s %s" % (m, results[fname][m]), end=", ")
        print()
        os.chdir(current_dir)


def get_commits(commits, sharedfiles):
    commit_count = 0
    for commit in commits:
        out_pc, _ = communicate_sp("git cat-file -p %s" % commit)
        for l in out_pc.split("\n"):
            if l.startswith("parent"):
                parent_commit = l.split()[1]
                break
        out_fnames, _ = communicate_sp("git diff {} {} --name-only".format(commit, parent_commit))
        count_flag = False
        for fname in out_fnames.splitlines():
            for wanted in [".py", ".c", ".cpp", ".F90", ".f90", ".java"]:
                if wanted in fname and "__init__.py" not in fname:
                    if fname in sharedfiles:
                        count_flag = True
            if count_flag:
                commit_count += 1
                break
    return commit_count


def get_files(commits):
    files_changed = set()
    for commit in commits:
        out_pc, _ = communicate_sp("git cat-file -p %s" % commit)
        for l in out_pc.split("\n"):
            if l.startswith("parent"):
                parent_commit = l.split()[1]
                break
        out_fnames, _ = communicate_sp("git diff {} {} --name-only".format(commit, parent_commit))
        for fname in out_fnames.splitlines():
            for wanted in [".py", ".c", ".cpp", ".F90", ".f90", ".java"]:
                if wanted in fname and "__init__.py" not in fname:
                    #files_changed.append(fname)
                    files_changed.add(fname)
    return files_changed, len(files_changed)


def communicate_sp(cmd):
    cmd = shlex.split(cmd)
    with sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.DEVNULL) as p:
        out, err = p.communicate()
    return out.decode("utf-8"), err


if __name__ == '__main__':
    read_csv_file()
