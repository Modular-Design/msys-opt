from ..core import OptimizableType
import numpy as np
from ..core.generator import Limiter


class VectorType(OptimizableType):
    def __init__(self, default_value):
        super().__init__(np.array([0]), Limiter())
        self.set_value(default_value)

    def is_same(self, value) -> bool:
        return list(self.value) == list(value)

    def set_value(self, value) -> bool:
        if isinstance(value, np.ndarray):
            return super().set_value(value)
        elif isinstance(value, list):
            return super().set_value(np.array(value))
        elif isinstance(value, int) or isinstance(value, float):
            return super().set_value(np.array([value]))
        return False

    def to_dict(self) -> dict:
        res = super().to_dict()
        res["value"] = self.value.tolist()
        return res

    def from_dict(self, json: dict) -> bool:
        super().from_dict(json)
        if "value" in json.keys():
            self.value = np.array(json["value"])
        return True
