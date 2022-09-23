# Interview-schedule-bot

The bot is used to converse with potential candidates. The chatbot gives a brief description of the company and the job role then asks the candidate if they are willing to take up the job and schedules an interview.

Developed using Rasa 3.x

## Steps to run the Bot

### Create and run a python environemnt 

Using Anaconda Prompt, run the following commands in the your preferred directory 
```bash
conda create -n envname python=3.6 anaconda
conda activate envname
```
Or refer [here](https://www.geeksforgeeks.org/set-up-virtual-environment-for-python-using-anaconda/)

### Create a new rasa project

Run the following commmand after activating the python environment 
```bash
rasa init
```

### Install dependencies for the bot

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Run 'pip install rasa-sdk' in the python environment

### Overview of the files( also reffered to as dependencies)

`data/nlu/nlu.yml` - contains NLU training data

`data/nlu/rules.yml` - contains rules training data

`data/stories/stories*.yml` - contains stories training data

`actions.py` - contains custom action/api code

`domain.yml` - the domain file, including bot response templates

`config.yml` - training configurations for the NLU pipeline and policy ensemble

`tests/` - end-to-end tests

### Replace the files

Replace the default contents of the files with files in the repository 

### Run the bot

Use `rasa train` to train a model.

Then, to run, first set up your action server in one terminal window :
```bash
rasa run actions
```
In another prompt window, run the duckling server (for entity extraction):

```bash
docker run -p 8000:8000 rasa/duckling
```
Then to talk to the bot, run:
```
rasa shell --debug
```
Note that `--debug` mode will produce a lot of output meant to help you understand how the bot is working
under the hood. To simply talk to the bot, you can remove this flag.

Use should now be able to communicate with the bot in developer mode

