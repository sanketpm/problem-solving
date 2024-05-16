def CourseSchedule(nCourses, preReq) -> bool:
    preMap = {}

    for i in range(nCourses):
        preMap[i] = []

    for i, course in preReq:
        preMap[i].append(course)

    visited = set()

    def dfs(course):
        if course in visited:
            return False
        
        if preMap[course] == []:
            return True
        
        visited.add(course)

        for preCourse in preMap[course]:
            if not dfs(preCourse):
                return False
        
        visited.remove(course)
        preMap[course] = []

        return True

    for course in range(nCourses):
        if not dfs(course):
            return False

    return True

print(CourseSchedule(2, [[1, 0]]))
# print(CourseSchedule(5, [[0, 1],[0, 2], [1, 3], [1, 4], [3, 4]]))