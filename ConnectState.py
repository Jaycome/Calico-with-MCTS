"""
@author: Masoud Masoumi Moghadam
Code Script:
Code for running the functions that might be used in the game and the class of the gamestate
Adapted code from "Monte-Carlo-Tree-Search-Agent-for-the-Game-of-HEX" by Masoud Masoumi Moghadam et al. at https://github.com/masouduut94/MCTS-agent-python """

import random
from copy import deepcopy
import numpy as np
from meta import GameMeta

class GameState:    
    def __init__(self):
        self.tile_base=[]
        self.edgeTile=[]
        self.edgeTile2=[]
        self.tile_base2=[]
        self.marketTile=[]
        self.catGroup=[]
        self.marketTile=[]
        self.player1HandedTile=[]
        self.player2HandedTile=[]
        self.round=1
        self.to_play = GameMeta.PLAYERS['one']
        self.patch_tile=[]
        self.used_patch_tile=[]
    def initial_setting(self):
        #self.tile_base=[]
        for k in range(3):
            for i in range(1,7):
                for j in range(1,7):
                    self.patch_tile.append({
                                            'element':i,
                                            'pattern':j,
                                            })
        for row in range(GameMeta.ROWS):
                    for col in range(GameMeta.COLS):
                        if(row==1 and col==1):
                            self.tile_base.append({'row':row,
                                        'col':col,
                                        'element':0,
                                        'pattern':0,
                                        'goal_type':0,
                                        'token':0})
                        elif(row==2 and col==3):
                            self.tile_base.append({'row':row,
                                        'col':col,
                                        'element':0,
                                        'pattern':0,
                                        'goal_type':0,
                                        'token':0})
                        elif(row==3 and col==1):
                            self.tile_base.append({'row':row,
                                        'col':col,
                                        'element':0,
                                        'pattern':0,
                                        'goal_type':0,
                                        'token':0})
                        else:
                            self.tile_base.append({'row':row,
                                        'col':col,
                                        'element':0,
                                        'pattern':0,
                                        'token':0})
        self.edgeTile=[]
        self.edgeTile.append({'row':0,
                    'col':-1,
                    'element':GameMeta.TILE_ELEMENT['yellow'],
                    'pattern':GameMeta.TILE_PATTERN['stripes'],
            })
        self.edgeTile.append({'row':1,
                    'col':-1,
                    'element':GameMeta.TILE_ELEMENT['light_blue'],
                    'pattern':GameMeta.TILE_PATTERN['vines'],
            })
        self.edgeTile.append({'row':2,
                    'col':-1,
                    'element':GameMeta.TILE_ELEMENT['pink'],
                    'pattern':GameMeta.TILE_PATTERN['ferns'],
            })
        self.edgeTile.append({'row':3,
                    'col':-1,
                    'element':GameMeta.TILE_ELEMENT['purple'],
                    'pattern':GameMeta.TILE_PATTERN['quatrefoil'],
            })
        self.edgeTile.append({'row':4,
                    'col':-1,
                    'element':GameMeta.TILE_ELEMENT['yellow'],
                    'pattern':GameMeta.TILE_PATTERN['flowers'],
            })
        self.edgeTile.append({'row':5,
                    'col':-1,
                    'element':GameMeta.TILE_ELEMENT['green'],
                    'pattern':GameMeta.TILE_PATTERN['stripes'],
            })
        self.edgeTile.append({'row':5,
                    'col':0,
                    'element':GameMeta.TILE_ELEMENT['dark_blue'],
                    'pattern':GameMeta.TILE_PATTERN['dots'],
            })
        self.edgeTile.append({'row':5,
                    'col':1,
                    'element':GameMeta.TILE_ELEMENT['purple'],
                    'pattern':GameMeta.TILE_PATTERN['vines'],
            })
        self.edgeTile.append({'row':5,
                    'col':2,
                    'element':GameMeta.TILE_ELEMENT['yellow'],
                    'pattern':GameMeta.TILE_PATTERN['ferns'],
            })
        self.edgeTile.append({'row':5,
                    'col':3,
                    'element':GameMeta.TILE_ELEMENT['green'],
                    'pattern':GameMeta.TILE_PATTERN['quatrefoil'],
            })
        self.edgeTile.append({'row':5,
                    'col':4,
                    'element':GameMeta.TILE_ELEMENT['dark_blue'],
                    'pattern':GameMeta.TILE_PATTERN['flowers'],
            })
        self.edgeTile.append({'row':-1,
                    'col':5,
                    'element':GameMeta.TILE_ELEMENT['light_blue'],
                    'pattern':GameMeta.TILE_PATTERN['quatrefoil'],
            })
        self.edgeTile.append({'row':0,
                    'col':5,
                    'element':GameMeta.TILE_ELEMENT['pink'],
                    'pattern':GameMeta.TILE_PATTERN['flowers'],
            })
        self.edgeTile.append({'row':1,
                    'col':5,
                    'element':GameMeta.TILE_ELEMENT['dark_blue'],
                    'pattern':GameMeta.TILE_PATTERN['ferns'],
            })
        self.edgeTile.append({'row':2,
                    'col':5,
                    'element':GameMeta.TILE_ELEMENT['green'],
                    'pattern':GameMeta.TILE_PATTERN['vines'],
            })
        self.edgeTile.append({'row':3,
                    'col':5,
                    'element':GameMeta.TILE_ELEMENT['pink'],
                    'pattern':GameMeta.TILE_PATTERN['dots'],
            })
        self.edgeTile.append({'row':4,
                    'col':5,
                    'element':GameMeta.TILE_ELEMENT['light_blue'],
                    'pattern':GameMeta.TILE_PATTERN['stripes'],
            })
        
        self.edgeTile.append({'row':-1,
                    'col':0,
                    'element':GameMeta.TILE_ELEMENT['green'],
                    'pattern':GameMeta.TILE_PATTERN['flowers'],
            })
        self.edgeTile.append({'row':-1,
                    'col':1,
                    'element':GameMeta.TILE_ELEMENT['dark_blue'],
                    'pattern':GameMeta.TILE_PATTERN['quatrefoil'],
            })
        self.edgeTile.append({'row':-1,
                    'col':2,
                    'element':GameMeta.TILE_ELEMENT['light_blue'],
                    'pattern':GameMeta.TILE_PATTERN['ferns'],
            })
        self.edgeTile.append({'row':-1,
                    'col':3,
                    'element':GameMeta.TILE_ELEMENT['purple'],
                    'pattern':GameMeta.TILE_PATTERN['stripes'],
            })
        self.edgeTile.append({'row':-1,
                    'col':4,
                    'element':GameMeta.TILE_ELEMENT['yellow'],
                    'pattern':GameMeta.TILE_PATTERN['dots'],
            })



        self.tile_base2=[]
        for row in range(GameMeta.ROWS):
                    for col in range(GameMeta.COLS):
                        if(row==1 and col==1):
                            self.tile_base2.append({'row':row,
                                        'col':col,
                                        'element':0,
                                        'pattern':0,
                                        'goal_type':0,
                                        'token':0})
                        elif(row==2 and col==3):
                            self.tile_base2.append({'row':row,
                                        'col':col,
                                        'element':0,
                                        'pattern':0,
                                        'goal_type':0,
                                        'token':0})
                        elif(row==3 and col==1):
                            self.tile_base2.append({'row':row,
                                        'col':col,
                                        'element':0,
                                        'pattern':0,
                                        'goal_type':0,
                                        'token':0})
                        else:
                            self.tile_base2.append({'row':row,
                                        'col':col,
                                        'element':0,
                                        'pattern':0,
                                        'token':0})
        self.edgeTile2=[]
        self.edgeTile2.append({'row':0,
                    'col':-1,
                    'element':GameMeta.TILE_ELEMENT['yellow'],
                    'pattern':GameMeta.TILE_PATTERN['stripes'],
            })
        self.edgeTile2.append({'row':1,
                    'col':-1,
                    'element':GameMeta.TILE_ELEMENT['light_blue'],
                    'pattern':GameMeta.TILE_PATTERN['vines'],
            })
        self.edgeTile2.append({'row':2,
                    'col':-1,
                    'element':GameMeta.TILE_ELEMENT['pink'],
                    'pattern':GameMeta.TILE_PATTERN['ferns'],
            })
        self.edgeTile2.append({'row':3,
                    'col':-1,
                    'element':GameMeta.TILE_ELEMENT['purple'],
                    'pattern':GameMeta.TILE_PATTERN['quatrefoil'],
            })
        self.edgeTile2.append({'row':4,
                    'col':-1,
                    'element':GameMeta.TILE_ELEMENT['yellow'],
                    'pattern':GameMeta.TILE_PATTERN['flowers'],
            })
        self.edgeTile2.append({'row':5,
                    'col':-1,
                    'element':GameMeta.TILE_ELEMENT['green'],
                    'pattern':GameMeta.TILE_PATTERN['stripes'],
            })
        self.edgeTile2.append({'row':5,
                    'col':0,
                    'element':GameMeta.TILE_ELEMENT['dark_blue'],
                    'pattern':GameMeta.TILE_PATTERN['dots'],
            })
        self.edgeTile2.append({'row':5,
                    'col':1,
                    'element':GameMeta.TILE_ELEMENT['purple'],
                    'pattern':GameMeta.TILE_PATTERN['vines'],
            })
        self.edgeTile2.append({'row':5,
                    'col':2,
                    'element':GameMeta.TILE_ELEMENT['yellow'],
                    'pattern':GameMeta.TILE_PATTERN['ferns'],
            })
        self.edgeTile2.append({'row':5,
                    'col':3,
                    'element':GameMeta.TILE_ELEMENT['green'],
                    'pattern':GameMeta.TILE_PATTERN['quatrefoil'],
            })
        self.edgeTile2.append({'row':5,
                    'col':4,
                    'element':GameMeta.TILE_ELEMENT['dark_blue'],
                    'pattern':GameMeta.TILE_PATTERN['flowers'],
            })
        self.edgeTile2.append({'row':-1,
                    'col':5,
                    'element':GameMeta.TILE_ELEMENT['light_blue'],
                    'pattern':GameMeta.TILE_PATTERN['quatrefoil'],
            })

        self.edgeTile2.append({'row':0,
                    'col':5,
                    'element':GameMeta.TILE_ELEMENT['pink'],
                    'pattern':GameMeta.TILE_PATTERN['flowers'],
            })
        self.edgeTile2.append({'row':1,
                    'col':5,
                    'element':GameMeta.TILE_ELEMENT['dark_blue'],
                    'pattern':GameMeta.TILE_PATTERN['ferns'],
            })
        self.edgeTile2.append({'row':2,
                    'col':5,
                    'element':GameMeta.TILE_ELEMENT['green'],
                    'pattern':GameMeta.TILE_PATTERN['vines'],
            })
        self.edgeTile2.append({'row':3,
                    'col':5,
                    'element':GameMeta.TILE_ELEMENT['pink'],
                    'pattern':GameMeta.TILE_PATTERN['dots'],
            })
        self.edgeTile2.append({'row':4,
                    'col':5,
                    'element':GameMeta.TILE_ELEMENT['light_blue'],
                    'pattern':GameMeta.TILE_PATTERN['stripes'],
            })
        
        self.edgeTile2.append({'row':-1,
                    'col':0,
                    'element':GameMeta.TILE_ELEMENT['green'],
                    'pattern':GameMeta.TILE_PATTERN['flowers'],
            })
        self.edgeTile2.append({'row':-1,
                    'col':1,
                    'element':GameMeta.TILE_ELEMENT['dark_blue'],
                    'pattern':GameMeta.TILE_PATTERN['quatrefoil'],
            })
        self.edgeTile2.append({'row':-1,
                    'col':2,
                    'element':GameMeta.TILE_ELEMENT['light_blue'],
                    'pattern':GameMeta.TILE_PATTERN['ferns'],
            })
        self.edgeTile2.append({'row':-1,
                    'col':3,
                    'element':GameMeta.TILE_ELEMENT['purple'],
                    'pattern':GameMeta.TILE_PATTERN['stripes'],
            })
        self.edgeTile2.append({'row':-1,
                    'col':4,
                    'element':GameMeta.TILE_ELEMENT['yellow'],
                    'pattern':GameMeta.TILE_PATTERN['dots'],
            })
        

        #tiles for public to take           
        self.marketTile=[]
        for i in range(3):
            newPatchTile=self.pick_one_tile()
            self.marketTile.append(
            {'row':-1,
            'col':-1,
            'element':self.patch_tile[newPatchTile]['element'],
            'pattern':self.patch_tile[newPatchTile]['pattern']
            })

        #tiles on hand
        self.player1HandedTile=[]
        for i in range(2):
            newPatchTile=self.pick_one_tile()
            self.player1HandedTile.append(
            {'player':1,
            'row':-1,
            'col':-1,
            'element':self.patch_tile[newPatchTile]['element'],
            'pattern':self.patch_tile[newPatchTile]['pattern']
            })

        self.player2HandedTile=[]
        for i in range(2):
            newPatchTile=self.pick_one_tile()
            self.player2HandedTile.append(
            {'player':2,
            'row':-1,
            'col':-1,
            'element':self.patch_tile[newPatchTile]['element'],
            'pattern':self.patch_tile[newPatchTile]['pattern']
            })
        #cat tile
        #catGroup=[]
    def cat_setting(self):
        while(len(self.catGroup)<6):
            randomValue=random.randint(1,6)
            if(randomValue not in self.catGroup):
                self.catGroup.append(randomValue)
        #print(catGroup)
        return self.catGroup

    #find neighbor for specific nodes
    #neighbor_pattern=((-1, 0),(0, -1),(-1, 1),(0, 1),(1, 0),(1, -1))
    def find_neighbor(self,playboard,row,col):
        neighbor = []
        neighbor_patterns = [[-1, 0], [0, -1], [-1, 1], [0, 1], [1, 0], [1, -1]]
        n=6
        neighborNode=[]
        edgeNode=[]
        #print("It's neighbors are:")
        for i in range(n):
            neighbor.append((row + neighbor_patterns[i][0], col + neighbor_patterns[i][1]))
        for i in range(25):
            for j in range(n):
                if(playboard[i]['row']==neighbor[j][0] and playboard[i]['col']==neighbor[j][1]):
                    neighborNode.append(i)
        for i in range(22):
            for j in range(n):
                if(self.edgeTile[i]['row']==neighbor[j][0] and self.edgeTile[i]['col']==neighbor[j][1]):
                    edgeNode.append(i)
        return neighborNode,edgeNode

    def find_neighbor3(self,playboard,row,col):
        neighbor = []
        neighbor_patterns = [[-1, 0], [0, -1], [-1, 1], [0, 1], [1, 0], [1, -1]]
        n=6
        neighborNode=[]
        edgeNode=[]
        for i in range(n):
            neighbor.append((row + neighbor_patterns[i][0], col + neighbor_patterns[i][1]))
        for i in range(25):
            for j in range(n):
                if(playboard[i]['row']==neighbor[j][0] and playboard[i]['col']==neighbor[j][1]):
                    neighborNode.append(i)
        for i in range(22):
            for j in range(n):
                if(self.edgeTile[i]['row']==neighbor[j][0] and self.edgeTile[i]['col']==neighbor[j][1]):
                    edgeNode.append(i)
        return neighborNode,edgeNode
    
    def find_neighbor4(self,playboard,row,col):
        neighbor = []
        neighbor_patterns = [[-1, 0], [0, -1], [-1, 1], [0, 1], [1, 0], [1, -1]]
        n=6
        neighborNode=[]
        edgeNode=[]
        for i in range(n):
            neighbor.append((row + neighbor_patterns[i][0], col + neighbor_patterns[i][1]))
        for i in range(25):
            for j in range(n):
                if(playboard[i]['row']==neighbor[j][0] and playboard[i]['col']==neighbor[j][1]):
                    neighborNode.append(i)
        for i in range(22):
            for j in range(n):
                if(self.edgeTile2[i]['row']==neighbor[j][0] 
                   and self.edgeTile2[i]['col']==neighbor[j][1]):
                    edgeNode.append(i)
        #print("It's neighbors are:")    
        #print(neighborNode)
        return neighborNode,edgeNode


    def find_element_group(self,playboard,playboardIndex,preGrouped):
        preGrouped.add(playboardIndex)
        k,edgeNode=self.find_neighbor3(playboard,playboard[playboardIndex]['row']
                                       ,playboard[playboardIndex]['col'])
        for i in range(len(k)):
            o={k[i]}
            if(playboard[k[i]]['element']==playboard[playboardIndex]['element'] 
               and playboard[playboardIndex]['element']
               !=GameMeta.TILE_ELEMENT['none'] 
               and playboard[playboardIndex]['element']
               !=GameMeta.TILE_ELEMENT['target_base']):
                # if the tile had already in the pregrouped set, then ignore it.
                if(preGrouped.issuperset(o)):
                    continue
                else:
                    preGrouped.add(k[i])
                    #print(preGrouped.issuperset(o))
                    preGrouped=self.find_element_group(playboard,k[i],preGrouped)
            else:
                ...#print("o is not in preGrouped")
        for i in range(len(edgeNode)):
            if(playboard[playboardIndex]['element']
               ==self.edgeTile[edgeNode[i]]['element']):
                preGrouped.add(edgeNode[i]+26)
        return preGrouped
    
    def find_element_group2(self,playboard,playboardIndex,preGrouped):
        preGrouped.add(playboardIndex)
        k,edgeNode=self.find_neighbor4(playboard,playboard[playboardIndex]['row']
                                       ,playboard[playboardIndex]['col'])
        for i in range(len(k)):
            o={k[i]}
            if(playboard[k[i]]['element']==playboard[playboardIndex]['element'] 
               and playboard[playboardIndex]['element']!=GameMeta.TILE_ELEMENT['none'] 
               and playboard[playboardIndex]['element']
               !=GameMeta.TILE_ELEMENT['target_base']):
                # if the tile had already in the pregrouped set, then ignore it.
                if(preGrouped.issuperset(o)):
                    continue
                else:
                    preGrouped.add(k[i])
                    #print(preGrouped.issuperset(o))
                    preGrouped=self.find_element_group2(playboard,k[i],preGrouped)
            else:
                ...#print("o is not in preGrouped")
        for i in range(len(edgeNode)):
            if(playboard[playboardIndex]['element']==self.edgeTile2[edgeNode[i]]['element']):
                preGrouped.add(edgeNode[i]+26)
        return preGrouped

    def rainbow_button(self,playboard):
        elementCount=set()
        groups=[]
        elementPoint=0
        for i in range(len(playboard)):
            blankPreGrouped=set()
            group=self.find_element_group(playboard,i,blankPreGrouped)
            if(group not in groups):
                if(len(group)>=3):
                    groups.append(group)

        for i in range(len(groups)):
            for j in groups[i]:
                if(j<25):#edge tile not count
                    elementCount.add(playboard[j]['element'])
        #print(elementCount)
        if(len(elementCount)==6):
            elementPoint+=3
        #print(elementPoint)
        return elementPoint
    
    def calculate_element_points(self,playboard):
        elementCount=set()
        groups=[]
        elementPoint=0
        for i in range(len(playboard)):
            blankPreGrouped=set()
            group=self.find_element_group(playboard,i,blankPreGrouped)
            if(group not in groups):
                if(len(group)>=3):
                    groups.append(group)

        elementPoint+=len(groups)*3
        for i in range(len(groups)):
            for j in groups[i]:
                if(j<25):#edge not count
                    elementCount.add(playboard[j]['element'])
        if(len(elementCount)==6):
            elementPoint+=3
        return elementPoint
    def sew_button_token(self,place,playboard):
        elementCount=set()
        groups=[]
        blankPreGrouped=set()
        elementCount=set()
        groups=[]
        token_type=0
        group=self.find_element_group(playboard,place,blankPreGrouped)

                

        if(len(group)>=3):
            count=0
            for i in group:
                if(i<25):
                    if(playboard[i]['token']==0):
                        count+=1
                    else:
                        break
                else:
                    count+=1
            if(count==len(group)):
                token_type=1
        
        #print("MILLIE turn:")
        #MILLIE
        blankPreGrouped=set()
        group=self.MILLIE(playboard,place,blankPreGrouped)
        if(len(group)>=3):
            count=0
            for i in group:
                if(i<25):
                    if(playboard[i]['token']==0):
                        count+=1
                    else:
                        break
                else:
                    count+=1
            if(count==len(group)):
                token_type=2

        #print("TIBBIT turn:")
        #TIBBIT
        groups=[]
        blankPreGrouped=set()
        group=self.TIBBIT(playboard,place,blankPreGrouped)
        if(len(group)>=4):
            count=0
            for i in group:
                if(i<25):
                    if(playboard[i]['token']==0):
                        count+=1
                    else:
                        break
                else:
                    count+=1
            if(count==len(group)):
                token_type=3



        #print("COCONUT turn:")
        #COCONUT
        groups=[]
        blankPreGrouped=set()
        group=self.COCONUT(playboard,place,blankPreGrouped)
        if(len(group)>=5):
            count=0
            for i in group:
                if(i<25):
                    if(playboard[i]['token']==0):
                        count+=1
                    else:
                        break
                else:
                    count+=1
            if(count==len(group)):
                token_type=4
        return token_type
    
    
    def calculate_element_points2(self,playboard):
        elementCount=set()
        groups=[]
        elementPoint=0
        for i in range(len(playboard)):
            blankPreGrouped=set()
            group=self.find_element_group2(playboard,i,blankPreGrouped)
            if(group not in groups):
                if(len(group)>=3):
                    groups.append(group)

        elementPoint+=len(groups)*3
        for i in range(len(groups)):
            for j in groups[i]:
                if(j<25):#edge tile not count
                    elementCount.add(playboard[j]['element'])
        if(len(elementCount)==6):
            elementPoint+=3
        return elementPoint

