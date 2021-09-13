#o(depth) t, o(depth) s
#doesn't work sometimes
def getYoungestCommonAncestor(top_ancestor, node1, node2):
  #edge case for node's being at top
  if node1.ancestor is None and node2.ancestor is None: return None
  elif node1.ancestor is None and node2.ancestor is not None: return node1
  elif node1.ancestor is not None and node2.ancestor is None: return node2
  #for each node, add their ancestors to a set called ancestors_found
  #there should be a curr_node1 & curr_node2 that travels on its ancestry, all the 
  #while adding its curr node that it's at to the set
  #start with each node's first ancestor
  curr_nodes = [node1.ancestor, node2.ancestor]
  all_ancestors_found = set()
  #loop, stop when 
  while not(len(curr_nodes) == 0):
    for node in curr_nodes:
      if node not in all_ancestors_found:
        all_ancestors_found.add(node)
      else:
        #there's a repeat, this node is the youngest common ancestor
        return node
    #for all eligible nodes, go to next node
    for i in range(len(curr_nodes)):
      curr_nodes[i] = curr_nodes[i].ancestor
      #if any of our curr nodes is None, then delete it from our list
      if curr_nodes[i] is None:
        del curr_nodes[i]
  #couldn't find a matching ancestor, this shouldn't happen assuming you get proper
  #descendant nodes
  return None


"""
Below code are the tests from algoexpert that identified some problems that 
worked and some that didn't.
"""


# Add, edit, or remove tests in this file.
# Treat it as your playground!

import program
import unittest


class StartAncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


progAT = StartAncestralTree
if hasattr(program, "AncestralTree"):
    progAT = program.AncestralTree


class AncestralTree(progAT):
    def addAsAncestor(self, descendants):
        for descendant in descendants:
            descendant.ancestor = self


ancestralTrees = {}
ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for letter in ALPHABET:
    ancestralTrees[letter] = AncestralTree(letter)
ancestralTrees["A"].addAsAncestor(
    [ancestralTrees["B"], ancestralTrees["C"], ancestralTrees["D"], ancestralTrees["E"], ancestralTrees["F"]]
)
ancestralTrees["B"].addAsAncestor([ancestralTrees["G"], ancestralTrees["H"], ancestralTrees["I"]])
ancestralTrees["C"].addAsAncestor([ancestralTrees["J"]])
ancestralTrees["D"].addAsAncestor([ancestralTrees["K"], ancestralTrees["L"]])
ancestralTrees["F"].addAsAncestor([ancestralTrees["M"], ancestralTrees["N"]])
ancestralTrees["H"].addAsAncestor([ancestralTrees["O"], ancestralTrees["P"], ancestralTrees["Q"], ancestralTrees["R"]])
ancestralTrees["K"].addAsAncestor([ancestralTrees["S"]])
ancestralTrees["P"].addAsAncestor([ancestralTrees["T"], ancestralTrees["U"]])
ancestralTrees["R"].addAsAncestor([ancestralTrees["V"]])
ancestralTrees["V"].addAsAncestor([ancestralTrees["W"], ancestralTrees["X"], ancestralTrees["Y"]])
ancestralTrees["X"].addAsAncestor([ancestralTrees["Z"]])


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        yca = program.getYoungestCommonAncestor(ancestralTrees["A"], ancestralTrees["A"], ancestralTrees["B"])
        self.assertTrue(yca == ancestralTrees["A"])

    def test_case_2(self):
        yca = program.getYoungestCommonAncestor(ancestralTrees["A"], ancestralTrees["B"], ancestralTrees["F"])
        self.assertTrue(yca == ancestralTrees["A"])

    def test_case_3(self):
        yca = program.getYoungestCommonAncestor(ancestralTrees["A"], ancestralTrees["G"], ancestralTrees["M"])
        self.assertTrue(yca == ancestralTrees["A"])

    def test_case_4(self):
        yca = program.getYoungestCommonAncestor(ancestralTrees["A"], ancestralTrees["U"], ancestralTrees["S"])
        self.assertTrue(yca == ancestralTrees["A"])

    def test_case_5(self):
        yca = program.getYoungestCommonAncestor(ancestralTrees["A"], ancestralTrees["Z"], ancestralTrees["M"])
        self.assertTrue(yca == ancestralTrees["A"])

    def test_case_6(self):
        yca = program.getYoungestCommonAncestor(ancestralTrees["A"], ancestralTrees["O"], ancestralTrees["I"])
        self.assertTrue(yca == ancestralTrees["B"])

    def test_case_7(self):
        yca = program.getYoungestCommonAncestor(ancestralTrees["A"], ancestralTrees["T"], ancestralTrees["Z"])
        self.assertTrue(yca == ancestralTrees["H"])

    def test_case_8(self):
        yca = program.getYoungestCommonAncestor(ancestralTrees["A"], ancestralTrees["T"], ancestralTrees["V"])
        self.assertTrue(yca == ancestralTrees["H"])

    def test_case_9(self):
        yca = program.getYoungestCommonAncestor(ancestralTrees["A"], ancestralTrees["T"], ancestralTrees["H"])
        self.assertTrue(yca == ancestralTrees["H"])

    def test_case_10(self):
        yca = program.getYoungestCommonAncestor(ancestralTrees["A"], ancestralTrees["W"], ancestralTrees["V"])
        self.assertTrue(yca == ancestralTrees["V"])

    def test_case_11(self):
        yca = program.getYoungestCommonAncestor(ancestralTrees["A"], ancestralTrees["Z"], ancestralTrees["B"])
        self.assertTrue(yca == ancestralTrees["B"])

    def test_case_12(self):
        yca = program.getYoungestCommonAncestor(ancestralTrees["A"], ancestralTrees["Q"], ancestralTrees["W"])
        self.assertTrue(yca == ancestralTrees["H"])

    def test_case_13(self):
        yca = program.getYoungestCommonAncestor(ancestralTrees["A"], ancestralTrees["A"], ancestralTrees["Z"])
        self.assertTrue(yca == ancestralTrees["A"])