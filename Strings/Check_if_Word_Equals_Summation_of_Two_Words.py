class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alph_val = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9', 'k': '10', 'l': '11', 'm': '12', 'n': '13', 'o': '14', 'p': '15', 'r': '16', 's': '17', 't': '18', 'u': '19', 'v': '20', 'w': '21', 'x': '22', 'y': '23', 'z': '24'}
        fw_val = int(''.join([alph_val[c] for c in firstWord]))
        sw_val = int(''.join([alph_val[c] for c in secondWord]))
        tw_val = int(''.join([alph_val[c] for c in targetWord]))
        
        return fw_val + sw_val == tw_val
