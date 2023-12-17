white_square = "`````````\n`````````\n`````````\n`````````\n`````````\n`````````"
black_square = white_square.replace("`", "#")

white_square_white_pawn = "`````````\n`````````\n```( )```\n```| |```\n``{   }``\n`````````"
black_square_white_pawn = "#########\n#########\n###( )###\n###| |###\n##{   }##\n#########"
white_square_black_pawn = "`````````\n`````````\n```(*)```\n```|*|```\n``{***}``\n`````````"
black_square_black_pawn = "#########\n#########\n###(*)###\n###|*|###\n##{***}##\n#########"

white_square_white_rook = "`````````\n``[UUU]``\n```| |```\n```{ }```\n``{   }``\n`````````"
white_square_black_rook = white_square_white_rook.replace(" ", "*")
black_square_white_rook = white_square_white_rook.replace("`", "#")
black_square_black_rook = black_square_white_rook.replace(" ", "*")

white_square_white_knight = "`````````\n```T \```\n```|\ )``\n```{ }```\n``{   }``\n`````````"
white_square_black_knight = white_square_white_knight.replace(" ", "*")
black_square_white_knight = white_square_white_knight.replace("`", "#")
black_square_black_knight = black_square_white_knight.replace(" ", "*")

white_square_white_bishop = "``` , ```\n```(^)```\n```/ \```\n```{ }```\n``{   }``\n`````````"
white_square_black_bishop = "``` , ```\n```(^)```\n```/*\```\n```{*}```\n``{***}``\n`````````"
black_square_white_bishop = white_square_white_bishop.replace("`", "#")
black_square_black_bishop = black_square_white_bishop.replace(" ", "*")

white_square_white_queen = "```_._```\n```\ /```\n```| |``\n``{   }``\n`{     }`\n`````````"
white_square_black_queen = white_square_white_queen.replace(" ", "*")
black_square_white_queen = white_square_white_queen.replace("`", "#")
black_square_black_queen = black_square_white_queen.replace(" ", "*")

white_square_white_king = "``` + ```\n```( )```\n```| |```\n``{   }``\n`{     }`\n`````````"
white_square_black_king = white_square_white_king.replace(" ", "*")
black_square_white_king = white_square_white_king.replace("`", "#")
black_square_black_king = black_square_white_king.replace(" ", "*")

black_piece_row = [white_square_black_rook, black_square_black_knight, white_square_black_bishop, black_square_black_king, white_square_black_queen, black_square_black_bishop, white_square_black_knight, black_square_black_rook]
white_piece_row = [black_square_white_rook, white_square_white_knight, black_square_white_bishop, white_square_white_queen, black_square_white_king, white_square_white_bishop, black_square_white_knight, white_square_white_rook]

white_row = [white_square, black_square, white_square, black_square, white_square, black_square, white_square, black_square]
black_row = [black_square, white_square, black_square, white_square, black_square, white_square, black_square, white_square]
black_pawn_row = [black_square_black_pawn, white_square_black_pawn, black_square_black_pawn, white_square_black_pawn, black_square_black_pawn, white_square_black_pawn, black_square_black_pawn, white_square_black_pawn]
white_pawn_row = [white_square_white_pawn, black_square_white_pawn, white_square_white_pawn, black_square_white_pawn, white_square_white_pawn, black_square_white_pawn, white_square_white_pawn, black_square_white_pawn]




first_row = black_piece_row
second_row = black_pawn_row
third_row = white_row
fourth_row = black_row
fifth_row = white_row
sixth_row = black_row
seventh_row = white_pawn_row
eighth_row = white_piece_row
