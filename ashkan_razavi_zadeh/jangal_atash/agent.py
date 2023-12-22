import mesa


class TreeCell(mesa.Agent):
  
      #   make loc and status for tree
       #  Can be "Fine", "Fire", or "Burned"
    

    def __init__(self, pos, model):
       
        super().__init__(pos, model)
        self.pos = pos
        self.condition = "Fine"

    def step(self):
  
       # if fire  change nearby from fine to fire 
       
        if self.condition == "Fire":
            for neighbor in self.model.grid.iter_neighbors(self.pos, True):
                if neighbor.condition == "Fine":
                    neighbor.condition = "Fire"
            self.condition = "Burned"
