###########################################
"""HERE WE WILL TEST EVERYTHING IS WORKING PROPERLY OR NOT"""
from grps import run
def runner(programm):
    result,error = run("UNTITLED",programm)
    error = error.show_error() if error else error
    return result if result else error
#############################################
#                  TOPICS
#         @TESTS 
#
#       ### INT FORMATION        
#         @1_0 Number 
#                         @1_1 show(Number)                          
#                         @1_2 show(int)  
#                                  @1_3 Arthematic + 
#                                  @1_4 Arthematic - 
#                                  @1_5 Arthematic *
#                                  @1_6 Arthematic / 
#                                  @1_7 Arthematic //
#                                  @1_8 Arthematic _/ 
#                                  @1_9 Arthematic <<
#                               @1_10 Logical  == 
#                               @1_10 Logical  <
#                               @1_10 Logical  >
#                               @1_10 Logical  <= 
#                               @1_10 Logical  >= 
##############################################################
    
#       ### STR FORMATION        
#         @2_0 STRING
#                    @2_1 show(STRING)  
#                          @2_2 Arthematic + 
#                          @2_3 Arthematic *                           
#                          @2_4 Logical  == 
#                          @2_5 Logical  <         
#                          @2_6 Logical  <=          [ > , <= , >=      Reapeated as above....]
#                    @2_7 show(str)
#
#                    @ method
#                              @2_8 find()
#                              @2_9 join()
    
#############################################################
    

###########################################################
#          
#       ### LIST FORMATION       
#         @3_0 Arthematic + 
#              @3_1  Logical  ==
#                                    @ method 
#                                          @3_2 append()
#                                          @3_3 pop()
#              @3_4 SLICING-
    
#       ### TUPLES FORMATION
#        Later...
#
#       ### VARIABLE ASSIGN
#         -1 single var -2 multiple var -3 pack var -4 unpack 
    
#####################################################
#       ###  FUNCTIONS
#    
#                     UNDER DEVELOPMENT
#       ### CLASSES
#                     UNDER DEVELOPMENT
#
#################################################

tests = []
#####################                        ##########################
#    INT                                     #     output
#####################                        ##########################
 
test1_0 = "45"                                #   >>        
tests.append(test1_0)
                     
test1_1 = "show(45)"                          #   >> 45
tests.append(test1_1)

test1_2 = "show(int)"                         #   >> GRPS OBJ <class 'int'>
tests.append(test1_2)

test1_3 = "show(12+5)"                        #   >> 17
tests.append(test1_3)

test1_4 = "show(12-5)"                        #   >> 7
tests.append(test1_4)

test1_5 = "show(12*5)"                        #   >> 60
tests.append(test1_5)

test1_6 = "show(12^5)"                        #   >>  248832
tests.append(test1_6)

test1_7 = "show(12/5)"                        #   >> 2.4
tests.append(test1_7)

test1_8 = "show(12_/5)"                       #   >> 2               [ _/ means question of division]
tests.append(test1_8)

test1_9 = "show(12<<5)"                       #   >> 384             [ << means bitwise left shift  ]
tests.append(test1_9)

test1_10 = "show(12>>5)"                      #   >> 0               [ >> means bitwise right shift ]
tests.append(test1_10)

test1_11 = "show(type(4) == int)"             #   >>  True
tests.append(test1_11)

test1_12 = "show(12*5 > 5+67)"                #   >>  False          [  60 > 72         False      ]
tests.append(test1_12)

test1_13 = "show(2^4 < 3^2)"                  #   >>   False         [  16 < 9          False      ]
tests.append(test1_13)

test1_14 = "show(2*4 <= 12)"                  #   >>   True        
tests.append(test1_14)

test1_15 = "show(5+5 >= 23)"                  #   >>   False         
tests.append(test1_15)

test1_16 = "show(2+45 != 23)"                 #   >>   True         
tests.append(test1_16)

test2_0 = " 'hello' "                         #   >>   hello       
tests.append(test2_0)

