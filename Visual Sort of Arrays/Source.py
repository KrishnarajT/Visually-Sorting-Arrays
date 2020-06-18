"""PROJECT TO VISUALIZE HOW SORTING ALGORITHMS WORK, GOAL IS TO COVER ALL THE MAJOR SORTING ALGORITHMS THAT WE
USUALLY USE, THE VISUALIZATION IS DONE USING PYGAME, AND VERY PRIMITIVE METHODS.

# ARRAY SORTS ARE PARTICULARLY USEFUL IN NUMEROUS PLACES.
LIKE SORTING YOUR PHONE CONTACTS, OR SORTING FILES IN A FOLDER, OR SORTING FILES IN YOUR COMPUTER BY YOUR FILE
EXPLORER THAT IS GOING TO HELP IN SEARCHING FOR THAT PARTICULAR FILE
OR SORING THE NAMES AND SCORES OF ALL YOUR PLAYERS IN A GAME, SO AS TO BE ABLE TO TELL WHO IS LEADING (MOSTLY IN
HUGE GAMES LIKE PUBG AND COD AND OTHER GAMES THAT HAVE A GLOBAL AUDIENCE) ETC

SORTING 2D ARRAYS IS ALSO USEFUL AND FINDS ITS MOST USE CASE SCENARIO IN PLACES LIKE IMAGE PROCESSING AND ALL,
WHERE YOU HAVE TO ENHANCE YOUR IMAGE, OR IN SAY A FOLDER THAT HAS A FOLDER THAT HAS ANOTHER FOLDER. OR IN PLACES
WHERE YOU HAVE TO RENDER IMAGES IN SOMEPLACES...ETC..

BY KPT
"""

import pyautogui
from Ky_Game import *
import time
import os
from math import floor
import random

pygame.font.init()
pygame.mixer.init()

'''Constants and Extra Utility functions used here and there'''

