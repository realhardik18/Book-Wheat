# BookWheat, The ultimate twitter bookmark tool

BookWheat is a Twitter bot that helps you save important tweets which are relevant to you categorically! it also supports discord integration, which means with a quick setup, you can now send important tweets to your favorite discord text channel!

![BookWheat on twitter](https://media.discordapp.net/attachments/949536219786784779/1013473569143005215/unknown.png?width=474&height=422)

# Overview video!

Here's a short video that explains how BookWheat was made, and the tools it uses such as Redis,Tweepy,Heroku and Discord.py(click on the picture!)
[![vid](https://img.youtube.com/vi/UKb11J7cTY0/0.jpg)](https://www.youtube.com/watch?v=UKb11J7cTY0)

## How it works

### How the data is stored:
the data is stored in the form of redis keys. each key stores the information related to a particular user. 
the file [db_methods.py](https://github.com/realhardik18/Book-Wheat/blob/main/twitter-bot/db_methods.py) has various methods to retrive the data and store it.
in a particular key, the bot stores the twitter handle and user id of the associated user, along side this it also stores the data of all the saved tweets of that particular user.
this data has the name of each category, the discord webhook url for this category(for discord intergration) and a list of tweets saved!

### How the data is accessed:
when ever the bot has to retrive the saved tweets of the authorized user via the website, it searches the all the keys for the desired user, and then returns all the data
stored for that particular user, this data is then displayed on the website portal. retriving methods are also stored under [db_methods.py](https://github.com/realhardik18/Book-Wheat/blob/main/flask_app/db_methods.py)


## How to run it locally?

to run the **Twitter Bot** locally first clone the repo 
* then navigate to the [twitter bot](https://github.com/realhardik18/Book-Wheat/tree/main/twitter-bot) folder
* now run `pip install -r requirements.txt` in the terminal to download all the associated packages
* now create a file called `creds.py` and fill out the following information
![instructions](https://media.discordapp.net/attachments/949536219786784779/1013479743510810764/instructions.png?width=1025&height=218)
now you can run [main.py](https://github.com/realhardik18/Book-Wheat/blob/main/twitter-bot/main.py) and your bot will be up and running!

### Prerequisites

python 3.9+

## More Information about Redis Stack

Here some resources to help you quickly get started using Redis Stack. If you still have questions, feel free to ask them in the [Redis Discord](https://discord.gg/redis) or on [Twitter](https://twitter.com/redisinc).

### Getting Started

1. Sign up for a [free Redis Cloud account using this link](https://redis.info/try-free-dev-to) and use the [Redis Stack database in the cloud](https://developer.redis.com/create/rediscloud).
1. Based on the language/framework you want to use, you will find the following client libraries:
    - [Redis OM .NET (C#)](https://github.com/redis/redis-om-dotnet)
        - Watch this [getting started video](https://www.youtube.com/watch?v=ZHPXKrJCYNA)
        - Follow this [getting started guide](https://redis.io/docs/stack/get-started/tutorials/stack-dotnet/)
    - [Redis OM Node (JS)](https://github.com/redis/redis-om-node)
        - Watch this [getting started video](https://www.youtube.com/watch?v=KUfufrwpBkM)
        - Follow this [getting started guide](https://redis.io/docs/stack/get-started/tutorials/stack-node/)
    - [Redis OM Python](https://github.com/redis/redis-om-python)
        - Watch this [getting started video](https://www.youtube.com/watch?v=PPT1FElAS84)
        - Follow this [getting started guide](https://redis.io/docs/stack/get-started/tutorials/stack-python/)
    - [Redis OM Spring (Java)](https://github.com/redis/redis-om-spring)
        - Watch this [getting started video](https://www.youtube.com/watch?v=YhQX8pHy3hk)
        - Follow this [getting started guide](https://redis.io/docs/stack/get-started/tutorials/stack-spring/)

The above videos and guides should be enough to get you started in your desired language/framework. From there you can expand and develop your app. Use the resources below to help guide you further:

1. [Developer Hub](https://redis.info/devhub) - The main developer page for Redis, where you can find information on building using Redis with sample projects, guides, and tutorials.
1. [Redis Stack getting started page](https://redis.io/docs/stack/) - Lists all the Redis Stack features. From there you can find relevant docs and tutorials for all the capabilities of Redis Stack.
1. [Redis Rediscover](https://redis.com/rediscover/) - Provides use-cases for Redis as well as real-world examples and educational material
1. [RedisInsight - Desktop GUI tool](https://redis.info/redisinsight) - Use this to connect to Redis to visually see the data. It also has a CLI inside it that lets you send Redis CLI commands. It also has a profiler so you can see commands that are run on your Redis instance in real-time
1. Youtube Videos
    - [Official Redis Youtube channel](https://redis.info/youtube)
    - [Redis Stack videos](https://www.youtube.com/watch?v=LaiQFZ5bXaM&list=PL83Wfqi-zYZFIQyTMUU6X7rPW2kVV-Ppb) - Help you get started modeling data, using Redis OM, and exploring Redis Stack
    - [Redis Stack Real-Time Stock App](https://www.youtube.com/watch?v=mUNFvyrsl8Q) from Ahmad Bazzi
    - [Build a Fullstack Next.js app](https://www.youtube.com/watch?v=DOIWQddRD5M) with Fireship.io
    - [Microservices with Redis Course](https://www.youtube.com/watch?v=Cy9fAvsXGZA) by Scalable Scripts on freeCodeCamp
