
# TIN Surface
This project was created for a CS/Geography course.  It creates a TIN (Triangulated Irregular Network) surface out of input vertices and triangles and stores it in a PR quadtree. It can then traverse the tree, and find local maxima and minima in the terrain. Project could be extended to find watershed, lines of sight, ect.

## Usage
Code is run through the python command window:

    main_pr_quadtree1.py [FILENAME] [CAPACITY]

 `capacity` is an integer that determines how many points (aka vertices) can be in one leaf of the pr_quadtree
 
`FILENAME` is a `.txt` file in the format:

    [LENGTH_OF_SQUARE_AREA]
    [NUMBER_OF_POINTS]
    [P1.X] [P1.Y] [P1.ELEVATION]
    ...
    [PN.X] [PN.Y] [PN.ELEVATION]
    [NUMBER_OF_TRIANGLES]
    [T1.V1] [T1.V2] [T1.V3] 
    ...
    [TN.V3] [TN.V4] [TN.V5]

Where each of the Triangle vertex is a reference to a point inserted based on it's position in the insertion order. `insert.txt` is included as an example of this format.
