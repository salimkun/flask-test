class Product:
  def __init__(self, id, name, price, description, quantity, timestamp):
    self.id = id
    self.name = name
    self.price = price
    self.description = description
    self.quantity = quantity
    self.timestamp = timestamp

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'price': self.price,
      'description': self.description,
      'quanitity': self.quantity,
      'timestamp':self.timestamp
    }