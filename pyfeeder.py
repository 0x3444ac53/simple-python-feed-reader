#!/usr/bin/python3
import feedparser
import os

# feed = feedparser.parse('https://fivethirtyeight.com/all/feed')
# feed = feedparser.parse('http://feeds.feedburner.com/linuxjournalcom')
config_dir = os.environ['HOME'] + '/.config/pyfeeder/'
browser = 'w3m'


def start():
    config = {}
    global browser
    with open(config_dir + 'config') as f:
        for i in f.readlines():
            ob = i.split(';;')
            if ob[0] == 'BROWSER':
                global browser
                browser = ob[1].strip(',').strip('\n')
                print(browser)
            config[ob[0].strip('\n').strip(',').strip(' ')] = ob[1].strip(
                '\n').strip(',').strip(' ')

    print(config)
    feed_menu(config)


def feed_menu(feeds):
    feed_list = list(feeds.keys())
    for i in feed_list:
        print(str(feed_list.index(i)) + ") " + i)
    feed_select = input('PICK FEED>>>  ')
    feed = feedparser.parse(feeds[feed_list[int(feed_select)]])

    for i in feed['entries']:
        i['read'] = 0
        print(i['title'])

    mainmenu(feed)


def mainmenu(feed):
    count = 0
    for i in feed['entries']:
        toprint = str(count) + ') ' + i['title']

        if i['read'] == 0:
            print(toprint + ' [UNREAD)')
        else:
            print(toprint)
        count += 1
    inputt = input("ARTICLE NUMBER>>>>  ")
    if inputt == 'b':
        feed_menu()
    else:
        read(feed, int(inputt))
    os.system('clear')


def read(feed, index):
    os.system('clear')
    title = feed['entries'][index]['title']
    print('Currently Reading\n' + title)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/.reading.html', 'w') as f:
        f.truncate()
        f.write("""
            <html lang="en">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="./style.css">
  <title>{}</title>
</head>
<div class="stuff">
<body>
<h1>{}</h1>
        """.format(title, title))
        try:
            f.write(feed['entries'][index]['content'][0]['value'])
        except KeyError:
            f.write(feed['entries'][index]['summary'])
        f.write("""
        <p><a href='{}'>Probably Fulll article</a></p>
</body>
</div>
</html>
        """.format(feed['entries'][index]['links'][0]['href']))
    feed['entries'][index]['read'] = 1
    os.system(browser + ' ' + dir_path + "/.reading.html")
    mainmenu(feed)


start()
