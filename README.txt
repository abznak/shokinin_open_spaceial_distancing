Open Space-ial Distancing

This is Tim Smith's solution to the "Open Space-ial Distancing" Shokinin puzzle.  The details of the puzzle are below.





======  From Andy's email:
Open Space-ial Distancing

Background

You've just fixed the build and you are hungry.  It's well past lunchtime.

Unfortunately, you are trapped at the back of your client's office in the furthest row of desks from the exit.  There is a food truck just outside the office, but it is leaving soon and is your only option for lunch today!

You'll need to make it to the other end of the office to leave the building, attack the food truck and satisfy your growling stomach.

Sounds easy?  Not so.

Some of the office is occupied with people who have wisely visited the food truck already and are now settling into their afternoon's work (i.e., sleeping peacefully at their desk).  

In a staggering display of 1960s utilitarian office design, there are identical beige formica desks every 2 metres across the width of the office and every 2 metres from the back of the office (where you sit) to the front... and access to deep fried heaven!  These desks form a perfectly bland grid of 10 rows of 10 desks each.

Challenge

Current company policy insists you must always keep at least 1.5m away from all colleagues (punishment for failing to do so is an extra 20 hours of online compliance training), so you'll need to find a way out of the office without going near any occupied desk.  


Not every desk is occupied.  The percentage of occupied desks is p.  (0.0 ≤ p ≤ 1.0)

Your task is to calculate the chance of finding an OHS-approved way to leave the office for various values of p.  

Start with a value of 0 for p (i.e., a completely empty office apart from yourself) and add 0.1 to it until you reach 1.0 (i.e., a fully occupied office including yourself).  For each value of p, randomly populate the office and try to plot a safe way through.  Repeat this process a significant number of times to be confident of your results.

Your calculation is the percentage of random offices which have (at least one) safe exit path for each value of p.  Sample output would look something like:

Number of samples for each p: 10000

1.0 0.000

0.9 0.000

0.8 0.000

0.7 0.000

0.6 0.011

0.5 0.074

0.4 0.625

0.3 0.940

0.2 1.000

0.1 1.000

0.0 1.000

Note: You are a mere IT consultant, so jumping 2 metres over or diagonally across an occupied desk is not a skill you have IRL.

======