import time, pytumblr, traceback


client = pytumblr.TumblrRestClient(
  '',
  '',
  '',
  ''
)

tags = ['your',
        'tags',
        'to',
        'follow',
        'and',
        'like']

while True:
    try:
        for tag in tags:
            for item in client.tagged(tag):
                client.like(item["id"] + item["reblog_key"])
                client.follow(item["blog_name"] + ".tumblr.com")
                print("Liked/Followed:",item["blog_name"])
    except Exception as e:
        print(str(traceback.format_exc()))
        time.sleep(60)
    except KeyboardInterrupt:
        print('shutting down :(')
        quit()
