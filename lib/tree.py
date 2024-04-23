class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    result = None
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0 and result == None:
      node = nodes_to_visit.pop(0)

      if node['id'] == id:
        result = node
      else:
        #Depth first
        #nodes_to_visit = node['children'] + nodes_to_visit

        #Breadth first
        nodes_to_visit = nodes_to_visit + node['children']
    
    return result



