from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'threadbookbotapp/home.html')


def card(request, card_id):

    import tweepy
    import time
    import re

    auth = tweepy.OAuthHandler('lpahsh0ZKC3Vigc3SvY1YxElU',
                               'fbgQoBpdyK6VxcFpRplpEmOyGaQ7mEJes6f0fZHLTvuZBGhdTG')

    auth.set_access_token('1285638475673489417-ecQW42KXUJpxEubS1PRFjboA7z8wkM',
                          'a1XnXo7JjD9F4T3l8i53qulfQWGE2HtLTis4AZpRIeR3D')

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    user = api.me()
    sair = False
    i = 0
    threads = []
    dot_length = []
    threads_body = []
    try:
        while not sair:
            if i == 0:
                main_id = card_id
            main = api.get_status(main_id, tweet_mode="extended", include_entities=True)
            result = re.sub(r"http\S+", "", main.full_text)
            threads.append(result)
            print(threads)
            if main.in_reply_to_status_id is None:
                print(main_id)
                for i in range(0, len(threads)):
                    i += 1
                    dot_length.append(i)
                threads.sort(reverse=True)
                for c in range(0, len(threads)):
                    if c != 0:
                        threads_body.append(threads[c])
                threads_body.sort(reverse=True)
                sair = True
            main_id = main.in_reply_to_status_id
            i += 1
        time.sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
    return render(request, 'threadbookbotapp/botpage.html',
                  {'tweets': threads, 'dot_length': dot_length,
                   'threads_body': threads_body})