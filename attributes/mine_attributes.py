#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import platform
import pandas as pd
import sys
sys.path.append("../")
from commits import git2data
from get_attributes import repo_attributes_reader

def get_projects_attributes(p_type):
    if p_type == 'cs':
        fname = "data/project_list_cs.csv"
        output_file = 'cs_projects_with_other_attributes.csv'
    else:
        fname = "data/project_list_se.csv"
        output_file = 'se_projects_with_other_attributes.csv'

    source_projects = up(os.getcwd()) + fname
    project_list = pd.read_csv(source_projects)
    cache = {}
    output_list = []
    for i in range(project_list.shape[0]):
            try:
                print("I am here at " + str(i))
                access_token = project_list.loc[i,'access_token']
                repo_owner = project_list.loc[i,'repo_owner']
                source_type = project_list.loc[i,'source_type']
                repo_name = project_list.loc[i,'repo_name']
                if 'num_dev' in project_list.columns:
                    developers = project_list.loc[i,'num_dev']
                else:
                    developers = 0
                git_url = project_list.loc[i,'git_url']
                api_base_url = project_list.loc[i,'api_base_url']
                project_name = repo_name
                if (git_url not in cache):
                    if (source_type.lower() == 'github_repo'):
                        git_data = git2data.git2data(access_token,repo_owner,source_type,git_url,api_base_url,repo_name)
                        commit_df, issue_df, create_date,release_df,git_stars,git_forks_count,git_watchers_count,max_language,git_tags_count = git_data.get_additional_data()
                        repo_reader = repo_attributes_reader(commit_df, issue_df, release_df,git_stars, git_forks_count, git_watchers_count, max_language, create_date, git_tags_count)
                        xAttributes = repo_reader.read_attributes()
                        developers = len(git_data.get_contributors())
                        row = [project_name, git_url, developers] + xAttributes
                        output_list.append(row)
                        cache[git_url] = row
                    else:
                        row = [project_name, git_url, developers] + ['?']*11
                        output_list.append(row)
                        cache[git_url] = row
                else:
                    output_list.append(cache[git_url])
            except ValueError as e:
                print("Exception occured for ",project_list.loc[i,'git_url'])
                print(e)

    output_df = pd.DataFrame(output_list, columns = ['Project Name', 'git_url', 'Developers', 'Commit #', 'Closed Issues', 'Releases', 'Tags', 'Open Issues', 'Duration', 'Stars', 'Forks', 'Watchers', 'Language', 'Latest commit year'])
    output_df.to_csv('../data/%s.csv' % output_file, index=False)


if __name__ == '__main__':
    project_type = sys.argv[1]
    get_projects_attributes(project_type)
