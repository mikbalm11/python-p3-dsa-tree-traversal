class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit = [self.root]
    while nodes_to_visit:
      # 1. Remove the first node from the `nodes_to_visit` list
      current = nodes_to_visit.pop()
      # 2. Add its value to the result list
      if current['id'] == id:
        return current
      # 3. Add its children (if any) to the BEGINNING of the `nodes_to_visit` list
      nodes_to_visit = nodes_to_visit + current['children']
    return None