#find cat pattern tile group for beginner
    def MILLIE(self,playboard,playboardIndex,preGrouped):
        preGrouped.add(playboardIndex)
        k,edgeNode=self.find_neighbor3(playboard,playboard[playboardIndex]['row'],playboard[playboardIndex]['col'])
        for i in range(len(k)):
            o={k[i]}
            if(playboard[playboardIndex]['pattern']!=GameMeta.TILE_PATTERN['none'] 
               and playboard[playboardIndex]['pattern']!=GameMeta.TILE_PATTERN['target_base'] 
               and (playboard[k[i]]['pattern']==self.catGroup[0] 
                    or playboard[k[i]]['pattern']==self.catGroup[1])):
                if(playboard[k[i]]['pattern']==playboard[playboardIndex]['pattern']):
                    #print("tile_base[playboardIndex]['pattern']=%d"%playboard[k[i]]['pattern'])
                    # if the tile had already in the pregrouped set, then ignore it.
                    if(preGrouped.issuperset(o)):
                        continue
                    else:
                        preGrouped.add(k[i])
                        #print(preGrouped.issuperset(o))
                        preGrouped=self.MILLIE(playboard,k[i],preGrouped)
            else:
                ...#print("o is not in preGrouped")
        return preGrouped
    def TIBBIT(self,playboard,playboardIndex,preGrouped):
        preGrouped.add(playboardIndex)
        k,edgeNode=self.find_neighbor3(playboard,playboard[playboardIndex]['row'],playboard[playboardIndex]['col'])
        for i in range(len(k)):
            o={k[i]}
            if(playboard[playboardIndex]['pattern']!=GameMeta.TILE_PATTERN['none'] 
               and playboard[playboardIndex]['pattern']!=GameMeta.TILE_PATTERN['target_base'] 
               and (playboard[k[i]]['pattern']==self.catGroup[0] 
                    or playboard[k[i]]['pattern']==self.catGroup[1])):
                if(playboard[k[i]]['pattern']==playboard[playboardIndex]['pattern']):
                    # if the tile had already in the pregrouped set, then ignore it.
                    if(preGrouped.issuperset(o)):
                        continue
                    else:
                        preGrouped.add(k[i])
                        #print(preGrouped.issuperset(o))
                        preGrouped=self.TIBBIT(playboard,k[i],preGrouped)
            else:
                ...#print("o is not in preGrouped")
        return preGrouped
    def COCONUT(self,playboard,playboardIndex,preGrouped):
        preGrouped.add(playboardIndex)
        k,edgeNode=self.find_neighbor3(playboard,playboard[playboardIndex]['row'],playboard[playboardIndex]['col'])
        for i in range(len(k)):
            o={k[i]}
            if(playboard[playboardIndex]['pattern']!=GameMeta.TILE_PATTERN['none'] 
               and playboard[playboardIndex]['pattern']!=GameMeta.TILE_PATTERN['target_base'] 
               and (playboard[k[i]]['pattern']==self.catGroup[0] 
                    or playboard[k[i]]['pattern']==self.catGroup[1])):
                if(playboard[k[i]]['pattern']==playboard[playboardIndex]['pattern']):
                    # if the tile had already in the pregrouped set, then ignore it.
                    if(preGrouped.issuperset(o)):
                        continue
                    else:
                        preGrouped.add(k[i])
                        #print(preGrouped.issuperset(o))
                        preGrouped=self.COCONUT(playboard,k[i],preGrouped)
            else:
                ...#print("o is not in preGrouped")
        return preGrouped

    def calculate_pattern_points(self,playboard):
        elementCount=set()
        groups=[]
        elementPoint=0

        #print("MILLIE turn:")
        #MILLIE
        for i in range(len(playboard)):
            blankPreGrouped=set()
            group=self.MILLIE(playboard,i,blankPreGrouped)
            if(group not in groups):
                if(len(group)>=3):
                    groups.append(group)
        elementPoint+=len(groups)*3

        #print("TIBBIT turn:")
        #TIBBIT
        groups=[]
        for i in range(len(playboard)):
            blankPreGrouped=set()
            group=self.TIBBIT(playboard,i,blankPreGrouped)
            if(group not in groups):
                if(len(group)>=4):
                    groups.append(group)


        elementPoint+=len(groups)*5

        #print("COCONUT turn:")
        #COCONUT
        groups=[]
        for i in range(len(playboard)):
            blankPreGrouped=set()
            group=self.COCONUT(playboard,i,blankPreGrouped)
            if(group not in groups):
                if(len(group)>=5):
                    groups.append(group)

        elementPoint+=len(groups)*7
        #print('pattern points=%d'%elementPoint)
        return elementPoint

    def calculate_goal_points(self,playboard,tileIndex):
        goalPoints=0
        for i in range(len(tileIndex)):
            if(playboard[tileIndex[i]]['goal_type']==0):
                goalPoints+=self.all_different_goal(playboard,tileIndex[i])
            elif(playboard[tileIndex[i]]['goal_type']==1):
                goalPoints+=self.pair_goal(playboard,tileIndex[i])
            elif(playboard[tileIndex[i]]['goal_type']==2):
                goalPoints+=self.triple_goal(playboard,tileIndex[i])
        return goalPoints

    #all different
    def all_different_goal(self,playboard,playboardIndex):
        neighbors,edgeNode=self.find_neighbor(playboard,playboard[playboardIndex]['row'],playboard[playboardIndex]['col'])
        countElement=set()
        countPattern=set()
        for i in range(len(neighbors)):
            if(playboard[neighbors[i]]['element'] not in countElement):
                countElement.add(playboard[neighbors[i]]['element'])
                #print("element:%d"%playboard[neighbors[i]]['element'])

            if(playboard[neighbors[i]]['pattern'] not in countPattern):
                countPattern.add(playboard[neighbors[i]]['pattern'])
                #print(playboard[neighbors[i]]['pattern'])
        if(len(countElement)==6 and len(countPattern)==6):
            #print('return 15')
            return 15
        elif(len(countElement)==6 or len(countPattern)==6):
            #print('return 10')
            return 10
        else:
            #print('return 0')
            return 0
    #2.2.2
    def pair_goal(self,playboard,playboardIndex):
        neighbors,edgeNode=self.find_neighbor(playboard,playboard[playboardIndex]['row'],playboard[playboardIndex]['col'])
        countElement=[]
        countPattern=[]
        countElementPair=0
        countPatternPair=0
        
        for i in range(len(neighbors)):
            countElement.append(playboard[neighbors[i]]['element'])
            countPattern.append(playboard[neighbors[i]]['pattern'])
        for i in range(1,7):
            countNumber=0
            for j in range(len(countElement)):
                if(i==countElement[j]):
                    countNumber+=1
            if(countNumber==2):
                countElementPair+=1

        for i in range(1,7):
            countNumber=0
            for j in range(len(countPattern)):
                if(i==countPattern[j]):
                    countNumber+=1
            if(countNumber==2):
                countPatternPair+=1
        if(countElementPair==3 and countPatternPair==3):
            return 11
        elif(countElementPair==3 or countPatternPair==3):
            return 7
        else:
            return 0
    #3.3
    def triple_goal(self,playboard,playboardIndex):
        neighbors,edgeNode=self.find_neighbor(playboard,playboard[playboardIndex]['row'],playboard[playboardIndex]['col'])
        countElement=[]
        countPattern=[]
        countElementPair=0
        countPatternPair=0
        for i in range(len(neighbors)):
            countElement.append(playboard[neighbors[i]]['element'])
            countPattern.append(playboard[neighbors[i]]['pattern'])
        for i in range(1,7):
            countNumber=0
            for j in range(len(countElement)):
                if(i==countElement[j]):
                    countNumber+=1
            if(countNumber==3):
                countElementPair+=1
        for i in range(1,7):
            countNumber=0
            for j in range(len(countPattern)):
                if(i==countPattern[j]):
                    countNumber+=1
            if(countNumber==3):
                countPatternPair+=1
        if(countElementPair==2 and countPatternPair==2):
            return 13
        elif(countElementPair==2 or countPatternPair==2):
            return 7
        else:
            return 0
    
    def possible_moves(self)-> list:
        moves=[]
        possible_place=set()
        for x in range(len(self.tile_base)):
            placeNeighbor,edgeNode=self.find_neighbor(self.tile_base,self.tile_base[x]['row'],self.tile_base[x]['col'])
            if(self.tile_base[x]['element']==0):
                if(len(placeNeighbor)==6):
                    for i in range(len(placeNeighbor)):
                        if(self.tile_base[placeNeighbor[i]]['element']!=0):
                            if(self.tile_base[placeNeighbor[i]]['element']!=7):
                                possible_place.add(x)
                            else:
                                continue
                        else:
                            continue
                else:
                    possible_place.add(x)
            else:
                continue
        for i in range(0,2):#handed tile
            for j in range(0,3):#pick market tile
                for p in possible_place:
                    moves.append((i,j,p))
        return moves
    def possible_moves2(self)-> list:
        moves=[]
        possible_place=set()
        for x in range(len(self.tile_base2)):
            placeNeighbor,edgeNode=self.find_neighbor(self.tile_base2,self.tile_base2[x]['row'],self.tile_base2[x]['col'])
            if(self.tile_base2[x]['element']==0):
                if(len(placeNeighbor)==6):
                    for i in range(len(placeNeighbor)):
                        if(self.tile_base2[placeNeighbor[i]]['element']!=0):
                            if(self.tile_base[placeNeighbor[i]]['element']!=7):
                                possible_place.add(x)
                            else:
                                continue
                        else:
                            continue
                else:
                    possible_place.add(x)
            else:
                continue
        for i in range(0,2):#handed tile
            for j in range(0,3):#pick market tile
                for p in possible_place:
                    moves.append((i,j,p))
        return moves
    
    def pick_one_tile(self):
        p=random.randint(1,107)
        while (p in self.used_patch_tile):
            p=random.randint(1,107)
        self.used_patch_tile.append(p)
        return p
      
    def last_player1_place_tile(self,move):
        self.tile_base[move[2]]['element']=self.player1HandedTile[move[0]]['element']
        self.tile_base[move[2]]['pattern']=self.player1HandedTile[move[0]]['pattern']
        self.tile_base[move[2]]['token']=self.sew_button_token(move[2],self.tile_base)
    def last_player2_place_tile(self,move):
        self.tile_base2[move[2]]['element']=self.player2HandedTile[move[0]]['element']
        self.tile_base2[move[2]]['pattern']=self.player2HandedTile[move[0]]['pattern']
        self.tile_base2[move[2]]['token']=self.sew_button_token(move[2],self.tile_base2)
    def player1_place_tile(self,move):
        self.tile_base[move[2]]['element']=self.player1HandedTile[move[0]]['element']
        self.tile_base[move[2]]['pattern']=self.player1HandedTile[move[0]]['pattern']
        self.player1HandedTile[move[0]]['element']=self.marketTile[move[1]]['element']
        self.player1HandedTile[move[0]]['pattern']=self.marketTile[move[1]]['pattern']
        newPatchTile=self.pick_one_tile()
        self.marketTile[move[1]]['element']=self.patch_tile[newPatchTile]['element']
        self.marketTile[move[1]]['pattern']=self.patch_tile[newPatchTile]['pattern']
    def player2_place_tile(self,move):
        self.tile_base2[move[2]]['element']=self.player2HandedTile[move[0]]['element']
        self.tile_base2[move[2]]['pattern']=self.player2HandedTile[move[0]]['pattern']
        self.player2HandedTile[move[0]]['element']=self.marketTile[move[1]]['element']
        self.player2HandedTile[move[0]]['pattern']=self.marketTile[move[1]]['pattern']
        newPatchTile=self.pick_one_tile()
        self.marketTile[move[1]]['element']=self.patch_tile[newPatchTile]['element']
        self.marketTile[move[1]]['pattern']=self.patch_tile[newPatchTile]['pattern']
        self.round+=1
    def move(self,move):
        if(self.to_play==GameMeta.PLAYERS['one']):
            self.player1_place_tile(move)
            self.tile_base[move[2]]['token']=self.sew_button_token(move[2],self.tile_base)
        elif(self.to_play==GameMeta.PLAYERS['two']):
            self.player2_place_tile(move)
            self.tile_base2[move[2]]['token']=self.sew_button_token(move[2],self.tile_base2)
        self.to_play = GameMeta.PLAYERS['two'] if self.to_play == GameMeta.PLAYERS['one'] else GameMeta.PLAYERS['one']

    @property
    def winner(self) -> int:
        pointsFromElement=0
        pointsFromPattern=0
        pointsFromElement+=self.rainbow_button(self.tile_base)
        for i in range(len(self.tile_base)):
            if(self.tile_base[i]['token']==1):
                pointsFromElement+=3
            elif(self.tile_base[i]['token']==2):
                pointsFromPattern+=3
            elif(self.tile_base[i]['token']==3):
                pointsFromPattern+=5
            elif(self.tile_base[i]['token']==4):
                pointsFromPattern+=7
        pointsFromGoal=self.calculate_goal_points(self.tile_base,(6,13,16))
        pointsTotal=pointsFromPattern+pointsFromElement+pointsFromGoal

        points2FromElement=0
        points2FromPattern=0
        points2FromElement+=self.rainbow_button(self.tile_base2)
        for i in range(len(self.tile_base2)):
            if(self.tile_base2[i]['token']==1):
                points2FromElement+=3
            elif(self.tile_base2[i]['token']==2):
                points2FromPattern+=3
            elif(self.tile_base2[i]['token']==3):
                points2FromPattern+=5
            elif(self.tile_base[i]['token']==4):
                points2FromPattern+=7
        points2FromGoal=self.calculate_goal_points(self.tile_base2,(6,13,16))
        points2Total=points2FromPattern+points2FromElement+points2FromGoal
        if(points2Total>pointsTotal):
            return GameMeta.PLAYERS['two']
        elif(pointsTotal>points2Total):
            return GameMeta.PLAYERS['one']
        elif(points2Total==pointsTotal):
            if(points2FromPattern>pointsFromPattern):
                return GameMeta.PLAYERS['two']
            elif(pointsFromPattern>points2FromPattern):
                return GameMeta.PLAYERS['one']
            elif(pointsFromPattern==points2FromPattern):
                if(points2FromElement>pointsFromElement):
                    return GameMeta.PLAYERS['two']
                elif(pointsFromElement>points2FromElement):
                    return GameMeta.PLAYERS['one']
                elif(points2FromElement==pointsFromElement):
                    return GameMeta.PLAYERS['draw']
                    

    def set_goal_tile(self,playboard):
        playboard[6]['element']=GameMeta.TILE_ELEMENT['target_base']
        playboard[6]['pattern']=GameMeta.TILE_PATTERN['target_base']
        playboard[13]['element']=GameMeta.TILE_ELEMENT['target_base']
        playboard[13]['pattern']=GameMeta.TILE_PATTERN['target_base']
        playboard[16]['element']=GameMeta.TILE_ELEMENT['target_base']
        playboard[16]['pattern']=GameMeta.TILE_PATTERN['target_base']
    def place_goal_tile(self,playboard,tileType,placeNumber):#example:([],(1,0,2),(7,13,16))
        for i in range(len(placeNumber)):
            playboard[placeNumber[i]]['goal_type']=tileType[i]