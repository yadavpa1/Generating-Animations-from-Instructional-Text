locations_dict = {}
locations_dict['AB_1'] =              (7.7982,-10.541,10.128)
locations_dict['AB_2'] =              (7.5795,-10.5458,10.1283)
locations_dict['AB_3'] =              (7.56995,-10.7788,10.1288)
locations_dict['AB_4'] =              (7.79198,-10.7686,10.1281)
locations_dict['AB_5'] =              (7.33952,-10.7795,10.1278)
locations_dict['A_1'] =               (7.80082,-11.0242,10.1276)
locations_dict['A_2'] =               (7.58226,-11.0255,10.1278)
locations_dict['A_3'] =               (7.34331,-11.0229,10.1267)
locations_dict['A_4'] =               (7.34159,-10.5585,10.1282)
locations_dict['Blender'] =           (7.8145,-10.191,10.384)
locations_dict['Casserole'] =         (10.513,-8.5701,10.137)
locations_dict['Pan'] =   (9.90919,-8.72713,10.141)
locations_dict['CuttingBoard'] =      (10.0259,-8.48764,10.1334)
locations_dict['Fire'] =              (8.75604,-8.82074,10.1531)
locations_dict['Knife'] =             (9.82127,-8.49234,10.1476)
locations_dict['Oil'] =               (9.8948,-8.9422,10.134)
locations_dict['Sink'] =              (7.5682,-9.2169,10.088)
locations_dict['Spatula'] =           (10.2736,-8.46861,10.1423)
locations_dict['Stove'] =             (8.7563,-8.8199,10.26)
locations_dict['Table_Side'] =        (9.2399,-9.4736,10.014)
locations_dict['Water'] =             (10.2045,-8.9454,10.1455)
locations_dict['AAA']=(10,20,30)
ingredient_state_dict = {}
ingredient_state_dict['bowl'] = ['tea','coffee','cheese','rice','masala']
ingredient_state_dict['solid']= ['onion','fish','potato','tomato','chilly']
def preprocess_tuples(res):
    list = []
    for tuple in res:
        new_tuple = (tuple[0].upper(),tuple[1].lower())
        list.append(new_tuple)          
    print(list)
    bowl_counter = 0
    solid_counter = 0
    final_list = []
    items_dict = {}
    for tuple in list:
        flag=0
        flag1 = 1
        for state,item_list in ingredient_state_dict.items():
            my_tuple=()
            if(tuple[1] in item_list and state=='bowl'):
                flag=1
                if(tuple[1] not in items_dict):
                    bowl_counter+=1;
                    if(bowl_counter>5):
                        print("No more bowls left in the kitchen.")
                    else:
                        items_dict[tuple[1]]='AB_'+str(bowl_counter)
                        my_tuple=(tuple[0],'AB_'+str(bowl_counter)) 
                else:
                    my_tuple=(tuple[0],items_dict[tuple[1]])
                                    
            elif(tuple[1] in item_list and state=='solid'):
                flag=1
                if(tuple[1] not in items_dict):
                    solid_counter+=1;
                    if(solid_counter>4):
                        print("No more solid items left in the kitchen.")
                    else:
                        items_dict[tuple[1]]='A_'+str(solid_counter)
                        my_tuple=(tuple[0],'A_'+str(solid_counter))
                else:
                    my_tuple=(tuple[0],items_dict[tuple[1]])
            else:
                for i in locations_dict:
                    if(tuple[1].lower()==i.lower() and flag1==1):
                        my_tuple=(tuple[0],i)
                        flag1=2
            if(flag==1 or flag1==2):
                final_list.append(my_tuple)
                flag=0
                flag1=3
    return (final_list,items_dict)

a,d = preprocess_tuples([('Take','AAA'),('Add','Water'),('Fry','fish'),('Add','oil'),('fry','FISH'),('boil','fish'),('add','onion'),('Take','CASSEROLE')])
print(a)
print("=================================")
print(d)
