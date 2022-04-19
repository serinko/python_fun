"""
A Python program pulling the top Star rated Python repositories on GitHub,
using plotly to visualise them.
"""

import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response
url = \
    'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {
    'Accept': 'application/vnd.github.v3+json'
}
r = requests.get(url, headers)
print(f"Status code: {r.status_code}")

# Process results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    decription = repo_dict['description']
    label = f"{owner}<br />{decription}"
    labels.append(label)

# Defining the top rating limit for cmax in colorscale
stars_max = int(repo_dicts[0]['stargazers_count'])

# Make visualisation
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'cmax': stars_max,
        'cmin': 0,
        'color': stars,
        'colorscale': 'Plasma',
        'line': {
            'width': 1.5,
            'color': 'white',
        },
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'template': 'plotly_dark',
    'titlefont': {'size': 30},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    }
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
