import own_fts as ft
import data_structs as G
##### 27/12/2019 solves 2 different numbers so far... can't do same numbers yet. issue with setting x2 y2.
# ft.full_grid_iter(0)

ft.populate_grid_across() ## run once only

x = 1


while x < 101:
    print("X times: ", x)
    G.changes_cnt = 0
    ft.grid_counts()
    ft.pop_non_empty()
    # print("G.grid_across_possible", G.grid_across_possible)
    

## see if puzzle solved:
    dicts_to_solve = ft.count_dicts_to_solve()

    if dicts_to_solve > 0:
        ft.populate_grid_down()
        ft.populate_grid_block()
        # value_to_find = ft.find_most_completed() ### not optimizing yet...
        # print("1) G.z2, G.x2, G.y2", G.z2, G.x2, G.y2)
        G.z2 = 1
        ft.set_x2_y2()
        # print("2) G.z2, G.x2, G.y2", G.z2, G.x2, G.y2)

        ft.populate_grid_block_possible()
        # print("G.grid_block_possible: ", G.grid_block_possible)
        ##### TO BE CONTINUED: SEE IF ONLY GHOST FT IN own_fts
        # ft.see_if_only_ghost_in_block()

        ## find only one nr in length and update with that value:
        ft.only_option()
        
        while G.z2 < 10:
            val_find = 1
            ret_val = 0

            while val_find < 10:
                # print("val_find", val_find)
                ret_val = ft.see_if_only_ghost_in_specific_block(val_find)
                if ret_val == 1:
                    # print("Update value: at block Z...", val_find, G.z2)
                    ft.find_the_xy_to_update(val_find)
                    # print('G.grid_across[G.x2][G.y2] before: ', G.grid_across[G.x2][G.y2])
                    G.grid_across[G.x2][G.y2] = val_find
                    G.changes_cnt = G.changes_cnt + 1                    
                    # print('G.grid_across[G.x2][G.y2] after: ', G.grid_across[G.x2][G.y2])
                    # G.x2 = 1
                    # G.y2 = 1
                val_find = val_find + 1
            G.x2 = 1
            G.y2 = 1
            G.z2 = G.z2 + 1
        G.z2 = 1
        G.x2 = 1
        G.y2 = 1

        # print("grid_across_possible", G.grid_across_possible)
        # print("grid_block_possible", G.grid_block_possible)
        # print("grid_down", G.grid_down)
        # print("grid_across", G.grid_across)
        # print("grid_block", G.grid_block)

        ########### now... find ghost numbers with only one
        # while 
        #     ft.update_nr_found(definite_nr)



    else:
        print("Sudoku solved")
        # print(G.grid_across)
        # print(G.grid_across.values())
        x1 = 1
        while x1 < 10:
            print(G.grid_across[x1].values())
            x1 = x1 + 1
        x = 102
        break

    if G.changes_cnt > 0:
        x = x + 1
        ft.reset_vals()
        # print("Values reset::")
    else:
        x = 102
        print("Unsolvable with current algo")
        # print("G.grid_across", G.grid_across)
        x1 = 1
        while x1 < 10:
            print(G.grid_across[x1].values())
            x1 = x1 + 1
        print("G.grid_block_possible", G.grid_block_possible)
        print("G.changes_cnt", G.changes_cnt)
        print("G.nr_counts", G.nr_counts)

    # ft.print_grid()
## Start with if only one missing value in across, down or block, complete that.



# d = {'1': 'one', '3': 'three', '2': 'two', '5': 'five', '4': 'four'}
# if 'one' in d.values():
#     print("Value found")


# ft.grid_across_iter(0)
# ft.grid_down_iter(0)
# ft.grid_block_iter(0)
