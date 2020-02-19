import data_structs as G

def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def populate_grid_across():
    #  needs an 'if exists' stmt to implement
    # file_nm = input("file name: ") # to input own file name
    # f = open(file_nm, "r")
    f = open("Text_files\grid01.txt", "r") 
    
    count_x = 1

    for to_strip in f:
        x = to_strip.strip()
        count_y = 1
        for y in x:
            if is_int(y) == True:
                G.grid_across[count_x][count_y] = int(y)
                count_y = count_y + 1   
        count_x = count_x + 1



## Counts how many of each number in grid.
def grid_counts():
    counter = 1
    while counter < (len(G.grid_across) + 1):
        result = 0
        while G.x1 < (len(G.grid_across[G.x1])):
            while G.y1 < (len(G.grid_across[G.x1]) +1):
                if G.grid_across[G.x1][G.y1] == counter:
                    result = result + 1
                G.y1 = G.y1 + 1
            G.x1 = G.x1 + 1
            G.y1 = 1
            # remove numbers completed from counting dict
            if result == 9:
                del G.nr_counts[counter]
            # otherwise set the number count for that number
            else:
                G.nr_counts[counter] = result
        counter = counter + 1
        G.x1 = 1
        G.y1 = 1
    # print("G.nr_counts: ", G.nr_counts)

## populate grid_down with grid_across by assigning xy to yx
def populate_grid_down():
    while G.x1 < (len(G.grid_across) + 1):
        while G.y1 < (len(G.grid_across[G.x1])+ 1):
            G.grid_down[G.y1][G.x1] = G.grid_across[G.x1][G.y1]
            G.y1 = G.y1 + 1
        G.y1 = 1
        G.x1 = G.x1 + 1
    G.x1 = 1
    G.y1 = 1


## change this to calculate based on number 9..?
def set_block_z_val():
    if G.x2 in range(1, 4) and G.y2 in range(1, 4):
        G.z2 = 1
    elif G.x2 in range(1, 4) and G.y2 in range(4, 7):
        G.z2 = 2
    elif G.x2 in range(1, 4) and G.y2 in range(7, 10):
        G.z2 = 3
    elif G.x2 in range(4, 7) and G.y2 in range(1, 4):
        G.z2 = 4
    elif G.x2 in range(4, 7) and G.y2 in range(4, 7):
        G.z2 = 5
    elif G.x2 in range(4, 7) and G.y2 in range(7, 10):
        G.z2 = 6
    elif G.x2 in range(7, 10) and G.y2 in range(1, 4):
        G.z2 = 7
    elif G.x2 in range(7, 10) and G.y2 in range(4, 7):
        G.z2 = 8
    elif G.x2 in range(7, 10) and G.y2 in range(7, 10):
        G.z2 = 9
    else:
        print("Nope: ", G.z2, G.x2, G.y2)

## populate grid_block with grid_across
def populate_grid_block():
    while G.x2 < (len(G.grid_across) + 1):       
        while G.y2 < (len(G.grid_across[G.x2])+ 1):
            set_block_z_val()
            G.grid_block[G.z2][G.x2][G.y2] = G.grid_across[G.x2][G.y2]
            G.y2 = G.y2 + 1
        G.y2 = 1
        G.x2 = G.x2 + 1
    G.y2 = 1
    G.x2 = 1
    G.z2 = 1
    

## use same principle of popping completed positions so that only empty positions remain
# values in this dict are lists as all possible values to be stored if no one definite value determined straight away
def pop_non_empty():
    while G.x1 < (len(G.grid_across) + 1):
        while G.y1 < (len(G.grid_across[G.x1]) +1):
            if G.grid_across[G.x1][G.y1] != 0:
                ## this would delete the completed values... and leave me with the empty spaces...
                del G.grid_across_possible[G.x1][G.y1]
                G.x2 = G.x1
                G.y2 = G.y1
                set_block_z_val()
                del G.grid_block_possible[G.z2][G.x2][G.y2]
            G.y1 = G.y1 + 1
        G.x1 = G.x1 + 1
        G.y1 = 1
    G.x1 = 1
    G.y1 = 1
    G.x2 = 1
    G.y2 = 1
    G.z2 = 1
    ## once pop_empty_dicts have run, only blank positions remain in grid_across_possible.
    ## can now start populating possibilities.
    pop_empty_dicts()

