#OBd

cc=[]
# print(cc)

# for i in cc:
    # print(i)


# filters indiv string and returns it clean

def indstring(a):
    def semicol1():
        global semi_str, bkc_dict, oleft_dict, toleft_dict, major_list

        bkc = semi_str[0]
        bkc_dict = {"background color":bkc.strip()}

        semi_str = semi_str[1].split('="')

        semi_oleft = semi_str[2]
        semi_toleft = semi_str[1]

        semi_oleft = semi_oleft.split('">')
        semi_oleft[1] = semi_oleft[1].split('</')
        semi_oleft[1] = semi_oleft[1][0]

        oleft_dict = {semi_oleft[0]:semi_oleft[1]}


        semi_toleft = semi_toleft.split('">')
        semi_toleft = semi_toleft[1]
        semi_toleft = semi_toleft.split('<br>')
        semi_toleft = semi_toleft[0]

        toleft_dict = {"texto #OBd":semi_toleft}

        major_list = [bkc_dict,oleft_dict,toleft_dict]

        print(major_list)

    if ';"' in a:
        global a2
        a2 = a
        # a2 is for the semicol2()

        a = a.split(';"',1)
        # for a_idx,i in enumerate(a):
        #     a.remove(a[0])

        a.remove(a[0])
        global aa

        aa = a[0]
        aa = aa.split("background-color:")




    # for b_idx,j in enumerate(aa):
    #     aa.remove(aa[0])

    # aa is a semi def filtered string save as global for future use

    # the problem is that a few strings have a ;" after de #color, and the rest has just a '"' after it
    # since the split is ';"' the rest is not computing..
    def jump():


        sct=False
        # sct = semicolon true, it indicates if the if ';"' was activated
        
        for i in aa:
            if ';"' in i:
                sct=True
        
                global semi_str
                aa.remove(aa[0])
                semi_str = aa[0].split(';"', 1)
                # print('it has ;"   ',i)
                # print('start semicol 1,  for '';"'' filtering ')
                semicol1()
        
        # if it dosent have a ';"' it will exec here:
        def semicol2():
        
            aa2= a2.split("#")
            aa2.remove(aa2[0])
            aa2.remove(aa2[1])
        
            semi2 = aa2[0].split('"', 1)
            global bkc2_dict, toleft2_dict, oleft2_dict
        
            bkc2 = semi2[0]
        
        
            bkc2_dict = {"background #OBd": ("#"+bkc2)}
        
        
            az= a[0].split('"texto #OBd">')
            az = az[1].split('<br>')
            azz=az[0]
        
            toleft2_dict = {"texto #OBd":azz}
        
            az.remove(az[0])
            # print(az)
            az=az[0].split('"codigo #OBd">')
            az.remove(az[0])
            az=az[0].split('</',1)
            oleft2_dict={"codigo #OBd":az[0]}
        
            major_list = [bkc2_dict, oleft2_dict, toleft2_dict]
        
            print(major_list)
        
        if sct == False:
            semicol2()
    
#
indstring(test)

# indstring(test2)
# indstring(test3)
