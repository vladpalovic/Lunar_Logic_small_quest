TRANS_TABLE = {
        'U': ('move_UP',
                    1, 2, 3,
                    1, 2, 3,
                    4, 5, 6,
             ),
        
        'D': ('move_DOWN',
                    4, 5, 6,
                    7, 8, 9,
                    7, 8, 9,
             ),
        
        'L':('move_LEFT',
                    1, 1, 2,
                    4, 4, 5,
                    7, 7, 8,
             ),
        
        'R':('move_RIGHT',
                    2, 3, 3,
                    5, 6, 6,
                    8, 9, 9,
             )
         }

def decode_PIN(code):
    '''
    Decoding PIN by use of the State Machine model,
    Transition Table defined in the structure "TRANS_TABLE"
    '''
    digit, PIN = 5, ''
    
    for c in code:
        if c == '\n':
            PIN += str(digit)
            
        else:
            digit = TRANS_TABLE[c][digit]

    else:
        if not c is '\n':         # missing '\n' in the last line
            PIN += str(digit)
    
    return PIN



def main():
    
    code = '''RLRLLLULULULUUDUULULRDDLURURDDLDUUDDLRDDUUUDD
LDLRLDDDLUDRDRRUDUURLRULLUDDRLURLUULDLLRLLUDLRLRUDLULRLRRL
LLRRDURRDLDULRDUDLRDRDRURULDU
DULRRDRLRLUDLLURURLLRLRDLLDLLDRDUURL
DUULULUUDUDLLRLRURULLDLRRLURDLLDUDUDDRURRLUDULULD
'''
    
    print("Decoded PIN is : ", decode_PIN(code))



if __name__ == "__main__":
    
    main()
