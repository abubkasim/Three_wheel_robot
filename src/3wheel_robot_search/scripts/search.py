#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def bfs(start, goal):
    queue = [(start, [start])]
    visited = set()

    while queue:
        (vertex, path) = queue.pop(0)
        if vertex in visited:
            continue
        visited.add(vertex)

        for neighbor in get_neighbors(vertex):
            if neighbor == goal:
                yield path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))

def get_neighbors(node):
    # Define the neighbors of each state here
    return []

def search_node():
    rospy.init_node('search_node', anonymous=True)
    start = 'state1'  # Set the start state
    goal = 'state2'   # Set the goal state
    paths = list(bfs(start, goal))
    rospy.loginfo("Paths: %s", paths)

if __name__ == '__main__':
    try:
        search_node()
    except rospy.ROSInterruptException:
        pass

