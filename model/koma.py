class Koma:
    
    def __init__(self, owner, pos):
        self._owner = owner
        self._pos = pos
        self._alive = True
        self._promoted = False
        self._drops = None
        
        
    def move(self, position):
        pass

    def eaten(self):
        self._alive = False
        self._owner = (self._owner + 1) % 2

class StepError(Exception):
    pass

class King(Koma):

    def move(self, pos):
        x, y = self._pos[0], self._pos[1]
        if x - 1 <= pos[0] <= x + 1 and y - 1 <= pos[1] <= y + 1 \
                                    and (x != pos or y != pos):
            self._pos = pos
        else:
            raise StepError('illegal step.')
''' King test
k = King(0, (0, 4))
k.move((1, 4))
print('jizz')
k.move((7122, 7122))
'''