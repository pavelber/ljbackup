from lxml import html
import requests
import re
import parse_comments

def download(username, plugin):
    if username == "" :
        return

    print(f"Downloading {username} journal. Sending callbacks to plugin {plugin.get_name()}")
    tree = parse_comments.tree_from_url("http://" + username + ".livejournal.com")
    link = tree.xpath("//a[@class='subj-link']/attribute::href")[0]
    print(link)
    counter = 3
    entries = []
    while True and counter:
        entry_tree = parse_comments.tree_from_url(link)
        header = entry_tree.xpath("//h1[contains(concat(' ',@class,' '),' entry-title ')]")[0].text
        print(header)
        body = entry_tree.xpath("//article[contains(concat(' ',@class,' '),' entry-content ')]")[0]
        body_html = html.tostring(body)
        print(body_html)
        comments = parse_comments.search_in_url(link)
        entry = {"link": link, "title": header, "body": body_html, "comments": comments}
        entries.append(entry)
        prev_link = entry_tree.xpath("//a[contains(concat(' ',@class,' '),' b-controls-prev ')]/attribute::href")[0]
        link = requests.get(prev_link).url
        counter-=1
