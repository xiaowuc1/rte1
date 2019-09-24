Test cases are roughly presented in increasing order of difficulty.

## Input File Format

The input file starts with a single line that is the ID of the test case.

The second line contains three space-separated positive integers, N, N, and M,
indicating that the graph has N vertices and M edges.

The next M lines contains three space-separated numbers, `u`, `v`, and `w`,
indicating that there is an undirected edge of weight `w` connecting vertices
`u` and `v`. These vertices are one-indexed.

The next line contains two space-separated positive integers, N and 1.

The next N lines each contain one value. These values comprise the `b` vector.

## Output File Format

The output file starts with a single line containing two space-separated
positive integers, N and 1.

The next N lines each contain one value. These values comprise the true answer
vector `x`.