test2_1 = "show('hello')"                     #   >>   hello       
tests.append(test2_1)

test2_2 = "show('hello '+' World!')"          #   >>   hello  World!
tests.append(test2_2)

test2_3 = "show('hello '*3)"                  #   >>   hello hello hello
tests.append(test2_3)

test2_4 = "show('a'== 'a')"                    #   >>   True
tests.append(test2_4)

test2_5 = "show('b'< 'a')"                     #   >>   False
tests.append(test2_5)

test2_6 = "show('b'<= 'a')"                    #   >>   False
tests.append(test2_6)

test2_7 = "show(str)"                          #   >>   GRPS OBJ <class 'str'>
tests.append(test2_7)

test2_8 = "STR = 'can you find x'; show(STR.find('x'))"            #   >>   13
tests.append(test2_8)

test2_9 = "x = [1,2,3];('dsf').join(x)"                            #   FAILED 

test3_0 = "age = ['My','age'] + ['is',5   ];show(age)"             #   [My, age, is, 5]
tests.append(test3_0)

test3_1 = "['My_ID',5] == ['My_ID',5];"                            #    True
tests.append(test3_1)

test3_2 = "x = ['My_ID',5]; y = x.append('name');  show(x)"        #    [My_ID, 5, 'name']
tests.append(test3_2)

test3_3 = "x = ['My_ID',5]; removed = x.pop();  show(removed);show(x)"            #  removed = 5 \n x =  [My_ID]
tests.append(test3_3)
 
test3_4 = "x = ['My_School','name','is','NSMB']; y = x[2:];show(y==['is','NSMB'])"            #  True
tests.append(test3_4)

test3_5 = "x = ['My_School','name','is','NSMB']; y = x[2:];show(y==['is','NSMB'])"            #  True
tests.append(test3_5)

test3_6 = "x = ['My_School']; y = is_list(x);show(y)"                                         #  True
tests.append(test3_6)

test4_0 = "fun x(name,id)// ;data = [name,id];//data; show( x('Rajeev',42342)); "                        #  True
tests.append(test4_0)


test5_0 = "import_ xmap;show(encode('This is a encoded message you can not read this'))"             #   ᮬᯀᯁᯋ᭸ᯁᯋ᭸᮹᭸ᮽᯆᮻᯇᮼᮽᮼ᭸ᯅᮽᯋᯋ᮹ᮿᮽ᭸ᯑᯇᯍ᭸ᮻ᮹ᯆ᭸ᯆᯇᯌ᭸ᯊᮽ᮹ᮼ᭸ᯌᯀᯁᯋ
tests.append(test5_0)

test5_1 = "import_ xmap;show(decode('ᮬᯀᯁᯋ᭸ᯁᯋ᭸᮹᭸ᮽᯆᮻᯇᮼᮽᮼ᭸ᯅᮽᯋᯋ᮹ᮿᮽ᭸ᯑᯇᯍ᭸ᮻ᮹ᯆ᭸ᯆᯇᯌ᭸ᯊᮽ᮹ᮼ᭸ᯌᯀᯁᯋ'))"             #   This is a encoded message you can not read this
tests.append(test5_1)

test6_0 = "import_ random_ ; show(random(100))"             #  Random value generator
tests.append(test3_0)

test6_1 = "import_ random_ ; show(rand_range(50,100))"             #  Random value generator
tests.append(test6_1)

test7_0 = "fun CapitalOnly(text)// ;show('after capitalize :'+text.capitalize());//;show(CapitalOnly('delhi'))"             #  True
tests.append(test7_0)

test8_0 = "show(type(4) == int); "             #  Class type
tests.append(test8_0)

test9_0 = "FOR i in (8,9):;show(i);END"

test9_1 = "import_ random_; 


# Testing all basic scripts 

import time
for i in tests:
    print(f"\n\n\n\nrunning script:\n{i}")
    time.sleep(1)
    print(f"Output deteted")
    print(f"{runner(i)}")
    time.sleep(2)
