from collections import deque

class TaskNode:
	def __init__(self, cnt, nxtTime):
		self.cnt = cnt
		self.nxtTime = nxtTime

	def show(self):
		print(self.cnt,":",self.nxtTime)

class Solution:
	print('Solution')
	q = deque()
	q.append(TaskNode(0, 0))
	q.append(TaskNode(1, 1))
	q.append(TaskNode(2, 2))
	q.append(TaskNode(3, 3))

	for tsk in q:
		print(tsk.cnt)


solution = Solution()

