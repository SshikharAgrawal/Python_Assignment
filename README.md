In this problem we need to understand, what exactly surrouned by 'X' means. It actually means that if we start from 'O' at the border, and we traverse only 'O', only those 'O' are not surrouned by 'X'. So the plan is the following:

Start dfs or bfs from all 'O', which are on the border.
When we traverse them, let us color them as '-1', temporary color.
Now, when we traverse all we wanted, all colors which are not -1' need to renamed to 'X' and all colors which are '-1' need to be renamed to 'O', and that is all!
Compexity: time complextiy is O(mn), where m and n are sizes of our board. Additional space complexity can also go upto O(mn) to keep stack of recursion.
