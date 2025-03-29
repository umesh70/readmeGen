import requests
import json


class nameFetch:
    def __init__(self,url,languages,headers):
        self.url = url
        self.languages = languages
        self.headers = headers
        self.names = []
    
    def sendRequest(self):
        # fetch the content based on both the languages
        for language in self.languages:
            try:
                params = {
                    'q': f'language:{language}',
                    'sort': 'stars',
                    'order': 'desc',
                    'per_page': 100 }
    
                reponse = requests.get(
                    url= self.url,
                    headers=self.headers,
                    params=params
                )
                reponse.raise_for_status()
                self.names.append(reponse.json())
            except requests.exceptions.RequestException as e:
                print(f"Error fetching data from GitHub API: {e}")
                return []
    
    def printNames(self):
        print(self.names)


    def cleanData(self):
        """
        1. understand the API reponse structure
        2. extract the names of the repositories
        3. store the names of the repositories in the json files
        """


headers = {
        'Accept': 'application/vnd.github.v3+json',
        # Uncomment and add your token if you need higher rate limits
        # 'Authorization': 'token YOUR_GITHUB_TOKEN'
    }

namefetcher = nameFetch(
    languages=['javascript','python'],
    headers= headers,
    url="https://api.github.com/search/repositories"
)

namefetcher.sendRequest()
namefetcher.printNames()