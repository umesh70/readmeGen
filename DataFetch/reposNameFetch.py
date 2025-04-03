import requests
import json


class repositoriesFetch:
    def __init__(self, url, languages, headers):
        self.url = url
        self.languages = languages
        self.headers = headers
    
    def retrieveRepositories(self):
        # fetch the content based on both the languages
        for language in self.languages:
            try:
                for page in range(1, 6):
                    params = {
                        'q': f'language:{language}',
                        'sort': 'stars',
                        'order': 'desc',
                        'per_page': 100,
                        'page': page
                    }
        
                    response = requests.get(
                        url= self.url,
                        headers=self.headers,
                        params=params
                    )

                    response.raise_for_status()
                    self.cleanData(response.json(), language)

            except requests.exceptions.RequestException as e:
                print(f"Error fetching data from GitHub API: {e}")
                return []

    def cleanData(self, repo, language):
        urls = [item['contents_url'][:-7] for item in repo['items']]
        filename = f"{language.lower()}Data.json"

        try:
            with open(filename, 'r') as f:
                existing_urls = json.load(f)
        except FileNotFoundError:
            existing_urls = []

        combined_urls = list(set(existing_urls + urls))

        with open(filename, 'w') as f:
            json.dump(combined_urls, f, indent=2)
            

headers = {
        'Accept': 'application/vnd.github.v3+json',
        # Uncomment and add your token if you need higher rate limits
        # 'Authorization': 'token YOUR_GITHUB_TOKEN'
    }

repositoriesFetcher = repositoriesFetch(
    languages=['javascript','python'],
    headers= headers,
    url="https://api.github.com/search/repositories"
)

repositoriesFetcher.retrieveRepositories()