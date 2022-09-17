# Interview-schedule-bot

The bot is used to converse with potential candidates, gives a brief description of the company and the job role then asks the candidate if they are willing to take up the job and schedules an interview.

Developed using Rasa 3.x


## Run the bot

Use `rasa train` to train a model.

Then, to run, first set up your action server in one terminal window, listening on port 5055:
```bash
rasa run actions
```
In another window, run the duckling server (for entity extraction):

```bash
docker run -p 8000:8000 rasa/duckling
```
Then to talk to the bot, run:
```
rasa shell --debug
```

Note that `--debug` mode will produce a lot of output meant to help you understand how the bot is working
under the hood. To simply talk to the bot, you can remove this flag.
