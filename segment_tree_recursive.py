class SegmentTree:
    """Segment tree using recursion"""

    def __init__(self, n):
        self.n = n
        self.tree = [0] * 4 * n  # List to store the segment tree

    def build_tree(self, input_array):
        self.input_array = input_array
        self.__build(
            0, 0, self.n - 1
            # Start building the tree from root node: pos = 0, and stores results from range [0, n-1]
        )

        print(self.tree)

    def __build(self, pos, st, end):
        """
        Performs two steps
        1. Get the results of left and right children by making recursive calls
        2. Update the result in the current node
        """
        if st == end:
            self.tree[pos] = self.input_array[st]
        else:
            mid = (st + end) // 2
            self.tree[pos] = self.__build(pos * 2 + 1, st, mid) + self.__build(
                pos * 2 + 2, mid + 1, end
            )

        return self.tree[pos]

    def query(self, l, r):
        if l == r:  # Trivial case, return the result directly
            return self.input_array[l]
        # Start the query from the root node for range [l, r]
        return self.__query_children(0, 0, self.n - 1, l, r)

    def __query_children(self, pos, st, end, l, r):
        """
        Recursively compute the result for range [l, r]
        The current node is stored at pos and has result from range [st, end] from the input array
        """
        if st > r or end < l:  # Skip this node as it doesn't cover any subarray from [l, r]
            return 0

        # The entire node is a subarray of [l, r], return its result
        if st == l and end == r:
            return self.tree[pos]
        else:  # The range [l, r] is a subarray of [st, end] so recursively compute the result by calling children
            mid = (st + end) // 2
            return self.__query_children(
                pos * 2 + 1, st, mid, l, min(r, mid)
            ) + self.__query_children(pos * 2 + 2, mid + 1, end, max(l, mid + 1), r)

    def update(self, loc, new_val):
        return self.__update(
            0, 0, self.n - 1, loc, new_val
        )  # Set the value of the element at loc to new_val

    def __update(self, pos, st, end, loc, new_val):
        """
        If we reach the node with loc then update it
        Else, if loc is within the range [l, r] then recursively update its children and then the current node
        """
        if st == end and st == loc:
            self.tree[pos] = new_val
        elif st <= loc and end >= loc:
            mid = (st + end) // 2
            self.tree[pos] = self.__update(
                pos * 2 + 1, st, mid, loc, new_val
            ) + self.__update(pos * 2 + 2, mid + 1, end, loc, new_val)

        return self.tree[pos]


if __name__ == "__main__":
    stree = SegmentTree(6)
    stree.build_tree([1, 2, 3, 4, 5, 6])
    print(stree.query(1, 4))
    stree.update(2, 5)
    print(stree.query(1, 4))
