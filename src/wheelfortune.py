import random


class WheelPiece:

    def __init__(self, label: str, amount: int, chance: float) -> None:
        self.label: str = label
        self.amount: int = amount
        self.chance: float = chance
        self._weight: float = 0.0
        self.index: int


class PickerWheel:

    def __init__(self, pieces: [WheelPiece]) -> None:
        self.pieces: [WheelPiece] = pieces
        self.accumulated_weight: float = 0.0
        self.non_zero_chances_indices: [int] = []
        self.calculate_weights_and_indices()
        if len(self.non_zero_chances_indices) == 0: print("You can't set all pieces chance to zero")

    def spin(self) -> WheelPiece:
        index: int = self.get_random_piece_index()
        piece: WheelPiece = self.pieces[index]

        if piece.chance == 0:
            index = random.choice(self.non_zero_chances_indices)
            piece = self.pieces[index]

        return piece

    def calculate_weights_and_indices(self) -> None:
        for index, piece in enumerate(self.pieces):
            self.accumulated_weight += piece.chance
            piece._weight = self.accumulated_weight
            piece.index = index

            if piece.chance > 0:
                self.non_zero_chances_indices.append(index)

    def get_random_piece_index(self) -> int:
        r = random.uniform(0.0, 1.0) * self.accumulated_weight

        for index, piece in enumerate(self.pieces):
             if piece._weight >= r:
                return index

        return 0
