
def isValidChessBoard(chess_board):
    black_pawn_counter = 0
    white_pawn_counter = 0
    black_piece_counter = 0
    white_piece_counter = 0
    white_king_counter = 0
    black_king_counter = 0

    valid_pos = []

    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(1, 9):
        for v in alph:
            valid_pos.append(str(i)+v)

    valid_piece = ['bpawn', 'bknight', 'bbishop', 'brook', 'bqueen', 'bking',
                   'wpawn', 'wknight', 'wbishop', 'wrook', 'wqueen', 'wking']
    for i in chess_board.keys():
        if i in valid_pos:
            print('we good')
        else:
            print('Houstan, that board square doesnt exist')

    for i in chess_board.values():
        val = i[:1]
        if i in valid_piece:
            print('this is right')

            if i =='bking':
                black_king_counter += 1
            elif i == 'wking':
                white_king_counter += 1

            if i == 'bpawn':
                black_pawn_counter += 1
            elif i == 'wpawn':
                white_pawn_counter +=1 

            if val == 'b':
                black_piece_counter += 1
            else:
                white_piece_counter += 1
            
            if white_king_counter > 1 or black_king_counter > 1:
                print('Houstan, we have too many kings')
                break

            if white_pawn_counter > 8 or black_pawn_counter > 8:
                print('Houstan, we have too many pawns')
                break
            
            if white_piece_counter > 16 or black_piece_counter > 16:
                print('Houstan, we are over 16')
                break
        else:
            print('Houstan, we have found a bug')
            break


chess_board = {'1h': 'bking', '1d': 'wking','2a': 'bpawn', '11a': 'wpawn', '3a': 'bpawn'}
print(isValidChessBoard(chess_board))


