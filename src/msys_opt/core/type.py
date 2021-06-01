from .optimizable import OptimizableInterface
from msys.core import Type


class OptimizableType(Type, OptimizableInterface):
    def __init__(self, default_value, generator=None):
        self.optimized = False
        self.generator = generator
        super().__init__(default_value)

    def is_optimized(self) -> bool:
        self.optimized

    def set_optimized(self, optimized: bool) -> bool:
        self.optimized = optimized
        return True
