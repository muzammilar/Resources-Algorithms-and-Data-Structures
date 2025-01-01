### 649. Dota2 Senate

In the Dota2 game, there are two factions:

* Radiant (denoted by 'R')
* Dire (denoted by 'D')

Senators from both factions take turns in the Senate. On each senator’s turn:

* A senator can ban a senator from the opposing faction.
* If a senator can’t ban anyone, they lose their seat in the Senate.
* A senator from one faction can ban a senator from the opposing faction by choosing them from the queue of senators waiting to act.

The goal is to determine which faction will win:

* If all senators from one faction are banned, the other faction wins.
* If the game continues indefinitely (with no winners), the game is a tie.
