from wheelfortune import WheelPiece, PickerWheel

fortune = PickerWheel(
    pieces=[
        WheelPiece(
            label="money",
            amount=1,
            chance=80.0
        ),
        WheelPiece(
            label="money",
            amount=10,
            chance=40.0
        ),
        WheelPiece(
            label="xp",
            amount=100,
            chance=20.0
        ),
    ]
)
piece = fortune.spin()
print(f"Label: {piece.label}; Amount: {piece.amount}")