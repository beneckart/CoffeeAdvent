Add a .env file to root that says:

 `OPENAI_API_KEY=sk-proj-FfbiTV...`


 I have a half-baked Flask web app for putting in data and running the algo, but I wouldn't use it. 

 Instead, just run `python app.py` and it will run `run_local_demo()` which just uses a manually created dictionary of people's notes for the day.

 TODO: make web app more usable, including adding field for which day is being input. change sqlite schema to add day field. make sure if it is the first entry for that day to skip running the algorithm

 Also, I scraped the official tasting notes and obfuscated them with rot13. Turns out they haven't posted notes for most of the days yet! 

> Qnl 01. Senzvyl: Onxrq Nccyr | Rney Terl | Onxre'f Pubpbyngr | Oreevrf
> 
> Qnl 02. Zrkvpb Wbfé Nethryyb Angheny: Fgenjoreel | Jvar | Qnex Pubpbyngr | Yvzr
> 
> Qnl 03. Rguvbcvn Unognzh Srxnqh Ntn: Wnfzvar | Ncevpbg | Ubarl | Grn-Yvxr
> 
> Qnl 04. Xraln Tvpungunvav NN: Tencrsehvg | Cyhz | Fhtne Pnar | Whvpl
> 
> Qnl 05. Thngrznyn Ry Fbpbeeb Znenpngheen: Punzbzvyr | Enj Fhtne | Nccyr | Juvgr Sybjre
> 
> Qnl 06. Ry Fnyinqbe Fnagn Ebfn Ubarl: Pbapbeq Tencr | Qrzrenen Fhtne | Ebfr | Qnex Pubpbyngr
> 
> Qnl 07. Rguvbcvn Orxryr Xnpunen Angheny: Zvkrq Oreevrf | Wnfzvar | Cyhz | Cvarnccyr
> 
> Qnl 08. Pbfgn Evpn Ynf Ynwnf Angheny: Pbapbeq Tencr | Inavyyn | Cbzrtenangr | 60% Qnex Pubpbyngr
> 
> Qnl 09. :
> 
> Qnl 10. :
> 
> Qnl 11. Pbybzovn Ncbagr Ivyyntr Ubarl: Qevrq Pureel | Enj Ubarl | Cncnln | Fvyxl
> 
> Qnl 12. :
> 
> Qnl 13. :
> 
> Qnl 14. :
> 
> Qnl 15. :
> 
> Qnl 16. Ry Fnyinqbe Fnagn Ebfn:
> 
> Qnl 17. :
> 
> Qnl 18. Rguvbcvn Funxvfb Srznyr-Cebqhprq Angheny: Cvarnccyr | Fgenjoreel | Wnfzvar | Fjrrg Grn
> 
> Qnl 19. :
> 
> Qnl 20. :
> 
> Qnl 21. :
> 
> Qnl 22. :
> 
> Qnl 23. :
> 
> Qnl 24. :
> 
