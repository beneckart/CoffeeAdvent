Add a .env file to root that says:

 `OPENAI_API_KEY=sk-proj-FfbiTV...`


 I have a half-based Flask web app for putting in data and running the algo, but I wouldn't use it. 

 Instead, just run `python app.py` and it will run `run_local_demo()` which just uses a manually created dictionary of people's notes for the day.

 TODO: make web app more usable, including adding field for which day is being input. change sqlite schema to add day field. make sure if it is the first entry for that day to skip running the algorithm

 Also, I scraped the official tasting notes and obfuscated them with rot13. Turns out they haven't posted notes for most of the days yet! 

 
