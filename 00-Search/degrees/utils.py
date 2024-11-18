def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    
    start = Node(source, None, None)
    frontier = QueueFrontier()
    frontier.add(start)

    explored = set()

    while True:

        if frontier.empty():
            # No solution
            return None

        node = frontier.remove()

        explored.add(node.state)

        neighbors = neighbors_for_person(node.state)

        for action, state in neighbors:
            if state == target:
                actions = []
                cells = []

                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent

                actions.reverse()
                cells.reverse()
                solution = [actions, cells]
                return solution

            if not frontier.contains_state(state) and state not in explored:
                child = Node(state, node, action)
                frontier.add(child)