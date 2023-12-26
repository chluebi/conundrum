---
title: Understanding the CRS Matrix format
date: 2023-12-26
draft: false
tags:
  - featured
  - numcs
  - linalg
---
The compressed row storage (CRS) format is a matrix storage format for sparse matrices, which is most useful for matrices which have a linear number of non-zero elements (compared to dense matrices having a quadratic number of non-zero elements).

### Storage

The format takes a $n \times m$ matrix $A$ and turns it into the following arrays:

- The ``val`` array stores all the values of the non-zero elements of the matrix, therefore it has length $\textrm{nnz}(A)$ (the number of non-zero elements in $A$)
- The `col_ind` array stores for each non-zero element of the matrix the column index it is in, therefore it has length $\textrm{nnz}(A)$
- The ``row_ptr`` array stores for each *row* when that row starts in the other two arrays, plus it always ends with the sentinel value, therefore it has length of $\textrm{rows}(A) + 1 = n + 1$

Therefore, the number of values we need to store a $n \times m$ matrix is
$$2 \cdot \textrm{nnz}(A) + n + 1$$

### Examples
$$
\begin{pmatrix}
1 & 0 & 2 \\\
3 & 4 & 5 \\\
0 & 0 & 0 \\\
0 & 0 & 6
\end{pmatrix}
$$
We start with
- `val = []`
- `col = []`
- `row_ptr = [1]`
The $1$ in the ``row_ptr`` array indicates that we are starting the first row with the first element in `val` (which has yet to be added). Also notice that we are doing $1$-indexing here.

Now go through the first row, the $1$ is in the first column, so we get
- `val = [1]`
- `col = [1]`
- `row_ptr = [1]`

The $2$ is in the third row, so we get
- `val = [1, 2]`
- `col = [1, 3]`
- `row_ptr = [1]`

Now we reach the end of the row, which means the next row will start with the *third* elements in `val` and `col` (because the first two elements belong to the first row).
- `val = [1, 2]`
- `col = [1, 3]`
- `row_ptr = [1, 3]`

After the next row:
- `val = [1, 2, 3, 4, 5]`
- `col = [1, 3, 1, 2, 3]`
- `row_ptr = [1, 3, 6]`

The next row is all zeroes, so all we will be adding is another $6$ to `row_ptr`:
- `val = [1, 2, 3, 4, 5]`
- `col = [1, 3, 1, 2, 3]`
- `row_ptr = [1, 3, 6, 6]`

And finally, after the last row:
- `val = [1, 2, 3, 4, 5, 6]`
- `col = [1, 3, 1, 2, 3, 3]`
- `row_ptr = [1, 3, 6, 6, 7]`



Here is another example:
$$
\begin{pmatrix}
1 & 0 & 4 \\\
2 & 0 & 5 \\\
3 & 0 & 6
\end{pmatrix}
$$
- `val = [1, 4, 2, 5, 3, 6]`
- `col = [1, 3, 1, 3, 1, 3]`
- `row_ptr = [1, 3, 5, 7]`


### Interesting specifics
- Adding an empty row to a matrix, means adding an element to `row_ptr`, adding an empty column, uses no additional storage
- The first element of `row_ptr` is always $1$, the last element (the sentinel value) is always $\textrm{nnz}(A)+1$
- The sentinel value could be inferred by other things (e.g., length of `row_ptr`) but we store it because it simplifies the specification of the format and the implementation of operations within it


### Compressed Column Storage
The sister format of compressed row storage is compressed column storage. The format is almost self-explanatory. Instead of going row-wise through the matrix and storing `col` and `row_ptr` we store `row` and `col_ptr`.


$$
\begin{pmatrix}
1 & 0 & 4 \\\
2 & 0 & 5 \\\
3 & 0 & 6 
\end{pmatrix}
$$
Becomes:
- `val = [1, 2, 3, 4, 5, 6]`
- `row = [1, 2, 3, 1, 2, 3]`
- `col_ptr = [1, 4, 7]`