class General :
    # INTITIALIZING THE WIDTH AND THE HEIGHT OF THE WINDOW.
    # THIS GAME WILL BE MADE WITH RESPECT TO THE HEGHT AND THE WIDTH OF THE MONITOR, AND WILL BE HALF OF THAT./
    
    change_sort_x = None
    go_to_data_label = None
    go_to_data_x = None
    change_sort_label = None
    change_elem_label = None
    initial_gap_y = None
    change_elem_x = None
    WIDTH, HEIGHT = pyautogui.size()
    
    # INITIALIZING THE WINDOW.
    
    WIN = pygame.display.set_mode( (WIDTH, HEIGHT), pygame.RESIZABLE )
    pygame.display.set_caption( "Visual Sorta Arrays" )
    
    # INITIALIZING THE FONTS.
    
    GAME_FONT = pygame.font.Font( os.path.join( "Assets", "kel.ttf" ), floor( WIDTH / 27.4 ) )
    
    # INTITIALIZING THE IMAGES.
    BG_IMAGE = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "BG_IMAGE.png" ) ),
                                       (WIDTH, HEIGHT) )
    ARRAY_IMAGE = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "ARRAY_IMAGE.png" ) ),
                                          (WIDTH, HEIGHT) )
    NUM_ELE_IMAGE = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "NUM_ELE_IMAGE.png" ) ),
                                            (WIDTH, HEIGHT) )
    SORT_IMAGE = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "SORT_IMAGE.png" ) ),
                                         (WIDTH, HEIGHT) )
    # INITIALIZING THE POSITIONS OF THE BUTTONS.
    
    MENU_START_BTN_LOWER = (floor( WIDTH / 2.7 ),
                            floor( HEIGHT / 2.33 ))
    MENU_START_BTN_UPPER = (floor( WIDTH / 1.60 ),
                            floor( HEIGHT / 1.73 ))
    
    MENU_EXIT_BTN_LOWER = (floor( WIDTH / 2.7 ),
                           floor( HEIGHT / 1.44 ))
    MENU_EXIT_BTN_UPPER = (floor( WIDTH / 1.60 ),
                           floor( HEIGHT / 1.17 ))
    
    NUMBER_OF_ELEM = 0
    CUR_SORT_METHOD = 0
    CUR_SORT_METHOD_COMPLEXITY = [ '', '', '' ]
    SORT_TIMINGS = [ ]
    SORT_FIGURES = [ ]
    MAINLIST = [ ]
    MAINLISTCOPY = [ ]
    MAINLISTCOPYSWAPED = [ ]
    swap = [ ]
    ARRAY_DISP_GAP = floor( WIDTH / 9.6 )
    COLOR1 = random.randint( 0, 255 )
    COLOR2 = random.randint( 0, 255 )
    Mainfont = pygame.font.Font( 'assets/Kel.ttf', 20 )
    
    @staticmethod
    def assignMainList() :
        General.MAINLIST = [ ]
        for var in range( General.NUMBER_OF_ELEM ) :
            randint = random.randrange( 50, 1000 )
            General.MAINLIST.append( randint )
    
    @staticmethod
    def assignComplexity() :
        if General.CUR_SORT_METHOD == 'Quick Sort' :
            General.CUR_SORT_METHOD_COMPLEXITY[ 0 ] = 'O(nlog(n))'
            General.CUR_SORT_METHOD_COMPLEXITY[ 1 ] = 'O(nlog(n))'
            General.CUR_SORT_METHOD_COMPLEXITY[ 2 ] = 'O(n^2)'
        elif General.CUR_SORT_METHOD == 'Merge Sort' :
            General.CUR_SORT_METHOD_COMPLEXITY[ 0 ] = 'O(nlog(n))'
            General.CUR_SORT_METHOD_COMPLEXITY[ 1 ] = 'O(nlog(n))'
            General.CUR_SORT_METHOD_COMPLEXITY[ 2 ] = 'O(nlog(n))'
        elif General.CUR_SORT_METHOD == 'Bubble Sort' :
            General.CUR_SORT_METHOD_COMPLEXITY[ 0 ] = 'O(n)'
            General.CUR_SORT_METHOD_COMPLEXITY[ 1 ] = 'O(n^2)'
            General.CUR_SORT_METHOD_COMPLEXITY[ 2 ] = 'O(n^2)'
        elif General.CUR_SORT_METHOD == 'Tim Sort' :
            General.CUR_SORT_METHOD_COMPLEXITY[ 0 ] = 'O(n)'
            General.CUR_SORT_METHOD_COMPLEXITY[ 1 ] = 'O(nlog(n))'
            General.CUR_SORT_METHOD_COMPLEXITY[ 2 ] = 'O(n^2)'
        elif General.CUR_SORT_METHOD == 'Heap Sort' :
            General.CUR_SORT_METHOD_COMPLEXITY[ 0 ] = 'O(nlog(n))'
            General.CUR_SORT_METHOD_COMPLEXITY[ 1 ] = 'O(nlog(n))'
            General.CUR_SORT_METHOD_COMPLEXITY[ 2 ] = 'O(nlog(n))'
        elif General.CUR_SORT_METHOD == 'Insertion Sort' :
            General.CUR_SORT_METHOD_COMPLEXITY[ 0 ] = 'O(n)'
            General.CUR_SORT_METHOD_COMPLEXITY[ 1 ] = 'O(n^2)'
            General.CUR_SORT_METHOD_COMPLEXITY[ 2 ] = 'O(n^2)'
        elif General.CUR_SORT_METHOD == 'Selection Sort' :
            General.CUR_SORT_METHOD_COMPLEXITY[ 0 ] = 'O(n^2)'
            General.CUR_SORT_METHOD_COMPLEXITY[ 1 ] = 'O(n^2)'
            General.CUR_SORT_METHOD_COMPLEXITY[ 2 ] = 'O(n^2)'
        elif General.CUR_SORT_METHOD == 'Bucket Sort' :
            General.CUR_SORT_METHOD_COMPLEXITY[ 0 ] = 'O(n + k)'
            General.CUR_SORT_METHOD_COMPLEXITY[ 1 ] = 'O(n + k)'
            General.CUR_SORT_METHOD_COMPLEXITY[ 2 ] = 'O(n^2)'
        elif General.CUR_SORT_METHOD == 'Cycle Sort' :
            General.CUR_SORT_METHOD_COMPLEXITY[ 0 ] = 'O(n^2)'
            General.CUR_SORT_METHOD_COMPLEXITY[ 1 ] = 'O(n^2)'
            General.CUR_SORT_METHOD_COMPLEXITY[ 2 ] = 'O(n^2)'
        elif General.CUR_SORT_METHOD == 'Counting Sort' :
            General.CUR_SORT_METHOD_COMPLEXITY[ 0 ] = 'O(n + k)'
            General.CUR_SORT_METHOD_COMPLEXITY[ 1 ] = 'O(n + k)'
            General.CUR_SORT_METHOD_COMPLEXITY[ 2 ] = 'O(n + k)'
        elif General.CUR_SORT_METHOD == 'Cocktail Sort' :
            General.CUR_SORT_METHOD_COMPLEXITY[ 0 ] = 'O(n)'
            General.CUR_SORT_METHOD_COMPLEXITY[ 1 ] = 'O(n^2)'
            General.CUR_SORT_METHOD_COMPLEXITY[ 2 ] = 'O(n^2)'
    
    @staticmethod
    def UpdateElement_( array, Box_Pos, Color ) :
        
        """draws instances of boxes on the screen with height 'array[Box_Pos]', 
        where Box_Pos is the position of the element in the array,
        does not update pygame window"""
        
        Cur_Rect_Width = (General.WIDTH - General.ARRAY_DISP_GAP) / len( array )
        
        Cur_Rect_Surface = pygame.Surface( (Cur_Rect_Width, array[ Box_Pos ]) )
        Cur_Rect_Surface_Bg = pygame.Surface( (Cur_Rect_Width, floor( General.HEIGHT / 1.08 )) )
        Cur_Rect_Surface.fill( Color )
        Cur_Rect_Surface_Bg.fill( color.get( "Black" ) )
        
        General.WIN.blit( Cur_Rect_Surface_Bg, (General.ARRAY_DISP_GAP / 2 + Box_Pos * Cur_Rect_Width, General.HEIGHT - floor( General.HEIGHT / 1.08 )) )
        General.WIN.blit( Cur_Rect_Surface, (General.ARRAY_DISP_GAP / 2 + Box_Pos * Cur_Rect_Width, General.HEIGHT - array[ Box_Pos ]) )
    
    @staticmethod
    def UpdateElementMerge_( array, Box_Pos, Color ) :
        
        """draws instances of boxes on the screen with height 'array[Box_Pos]',
        where Box_Pos is the position of the element in the array,
        does not update pygame window"""
        
        Cur_Rect_Width = (General.WIDTH - General.ARRAY_DISP_GAP) / General.NUMBER_OF_ELEM
        
        Cur_Rect_Surface = pygame.Surface( (Cur_Rect_Width, array[ Box_Pos ][ 0 ]) )
        Cur_Rect_Surface_Bg = pygame.Surface( (Cur_Rect_Width, floor( General.HEIGHT / 1.08 )) )
        Cur_Rect_Surface.fill( Color )
        Cur_Rect_Surface_Bg.fill( color.get( "Black" ) )
        
        General.WIN.blit( Cur_Rect_Surface_Bg, (General.ARRAY_DISP_GAP / 2 + Box_Pos * Cur_Rect_Width, General.HEIGHT - floor( General.HEIGHT / 1.08 )) )
        General.WIN.blit( Cur_Rect_Surface,
                          (General.ARRAY_DISP_GAP / 2 + Box_Pos * Cur_Rect_Width, General.HEIGHT - array[ Box_Pos ][ 0 ]) )
    
    @staticmethod
    def DrawAll_( array ) :
        """Draws all the elements of the array on the screen, in the unsorted order.
        Also updates the display, and waits for some time"""
        
        Cur_Rect_Width = (General.WIDTH - General.ARRAY_DISP_GAP) / len( array )
        
        General.WIN.fill( color.get( 'Black' ) )
        for i in range( len( array ) ) :
            Cur_Rect_Surface_Bg = pygame.Surface( (Cur_Rect_Width, array[ i ]) )
            Cur_Rect_Surface_Bg.fill( (General.COLOR1, General.COLOR2, floor( array[ i ] / (General.WIDTH / 255) )) )
            General.WIN.blit( Cur_Rect_Surface_Bg,
                              (General.ARRAY_DISP_GAP / 2 + i * Cur_Rect_Width, General.HEIGHT - array[ i ]) )
        pygame.display.update()
        pygame.time.wait( 1000 )
    
    @staticmethod
    def DrawAllMerge_( array ) :
        """Draws all the elements of the array on the screen, in the unsorted order.
        Also updates the display, and waits for some time"""
        
        Cur_Rect_Width = (General.WIDTH - General.ARRAY_DISP_GAP) / General.NUMBER_OF_ELEM
        
        General.WIN.fill( color.get( 'Black' ) )
        for i in range( len( array ) ) :
            Cur_Rect_Surface_Bg = pygame.Surface( (Cur_Rect_Width, array[ i ][ 0 ]) )
            Cur_Rect_Surface_Bg.fill(
                    (General.COLOR1, General.COLOR2, floor( array[ i ][ 0 ] / (General.WIDTH / 255) )) )
            General.WIN.blit( Cur_Rect_Surface_Bg,
                              (General.ARRAY_DISP_GAP / 2 + i * Cur_Rect_Width, General.HEIGHT - array[ i ][ 0 ]) )
        pygame.display.update()
        pygame.time.wait( 1000 )
    
    @staticmethod
    def DispArray_( array, swap, Time ) :
        
        """displays the sorting pattern on the screen.
        This pattern is dependent on the swap[] array.
        It reads swap[], and swaps the elements of 'array[]' according to swap[], 
        displays and updates the display after every iteration, also has FPS regulation
        at 60."""
        
        Pos = 0
        clock = pygame.time.Clock()
        General.DispTextOnSortScreen_( Time )
        pygame.display.update()
        done_disp = False
        while 1 :
            if General.CUR_SORT_METHOD == 'Counting Sort' :
                if not done_disp :
                    for i in range( len( array ) ) :
                        General.UpdateElement_( array, i, color.get( 'Green' ) )
                        pygame.display.update()
                        General.UpdateElement_( array, i, (General.COLOR1, General.COLOR2, floor( array[ i ] / (General.WIDTH / 255) )) )
                        for event in pygame.event.get() :
                            if event.type == pygame.QUIT :
                                pygame.display.quit()
                                return 0
                            elif event.type == pygame.KEYDOWN :
                                if event.key == pygame.K_r :
                                    return 1
                                elif event.key == pygame.K_s :
                                    return 2
                                elif event.key == pygame.K_d :
                                    return 4
                            elif checkMouse( General.change_elem_x, General.initial_gap_y, General.change_elem_x +
                                                                                           General.change_elem_label.get_width(),
                                             General.change_elem_label.get_height(), event ) :
                                return 1
                            elif checkMouse( General.change_sort_x, General.initial_gap_y, General.change_sort_x +
                                                                                           General.change_sort_label.get_width(),
                                             General.change_sort_label.get_height(), event ) :
                                return 2
                            elif checkMouse( General.go_to_data_x, General.initial_gap_y, General.go_to_data_x +
                                                                                          General.change_sort_label.get_width(),
                                             General.go_to_data_label.get_height(), event ) :
                                return 4
                    done_disp = True
            elif General.CUR_SORT_METHOD == 'Bucket Sort' :
                if not done_disp :
                    while Pos < len( swap ) - 2 :
                        array[ swap[ Pos ] ] = 1000 * swap[ Pos + 1 ]
                        General.UpdateElement_( array, swap[ Pos ], color.get( 'Green' ) )
                        pygame.display.update()
                        General.UpdateElement_( array, swap[ Pos ], (General.COLOR1, General.COLOR2, floor( array[ swap[ Pos ] ] / (
                                General.WIDTH / 255) )) )
                        Pos += 2
                        for event in pygame.event.get() :
                            if event.type == pygame.QUIT :
                                pygame.display.quit()
                                return 0
                            elif event.type == pygame.KEYDOWN :
                                if event.key == pygame.K_r :
                                    return 1
                                elif event.key == pygame.K_s :
                                    return 2
                                elif event.key == pygame.K_d :
                                    return 4
                            elif checkMouse( General.change_elem_x, General.initial_gap_y, General.change_elem_x +
                                                                                           General.change_elem_label.get_width(),
                                             General.change_elem_label.get_height(), event ) :
                                return 1
                            elif checkMouse( General.change_sort_x, General.initial_gap_y, General.change_sort_x +
                                                                                           General.change_sort_label.get_width(),
                                             General.change_sort_label.get_height(), event ) :
                                return 2
                            elif checkMouse( General.go_to_data_x, General.initial_gap_y, General.go_to_data_x +
                                                                                          General.change_sort_label.get_width(),
                                             General.go_to_data_label.get_height(), event ) :
                                return 4
                    array = sorted( array )
                    for i in range( len( array ) ) :
                        General.UpdateElement_( array, i, color.get( 'Green' ) )
                        pygame.display.update()
                        General.UpdateElement_( array, i, (General.COLOR1, General.COLOR2, floor( array[ i ] / (General.WIDTH / 255) )) )
                    done_disp = True
            elif General.CUR_SORT_METHOD == 'Merge Sort' :
                if not done_disp :
                    while Pos < (len( swap ) - 10) :
                        clock.tick( 60 )
                        array[ swap[ Pos ] ] = swap[ Pos + 1 ]
                        General.UpdateElementMerge_( array, swap[ Pos ], (
                            General.COLOR1, General.COLOR2, floor( swap[ Pos + 1 ][ 0 ] / (General.WIDTH / 255) )) )
                        Pos += 2
                        array[ swap[ Pos ] ] = swap[ Pos + 1 ]
                        General.UpdateElementMerge_( array, swap[ Pos ], (
                            General.COLOR1, General.COLOR2, floor( swap[ Pos + 1 ][ 0 ] / (General.WIDTH / 255) )) )
                        Pos += 2
                        array[ swap[ Pos ] ] = swap[ Pos + 1 ]
                        # General.UpdateElementsingle_( array, swap[ Pos ], color.get( "Green" ) )
                        General.UpdateElementMerge_( array, swap[ Pos ], (
                            General.COLOR1, General.COLOR2, floor( swap[ Pos + 1 ][ 0 ] / (General.WIDTH / 255) )) )
                        Pos += 2
                        array[ swap[ Pos ] ] = swap[ Pos + 1 ]
                        # General.UpdateElementsingle_( array, swap[ Pos ], color.get( "Green" ) )
                        General.UpdateElementMerge_( array, swap[ Pos ], (
                            General.COLOR1, General.COLOR2, floor( swap[ Pos + 1 ][ 0 ] / (General.WIDTH / 255) )) )
                        Pos += 2
                        array[ swap[ Pos ] ] = swap[ Pos + 1 ]
                        # General.UpdateElementsingle_( array, swap[ Pos ], color.get( "Green" ) )
                        General.UpdateElementMerge_( array, swap[ Pos ], (
                            General.COLOR1, General.COLOR2, floor( swap[ Pos + 1 ][ 0 ] / (General.WIDTH / 255) )) )
                        Pos += 2
                        pygame.display.update()
                        
                        for event in pygame.event.get() :
                            if event.type == pygame.QUIT :
                                pygame.display.quit()
                                return 0
                            elif event.type == pygame.KEYDOWN :
                                if event.key == pygame.K_r :
                                    return 1
                                elif event.key == pygame.K_s :
                                    return 2
                                elif event.key == pygame.K_d :
                                    return 4
                            elif checkMouse( General.change_elem_x, General.initial_gap_y, General.change_elem_x +
                                                                                           General.change_elem_label.get_width(),
                                             General.change_elem_label.get_height(), event ) :
                                return 1
                            elif checkMouse( General.change_sort_x, General.initial_gap_y, General.change_sort_x +
                                                                                           General.change_sort_label.get_width(),
                                             General.change_sort_label.get_height(), event ) :
                                return 2
                            elif checkMouse( General.go_to_data_x, General.initial_gap_y, General.go_to_data_x +
                                                                                          General.change_sort_label.get_width(),
                                             General.go_to_data_label.get_height(), event ) :
                                return 4
                    done_disp = True
            else :
                if not done_disp :
                    skip = 2
                    if General.CUR_SORT_METHOD == 'Bubble Sort' :
                        skip = floor( General.NUMBER_OF_ELEM / 3 )
                        if skip % 2 == 1 :
                            skip += 1
                        if General.NUMBER_OF_ELEM == 50 :
                            skip = 2
                    elif General.CUR_SORT_METHOD == 'Cocktail Sort' :
                        skip = floor( General.NUMBER_OF_ELEM / 4 )
                        if skip % 2 == 1 :
                            skip += 1
                    elif General.CUR_SORT_METHOD == 'Insertion Sort' :
                        skip = floor( General.NUMBER_OF_ELEM / 4 )
                        if skip % 2 == 1 :
                            skip += 1
                        if General.NUMBER_OF_ELEM == 50 :
                            skip = 2
                    elif General.CUR_SORT_METHOD == 'Heap Sort' :
                        skip = floor( General.NUMBER_OF_ELEM / 80 )
                        if skip % 2 == 1 :
                            skip += 1
                        if skip == 0 :
                            skip = 2
                    while Pos < (len( swap ) - skip) :
                        clock.tick( 60 )
                        j = Pos
                        while j < Pos + skip :
                            array[ swap[ j ] ], array[ swap[ j + 1 ] ] = array[ swap[ j + 1 ] ], array[ swap[ j ] ]
                            if j == Pos :
                                General.UpdateElement_( array, swap[ j ], color.get( 'White' ) )
                                General.UpdateElement_( array, swap[ j + 1 ], color.get( 'White' ) )
                            else :
                                General.UpdateElement_( array, swap[ j ], (General.COLOR1, General.COLOR2,
                                                                           floor( array[ swap[ j ] ] / (General.WIDTH / 255) )) )
                                General.UpdateElement_( array, swap[ j + 1 ], (General.COLOR1, General.COLOR2,
                                                                               floor( array[ swap[ j + 1 ] ] / (General.WIDTH / 255) )) )
                            j += 2
                        
                        pygame.display.update()
                        
                        for i in range( Pos, Pos + skip ) :
                            General.UpdateElement_( array, swap[ i ], (General.COLOR1, General.COLOR2,
                                                                       floor( array[ swap[ i ] ] / (General.WIDTH / 255) )) )
                        
                        Pos += skip
                        for event in pygame.event.get() :
                            if event.type == pygame.QUIT :
                                pygame.display.quit()
                                return 0
                            elif event.type == pygame.KEYDOWN :
                                if event.key == pygame.K_r :
                                    return 1
                                elif event.key == pygame.K_s :
                                    return 2
                                elif event.key == pygame.K_d :
                                    return 4
                            elif checkMouse( General.change_elem_x, General.initial_gap_y, General.change_elem_x +
                                                                                           General.change_elem_label.get_width(),
                                             General.change_elem_label.get_height(), event ) :
                                return 1
                            elif checkMouse( General.change_sort_x, General.initial_gap_y, General.change_sort_x +
                                                                                           General.change_sort_label.get_width(),
                                             General.change_sort_label.get_height(), event ) :
                                return 2
                            elif checkMouse( General.go_to_data_x, General.initial_gap_y, General.go_to_data_x +
                                                                                          General.change_sort_label.get_width(),
                                             General.go_to_data_label.get_height(), event ) :
                                return 4
                    array = sorted( array )
                    for i in range( len( array ) ) :
                        General.UpdateElement_( array, i, color.get( 'Green' ) )
                        pygame.display.update()
                        General.UpdateElement_( array, i, (General.COLOR1, General.COLOR2, floor( array[ i ] / (General.WIDTH / 255) )) )
                    done_disp = True
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    pygame.display.quit()
                    return 0
                elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_r :
                        return 1
                    elif event.key == pygame.K_s :
                        return 2
                    elif event.key == pygame.K_d :
                        return 4
                elif checkMouse( General.change_elem_x, General.initial_gap_y, General.change_elem_x +
                                                                               General.change_elem_label.get_width(),
                                 General.change_elem_label.get_height(), event ) :
                    return 1
                elif checkMouse( General.change_sort_x, General.initial_gap_y, General.change_sort_x +
                                                                               General.change_sort_label.get_width(),
                                 General.change_sort_label.get_height(), event ) :
                    return 2
                elif checkMouse( General.go_to_data_x, General.initial_gap_y, General.go_to_data_x +
                                                                              General.change_sort_label.get_width(),
                                 General.go_to_data_label.get_height(), event ) :
                    return 4
    
    @staticmethod
    def DispTextOnSortScreen_( Time = 1.00 ) :
        main_Font = pygame.font.Font( 'Assets\F-Roboto-Light.ttf', floor( General.WIDTH / 76.8 ) - 1 )
        
        # LABELS
        General.initial_gap_x = 10
        General.initial_gap_y = 10
        
        b_complexity_label = main_Font.render( f"Best : {General.CUR_SORT_METHOD_COMPLEXITY[ 0 ]}, ", 1,
                                               color.get( "White" ) )
        a_complexity_label = main_Font.render( f"Average : {General.CUR_SORT_METHOD_COMPLEXITY[ 1 ]}, ", 1,
                                               color.get( "White" ) )
        w_complexity_label = main_Font.render( f"Worst : {General.CUR_SORT_METHOD_COMPLEXITY[ 2 ]},", 1,
                                               color.get( "White" ) )
        sort_name_label = main_Font.render( f"Current Sort : {General.CUR_SORT_METHOD},", 1, color.get( "White"
                                                                                                        ) )
        elem_num_label = main_Font.render( f"Number of elements : {General.NUMBER_OF_ELEM},", 1, color.get( "White"
                                                                                                            ) )
        swap_no_label = main_Font.render( f"Number of swaps : {len( General.swap )},", 1, color.get( "White" ) )
        time_label = main_Font.render( f"Time taken : {Time} ms", 1, color.get( "White" ) )
        General.change_elem_label = main_Font.render( " Change No.Elements (R) ", 1, color.get( "White" ) )
        General.change_sort_label = main_Font.render( " Change Sort (S) ", 1, color.get( "White" ) )
        General.go_to_data_label = main_Font.render( " See Net Results (D) ", 1, color.get( "White" ) )
        
        elem_num_label_x = sort_name_label.get_width() + General.initial_gap_x * 2
        number_of_swaps_x = elem_num_label_x + elem_num_label.get_width() + General.initial_gap_x
        time_taken_x = number_of_swaps_x + swap_no_label.get_width() + General.initial_gap_x
        General.change_elem_x = time_taken_x + time_label.get_width() + General.initial_gap_x
        General.change_sort_x = General.change_elem_x + General.change_elem_label.get_width() + General.initial_gap_x
        General.go_to_data_x = General.change_sort_x + General.change_sort_label.get_width() + \
                               General.initial_gap_x
        a_complexity_label_x = b_complexity_label.get_width() + General.initial_gap_x * 2
        w_complexity_label_x = a_complexity_label_x + a_complexity_label.get_width() + General.initial_gap_x
        
        General.WIN.blit( sort_name_label, (General.initial_gap_x, General.initial_gap_y) )
        General.WIN.blit( elem_num_label, (elem_num_label_x, General.initial_gap_y) )
        General.WIN.blit( swap_no_label, (number_of_swaps_x, General.initial_gap_y) )
        General.WIN.blit( time_label, (time_taken_x, General.initial_gap_y) )
        General.WIN.blit( General.change_elem_label, (General.change_elem_x, General.initial_gap_y) )
        General.WIN.blit( General.change_sort_label, (General.change_sort_x, General.initial_gap_y) )
        General.WIN.blit( General.go_to_data_label, (General.go_to_data_x, General.initial_gap_y) )
        General.WIN.blit( b_complexity_label, (General.initial_gap_x, General.initial_gap_y * 4) )
        General.WIN.blit( a_complexity_label, (a_complexity_label_x, General.initial_gap_y * 4) )
        General.WIN.blit( w_complexity_label, (w_complexity_label_x, General.initial_gap_y * 4) )
    
    @staticmethod
    def Run_DispDataScreen_() :
        text_size = floor( General.WIDTH / 48 )
        y_gap = text_size + 10
        x_gap = floor( General.WIDTH / 19.2 )
        init_y_gap = floor( General.WIDTH / 9.6 )
        
        General.WIN.blit( General.ARRAY_IMAGE, ORIGIN )
        
        text_font = pygame.font.Font( 'Assets/f-Roboto-light.ttf', text_size )
        title_font = pygame.font.Font( 'Assets/KEL.ttf', floor( General.WIDTH / 27.4 ) )
        
        title_lbl = title_font.render( 'Stats for all Algorithms', 1, color.get( 'Blue' ) )
        quick_lbl = text_font.render(
                f'{General.SORT_TIMINGS[ 3 ][ 1 ]} :        Time : {General.SORT_TIMINGS[ 3 ][ 0 ]} ms          Swaps : '
                f'{General.SORT_FIGURES[ 3 ][ 0 ]}          Elements :  '
                f'{General.NUMBER_OF_ELEM}', 1,
                color.get( "Black" ) )
        bubble_lbl = text_font.render(
                f'{General.SORT_TIMINGS[ 1 ][ 1 ]} :        Time : {General.SORT_TIMINGS[ 1 ][ 0 ]} ms          Swaps : '
                f'{General.SORT_FIGURES[ 1 ][ 0 ]}          Elements :  '
                f'{General.NUMBER_OF_ELEM}', 1,
                color.get( "Black" ) )
        selection_lbl = text_font.render(
                f'{General.SORT_TIMINGS[ 0 ][ 1 ]} :        Time : {General.SORT_TIMINGS[ 0 ][ 0 ]} ms          Swaps : '
                f'{General.SORT_FIGURES[ 0 ][ 0 ]}          Elements :  '
                f'{General.NUMBER_OF_ELEM}', 1,
                color.get( "Black" ) )
        merge_lbl = text_font.render(
                f'{General.SORT_TIMINGS[ 10 ][ 1 ]} :        Time : {General.SORT_TIMINGS[ 10 ][ 0 ]} ms          Swaps : '
                f'{General.SORT_FIGURES[ 10 ][ 0 ]}          Elements :  '
                f'{General.NUMBER_OF_ELEM}', 1,
                color.get( "Black" ) )
        Cycle_lbl = text_font.render(
                f'{General.SORT_TIMINGS[ 2 ][ 1 ]} :        Time : {General.SORT_TIMINGS[ 2 ][ 0 ]} ms          Swaps : '
                f'{General.SORT_FIGURES[ 2 ][ 0 ]}          Elements :  '
                f'{General.NUMBER_OF_ELEM}', 1,
                color.get( "Black" ) )
        insertion_lbl = text_font.render(
                f'{General.SORT_TIMINGS[ 8 ][ 1 ]} :        Time : {General.SORT_TIMINGS[ 8 ][ 0 ]} ms          Swaps : '
                f'{General.SORT_FIGURES[ 8 ][ 0 ]}          Elements :  '
                f'{General.NUMBER_OF_ELEM}', 1,
                color.get( "Black" ) )
        counting_lbl = text_font.render(
                f'{General.SORT_TIMINGS[ 7 ][ 1 ]} :        Time : {General.SORT_TIMINGS[ 7 ][ 0 ]} ms          Swaps : '
                f'{General.SORT_FIGURES[ 7 ][ 0 ]}          Elements :  '
                f'{General.NUMBER_OF_ELEM}', 1,
                color.get( "Black" ) )
        tim_lbl = text_font.render(
                f'{General.SORT_TIMINGS[ 5 ][ 1 ]} :        Time : {General.SORT_TIMINGS[ 5 ][ 0 ]} ms          Swaps : '
                f'{General.SORT_FIGURES[ 5 ][ 0 ]}          Elements :  '
                f'{General.NUMBER_OF_ELEM}', 1,
                color.get( "Black" ) )
        heap_lbl = text_font.render(
                f'{General.SORT_TIMINGS[ 4 ][ 1 ]} :        Time : {General.SORT_TIMINGS[ 4 ][ 0 ]} ms          Swaps : '
                f'{General.SORT_FIGURES[ 4 ][ 0 ]}          Elements :  '
                f'{General.NUMBER_OF_ELEM}', 1,
                color.get( "Black" ) )
        bucket_lbl = text_font.render(
                f'{General.SORT_TIMINGS[ 9 ][ 1 ]} :        Time : {General.SORT_TIMINGS[ 9 ][ 0 ]} ms          Swaps : '
                f'{General.SORT_FIGURES[ 9 ][ 0 ]}          Elements :  '
                f'{General.NUMBER_OF_ELEM}', 1,
                color.get( "Black" ) )
        cocktail_lbl = text_font.render(
                f'{General.SORT_TIMINGS[ 6 ][ 1 ]} :        Time : {General.SORT_TIMINGS[ 6 ][ 0 ]} ms          Swaps : '
                f'{General.SORT_FIGURES[ 6 ][ 0 ]}          Elements :  '
                f'{General.NUMBER_OF_ELEM}', 1,
                color.get( "Black" ) )
        General.SORT_TIMINGS = sorted( General.SORT_TIMINGS )
        General.SORT_FIGURES = sorted( General.SORT_FIGURES )
        most_time_lbl = text_font.render( f'Most Time consumed by : '
                                          f'{General.SORT_TIMINGS[ len( General.SORT_TIMINGS ) - 1 ][ 1 ]} : '
                                          f'{General.SORT_TIMINGS[ len( General.SORT_TIMINGS ) - 1 ][ 0 ]}', 1,
                                          color.get( 'Red' ) )
        least_time_lbl = text_font.render( f'Least Time consumed by : '
                                           f'{General.SORT_TIMINGS[ 0 ][ 1 ]} : '
                                           f'{General.SORT_TIMINGS[ 0 ][ 0 ]}', 1,
                                           color.get( 'Blue' ) )
        most_swap_lbl = text_font.render( f'Most Swaps taken by : '
                                          f'{General.SORT_FIGURES[ len( General.SORT_FIGURES ) - 1 ][ 1 ]} : '
                                          f'{General.SORT_FIGURES[ len( General.SORT_FIGURES ) - 1 ][ 0 ]}', 1,
                                          color.get( 'Red' ) )
        least_swap_lbl = text_font.render( f'Least Swaps taken by : '
                                           f'{General.SORT_FIGURES[ 0 ][ 1 ]} : '
                                           f'{General.SORT_FIGURES[ 0 ][ 0 ]}', 1,
                                           color.get( 'Blue' ) )
        General.SORT_TIMINGS = [ ]
        General.SORT_FIGURES = [ ]
        General.WIN.blit( title_lbl, (floor( General.WIDTH / 4.8 ), floor( General.HEIGHT / 21.6 )) )
        General.WIN.blit( selection_lbl, (x_gap, init_y_gap) )
        General.WIN.blit( quick_lbl, (x_gap, init_y_gap + y_gap) )
        General.WIN.blit( merge_lbl, (x_gap, init_y_gap + 2 * y_gap) )
        General.WIN.blit( bubble_lbl, (x_gap, init_y_gap + 3 * y_gap) )
        General.WIN.blit( Cycle_lbl, (x_gap, init_y_gap + 4 * y_gap) )
        General.WIN.blit( insertion_lbl, (x_gap, init_y_gap + 5 * y_gap) )
        General.WIN.blit( bucket_lbl, (x_gap, init_y_gap + 6 * y_gap) )
        General.WIN.blit( counting_lbl, (x_gap, init_y_gap + 7 * y_gap) )
        General.WIN.blit( heap_lbl, (x_gap, init_y_gap + 8 * y_gap) )
        General.WIN.blit( tim_lbl, (x_gap, init_y_gap + 9 * y_gap) )
        General.WIN.blit( cocktail_lbl, (x_gap, init_y_gap + 10 * y_gap) )
        General.WIN.blit( most_time_lbl, (x_gap, init_y_gap + 13 * y_gap) )
        General.WIN.blit( least_time_lbl, (x_gap, init_y_gap + 14 * y_gap) )
        General.WIN.blit( most_swap_lbl, (x_gap, init_y_gap + 15 * y_gap) )
        General.WIN.blit( least_swap_lbl, (x_gap, init_y_gap + 16 * y_gap) )

