# Predictive-Model-Football
  Gamble responsibly
  
  Using data from the last ~4 years this program tries to predict how many yards Josh Allen (the current QB1 for the Buffalo Bills) will get 
  depending on what team they are playing.
  
  The program is set to provide the yards against the patriots by default, to see any other team look 
  for the abbreviated name, and replace "pats" on line 63 of "josh.py" with whichever team you wish to see. 

  Abbreviated Names:
    jets, pats, lions, rams, niners, chiefs, colts, dolphins, hawks, titans, texans, ravens, jags, cardinals, raiders, chargers, bengals, 
    eagles, commanders, broncos, cowboys, giants, bucs, ravens, vikings, packers, steelers, browns, bears, saints, falcons.

Example output:
Data Loaded Successfully.
   year   team  yards
0  2024   jets    182
1  2024   jets    215
2  2024   pats    154
2  2024   pats    154
3  2024  lions    362
4  2024  rams     342
Training Set Size: (72, 31)
Testing Set Size: (18, 31)

Mean Absolute Error: 77.2534537037037
R-squared Score: -0.21182772322162147
Predicted Passing Yards for pats in 2024: 170.4725

