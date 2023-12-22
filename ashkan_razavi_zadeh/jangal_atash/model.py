import mesa

from .agent import TreeCell


class ForestFire(mesa.Model):
  
   # Simple model 
   

    def __init__(self, width=100, height=100, density=0.65):
       
       # Create a new 
        
        # object for model
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.SingleGrid(width, height, torus=False)

        self.datacollector = mesa.DataCollector(
            {
                "Fine": lambda m: self.count_type(m, "Fine"),
                "Fire": lambda m: self.count_type(m, "Fire"),
                "Burned": lambda m: self.count_type(m, "Burned"),
            }
        )

        # jaygozari har shart ba tavjoh  tarakom = shanse vojode derakht
        for contents, (x, y) in self.grid.coord_iter():
            if self.random.random() < density:
               
                new_tree = TreeCell((x, y), self)
                # avli ha  = fire
                if x == 0:
                    new_tree.condition = "Fire"
                self.grid.place_agent(new_tree, (x, y))
                self.schedule.add(new_tree)

        self.running = True
        self.datacollector.collect(self)

    def step(self):

        self.schedule.step()
        self.datacollector.collect(self)

        # agar atash nabod stop she
        if self.count_type(self, "Fire") == 0:
            self.running = False

    @staticmethod
    def count_type(model, tree_condition):
        
       # tree - condition for  numbers ? 
       # masaln fire  3 ta 
        
        count = 0
        for tree in model.schedule.agents:
            if tree.condition == tree_condition:
                count += 1
        return count

