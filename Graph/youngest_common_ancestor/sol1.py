# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


# d: depth, n: node numbers
# time: O(d) | space: O(n)
def getYoungestCommonAncestor(top_ancestor, descendant_one, descendant_two):
    common_ancestor = {}
    common_ancestor[descendant_one.name] = descendant_one
    common_ancestor[descendant_two.name] = descendant_two
    while True:
        ancestor_one = descendant_one.ancestor
        ancestor_two = descendant_two.ancestor
        if ancestor_one is not None:
            descendant_one = ancestor_one
            if ancestor_one.name not in common_ancestor:
                common_ancestor[ancestor_one.name] = ancestor_one
            else:
                return common_ancestor[ancestor_one.name]
        if ancestor_two is not None:
            descendant_two = ancestor_two
            if ancestor_two.name not in common_ancestor:
                common_ancestor[ancestor_two.name] = ancestor_two
            else:
                return common_ancestor[ancestor_two.name]
