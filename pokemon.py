# Stores the main information on the pokemon 
class Pokemon():
  def __init__(self, name, level, ptype):
    # Base information for Pokemon 
    self.name = str(name) 
    self.level = int(level)
    self.ptype = str(ptype)
    # self.image = link ???
    
    # Moves for Pokemon 
    self.moves = []
    
    # Base stats for pokemon 
    self.healthPoints = 100
    self.atttackstat = 100
    self.defstat = 100 
    self.speedstat = 100
    self.spattackstat = 100
    self.spdefstat = 100
    
  # Adds new moves to Pokemon 
  def learnMove(self, move):
    if len(self.moves) == 4:
      return "Cannot add/learn more moves"
    else:
      self.moves.append(move)
      
  # Deletes move from Pokemon 
  # def forgetMove(self, move):
    # del self.moves(move)    # Need to remove from list, need proper syntax
  
  # Prints information and stats of Pokemon 
  def information(self):
    print(f"Name: {self.name}")
    return (f"Type: {self.ptype}, Level: {self.level}")  # Return ensures that 'None' doesn't print out
    