'''SORT FUNCTIONS'''

class Sort( General ) :
    
    @staticmethod
    def binary_search( the_array, item, start, end ) :
        if start == end :
            if the_array[ start ] > item :
                return start
            else :
                return start + 1
        if start > end :
            return start
        
        mid = (start + end) // 2
        if the_array[ mid ] < item :
            return Sort.binary_search( the_array, item, mid + 1, end )
        elif the_array[ mid ] > item :
            return Sort.binary_search( the_array, item, start, mid - 1 )
        else :
            return mid
    
    @staticmethod
    def Tim_insertion_sort( array, left = 0, right = None ) :
        if right is None :
            right = len( array ) - 1
        
        # Loop from the element indicated by
        # `left` until the element indicated by `right`
        for i in range( left + 1, right + 1 ) :
            # This is the element we want to position in its
            # correct place
            key_item = array[ i ]
            
            # Initialize the variable that will be used to
            # find the correct position of the element referenced
            # by `key_item`
            j = i - 1
            
            # Run through the list of items (the left
            # portion of the array) and find the correct position
            # of the element referenced by `key_item`. Do this only
            # if the `key_item` is smaller than its adjacent values.
            while j >= left and array[ j ] > key_item :
                # Shift the value one position to the left
                # and reposition `j` to point to the next element
                # (from right to left)
                array[ j + 1 ] = array[ j ]
                j -= 1
            
            # When you finish shifting the elements, position
            # the `key_item` in its correct location
            array[ j + 1 ] = key_item
        
        return array
    
    @staticmethod
    def Tim_merge( left, right ) :
        # If the first array is empty, then nothing needs
        # to be merged, and you can return the second array as the result
        if len( left ) == 0 :
            return right
        
        # If the second array is empty, then nothing needs
        # to be merged, and you can return the first array as the result
        if len( right ) == 0 :
            return left
        
        result = [ ]
        index_left = index_right = 0
        
        # Now go through both arrays until all the elements
        # make it into the resultant array
        while len( result ) < len( left ) + len( right ) :
            # The elements need to be sorted to add them to the
            # resultant array, so you need to decide whether to get
            # the next element from the first or the second array
            if left[ index_left ] <= right[ index_right ] :
                result.append( left[ index_left ] )
                index_left += 1
            else :
                result.append( right[ index_right ] )
                index_right += 1
            
            # If you reach the end of either array, then you can
            # add the remaining elements from the other array to
            # the result and break the loop
            if index_right == len( right ) :
                result += left[ index_left : ]
                break
            
            if index_left == len( left ) :
                result += right[ index_right : ]
                break
        
        return result
    
    @staticmethod
    def Partition_( array, swap, start, end ) :
        pivot = array[ start ]
        low = start + 1
        high = end
        
        while True :
            
            # If the current value we're looking at is larger than the pivot
            # it's in the right place (right side of pivot) and we can move left,
            # to the next element.
            # We also need to make sure we haven't surpassed the low pointer, since that
            # indicates we have already moved all the elements to their correct side of the pivot
            while low <= high and array[ high ] >= pivot :
                high = high - 1
            
            # Opposite process of the one above
            while low <= high and array[ low ] <= pivot :
                low = low + 1
            
            # We either found a value for both high and low that is out of order
            # or low is higher than high, in which case we exit the loop
            if low <= high :
                array[ low ], array[ high ] = array[ high ], array[ low ]
                swap.append( low )
                swap.append( high )
                # The loop continues
            else :
                # We exit out of the loop
                break
        
        array[ start ], array[ high ] = array[ high ], array[ start ]
        swap.append( start )
        swap.append( high )
        
        return high
    
    @staticmethod
    def Heapify( array, swap, n, i ) :
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2
        
        # See if left child of root exists and is
        # greater than root
        if l < n and array[ i ] < array[ l ] :
            largest = l
            
            # See if right child of root exists and is
        # greater than root
        if r < n and array[ largest ] < array[ r ] :
            largest = r
            
            # Change root, if needed
        if largest != i :
            array[ i ], array[ largest ] = array[ largest ], array[ i ]  # swap
            swap.append( i )
            swap.append( largest )
            # Heapify the root.
            Sort.Heapify( array, swap, n, largest )
        
        # The main function to sort an array of given size
    
    @staticmethod  # works
    def QuickSort_( array, swap, start, end ) :  # 5
        if start > end :
            return
        
        p = Sort.Partition_( array, swap, start, end )
        Sort.QuickSort_( array, swap, start, p - 1 )
        Sort.QuickSort_( array, swap, p + 1, end )
    
    @staticmethod  # works
    def MergeSort( array, swap ) :  # 4
        elepos = array[ 0 ][ 1 ]
        if len( array ) > 1 :
            mid = len( array ) // 2
            left = array[ :mid ]
            right = array[ mid : ]
            
            # Recursive call on each half
            Sort.MergeSort( left, swap )
            Sort.MergeSort( right, swap )
            # Two iterators for traversing the two halves
            i = 0
            j = 0
            
            # Iterator for the main list
            k = 0
            
            while i < len( left ) and j < len( right ) :
                if left[ i ] < right[ j ] :
                    # The value from the left half has been used
                    array[ k ] = left[ i ]
                    # Move the iterator forward
                    i += 1
                else :
                    array[ k ] = right[ j ]
                    j += 1
                # Move to the next slot
                k += 1
            # For all the remaining values
            while i < len( left ) :
                array[ k ] = left[ i ]
                i += 1
                k += 1
            
            while j < len( right ) :
                array[ k ] = right[ j ]
                j += 1
                k += 1
            
            for i in range( len( array ) ) :
                General.MAINLISTCOPYSWAPED[ i + elepos ] = array[ i ]
                swap.append( i + elepos )
                swap.append( array[ i ] )
    
    @staticmethod  # works
    def SelectionSort( array, swap ) :  # 1
        for i in range( len( array ) ) :
            min_idx = i
            for j in range( i + 1, len( array ) ) :
                if array[ min_idx ] > array[ j ] :
                    min_idx = j
            array[ i ], array[ min_idx ] = array[ min_idx ], array[ i ]
            swap.append( i )
            swap.append( min_idx )
    
    @staticmethod  # works
    def BubbleSort( array, swap ) :  # 2
        for j in range( len( array ) ) :
            for i in range( len( array ) - 1 ) :
                if array[ i ] > array[ i + 1 ] :
                    array[ i ], array[ i + 1 ] = array[ i + 1 ], array[ i ]
                    swap.append( i )
                    swap.append( i + 1 )
    
    @staticmethod  # works
    def CycleSort( array, swap ) :
        writes = 0
        
        # Loop through the array to find cycles to rotate.
        for cycleStart in range( 0, len( array ) - 1 ) :
            item = array[ cycleStart ]
            # Find where to put the item.
            pos = cycleStart
            for i in range( cycleStart + 1, len( array ) ) :
                if array[ i ] < item :
                    pos += 1
            
            # If the item is already there, this is not a cycle.
            if pos == cycleStart :
                continue
            
            # Otherwise, put the item there or right after any duplicates.
            while item == array[ pos ] :
                pos += 1
            array[ pos ], item = item, array[ pos ]
            swap.append( pos )
            swap.append( cycleStart )
            writes += 1
            # Rotate the rest of the cycle.
            while pos != cycleStart :
                # Find where to put the item.
                pos = cycleStart
                for i in range( cycleStart + 1, len( array ) ) :
                    if array[ i ] < item :
                        pos += 1
                
                # Put the item there or right after any duplicates.
                while item == array[ pos ] :
                    pos += 1
                array[ pos ], item = item, array[ pos ]
                swap.append( pos )
                swap.append( cycleStart )
                writes += 1
                # General.UpdateElement_( array, writes, color.get( 'Green' ) )
        
        return writes
    
    @staticmethod  # works
    def HeapSort( array, swap ) :
        n = len( array )
        
        # Build a maxheap.
        # Since last parent will be at ((n//2)-1) we can start at that location.
        for i in range( n // 2 - 1, -1, -1 ) :
            Sort.Heapify( array, swap, n, i )
            
            # One by one extract elements
        for i in range( n - 1, 0, -1 ) :
            array[ i ], array[ 0 ] = array[ 0 ], array[ i ]  # swap
            swap.append( i )
            swap.append( 0 )
            Sort.Heapify( array, swap, i, 0 )
    
    @staticmethod
    def CocktailSort( array, swap ) :
        n = len( array )
        swapped = True
        start = 0
        end = n - 1
        while swapped :
            
            # reset the swapped flag on entering the loop,
            # because it might be true from array previous
            # iteration.
            swapped = False
            
            # loop from left to right same as the bubble
            # sort
            for i in range( start, end ) :
                if array[ i ] > array[ i + 1 ] :
                    array[ i ], array[ i + 1 ] = array[ i + 1 ], array[ i ]
                    swap.append( i )
                    swap.append( i + 1 )
                    swapped = True
            
            # if nothing moved, then array is sorted.
            if not swapped :
                break
            
            # otherwise, reset the swapped flag so that it
            # can be used in the next stage
            swapped = False
            
            # move the end point back by one, because
            # item at the end is in its rightful spot
            end = end - 1
            
            # from right to left, doing the same
            # comparison as in the previous stage
            for i in range( end - 1, start - 1, -1 ) :
                if array[ i ] > array[ i + 1 ] :
                    array[ i ], array[ i + 1 ] = array[ i + 1 ], array[ i ]
                    swap.append( i )
                    swap.append( i + 1 )
                    swapped = True
            
            # increase the starting point, because
            # the last stage would have moved the next
            # smallest number to its rightful spot.
            start = start + 1
    
    @staticmethod
    def Timsort( array ) :
        min_run = 32
        n = len( array )
        
        # Start by slicing and sorting small portions of the
        # input array. The size of these slices is defined by
        # your 'min_run' size.
        for i in range( 0, n, min_run ) :
            Sort.Tim_insertion_sort( array, i, min( (i + min_run - 1), n - 1 ) )
        
        # Now you can start merging the sorted slices.
        # Start from `min_run`, doubling the size on
        # each iteration until you surpass the length of
        # the array.
        size = min_run
        while size < n :
            # Determine the arrays that will
            # be merged together
            for start in range( 0, n, size * 2 ) :
                # Compute the `midpoint` (where the first array ends
                # and the second starts) and the `endpoint` (where
                # the second array ends)
                midpoint = start + size - 1
                end = min( (start + size * 2 - 1), (n - 1) )
                
                # Merge the two subarrays.
                # The `left` array should go from `start` to
                # `midpoint + 1`, while the `right` array should
                # go from `midpoint + 1` to `end + 1`.
                merged_array = Sort.Tim_merge(
                        left = array[ start :midpoint + 1 ],
                        right = array[ midpoint + 1 :end + 1 ] )
                
                # Finally, put the merged array back into
                # your array
                array[ start :start + len( merged_array ) ] = merged_array
            
            # Each iteration should double the size of your arrays
            size *= 2
        
        return array
    
    @staticmethod  # works
    def BucketSort( array, swap ) :
        bucket = [ ]
        
        # Create empty buckets
        for i in range( len( array ) ) :
            bucket.append( [ ] )
        
        # Insert elements into their respective buckets
        for j in array :
            index_b = int( 10 * j )
            bucket[ index_b ].append( j )
        
        # Get the sorted elements
        k = 0
        for i in range( len( array ) ) :
            for j in range( len( bucket[ i ] ) ) :
                array[ k ] = bucket[ i ][ j ]
                swap.append( k )
                swap.append( bucket[ i ][ j ] )
                k += 1
        
        # Sort the elements of each bucket
        for i in range( len( array ) ) :
            bucket[ i ] = sorted( bucket[ i ] )
        
        k = 0
        for i in range( len( array ) ) :
            for j in range( len( bucket[ i ] ) ) :
                array[ k ] = bucket[ i ][ j ]
                k += 1
    
    @staticmethod  # works
    def CountingSort( array, swap ) :
        max_val = 0
        for j in range( len( array ) ) :
            if array[ j ] > max_val :
                max_val = array[ j ]
        
        m = max_val + 1
        count = [ 0 ] * m
        
        for a in array :
            # count occurences
            count[ a ] += 1
        i = 0
        for a in range( m ) :
            for c in range( count[ a ] ) :
                array[ i ] = a
                swap.append( i )
                swap.append( a )
                i += 1
        return array
    
    @staticmethod  # works
    def InsertionSort( array, swap ) :
        # Traverse through 1 to len(arr)
        for i in range( 1, len( array ) ) :
            
            key = array[ i ]
            
            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i - 1
            while j >= 0 and key < array[ j ] :
                array[ j + 1 ] = array[ j ]
                swap.append( j + 1 )
                swap.append( j )
                j -= 1
            array[ j + 1 ] = key

'''SCREEN FUNCTIONS'''

class Screen( General ) :
    @staticmethod
    def dispDataScreen_() :
        Screen.dispSortScreen_empty_()
        General.Run_DispDataScreen_()
        menu_font = pygame.font.Font( 'Assets/KEL.ttf', floor( General.WIDTH / 38.4 ) )
        back_to_menu_label = menu_font.render( " BACK TO MENU ", 1, color.get( 'Black' ) )
        General.WIN.blit( back_to_menu_label, (General.WIDTH - floor( General.WIDTH / 32 ) - back_to_menu_label.get_width(),
                                               General.HEIGHT - floor( General.WIDTH / 32 ) - back_to_menu_label.get_height()) )
        while 1 :
            pygame.display.update()
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    pygame.display.quit()
                    return 0
                if checkMouse( General.WIDTH - floor( General.WIDTH / 32 ) - back_to_menu_label.get_width(),
                               General.HEIGHT - floor( General.WIDTH / 32 ) - back_to_menu_label.get_height(),
                               General.WIDTH - floor( General.WIDTH / 32 ), General.HEIGHT - floor( General.WIDTH / 32 ), event ) :
                    return 1
    
    @staticmethod
    def dispSortScreen_() :
        disp_Screen_1D_Loop = True
        result = False
        General.WIN.blit( General.ARRAY_IMAGE, ORIGIN )
        while disp_Screen_1D_Loop :
            pygame.display.update()
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    disp_Screen_1D_Loop = False
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_r :
                        disp_Screen_1D_Loop = False
                        result = 2
                    elif event.key == pygame.K_s :
                        disp_Screen_1D_Loop = False
                        result = 3
            if General.CUR_SORT_METHOD == 'Selection Sort' :
                disp_Screen_1D_Loop = False
                General.assignComplexity()
                General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
                General.MAINLISTCOPY = General.MAINLIST[ : ]
                General.swap = [ ]
                T1 = time.time()
                Sort.SelectionSort( General.MAINLISTCOPYSWAPED, General.swap )
                Time = round( time.time() - T1, 5 )
                General.DrawAll_( General.MAINLISTCOPY )
                result = General.DispArray_( General.MAINLISTCOPY, General.swap, Time )
            elif General.CUR_SORT_METHOD == 'Bubble Sort' :
                disp_Screen_1D_Loop = False
                General.assignComplexity()
                General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
                General.MAINLISTCOPY = General.MAINLIST[ : ]
                General.swap = [ ]
                T1 = time.time()
                Sort.BubbleSort( General.MAINLISTCOPYSWAPED, General.swap )
                Time = round( time.time() - T1, 5 )
                General.DrawAll_( General.MAINLISTCOPY )
                result = General.DispArray_( General.MAINLISTCOPY, General.swap, Time )
            elif General.CUR_SORT_METHOD == 'Cycle Sort' :
                disp_Screen_1D_Loop = False
                General.assignComplexity()
                General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
                General.MAINLISTCOPY = General.MAINLIST[ : ]
                General.swap = [ ]
                T1 = time.time()
                Sort.CycleSort( General.MAINLISTCOPYSWAPED, General.swap )
                Time = round( time.time() - T1, 5 )
                General.DrawAll_( General.MAINLISTCOPY )
                result = General.DispArray_( General.MAINLISTCOPY, General.swap, Time )
            elif General.CUR_SORT_METHOD == 'Merge Sort' :
                General.MAINLIST = [ ]
                for i in range( General.NUMBER_OF_ELEM ) :
                    General.MAINLIST.append( [ random.randrange( 50, 1000 ), i ] )
                disp_Screen_1D_Loop = False
                General.assignComplexity()
                General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
                General.MAINLISTCOPY = General.MAINLIST[ : ]
                General.swap = [ ]
                T1 = time.time()
                Sort.MergeSort( General.MAINLISTCOPYSWAPED, General.swap )
                Time = round( time.time() - T1, 5 )
                General.DrawAllMerge_( General.MAINLISTCOPY )
                result = General.DispArray_( General.MAINLISTCOPY, General.swap, Time )
                General.assignMainList()
            elif General.CUR_SORT_METHOD == 'Quick Sort' :
                General.assignComplexity()
                General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
                General.MAINLISTCOPY = General.MAINLIST[ : ]
                General.swap = [ ]
                T1 = time.time()
                Sort.QuickSort_( General.MAINLISTCOPYSWAPED, General.swap, 0, len( General.MAINLISTCOPYSWAPED ) - 1 )
                Time = round( time.time() - T1, 5 )
                General.DrawAll_( General.MAINLISTCOPY )
                result = General.DispArray_( General.MAINLISTCOPY, General.swap, Time )
                disp_Screen_1D_Loop = False
            elif General.CUR_SORT_METHOD == 'Heap Sort' :
                disp_Screen_1D_Loop = False
                General.assignComplexity()
                General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
                General.MAINLISTCOPY = General.MAINLIST[ : ]
                General.swap = [ ]
                T1 = time.time()
                Sort.HeapSort( General.MAINLISTCOPYSWAPED, General.swap )
                Time = round( time.time() - T1, 5 )
                General.DrawAll_( General.MAINLISTCOPY )
                result = General.DispArray_( General.MAINLISTCOPY, General.swap, Time )
            elif General.CUR_SORT_METHOD == 'Cocktail Sort' :
                disp_Screen_1D_Loop = False
                General.assignComplexity()
                General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
                General.MAINLISTCOPY = General.MAINLIST[ : ]
                General.swap = [ ]
                T1 = time.time()
                Sort.CocktailSort( General.MAINLISTCOPYSWAPED, General.swap )
                Time = round( time.time() - T1, 5 )
                General.DrawAll_( General.MAINLISTCOPY )
                result = General.DispArray_( General.MAINLISTCOPY, General.swap, Time )
            elif General.CUR_SORT_METHOD == 'Bucket Sort' :
                General.assignMainList()
                disp_Screen_1D_Loop = False
                General.assignComplexity()
                General.MAINLISTCOPYSWAPED = [ ]
                for i in range( len( General.MAINLIST ) ) :
                    General.MAINLISTCOPYSWAPED.append( General.MAINLIST[ i ] / 1000 )
                General.MAINLISTCOPY = General.MAINLIST[ : ]
                General.swap = [ ]
                T1 = time.time()
                Sort.BucketSort( General.MAINLISTCOPYSWAPED, General.swap )
                Time = round( time.time() - T1, 5 )
                General.DrawAll_( General.MAINLISTCOPY )
                result = General.DispArray_( General.MAINLISTCOPY, General.swap, Time )
            elif General.CUR_SORT_METHOD == 'Counting Sort' :
                disp_Screen_1D_Loop = False
                General.assignComplexity()
                General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
                General.MAINLISTCOPY = General.MAINLIST[ : ]
                General.swap = [ ]
                T1 = time.time()
                Sort.CountingSort( General.MAINLISTCOPYSWAPED, General.swap )
                Time = round( time.time() - T1, 5 )
                General.DrawAll_( General.MAINLISTCOPY )
                result = General.DispArray_( General.MAINLISTCOPYSWAPED, General.swap, Time )
            elif General.CUR_SORT_METHOD == 'Insertion Sort' :
                disp_Screen_1D_Loop = False
                General.assignComplexity()
                General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
                General.MAINLISTCOPY = General.MAINLIST[ : ]
                General.swap = [ ]
                T1 = time.time()
                Sort.InsertionSort( General.MAINLISTCOPYSWAPED, General.swap )
                Time = round( time.time() - T1, 5 )
                General.DrawAll_( General.MAINLISTCOPY )
                result = General.DispArray_( General.MAINLISTCOPY, General.swap, Time )
        return result
    
    @staticmethod
    def dispSortScreen_empty_() :
        General.assignMainList()
        General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
        General.swap = [ ]
        T1 = time.time()
        Sort.SelectionSort( General.MAINLISTCOPYSWAPED, General.swap )
        Time = round( round( time.time() - T1, 5 ) * 1000, 2 )
        General.SORT_TIMINGS.append( [ Time, 'Selection Sort' ] )
        General.SORT_FIGURES.append( [ len( General.swap ), 'Selection Sort' ] )
        
        General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
        General.swap = [ ]
        T1 = time.time()
        Sort.BubbleSort( General.MAINLISTCOPYSWAPED, General.swap )
        Time = round( round( time.time() - T1, 5 ) * 1000, 2 )
        General.SORT_TIMINGS.append( [ Time, 'Bubble Sort' ] )
        General.SORT_FIGURES.append( [ len( General.swap ), 'Bubble Sort' ] )
        
        General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
        General.swap = [ ]
        T1 = time.time()
        Sort.CycleSort( General.MAINLISTCOPYSWAPED, General.swap )
        Time = round( round( time.time() - T1, 5 ) * 1000, 2 )
        General.SORT_TIMINGS.append( [ Time, 'Cycle Sort' ] )
        General.SORT_FIGURES.append( [ len( General.swap ), 'Cycle Sort' ] )
        
        General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
        General.swap = [ ]
        T1 = time.time()
        Sort.QuickSort_( General.MAINLISTCOPYSWAPED, General.swap, 0, len( General.MAINLISTCOPYSWAPED ) - 1 )
        Time = round( round( time.time() - T1, 5 ) * 1000, 2 )
        General.SORT_TIMINGS.append( [ Time, 'Quick Sort' ] )
        General.SORT_FIGURES.append( [ len( General.swap ), 'Quick Sort' ] )
        
        General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
        General.swap = [ ]
        T1 = time.time()
        Sort.HeapSort( General.MAINLISTCOPYSWAPED, General.swap )
        Time = round( round( time.time() - T1, 5 ) * 1000, 2 )
        General.SORT_TIMINGS.append( [ Time, 'Heap Sort' ] )
        General.SORT_FIGURES.append( [ len( General.swap ), 'Heap Sort' ] )
        
        General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
        T1 = time.time()
        Sort.Timsort( General.MAINLISTCOPYSWAPED )
        Time = round( round( time.time() - T1, 5 ) * 1000, 2 )
        General.SORT_TIMINGS.append( [ Time, 'Tim Sort' ] )
        General.SORT_FIGURES.append( [ len( General.swap ), 'Tim Sort' ] )
        
        General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
        General.swap = [ ]
        T1 = time.time()
        Sort.CocktailSort( General.MAINLISTCOPYSWAPED, General.swap )
        Time = round( round( time.time() - T1, 5 ) * 1000, 2 )
        General.SORT_TIMINGS.append( [ Time, 'Cocktail Sort' ] )
        General.SORT_FIGURES.append( [ len( General.swap ), 'Cocktail Sort' ] )
        
        General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
        General.swap = [ ]
        T1 = time.time()
        Sort.CountingSort( General.MAINLISTCOPYSWAPED, General.swap )
        Time = round( round( time.time() - T1, 5 ) * 1000, 2 )
        General.SORT_TIMINGS.append( [ Time, 'Counting Sort' ] )
        General.SORT_FIGURES.append( [ len( General.swap ), 'Counting Sort' ] )
        
        General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
        General.swap = [ ]
        T1 = time.time()
        Sort.InsertionSort( General.MAINLISTCOPYSWAPED, General.swap )
        Time = round( round( time.time() - T1, 5 ) * 1000, 2 )
        General.SORT_TIMINGS.append( [ Time, 'Insertion Sort' ] )
        General.SORT_FIGURES.append( [ len( General.swap ), 'Insertion Sort' ] )
        
        General.assignMainList()
        General.MAINLISTCOPYSWAPED = [ ]
        for i in range( len( General.MAINLIST ) ) :
            General.MAINLISTCOPYSWAPED.append( General.MAINLIST[ i ] / 1000 )
        General.swap = [ ]
        T1 = time.time()
        Sort.BucketSort( General.MAINLISTCOPYSWAPED, General.swap )
        Time = round( round( time.time() - T1, 5 ) * 1000, 2 )
        General.SORT_TIMINGS.append( [ Time, 'Bucket Sort' ] )
        General.SORT_FIGURES.append( [ len( General.swap ), 'Bucket Sort' ] )
        
        General.MAINLIST = [ ]
        for i in range( General.NUMBER_OF_ELEM ) :
            General.MAINLIST.append( [ random.randrange( 50, 1000 ), i ] )
        General.MAINLISTCOPYSWAPED = General.MAINLIST[ : ]
        General.swap = [ ]
        T1 = time.time()
        Sort.MergeSort( General.MAINLISTCOPYSWAPED, General.swap )
        Time = round( round( time.time() - T1, 5 ) * 1000, 2 )
        General.SORT_TIMINGS.append( [ Time, 'Merge Sort' ] )
        General.SORT_FIGURES.append( [ len( General.swap ), 'Merge Sort' ] )
    
    @staticmethod
    def selectSortScreen_() :
        select_Sort_Screen_Loop = True
        General.WIN.blit( General.SORT_IMAGE, ORIGIN )
        while select_Sort_Screen_Loop :
            pygame.display.update()
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    pygame.display.quit()
                    return 0
                elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_1 or event.key == pygame.K_s :
                        select_Sort_Screen_Loop = False
                        General.CUR_SORT_METHOD = 'Selection Sort'
                    elif event.key == pygame.K_2 or event.key == pygame.K_b :
                        select_Sort_Screen_Loop = False
                        General.CUR_SORT_METHOD = 'Bubble Sort'
                    elif event.key == pygame.K_3 or event.key == pygame.K_c :
                        select_Sort_Screen_Loop = False
                        General.CUR_SORT_METHOD = 'Cycle Sort'
                    elif event.key == pygame.K_4 or event.key == pygame.K_m :
                        select_Sort_Screen_Loop = False
                        General.CUR_SORT_METHOD = 'Merge Sort'
                    elif event.key == pygame.K_5 or event.key == pygame.K_q :
                        select_Sort_Screen_Loop = False
                        General.CUR_SORT_METHOD = 'Quick Sort'
                    elif event.key == pygame.K_6 or event.key == pygame.K_h :
                        select_Sort_Screen_Loop = False
                        General.CUR_SORT_METHOD = 'Heap Sort'
                    elif event.key == pygame.K_7 or event.key == pygame.K_t :
                        select_Sort_Screen_Loop = False
                        General.CUR_SORT_METHOD = 'Cocktail Sort'
                    elif event.key == pygame.K_8 or event.key == pygame.K_r :
                        select_Sort_Screen_Loop = False
                        General.CUR_SORT_METHOD = 'Bucket Sort'
                    elif event.key == pygame.K_9 or event.key == pygame.K_n :
                        select_Sort_Screen_Loop = False
                        General.CUR_SORT_METHOD = 'Counting Sort'
                    elif event.key == pygame.K_0 or event.key == pygame.K_i :
                        select_Sort_Screen_Loop = False
                        General.CUR_SORT_METHOD = 'Insertion Sort'
        return 3
    
    @staticmethod
    def selectNumEle_() :
        select_Num_Ele_Loop = True
        General.WIN.blit( General.NUM_ELE_IMAGE, ORIGIN )
        while select_Num_Ele_Loop :
            pygame.display.update()
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    pygame.display.quit()
                    return 0
                elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_1 :
                        select_Num_Ele_Loop = False
                        General.MAINLIST = [ ]
                        General.MAINLISTCOPY = [ ]
                        General.NUMBER_OF_ELEM = 50
                    if event.key == pygame.K_2 :
                        select_Num_Ele_Loop = False
                        General.MAINLIST = [ ]
                        General.MAINLISTCOPY = [ ]
                        General.NUMBER_OF_ELEM = 300
                    if event.key == pygame.K_3 :
                        select_Num_Ele_Loop = False
                        General.MAINLIST = [ ]
                        General.MAINLISTCOPY = [ ]
                        General.NUMBER_OF_ELEM = 700
                    if event.key == pygame.K_4 :
                        select_Num_Ele_Loop = False
                        General.MAINLIST = [ ]
                        General.MAINLISTCOPY = [ ]
                        General.NUMBER_OF_ELEM = 1000
                    if event.key == pygame.K_5 :
                        select_Num_Ele_Loop = False
                        General.MAINLIST = [ ]
                        General.MAINLISTCOPY = [ ]
                        General.NUMBER_OF_ELEM = General.WIDTH - General.ARRAY_DISP_GAP
        General.assignMainList()
        printList( General.MAINLIST )
        return 2
    
    @staticmethod
    def menuScreen_() :
        menu_Screen_Loop = True
        result = False
        General.WIN.blit( General.BG_IMAGE, ORIGIN )
        while menu_Screen_Loop :
            pygame.display.update()
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    menu_Screen_Loop = False
                    pygame.display.quit()
                if checkMouse( General.MENU_START_BTN_LOWER[ 0 ], General.MENU_START_BTN_LOWER[ 1 ],
                               General.MENU_START_BTN_UPPER[ 0 ], General.MENU_START_BTN_UPPER[ 1 ], event ) :
                    result = True
                    menu_Screen_Loop = False
                if checkMouse( General.MENU_EXIT_BTN_LOWER[ 0 ], General.MENU_EXIT_BTN_LOWER[ 1 ],
                               General.MENU_EXIT_BTN_UPPER[ 0 ], General.MENU_EXIT_BTN_UPPER[ 1 ], event ) :
                    result = False
                    menu_Screen_Loop = False
        
        return result

def main() :
    QUIT = Screen.menuScreen_()
    while QUIT != 0 :
        if QUIT == 1 :
            QUIT = Screen.selectNumEle_()
        elif QUIT == 2 :
            QUIT = Screen.selectSortScreen_()
        elif QUIT == 3 :
            QUIT = Screen.dispSortScreen_()
        elif QUIT == 4 :
            QUIT = Screen.dispDataScreen_()

main()
