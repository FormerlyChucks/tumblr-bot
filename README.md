# tumblr-bot
Tumblr bot, made to automate gaining followers

# Getting set up!

* Figure out how to install Python, Pip and Git
* In your terminal:

      git clone https://github.com/SlickTalk/tumblr-bot
      cd tumblr-bot
      pip3 install pytumblr
      
* Assuming you have a Tumblr account, go [here](https://www.tumblr.com/oauth/apps) to get signed up for the API
* Go [here](https://api.tumblr.com/console/calls/user/info) to get your keys
    * Select "PYTHON"
    * Copy the `client = pytumblr.TumblrRestClient(...)` part, which contains your four keys
* Open main.py in your favorite text editor
    * Replace the `client = pytumblr.TumblrRestClient(...)` in the file with your copied text
    * In your terminal, run:
      
          python3 main.py
