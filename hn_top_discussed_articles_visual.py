"""An up to date graph of the most commented articles on Hacker-News."""

from operator import itemgetter
import requests
import json
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response
url = \
    'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts = []
comments, titles_links = [], [],
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    try:
        # Build a dictionary for each article
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }

    except KeyError:
        print(f"ID: {submission_id}\tstatus: Key Error")

    else:
        # comment = submission_dict['comments']
        # title = submission_dict['title']
        # url = f"http://news.ycombinator.com/item?id={submission_id}"
        # title_link = f"<a href='{url}'>{title}</a>"
        # comments.append(comment)
        # titles_links.append(title_link)
        submission_dicts.append(submission_dict)

submission_dicts_sorted = sorted(
    submission_dicts,
    key=itemgetter('comments'),
    reverse=True,
)
max_comments = int(submission_dicts_sorted[0]['comments'])

for dict in submission_dicts_sorted:
    comment = dict['comments']
    title = dict['title']
    url = dict['hn_link']
    title_link = f"<a href='{url}'>{title}</a>"
    comments.append(comment)
    titles_links.append(title_link)

# Make visualisation
data = [{
    'type': 'bar',
    'x': titles_links,
    'y': comments,
    'hovertext': titles_links,
    'marker': {
        'cmax': max_comments,
        'cmin': 0,
        'color': comments,
        'colorscale': 'Viridis',
        'line': {
            'width': 1.5,
            'color': 'rgb(25,25,25)',
        },
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': f'Most-commented articles on Hacker News',
    'template': 'plotly_dark',
    'titlefont': {'size': 30},
    'xaxis': {
        'title': 'Article',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    }
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename=f'hn_commented_articles.html')
