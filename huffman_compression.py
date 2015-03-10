import Queue
import string
text_file = open("ascii.txt","r")
text = text_file.read()
text_file.close()

characters = {}
freq = []

#print text[0]

for items in text:
	if items in characters:
		characters[items] += 1
	else:
		characters[items] = 1

print characters

for items in characters:
	tup = (characters[items], items)
	freq.append(tup)

print freq


class HuffmanNode(object):
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right
        self.root = root     # Why?  Not needed for anything.
    def children(self):
        return((self.left, self.right))


def create_tree(frequencies):
    p = Queue.PriorityQueue()
    for value in frequencies:    # 1. Create a leaf node for each symbol
        p.put(value)             #    and add it to the priority queue
    while p.qsize() > 1:         # 2. While there is more than one node
        l, r = p.get(), p.get()  # 2a. remove two highest nodes
        node = HuffmanNode(l, r) # 2b. create internal node with children
        p.put((l[0]+r[0], node))
        #print (l[0]+r[0], node) # 2c. add new node to queue      
    return p.get()               # 3. tree is complete - return root node

node = create_tree(freq)
print node

# Recursively walk the tree down to the leaves,
#   assigning a code value to each symbol
def walk_tree(node, prefix="", code={}):
	for value in freq:
		code[value] = None
		curr_branch = node
		if curr_branch[1].children() != None:
			### check left right, go whichever is available


	print code


	tree = Queue.PriorityQueue
	tree.put(node)

	while tree.qsize() > 0:
		tree.put(node[1].children)



	







		#print curr_branch[1].left
		#print node[1].right
		#while curr_branch[1].children:  #fix this, check for children first
			#go right if there is still a branch on the right append a 1 for each right step
		#	if isinstance(curr_branch[1].right[1], basestring):
				# also append 1 here to code and associate w/ printed symbol below
		#		print curr_branch[1].right
		#		curr_branch[1].right = None
		#		print curr_branch[1].right
		#		curr_branch = curr_branch[1].right[1]

				#curr_branch[1].right
		#	elif not isinstance(curr_branch[1].right[1], basestring):
		#		curr_branch = curr_branch[1].right

				#append 1 here
	return(code)


code = walk_tree(node)
#for i in sorted(characters, reverse=True):
#    print(i[1], '{:6.2f}'.format(i[0]), code[i[1]])
