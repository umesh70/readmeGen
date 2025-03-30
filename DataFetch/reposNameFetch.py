import requests
import json


class repositoriesFetch:
    def __init__(self,url,languages,headers):
        self.url = url
        self.languages = languages
        self.headers = headers
        self.repositories = []
        self.urls=[]
    
    def retrieveRepositories(self):
        # fetch the content based on both the languages
        for language in self.languages:
            try:
                params = {
                    'q': f'language:{language}',
                    'sort': 'stars',
                    'order': 'desc',
                    'per_page': 1 
                }
    
                reponse = requests.get(
                    url= self.url,
                    headers=self.headers,
                    params=params
                )

                reponse.raise_for_status()
                self.repositories.append(reponse.json())

                for repo in self.repositories:
                    if(repo['url']):
                        self.urls.append(repo['url'])
                        print(repo['url'])

            except requests.exceptions.RequestException as e:
                print(f"Error fetching data from GitHub API: {e}")
                return []
    
    def printData(self):
        print("repos, urls = ", self.repositories, self.urls)


    def cleanData(self):
        """
        1. understand the API reponse structure
        2. extract the urls of the repositories
        3. store the urls of the repositories in the json files
        """


headers = {
        'Accept': 'application/vnd.github.v3+json',
        # Uncomment and add your token if you need higher rate limits
        # 'Authorization': 'token YOUR_GITHUB_TOKEN'
    }

repositoriesFetcher = repositoriesFetch(
    languages=['python'],
    headers= headers,
    url="https://api.github.com/search/repositories"
)

repositoriesFetcher.retrieveRepositories()
# repositoriesFetcher.printData()