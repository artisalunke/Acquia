import glob
import requests
from datetime import datetime
from requests.exceptions import RequestException

url = 'https://backlog.acquia.com/rest/api/2/issue/'
username = 'doc.bot'
password = 'qwerty123456!'


def create_story(summary, description):
    json = {
        'fields': {
            'issuetype': {
                'name': 'Task'
            },
            'project': {
                'key': 'DOC'
            },
            'summary': summary,
            'description': description
        }
    }

    try:
        response = requests.post(url, json=json, auth=requests.auth.HTTPBasicAuth(username, password))
        print(response.text)
    except RequestException as re:
        print(re)


def search_directive():
    for filename in glob.iglob('../../docs/**/*.rst'):
        with open(filename, 'r') as f:
            searchlines = f.readlines()
        for i, line in enumerate(searchlines):
            if '.. review-date::' in line:
                try:
                    review_date = datetime.strptime(line.split(' ')[2], '%Y-%m-%d')
                    if datetime.today().date() == review_date.date():
                        doc = filename.split('/')[-1]
                        summary = 'Review document {}'.format(doc)
                        description = 'Annual review of document {}. The document was last reviewed on {}'\
                            .format(doc, review_date.date())
                        create_story(summary, description)
                except ValueError as e:
                    print('Error parsing string \'{}\' as date in document \'{}\''.format(line.split(' ')[2], filename))


if __name__ == '__main__':
    search_directive()