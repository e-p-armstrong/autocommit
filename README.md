# Autocommit - never lose work again!

If you never want to lose work, it makes sense to commit frequently. But committing frequently, no matter how short your command line alias for git commit and push is, is a drain on your attention and breaks you out of your zone. It's a chore that pulls you away from code. Like the software equivalent of doing laundry or a larva inject in StarCraft 2. Busywork. Bad.

And actually naming the commits, so that you can look through the history later and have the slightest clue of what you were doing, makes it 100x worse. Naming things is [one of the two great problems in programming](https://martinfowler.com/bliki/TwoHardThings.html), and it definitely pulls you out of coding to think "what should I call this commit?" So the choice is between good zones (committing only when you think of it, not according to a routine); a good commit history (committing frequently, with names); and a commit history cluttered with meaningless names (committing frequently with an alias that uses a generic name). In other words, you've always had to pick between the bliss of productivity and the benefits of good version history.

Not anymore!

Autocommit is a super-lightweight and configurable script that lets AI handle the committing for you. It can use local or API-hosted models from a variety of providers — anything compatible with OpenAI-style API requests. By default it points to the endpoint offered by the [Text Generation Webui in server mode](https://github.com/oobabooga/text-generation-webui), but all you need to do is change the YAML file to point at the provider you want. I recommend small models: they should be able to handle it. Every commit except the first commit in this repo was written by a Q_8 quant of Mistral 7b, running locally on my old Macbook, committing every 10 seconds.

Usage:

1. clone this repo
```
git clone https://github.com/e-p-armstrong/autocommit.git
```
2. Install the requirements:
```
pip install -r requirements.txt
```
2. Go to the directory you want to autocommit in.
3. Do your OS's version of `pwd` to print the absolute path to the directory you're in.
```
pwd
```
4. take this path and put it in the relevant spot in config.yaml, in this repo. Configure anything else you want to while you're at it.
```yaml
repo_path: "/Users/evan/repos/autocommit" # Replace this with the path to the repo you're working in (this repo wrote its own commits)
interval_seconds: 10 # As the commit history of this repo has perhaps demonstrated, once every 10 seconds is... a lot haha
api_key: "put your key here"
base_url: "http://127.0.0.1:5000/v1/" # change based on your api provider. This is the default root for Ooba. I actually don't know what the right setting for using OpenAI is, I think it might be 
push: true # whether it git pushes as well as committing
model: "NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO"
```
5. Run the script!
```
python autocommit.py
```
6. Never lose work again! √

