#!/usr/bin/python3
"""
100-count - A script to count specific keywords in hot articles
from a subreddit.
This script uses the Reddit API to count occurrences of given keywords in
the titles of hot articles from a specified subreddit. It handles pagination
through recursive calls and prints the keyword counts in a sorted order.

Example usage:
    python3 100-main.py <subreddit> 'keyword1 keyword2 keyword3'
"""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively fetches hot articles from a given
    subreddit and counts the occurrences of keywords.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count in the article titles.
        after (str): The parameter to get the next page of results
        (used in recursion).
        counts (dict): A dictionary to store keyword counts.
    Returns:
        None: Results are printed directly.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    base_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code != 200:
        return

    data = response.json()
    articles = data.get('data', {}).get('children', [])

    for article in articles:
        title = article['data']['title'].lower().split()
        for word in word_list:
            counts[word] = counts.get(word, 0) + title.count(word.lower())

    after = data.get('data', {}).get('after', None)
    if after:
        return count_words(subreddit, word_list, after, counts)

    sorted_counts = sorted(
        counts.items(), key=lambda x: (-x[1], x[0])
    )

    for word, count in sorted_counts:
        if count > 0:
            print(f'{word}: {count}')
