import requests

from urllib.parse import urljoin
from prettytable import PrettyTable

class GithubAPI:
    __root_api = "https://api.github.com/repos/"
    def __init__(self,repo_name):
        self.__repo_api_url = urljoin(GithubAPI.__root_api,repo_name)
    
    def __get(self,ressource,params=None):
        if params == None:
            url = urljoin(self.__repo_api_url,ressource)
            print(url)
            return requests.get(url).json()
        else:
            raise NotImplementedError()

    def get_issues(self):
        return self.__get("issues")
    
    def show_issues(self):
        issues = self.get_issues()
        for issue in issues:
            print(
                """
name: {}
author: {}
labels: {}
======================"""
            )

#githubAPI = GithubAPI("epoberezkin/ajv/")

#githubAPI.show_issues()

print("List of issues :\n" + "\n".join(map(lambda issue:"""\nname: {}\nauthor: {}\nlabels: {}\n======================""".format(issue["title"],issue["user"]["login"],' - '.join(map(lambda x:x["name"],issue["labels"]))),requests.get("https://api.github.com/repos/epoberezkin/ajv/issues").json())))