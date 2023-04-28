class Item:
   
    def __init__(self, count = 3, max_count = 16):
        self._count = count
        self._max_count = 16
        
    def update_count(self, val):
        if val <= self._max_count:
            self._count = val
            return True
        else:
            return False

    @property
    def count(self):
        return self._count

#===============================================================================================================
#Task 1:

    def __add__(self, num):
        """ Сложение с числом """
        return self.count + num
    
    def __mul__(self, num):
        """ Умножение на число """
        return self.count * num
    
    def __lt__(self, num):
        """ Сравнение меньше """
        return self.count < num
    
    def __len__(self):
        """ Получение длины объекта """
        return self.count

#===============================================================================================================
#Task 2:

    def __gt__(self, num):
        return self.count > num
    
    def __ge__(self, num):
        return self.count >= num
    
    def __le__(self, num):
        return self.count <= num

    def __eq__(self, num):
        return self.count == num

    def __ne__(self, num):
        return self.count != num

    def __iadd__(self, num):
        
        if (self.count + num > self._max_count):
            return self._max_count

        return self.count + num

    def __isub__(self, num):
        
        if (self.count - num < 0):
            return 0

        return self.count - num

    def __imul__(self, num):
        
        if (self.count * num > self._max_count):
            return self._max_count

        return self.count * num

#===============================================================================================================
#Task 3:

class Fruit(Item):
    
    def __init__(self, ripe = True, **kwargs):
        super().__init__(**kwargs)
        self._ripe = ripe


class Vegetable(Item):
    
    def __init__(self, ripe = True, **kwargs):
        super().__init__(**kwargs)
        self._ripe = ripe


class Food(Item):
    
    def __init__(self, saturation, **kwargs):
        super().__init__(**kwargs)
        self._saturation = saturation
        
    @property
    def eatable(self):
        return self._saturation > 0


class Tomato(Vegetable, Food):
    
    def __init__(self, ripe, count = 1, max_count = 60, color = 'red', saturation = 5):
        super().__init__(saturation = saturation, ripe = ripe, count = count, max_count = max_count)
        self._color = color
        
    @property
    def eatable(self):
        return super().eatable and self._ripe


class Сucumber(Vegetable, Food):
    
    def __init__(self, ripe, count = 1, max_count = 10, color = 'green', saturation = 1):
        super().__init__(saturation = saturation, ripe = ripe, count = count, max_count = max_count)
        self._color = color
            
    @property
    def eatable(self):
        return super().eatable and self._ripe


class Kiwi(Fruit, Food):
    
    def __init__(self, ripe, count = 1, max_count = 50, color = 'green', saturation = 5):
        super().__init__(saturation = saturation, ripe = ripe, count = count, max_count = max_count)
        self._color = color
    
    @property
    def color(self):
        return self._color
        
    @property
    def eatable(self):
        return super().eatable and self._ripe


class Pear(Fruit, Food):
   
    def __init__(self, ripe, count = 1, max_count = 32, color = 'yellow', saturation = 7):
        super().__init__(saturation = saturation, ripe = ripe, count = count, max_count = max_count)
        self._color = color
    
    @property
    def color(self):
        return self._color
        
    @property
    def eatable(self):
        return super().eatable and self._ripe

#===============================================================================================================
#Task 4:

class Inventory(Food):

    def __init__(self, size = 20):
        self._size = size
        self._lst = [None for i in range(size)]
        
    def add_item(self, item, index):

        if (index > self._size - 1):
            print('Index', index, 'is out of range')
            return False

        if (self._lst[index] != None):
            print('The cell number', index, 'is already taken')
            return False

        if (item.eatable == False):
            print(type(item).__name__, 'is not eatable item')
            return False

        self._lst[index] = item
        return True

    def take_item(self, amount, index):

        if (index > self._size - 1):
           print('Index', index, 'is out of range')
           return None

        if (self._lst[index] == None):
           print('Cell number', index, 'is empty')
           return None

        if (self._lst[index].count - amount <= 0):

            tmp = self._lst[index].count

            self._lst[index] = None 
            return tmp

        self._lst[index].count -= amount
        return amount


#===============================================================================================================
#Task 5:

class Queue:

    def __init__(self):
        self._queue = []

    def push(self, elem):
        self._queue.append(elem)

    def pop(self):

        if (len(self._queue) == 0):
            return None

        return self._queue.pop(0)

    @property
    def get_list(self):
        lst = self._queue.copy()
        return lst

