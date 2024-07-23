https://codeforces.com/contest/1994/problem/F

F. Stardew Valley
time limit per test = 2 seconds
memory limit per test = 256 megabytes

Pelican Town represents 𝑛
 houses connected by 𝑚
 bidirectional roads. Some roads have NPCs standing on them. Farmer Buba needs to walk on each road with an NPC and talk to them.

Help the farmer find a route satisfying the following properties:

The route starts at some house, follows the roads, and ends at the same house.
The route does not follow any road more than once (in both directions together).
The route follows each road with an NPC exactly once.
Note that the route can follow roads without NPCs, and you do not need to minimize the length of the route.
It is guaranteed that you can reach any house from any other by walking on the roads with NPCs only.

Input
Each test consists of multiple test cases. The first line contains an integer 𝑡
 (1≤𝑡≤104) — the number of test cases. Then follows the description of the test cases.

The first line of each test case contains two integers 𝑛
 and 𝑚
 (2≤𝑛≤5⋅105,1≤𝑚≤5⋅105) — the number of houses and roads in Pelican Town respectively.

In each of the next 𝑚
 lines, three integers 𝑢, 𝑣, and 𝑐 (1≤𝑢,𝑣≤𝑛,𝑐=0/1) are given — 
 the ends of the road and whether an NPC is on this road. 
 If 𝑐=1, then the road has an NPC. If 𝑐=0, then the road has no NPC.

The graph may contain multiple edges and loops, and if there are multiple edges with NPCs standing on them, the route must follow each of these roads.

It is guaranteed that you can reach any house from any other by walking on the roads with NPCs only.

It is guaranteed that the sum of 𝑛 and 𝑚 for all test cases does not exceed 5⋅105

Output
For each test case, if there is no solution, then output "No" (without quotes).

Otherwise, output "Yes" (without quotes), and then output 𝑘
 — the number of roads in the route. In the next line, output 𝑘+1
 numbers — the houses of the route in the order of traversal. Note that the first house should match the last one, as the route is cyclic.

If there are multiple answers, you can print any of them.

You can output each letter in any case (for example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as a positive answer).

Example input
3
3 2
1 2 1
2 3 1
3 3
1 2 1
1 3 1
2 3 0
5 9
1 2 0
5 2 1
5 4 1
5 1 1
2 3 1
5 2 1
4 1 0
4 3 0
5 2 0

output
NO
YES
3
1 2 3 1 
YES
7
1 2 5 4 3 2 5 1 

Note that in the third test case, there are multiple edges (5,2)
You must walk on two of them.
