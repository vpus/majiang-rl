import random

class MajiangEnv(object):
    def __init__(self):
        super(MajiangEnv, self).__init__()
        print("init")
        self.action_space_size = 13
        self.game_phase = 0
        self.reset()
        self.observation_space_size = len(self.get_state())

    def step(self, action, player_id):
        ## Some action
        if action 
        if player_id == 1:
            

        # if done
        if len(self.deck) == 0:
            done = True
        else:
            done = False
        
        return next_state, self.reward, done

    def reset(self):
        self.deck = []
        for i in range(108):
            self.deck.append(i)
        random.shuffle(self.deck)
        self.player_1_hand = []
        self.player_2_hand = []
        self.player_3_hand = []
        self.player_4_hand = []
        for _ in range(13):
            self.player_1_hand.append(self.deck.pop(0))
            self.player_2_hand.append(self.deck.pop(0))
            self.player_3_hand.append(self.deck.pop(0))
            self.player_4_hand.append(self.deck.pop(0))
        self.game_phase = 1
        self.player_1_simple = self.select_simple(self.player_1_hand)
        self.player_2_simple = self.select_simple(self.player_2_hand)
        self.player_3_simple = self.select_simple(self.player_3_hand)
        self.player_4_simple = self.select_simple(self.player_4_hand)
        self.game_phase = 2
        
    def get_state(self):
        return []
        
    def id2symbol(self, id):
        if id < 36:
            prefix = 'BIN'
        elif id < 72:
            prefix = 'TIAO'
        else:
            prefix = 'WAN'
        value = id % 36 // 4 + 1
        return "{1}{0}".format(prefix, value)

    def symbol2id(self, prefix, value):
        if prefix == 'O':
            prefix_factor = 0
        elif prefix == '|':
            prefix_factor = 1
        else:
            prefix_factor = 2
        base = prefix_factor*36+(value-1)*4
        return base, base+1, base+2, base+3
    
    def select_simple(self, hand):
        bin_amount = 0
        tiao_amount = 0
        wan_amount = 0
        for tile in hand:
            if tile < 36:
                bin_amount += 1
            elif tile < 72:
                tiao_amount += 1
            else:
                wan_amount += 1
        return [bin_amount, tiao_amount, wan_amount].index(min([bin_amount, tiao_amount, wan_amount]))