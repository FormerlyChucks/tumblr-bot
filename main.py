import pytumblr
import time
from halo import Halo

spinner = Halo(spinner={'interval': 100, 'frames': ['-', '+', '*', '+', '-']})

client = pytumblr.TumblrRestClient(
  '',
  '',
  '',
  ''
)

tags = ['your', 'tags', 'to', 'follow', 'and', 'like']

while True:
    try:
        spinner.start()
        for tag in tags:
            for item in client.tagged(tag):
                client.like(item["id"] , item["reblog_key"])
                print("Liked: " + item["blog_name"] + ".tumblr.com")
                client.follow(item["blog_name"] + ".tumblr.com")
                print("Followed: " + item["blog_name"] + ".tumblr.com")
        
    except Exception as e:
        exc = str(str(e))
        spinner.fail(text=exc)
        time.sleep(60)
        
    except KeyboardInterrupt:
        spinner.warn(text='shutting down :(')
        quit()
