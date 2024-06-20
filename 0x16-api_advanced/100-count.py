#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    # Normalize word_list to lowercase and initialize counts
    word_list = [word.lower() for word in word_list]
    for word in word_list:
        if word not in counts:
            counts[word] = 0

    # URL for the subreddit with optional pagination
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100}
    if after:
        params['after'] = after

    headers = {'User-Agent': 'Mozilla/5.0'}

    # Request the data from Reddit
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return

    data = response.json()
    if 'data' not in data or 'children' not in data['data']:
        return

    # Process each post title
    for post in data['data']['children']:
        title = post['data']['title'].lower().split()
        for word in word_list:
            counts[word] += title.count(word)

    # Pagination
    after = data['data']['after']
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        # Sort and print the results
        sorted_counts = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")
