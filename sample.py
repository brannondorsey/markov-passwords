import pickle
import time
import numpy as np

max_ngrams = 3 # ngram size
num_generate = 10000 # number of passwords to generate

# generate a single new password using a stats dict
# created during the training phase 
def gen_password(stats, n):
	output = '`' * n
	for i in range(100):
		output += gen_char(output[i:i + n])
		if output[-1] == '\n':
			return output[0:-1].replace('`', '')[0:-1]

# Sample a character if the ngram appears in the stats dict.
# Otherwise recursively decrement n to try smaller grams in
# hopes to find a match (e.g. "off" becomes "of").
# This is a deviation from a vanilla markov text generator
# which one n-size. This generator uses all values <= n.
# preferencing higher values of n first. 
def gen_char(ngram):
	if ngram in stats:
		# sample from the probability distribution
		return np.random.choice(stats[ngram].keys(), p=stats[ngram].values())
	else:
		print('{} not in stats dict'.format(ngram))
		return gen_char(ngram[0:-1])

with open('data/{}-gram.pickle'.format(max_ngrams)) as file:
	stats = pickle.load(file)

# start = time.time()

for i in xrange(num_generate):
	pw = gen_password(stats, max_ngrams)
	if pw is not None:
		print(pw)

# print('finished in {:.2f} seconds'.format(time.time() - start))
