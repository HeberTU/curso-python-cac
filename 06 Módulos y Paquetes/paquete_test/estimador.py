from typing import List

class Estimador():
    
    def predict(self, y: List[float])->List[float]:
        return [val*0.1 + 3 for val in y]