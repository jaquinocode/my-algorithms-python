'''
1->2->4        3->5->6
^              ^

'''
#o(n) time, o(1) space
def merge_two_lists(l1, l2):
  #initialize left and right pointer to head of l1 and l2 respectively
  left = l1
  right = l2

  #enter loop
  #stop when left and right are both None
  while not(left is None and right is None):
  #compare left and right, left wins if right is None and vice versa
    #if a tie, left wins
    winner_dir = get_winner_dir(left, right)  #string

    #save that e to a var, then incr arrow that won
    winner_node = left if winner_dir == 'left' else right
    if winner_dir == 'left': #left won
      left = left.next
    elif winner_dir == 'right': #right won
      right = right.next

    #todo: if result not set, set it to this e, set it as the tail as well
    
    #set tail's next to e
    tail.next = winner_node
    #e.next set to None
    winner_node.next = None
    #incr tail
    tail = tail.next
    #go to next loop