def pop_empty_dicts():
    x = 1
    while x < 10:
        if len(G.grid_across_possible[x].values()) == 0:
            del G.grid_across_possible[x]
        x = x + 1

def count_dicts_to_solve():
    return(len(G.grid_across_possible))

def reset_vals():
    G.x1 = 1
    G.y1 = 1
    G.x2 = 1
    G.y2 = 1
    G.z2 = 1
    G.nr_counts = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

# keeps track of all possible numbers for that position
# first pop out all completed items, so that only open spaces in here
    ## change to new one in data_structs
    G.grid_across_possible = {1:{1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}, 
2:{1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}, 
3:{1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}, 
4:{1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]},
5:{1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]},
6:{1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]},
7:{1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]},
8:{1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]},
9:{1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
}

    G.grid_block_possible = {1:{1:{1:[], 2:[], 3:[]}, 2:{1:[], 2:[], 3:[]}, 3:{1:[], 2:[], 3:[]}},
2:{1:{4:[], 5:[], 6:[]}, 2:{4:[], 5:[], 6:[]}, 3:{4:[], 5:[], 6:[]}},
3:{1:{7:[], 8:[], 9:[]}, 2:{7:[], 8:[], 9:[]}, 3:{7:[], 8:[], 9:[]}},
4:{4:{1:[], 2:[], 3:[]}, 5:{1:[], 2:[], 3:[]}, 6:{1:[], 2:[], 3:[]}},
5:{4:{4:[], 5:[], 6:[]}, 5:{4:[], 5:[], 6:[]}, 6:{4:[], 5:[], 6:[]}},
6:{4:{7:[], 8:[], 9:[]}, 5:{7:[], 8:[], 9:[]}, 6:{7:[], 8:[], 9:[]}},
7:{7:{1:[], 2:[], 3:[]}, 8:{1:[], 2:[], 3:[]}, 9:{1:[], 2:[], 3:[]}},
8:{7:{4:[], 5:[], 6:[]}, 8:{4:[], 5:[], 6:[]}, 9:{4:[], 5:[], 6:[]}},
9:{7:{7:[], 8:[], 9:[]}, 8:{7:[], 8:[], 9:[]}, 9:{7:[], 8:[], 9:[]}}}
    
    G.grid_down = {1:{1:0},
2:{1:0},
3:{1:0},
4:{1:0},
5:{1:0},
6:{1:0},
7:{1:0},
8:{1:0},
9:{1:0}
}

    G.grid_block = {1:{1:{1:0, 2:0, 3:0}, 2:{1:0, 2:0, 3:0}, 3:{1:0, 2:0, 3:0}},
2:{1:{4:0, 5:0, 6:0}, 2:{4:0, 5:0, 6:0}, 3:{4:0, 5:0, 6:0}},
3:{1:{7:0, 8:0, 9:0}, 2:{7:0, 8:0, 9:0}, 3:{7:0, 8:0, 9:0}},
4:{4:{1:0, 2:0, 3:0}, 5:{1:0, 2:0, 3:0}, 6:{1:0, 2:0, 3:0}},
5:{4:{4:0, 5:0, 6:0}, 5:{4:0, 5:0, 6:0}, 6:{4:0, 5:0, 6:0}},
6:{4:{7:0, 8:0, 9:0}, 5:{7:0, 8:0, 9:0}, 6:{7:0, 8:0, 9:0}},
7:{7:{1:0, 2:0, 3:0}, 8:{1:0, 2:0, 3:0}, 9:{1:0, 2:0, 3:0}},
8:{7:{4:0, 5:0, 6:0}, 8:{4:0, 5:0, 6:0}, 9:{4:0, 5:0, 6:0}},
9:{7:{7:0, 8:0, 9:0}, 8:{7:0, 8:0, 9:0}, 9:{7:0, 8:0, 9:0}}}

