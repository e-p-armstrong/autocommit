# Autocommit - never lose work again!

If you never want to lose work, it makes sense to commit frequently. But committing frequently, no matter how short your command line alias for git commit and push is, is a drain on your attention and breaks you out of your zone. It's a chore that pulls you away from code. Like the software equivalent of doing laundry or a larva inject in StarCraft 2. Busywork. Bad.

And actually naming the commits, so that you can look through the history later and have the slightest clue of what you were doing, makes it 100x worse. Naming things is [one of the two great problems in programming](https://martinfowler.com/bliki/TwoHardThings.html), and it definitely pulls you out of coding to think "what should I call this commit?" So the choice is between good zones (committing only when you think of it, not according to a routine); a good commit history (committing frequently, with names); and a commit history cluttered with meaningless names (committing frequently with an alias that uses a generic name). In other words, you've always had to pick between the bliss of productivity and the benefits of good version history.

Not anymore!

Autocommit is a super-lightweight and configurable script that lets AI handle the committing for you. It can use local or API-hosted models from a variety of providers — anything compatible with OpenAI-style API requests. By default it points to the endpoint offered by the [Text Generation Webui in server mode](https://github.com/oobabooga/text-generation-webui), but all you need to do is change the YAML file to point at the provider you want. I recommend small models: they should be able to handle it. Every commit except the first commit in this repo was written by a Q_8 quant of Mistral 7b, running locally on my old Macbook, committing every 10 seconds.

## Usage:

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
base_url: "http://127.0.0.1:5000/v1/" # change based on your api provider. This is the default root for Ooba. I actually don't know what the right setting for using OpenAI is, I think it might be https://api.openai.com/v1/ but I am not sure
push: true # whether it git pushes as well as committing
model: "NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO"
```
5. Run the script!
```
python autocommit.py
```
6. Never lose work again! √

## API provider base urls list (feel free to add):
```
- http://127.0.0.1:5000/v1/ # for if you are running models locally on Oobabooga with the api extension. This is the best option because this is free and the task is simple. The model I used to write the commit messages for this one can literally run on a phone.
- https://api.together.xyz # together.ai, which is real cheap, real flexible, real high-quality, and real unreliable with their capacity sometimes (still love 'em though)
- https://api.openai.com/v1/ # OpenAI 🤮. But it might work well with 3.5 Turbo. Don't actually know if this one works, someone tell me.
- more to come, feel free to add your favorite! 
```

## Notes and possible areas for improvement:
- If your company tracks performance through number of commits this is practically cheating lol
- It currently doesn't make the first commit of a project
- I don't know if it works on windows
- the list of API providers should be expanded.

## Repo Mascot
What, you thought that just because this is a very lightweight repo I wouldn't include an Anime mascot? Think again my friend!
```

                                       ..-*%@@@%#@@%%*=...                                          
                                     ..*@@@@%%%%%%%#%#*#*...                                        
                                    .=%@@@@#####*#######+*=-..                                      
                                  ..+%%%@%#####**+++*-=+##%%#:.                                     
                                  .+@@%#%##*#**+**#*##*##@%%@%:                                     
                                 .-@@@%%%######***##%####%@%@@#:                                    
                                 .#@@@@@@%%@%%#%##%%%%%%%%@%@@%=.                                   
                                .=@@@%%@@%@%%%%%%%%%%-%%%%@%@@@+-                                   
                                .*%@@%%@%%+%##%%%%%%*:=#%%%%%@@%::.                                 
                               .++@@@%%%%#=#*######%+-:-#%%%%@@%+-.                                 
                              .-=+@@@%%@#=:-=:#####*-=*#%%%%%@@@#=:.                                
                             .:--%@@%%%@.................*#%%%#@%*::.                               
                             ..:+%@@%%%%...O..........O..-+%%#%@@+=.:.                              
                            .:.+=%@@%%%%*................-%%%@@@@*:+.:.                             
                          ..-:*=:#@@@%%%*+-:::.......:::-+%%%@@@@%-.+:.                             
                          ..-**::@@@@%%%#*::...\___/....-%%%%@@@%%+.:=.                             
                          ..=-=-#%%@@%%%%##-..........:+#%%%%@@%%%*.:=                              
                           .+::*%%%%@%%%%####+::...:-*##*%%%%@###%#*-:.                             
                           ..==-%%#%%%%%%##***+++==++****%%%%%%###*...                              
                             .:.**=*#%%%#*-:##+++++++#%=:#%###+=:=:.                                
                             ...:+..++#+=#%@%*+++===++%@%%+:*=.....                                 
                               ..:-:.:=*@@@%++++====--=#%%%*=:..                                    
                              ..:+#%@@@@@@%*+++=-::.:::=#%@@@@%%#+:...                              
                          .-#@@%%##%%%%%%##=-:.:..:::...*##%%#####%%@@#=.                           
                          :#%%#####%######-.:...........:%#####%######%%+.                          
                         .-%%%####@%#####*:..............+#####%@#####%%#.                          
                         .=@%@%###%%#####+...............:######%%##%%%%#..                         
                         .+@%@%#%%######*:................+#######%#%@%@%:                          
                         .#@%%%%%%######+.....-*%%%%+:....-#######%#%@%%%:.                         
                         .#@%@@%%%%%###%:..:#@@@@@@@@@@*...*#####%%%%@%%%-                          
                        .+%@%%@%%%%%%%#*..=@@@@@@@%%@@@@@-.=#%#%%%%%@@%%@=.                         
                       .-%@%%%@%%%%%%%%:.=@@@@@@@@%@*+@@@@:.%%%%%%@%@@%@@%=.                        
                      .-%@@@%%@@%@%%%%#.:#@@%-%@=#+**+@@@@+.*%%%%@%%@@@@@@@-                        
                      .-*%@@@%@@%@%%%%*::#@@%-%%-#+**=@@@@*:*%%%%@@%@@@@%%@:.                       
                      .+%@@@@@@@@@@%@%*-:+@@@@%#-#%@@%%@@@=-+@@@@@@@@%@@@%@.                        
                     .*@@@@@@@@@@@@@@%*+::+@@%*#@@@@@@@@@=--+@@@@@@@@@@@@@@*.                       
                    ..#@@@@@%@@@@@@@@#++-.:-#@@@@@@@@@@#-::=+%@@@@@@@@@@@@@%*..                     
                   .:#@%%%%@@@@@@@@@@#-==:..::-+##%#+-::::-++#@@@@@@@@@@%%%@#:.                     
                  .:#@@@%@@@@@@@@@@@@*=:=-........:::.:..-=++#@@@@@@@@@%%@@@%=.                     
                  .-+*%@@@%%@@@@@@@@%++-:-:......::.....-==++*@@@@@@%@%@@@%%%*.                     
                  .+%@@@@@@%@%%@@@@@%+==::-.....::.....-==++-+@@@@@%#%@@%@@@@@*.                    
                ..#@@@@@@%@@%.=@@@@@#-===:::..:::.....:====:=+@@@@@%=#%@@%@@@@@%-.                  
                .=%%@@@%@@@@%+*@@@@%-::==-::.::......:===:.--=%@@@@@*#%@@@@@%@%#-.                  
                ..=%@%%%%%@@*-@@@@#==:..:--::..:::..:=-:..=--:=%@@@@--#@%%%%%@@#.                   
                  -%@@@%%%%@@@@@@@#=-++==:..::::::.:-:.:-=:--==#@@@@*=@%%%%%%@@*.                   
                  .+%@@@@%%@@@@@@@%%@@%#**+=-=--::----=+=+**#%@@@@@@@@@%%%%%%%#:.                   
                  .:#@@@@%%@@@@@@%%@@@@@%%%%%#########%%%%%@@@@@@@@@@@%##%@@@%-.                    
                   .*@@@%%%%%@@@%%@@@@@@@%%%%%%%%%%%%%%%%%%@@@@@%@@@@%#%%%@@@#.                     
                   .=%@@@@%%#%@@%@@@%%@@@@%%%%%%%%%%%%%%%@@@@%@@@@@@%%%%%@@@%+.                     
                   ..%@@@%=::=+%%@@%%%%#%########%%###%###%%%%%@@%%=::-+%@@%#:.                     
                    .*%%%==+:..:::*%%%#%%###%###%%####%##%%#%%##:::::==.-#@%*..                     
                    .=%%*++-:::*%%+-*%%%%%%%%%%%%%%%%%%%%%@%%#+-#%*-::-*=*%%=.                      
                    .*%@*%+-:-#####%##%@%%%%%%%%%%%%%%%%%%%%%##%####=:-#%#@#-.                      
                   .*@@%%*#=-%%%%##%%%@@%%%%%%%%%@%%%%%%%%%@%%%###%%%++%#%@-.                       
                  .+@@@@@@%*%@@@%%%%%%@%%%%%@%%@@@@@@%%%%%%@%%%%%%@@@%%%@@*.                        
```