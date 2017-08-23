class Solution:
	def distributeCandies(self, candies):
		"""
		:type candies: List[int]
		:rtype: int
		"""

		# She can only take half of the list
		# From the amount she can take, find the max amount of unique candy she can take
		sister_amount = candies / 2
		num_of_unique_candy = 0

		my_hash = {}
		for candy in candies:
			if candy not in my_hash:
				my_hash[candy] = 1

		for key in my_hash.keys():
			num_of_unique_candy += 1

		if num_of_unique_candy > sister_amount:
			# num of unique candy is higher than sister amount, so sister amount is the max we can return
			return sister_amount
		else:
			# num of qunieu candy is lower, so return that
			return num_of_unique_candy