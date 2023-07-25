from typing import Tuple, List

class ParamValidator:
    def __init__(self,_data):
        self._data = _data
    
    def required_check(self, required:List[str]) -> bool:
        for param in required:
            if param not in self._data:
                print(param)
                return param
        return None

    def type_check(self, typecheck:List[Tuple[str,list]]) -> bool:
        for (param,_tuple) in typecheck:
            if _tuple.__contains__(param):
                return param
        return None