def set_x2_y2():
    while G.x1 < 10:
        if G.x1 in (G.grid_across_possible.keys()):
            while G.y1 < 10:
                if G.y1 in (G.grid_across_possible[G.x1].keys()):
                    G.x2 = G.x1
                    G.y2 = G.y1
                    val = 1
                    while val < 10:
                        value_to_find = val
                        across = see_if_value_in_across(value_to_find)
                        down = see_if_value_in_down(value_to_find)
                        block = see_if_value_in_block(value_to_find)

                        if across == 1 and down == 1 and block == 1:
                            add_ghost_numbers(value_to_find)
                            ## ft.update_nr_found(value_to_find) ## change this to ghost numbers first
                            # print("Ghost nr Updated!", value_to_find)
                            # print("G.grid_across_possible", G.grid_across_possible)
                            # print("G.z2, G.x2, G.y2", G.z2, G.x2, G.y2)
                        val = val + 1
                        
                    # print("G.x1, G.y2: ", G.x2, G.y2)
                    # print("G.grid_across_possible[G.x1][G.y1]: ", G.grid_across_possible[G.x1][G.y1])
                # print("G.z2, G.x2, G.y2", G.z2, G.x2, G.y2)
                # print("G.grid_across_possible: ", G.grid_across_possible)
                G.y1 = G.y1 + 1
        G.x1 = G.x1 + 1
        G.y1 = 1
    G.x1 = 1
    G.y1 = 1
    G.x2 = 1
    G.y2 = 1
    G.z2 = 1
    # print("G.grid_across_possible: ", G.grid_across_possible)



def see_if_value_in_across(int):
    # print("find in across", int)
    if int not in G.grid_across[G.x2].values():
        # print("find value in across: ", int)
        # print("G.grid_across[G.x2]", G.grid_across[G.x2])
        return(1)
    return(0)

def see_if_value_in_down(int):
    # print("start down: G.grid_down[G.y2]", G.grid_down[G.y2])
    if int not in G.grid_down[G.y2].values():
        # print("find value in down: ", int)
        # print(G.grid_down[G.y2])
        # print("G.grid_down[G.y2]", G.grid_down[G.y2])
        return(1)
    return(0)


def see_if_value_in_block(int):
    set_block_z_val()
    # print("start block: G.grid_block[G.z2]", G.grid_block[G.z2])
    for key in G.grid_block_possible[G.z2]:
        # print("key", key)
        if int in G.grid_block[G.z2][key].values():
            # print("find value in block: ", int)
            # print("G.grid_block[G.z2].values()", G.grid_block[G.z2][key].values())
            return(0)
    return(1)

def add_ghost_numbers(int):
    G.grid_across_possible[G.x2][G.y2].append(int)
    # print("G.grid_across_possible[G.x2]: ", G.grid_across_possible[G.x2])
    # print("G.grid_across_possible[G.x2][G.y2]: ", G.grid_across_possible[G.x2][G.y2])

# populate grid_block_possible with grid_across_possible, as this is how we find single possible values...
def populate_grid_block_possible():
    # print("G.grid_block before: ", G.grid_block)
    while G.x2 < 10: #(len(G.grid_across_possible) + 1):
        # print("G.grid_block_possible: ", G.grid_block_possible)
        if G.x2 in G.grid_across_possible:   
            while G.y2 < 10: #(len(G.grid_across_possible[G.x2])+ 1):
                set_block_z_val()
                # print("err z x y", G.z2, G.x2, G.y2)            
                if G.y2 in G.grid_across_possible[G.x2] and G.y2 in G.grid_block_possible[G.z2][G.x2]:
                    # print("G.z2 V2: ", G.z2)
                    # print("G.x2 V2: ", G.x2)
                    # print("G.y2 V2: ", G.y2)
                    # print('G.grid_block_possible[G.z2][G.x2]', G.grid_block_possible[G.z2][G.x2])
                    # print('G.grid_block_possible[G.z2][G.x2][G.y2]', G.grid_block_possible[G.z2][G.x2][G.y2])
                    # print('G.grid_across_possible[G.x2]: ', G.grid_across_possible[G.x2])
                    G.grid_block_possible[G.z2][G.x2][G.y2] = G.grid_across_possible[G.x2][G.y2]
                # else:
                #     print("G.y2 not in G.grid_across_possible[G.x1]: ", G.y2, G.grid_across_possible[G.x1] )

                # print("G.grid_block[G.z2]", G.grid_block[G.z2])
                G.y2 = G.y2 + 1
            G.y2 = 1
        G.x2 = G.x2 + 1
    # print("G.grid_across_possible: ", G.grid_across_possible)  
    # print("G.grid_block_possible: ", G.grid_block_possible)  
    G.y2 = 1
    G.x2 = 1
    G.z2 = 1

