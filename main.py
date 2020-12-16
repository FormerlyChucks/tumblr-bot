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
        'like',
        'and'
        'follow']

while True:
    try:
        for tag in tags:
            for item in client.tagged(tag):
                if item["id"] is not None:
                    client.like(item["id"],item["reblog_key"])
                if item["blog_name"] is not None:
                    client.follow(item["blog_name"] + ".tumblr.com")
                print("Liked/Followed: ",item["blog_name"])
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
