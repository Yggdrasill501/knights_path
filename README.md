# Algorithm for shortest path of Knight

## Depth search
Depth search of chessboard is stored in [depth_first_search package](/depth_first_search), [knights_tour file](/depth_first_search/knights_tour.py) 
and for user interaction [console file](/depth_first_search/console.py)

### Knights Tour
Knight tour contains class [KnightTour](https://github.com/Yggdrasill501/knights_path/blob/main/depth_first_search/knights_tour.py#L9-L188)
that stores implementation of [depth first search](https://en.wikipedia.org/wiki/Depth-first_search) algorithm and [Warnsdorff's rule](https://en.wikipedia.org/wiki/Knight%27s_tour)

#### KnightTour class contains:
-  [Constructor](https://github.com/Yggdrasill501/knights_path/blob/main/depth_first_search/knights_tour.py#L12-L22) 
Method that initialize class, get chessboard size from user input, chessboard that generate chessboard that is list of lists 
which is representation of squared chessboard of chessboard size and it's filled with -1, moves row that represent how 
knight can move on the chessboard, moves row represents the possible changes in the row positions, moves column represents 
the possible changes in the column positions, count represents the number of possible moves.

- [Find path](https://github.com/Yggdrasill501/knights_path/blob/main/depth_first_search/knights_tour.py#L25-L39) 
Starts the search for a knight's tour from the given position, Row index to start the tour from, default is 0.
Column index to start the tour from, defaults to 0.