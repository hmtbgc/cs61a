class Pair:
	def __init__(self, first, second):
		self.first = first
		self.second = second

	def __repr__(self):
		return 'Pair({0}, {1})'.format(self.first, self.second)

class nil:
	def __repr__(self):
		return 'nil'

nil = nil()
q_ex = Pair('+', Pair(2, Pair(3, nil)))
q_1 = 4.67
q_2 = True
q_3 = 'list'
q_4 = Pair('cons', Pair(2, Pair(3, nil)))
q_5 = Pair('if', Pair(Pair('<', Pair('x', Pair(0, nil))), Pair(1, Pair(Pair('+', Pair('x', Pair(1, nil))), nil))))
q_6 = Pair('quote', Pair('hello', nil))
