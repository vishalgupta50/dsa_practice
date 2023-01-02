"""
"Sherlock has been a great mastermind, but Jim Moriarty never resists to trick Sherlock."
"This time again,Jim decided to give Sher ock a weird TREE ENIGMA puzzle.If Sherlock fails to solve this, Moriarty will wreak havoc
in the lives of people Sherlock loves."
Sherlockis provided a tree comprising N nodes. The tree is rooted at node 1.
Every node has a binary value assigned to it ·either 0 or 1.These initialvalues are denoted by an array Arr [ ). However. some of
these binary values are corrupted.
These values have to be replaced with correct binary values. These correct values are denoted by another array Brr [ J .
Sherlock can only perform the given two types of operations on the tree ·
"1.Invert the value of ;th node ,i.e in case the value is 0,change it to 1,or vice-versa."
"2. Invert the values of all the nodes in the subtree of;th node ,i.e allthe nodes in the subtree of node i(includingi) ."
"In order to solve this puzzle,Sherlock has to find out the minimum number of operations required to change the values of nodes to correct ones."

Input
First line contains a single integer N·the number of nodes in the tree.  N 1lines follow.
"Each line contains 2 space-separatedintegers U ,V on eachline denoting that there is an edge between U and V."
"The next line contains N space-separatedintegers of the array Arr [ ],denot ng the initialvalues of the nodes. Eachinteger is either 0 or 1."
"The next line contains N space-separatedintegers of the array Brr [ ],denoting the required correct values of the nodes. Each integer is either O or 1."

Output
Output the minimum number of operations needed by Sherlock to change the values of the nodes frominitial to the correct ones.
Constraints
1<=N< =105
"1<= Arr;,Brr;< ={0,1}"
"1<=U,V<:N ,U! V"


Input:
7
3 7
1 7
7 4
3 2
1 6
5 1
1 0 1 1 1 1 0
0 0 1 0 1 0 1

Output: 3


"""