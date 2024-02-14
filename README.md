# Autocommit - never lose work again!

If you never want to lose work, it makes sense to commit frequently. But committing frequently, no matter how short your command line alias for git commit and push is, is a drain on your attention and breaks you out of your zone. It's a chore that pulls you away from code. Like the software equivalent of doing laundry or a larva inject in StarCraft 2. Busywork. Bad.

And actually naming the commits, so that you can look through the history later and have the slightest clue of what you were doing, makes it 100x worse. Naming things is [one of the two great problems in programming](https://martinfowler.com/bliki/TwoHardThings.html), and it definitely pulls you out of coding to think "what should I call this commit?" So the choice is between good zones (committing only when you think of it, not according to a routine); a good commit history (committing frequently, with names); and a commit history cluttered with meaningless names (committing frequently with an alias that uses a generic name). In other words, you've always had to pick between the bliss of productivity and the benefits of good version history.

Not anymore!

Autocommit is a super-lightweight and configurable script that lets AI handle the committing for you. It can use local or API-hosted models from a variety of providers — anything compatible with OpenAI-style API requests. By default it points to the endpoint offered by the [Text Generation Webui in server mode](https://github.com/oobabooga/text-generation-webui), but all you need to do is change the YAML file to point at the provider you want. Recommend small models: they should be able to handle it. Every commit except the first commit in this repo was handled by a Q_8 quant of Mistral 7b, running locally.

Features:
- 