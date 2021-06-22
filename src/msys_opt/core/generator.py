from msys.core.serializer import SerializerInterface


class Generator(SerializerInterface):
    def generate(self) -> None:
        pass


class Limiter(Generator):
    def __init__(self):
        self.min = []
        self.max = []
        self.step = []
        self.rule = ""
        self.elements = []

    def generate(self) -> None:
        pass

    def from_dict(self, json: dict) -> bool:
        if "min" in json.keys():
            self.min = json["min"]

        if "max" in json.keys():
            self.max = json["max"]

        if "step" in json.keys():
            self.step = json["step"]

        if "rule" in json.keys():
            self.rule = json["rule"]

        if "elements" in json.keys():
            self.elements = json["elements"]

        return True

    def to_dict(self) -> dict:
        return dict(min=self.min, max=self.max, step=self.step, rule=self.rule, elements=self.elements)
