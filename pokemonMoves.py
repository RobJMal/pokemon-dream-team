# Defines a move for a pokemon
class Move():
  def __init__(self, name, type, damage = 50, accuracy = 100, effects = None):
    self.name = str(name)
    self.type = str(type) 
    
    self.damage = damage
    self.accuracy = accuracy
    self.effects = effects

"""
--------------- Normal Type Moves ---------------
"""
tri_attack = Move("Tri Attack", "Normal", 80, 100)


    
"""
--------------- Electric Type Moves --------------
"""
zap_cannon = Move("Zap Cannon", "Electric", 120, 50)
