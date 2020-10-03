import requests

#Makes an API call and stores the answer
url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code",r.status_code)

#Stores the API response in a variable
response_dict = r.json()
print("Total repositories: ", response_dict['total_count'])

#Explores the information about the repositories
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

#Analyzes the first repository
repo_dict = repo_dicts[0]

print("\nSelect information about first repository:")
print('Name: ', repo_dict['name'])
print('Owner: ', repo_dict['owner']['login'])
print('Stars: ', repo_dict['stargazers_count'])
print('Repository: ', repo_dict['html_url'])
print('Created: ', repo_dict['created_at'])
print('Updated: ', repo_dict['updated_at'])
print('Description: ', repo_dict['description'])
