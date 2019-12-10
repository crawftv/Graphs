def get_parents(family_tree, starting_node):
    try:
        return family_tree[starting_node]["parents"]
    except KeyError:
        return []


def earliest_ancestor(ancestors, starting_node):
    # create family_tree
    family_tree = {}
    parents = [i[0] for i in ancestors]
    children = [i[1] for i in ancestors]
    family_members = set(parents + children)
    for i in family_members:
        family_tree[i] = {"parents": set(), "children": set()}
    for i in ancestors:
        family_tree[i[0]]["children"].add(i[1])
        family_tree[i[1]]["parents"].add(i[0])

    # start
    ancestors = []
    parents = get_parents(family_tree, starting_node)

    if len(parents) > 0:
        for i in parents:
            ancestors.append(i)
    else:
        return -1

    #    import pdb;pdb.set_trace()
    while len(ancestors) > 0:
        new_ancestors = []
        for xx in ancestors:
            parents = get_parents(family_tree, xx)
            for yy in parents:
                ancestors.append(yy)
            if len(ancestors) > 1:
                ancestors.pop(0)
            else:
                return min(ancestors)

    return


if __name__ == "__main__":
    test_ancestors = [
        (1, 3),
        (2, 3),
        (3, 6),
        (5, 6),
        (5, 7),
        (4, 5),
        (4, 8),
        (8, 9),
        (11, 8),
        (10, 1),
    ]
    s = earliest_ancestor(test_ancestors, 3)
    print(s)
