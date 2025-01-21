class SegmentTree:
    """Segment tree iterative implementation"""

    def __init__(self, n):
        self.n = n
        self.tree = [0] * 2 * n

    def build(self, input_array):
        """
            Build the segment tree
        """
        # This is the bottom level of the tree, each node contains 1 element!
        self.tree[self.n: 2 * self.n] = input_array

        # Build the tree bottom-up
        for i in range(self.n - 1, 0, -1):
            # node(i) -> left_child: 2i and right_child: 2i+1
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

        print(self.tree)

    def query(self, l, r):
        """
            Query the sum of range [l, r]
        """
        result = 0

        # Adding n as we start computing the result bottom-up
        l += self.n
        r += self.n

        while l <= r and l != 0:
            if l & 1:   # l is the right child! add it to result as we'll skip it's parent
                result += self.tree[l]
                l += 1  # This will skip the parent of l!
            if not (r & 1):  # r is the left child! add it to result as we'll skip it's parent
                result += self.tree[r]
                r -= 1  # This will skip the parent of r!
            # Move to the parents of l and r, parent(l) = floor(l/2)
            l //= 2
            r //= 2
        return result

    def update(self, pos, val):
        # Adding n as we start updating the tree bottom-up
        pos += self.n
        diff = val - self.tree[pos]
        while pos > 0:  # Update node(pos) -> parent(pos) -> so on until root
            self.tree[pos] += diff
            pos //= 2


if __name__ == "__main__":
    stree = SegmentTree(6)
    stree.build([1, 2, 3, 4, 5, 6])
    print(stree.query(1, 4))
    stree.update(2, 5)
    print(stree.query(1, 4))