# input block number to search through and value to look for. if only on of this value in count, populate at position XY in grid_across
def see_if_only_ghost_in_specific_block(int):
    #### CONTINUE HERE
    ## amend to iterate on z2, x2, y2 yourself... and do counts of each number in each array...
    ## see: https://stackoverflow.com/questions/50698390/find-a-key-if-a-value-exists-in-a-nested-dictionary
    # print("G.grid_block_possible.values()", G.grid_block_possible.values()) 
    counting = 0
    # val_find = 1
    # print("G.grid_block_possible[G.x1].values(): ", G.grid_block_possible[G.x1].values())
    if G.z2 in G.grid_block_possible: #G.grid_block_possible[G.x1].values():
        # print("G.z2", G.z2)
        G.x2 = 1
        while G.x2 < 10:
            if G.x2 in G.grid_block_possible[G.z2]:
                # print("G.x2", G.x2)
                G.y2 = 1
                while G.y2 < 10:
                    if G.y2 in G.grid_block_possible[G.z2][G.x2]:
                        # print("G.y2", G.y2)
                        # print(G.grid_block_possible[G.z2][G.x2][G.y2])
                        if int in G.grid_block_possible[G.z2][G.x2][G.y2]:
                            counting = counting + 1
                    G.y2 = G.y2 + 1
            G.x2 = G.x2 + 1
        # print("x, v: ", x, v)

        # print("G.x1 in G.grid_block_possible[G.x1].values(): ", G.x1 in G.grid_block_possible[G.x1].values())
    G.x2 = 1
    G.y2 = 1
    if counting != 1:
        # print("Count for false: ", counting)
        return(0)
    else:
        # print("Count for true: ", counting) 
        # print("G.grid_block_possible.values()", G.grid_block_possible.values()) 
        return(1)
    
## input the value that there's only one of in block Z%, find the position it's at and update grid_across at XY
def find_the_xy_to_update(int):
    G.x2 = 1
    # print("G.z2...", G.z2)
    while G.x2 < 10:
        if G.x2 in G.grid_block_possible[G.z2]:
            G.y2 = 1
            while G.y2 < 10:
                # print("G.grid_block_possible[G.z2][G.x2]", G.grid_block_possible[G.z2][G.x2])
                if G.y2 in G.grid_block_possible[G.z2][G.x2]:
                    # print("G.grid_block_possible[G.z2][G.x2][G.y2]", G.grid_block_possible[G.z2][G.x2][G.y2])
                    if int in G.grid_block_possible[G.z2][G.x2][G.y2]:
                        # print("Set val at pos ZXY: ", int, G.z2, G.x2, G.y2)
                        return(0)
                G.y2 = G.y2 + 1
        G.x2 = G.x2 + 1
    return(0)

def only_option():
    while G.z2 < 10:
        # val_find = 1
        # print("G.grid_block_possible[G.x1].values(): ", G.grid_block_possible[G.x1].values())
        if G.z2 in G.grid_block_possible: #G.grid_block_possible[G.x1].values():
            # print("G.z2", G.z2)
            G.x2 = 1
            while G.x2 < 10:
                if G.x2 in G.grid_block_possible[G.z2]:
                    # print("G.x2", G.x2)
                    G.y2 = 1
                    while G.y2 < 10:
                        if G.y2 in G.grid_block_possible[G.z2][G.x2]:
                            # print("G.y2", G.y2)
                            # print(G.grid_block_possible[G.z2][G.x2][G.y2])
                            if len(G.grid_block_possible[G.z2][G.x2][G.y2]) == 1:
                                G.grid_across[G.x2][G.y2] = G.grid_block_possible[G.z2][G.x2][G.y2][0]
                                G.changes_cnt = G.changes_cnt + 1
                                # print("G.grid_block_possible[G.z2][G.x2][G.y2]", G.grid_block_possible[G.z2][G.x2][G.y2])
                                # print("G.grid_across[G.x2][G.y2]", G.grid_across[G.x2][G.y2])
                        G.y2 = G.y2 + 1
                G.x2 = G.x2 + 1
            # print("x, v: ", x, v)

            # print("G.x1 in G.grid_block_possible[G.x1].values(): ", G.x1 in G.grid_block_possible[G.x1].values())
        G.z2 = G.z2 + 1
    G.z2 = 1
    G.x2 = 1
    G.y2 = 1

