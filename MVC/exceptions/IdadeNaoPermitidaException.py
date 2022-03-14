class IdadeNaoPermitida(Exception):
    def __init__(self):
        super().__init__("É necessário ter, no mínimo, 21 anos para adotar um animal da ONG.")
