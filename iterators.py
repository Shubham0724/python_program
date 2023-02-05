#__iter__() : to initialize an iterator, use the __iter__() method.
#_next__() : This method returns the next item of the sequence.

#Using inbuilt iterators:
string = 'Hello World'
iterObj = iter(string)

while True:
    try:
        char1 = next(iterObj)
        print(char1)
    except StopIteration:
        break


#Creating Custom iterators:
class multipleOf4:
  def __iter__(self):
    self.count = 0
    return self

  def __next__(self):
    if self.count <= 24:
      x = self.count
      self.count += 4
      return x
    else:
      raise StopIteration

obj1 = multipleOf4()
number = iter(obj1)

for x in number:
  print(x)    