# def see_if_only_ghost_in_block(int):
#     #### CONTINUE HERE
#     ## amend to iterate on z2, x2, y2 yourself... and do counts of each number in each array...
#     ## see: https://stackoverflow.com/questions/50698390/find-a-key-if-a-value-exists-in-a-nested-dictionary
#     print("G.grid_block_possible.values()", G.grid_block_possible.values())
#     counting = 0
#     while G.z2 < 10:
#         # val_find = 1
#         # print("G.grid_block_possible[G.x1].values(): ", G.grid_block_possible[G.x1].values())
#         if G.z2 in G.grid_block_possible: #G.grid_block_possible[G.x1].values():
#             print("G.z2", G.z2)
#             G.x2 = 1
#             while G.x2 < 10:
#                 if G.x2 in G.grid_block_possible[G.z2]:
#                     print("G.x2", G.x2)
#                     G.y2 = 1
#                     while G.y2 < 10:
#                         if G.y2 in G.grid_block_possible[G.z2][G.x2]:
#                             print("G.y2", G.y2)
#                             print(G.grid_block_possible[G.z2][G.x2][G.y2])
#                             if int in G.grid_block_possible[G.z2][G.x2][G.y2]:
#                                 counting = counting + 1
#                         G.y2 = G.y2 + 1
#                 G.x2 = G.x2 + 1
#             # print("x, v: ", x, v)

#             # print("G.x1 in G.grid_block_possible[G.x1].values(): ", G.x1 in G.grid_block_possible[G.x1].values())
#         G.z2 = G.z2 + 1
#     G.z2 = 1
#     G.x2 = 1
#     G.y2 = 1
#     return(counting)

def update_nr_found(int):
    # d.update(y = 3, z = 0)
    # print(G.grid_across[G.x2])
    G.grid_across[G.x2][G.y2] = int
    # print(G.grid_across[G.x2])
    G.grid_across[G.y2][G.x2] = int
    # print("G.grid_block before: ", G.grid_block)
    G.grid_block[G.z2][G.x2][G.y2] = int ## see if block always updated by y2 value..?
    # print("G.grid_block after: ", G.grid_block)

#######################################################


def grid_across_iter(int):
    while G.x1 < 5:
        while G.y1 < 5:
            if G.grid_across[G.x1][G.y1] == int:
                print(G.grid_across[G.x1][G.y1])
                print(G.x1, G.y1)
            G.y1 = G.y1 + 1
        G.x1 = G.x1 + 1
        G.y1 = 1
    G.x1 = 1
    G.y1 = 1


def grid_down_iter(int):
    while G.x2 < 5:
        while G.y2 < 5:
            if G.grid_down[G.x2][G.y2] == int:
                print(G.grid_down[G.x2][G.y2])
                print(G.x2, G.y2)
            G.y2 = G.y2 + 1
        G.x2 = G.x2 + 1
        G.y2 = 1
    G.x2 = 1
    G.y2 = 1


def grid_block_iter(int):
    while G.x3 < 5:
        while G.y3 < 5:
            if G.grid_block[G.x3][G.y3] == int:
                print(G.grid_block[G.x3][G.y3])
                print(G.x3, G.y3)
            G.y3 = G.y3 + 1
        G.x3 = G.x3 + 1
        G.y3 = 1
    G.x3 = 1
    G.y3 = 1