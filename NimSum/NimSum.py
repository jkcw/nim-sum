class NimSum:
    def __init__(self, piles: list, rule: bool):
        self.piles = piles
        """
        self.rule
        True: Player who make the last move wins
        False: Player who make the last move loses
        """
        self.rule = rule

    def get_nim_sum(self):
        nim_sum = 0
        for i in range(len(self.piles)):
            nim_sum = nim_sum ^ self.piles[i]
        return format(nim_sum, 'b')

    def get_sequence(self):
        """
        True: Start first
        False: Play as the second player
        """
        if self.get_nim_sum() == '0':
            return False
        else:
            return True
