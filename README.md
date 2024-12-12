Abstract: Even prior to the meme stock craze, retail traders were actively sharing trade ideas on various online communities. From Twitter to Discord, traders followed in the footsteps of “gurus” who pitched “plays” which would supposedly make them money. When there can be several hundred thousand users on a server, any alert could have a direct, noticeable impact on the market. The goal of this project is to analyze the time surrounding each alert from two angles - prices and trades - to determine the impact of these alerts on the market. We notice that in the minutes following a buy alert, the best bid of the contract in question increases much more than its neighboring contracts. Similarly, in the minutes following a sell alert, the best ask of the contract in question decreases more than its neighboring contracts. There are less noticeable impacts on aggregate trades due to the sheer quantity of trades that happen in any given period. 

Description of code:

- All files labelled callapi*.py were used to call the ThetaData API for the necessary data. This requires having the theta data Java terminal open locally.
- All files labelled evaluation*.py were used to evaluate outputs, generate figures, and run statistical tests
- All files labelled helper*.py purely contain helper functions used in the other files.
- All files labelled processing*.py were used to convert raw data obtained through the callapi*.py files into consolidated, cleaned files usable in the evaluation*.py files

Please email me at LwL@mit.edu if specific questions about the code arise.



