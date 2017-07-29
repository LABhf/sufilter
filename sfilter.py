# these are debug files
# cant show it...

# this is the empty list for the strf() to append the 'el'
cc=[]
super_list=[]
def r(i):
    # Faster .remove function, for these lists
    i.remove(i[0])

def sp(i,b,c):
    if type(i) == str:
        # print("is str")
        i = i.split(b,c)
    elif type(i) == list:
        # print("is list")
        i = i[0].split(b,c)
    return i


def strf():
    # open string data file
    with open("sdata.txt", encoding='utf8') as infile:
        for strv in infile:
            # print(strv)
            strv = strv.split("<a style=")
            for idx,el in enumerate(strv):
                # print(idx,"#####", el)
                cc.append(el)
    cc.remove(cc[0])
strf()

def listfilter():
    # sorts trough data in cc and execs the indstring function
    for i in cc:
        i = str(i)
        # print(i)
        indstring(i)

def indstring(a):
    def semicoltrue(a):
        global bkc_dict, oleft_dict, toleft_dict, major_list, super_list

        a = a.split(';"', 1)
        ac = a[0].split()
        bkc =ac[1]

        bkc_dict={"background color": bkc}

        a.remove(a[0])

        a = a[0].split('"texto oleft">')
        a.remove(a[0])
        a = a[0].split('<br>')
        toleft=a[0]

        toleft_dict = {"texto oleft": toleft}

        a.remove(a[0])
        a = a[0].split('codigo oleft">')
        a.remove(a[0])
        a = a[0].split('</span>',1)
        oleft = a[0]

        oleft_dict ={"codigo oleft": oleft}

        major_list =[bkc_dict, toleft_dict, oleft_dict]

        # print(major_list)
        super_list.append(major_list)
    # #####################################################################

    def semicolFalse(a):
        global bkc_dict, oleft_dict, toleft_dict, major_list, super_list
        a = sp(a,"#",1)
        r(a)
        a= sp(a,'"',1)
        bkc=a[0]
        bkc_dict = {"background color":("#"+bkc)}

        r(a)
        a = sp(a, '"texto #OBd">',1)
        r(a)
        a = sp(a,"<br>",1 )
        toleft=a[0]
        toleft_dict={"texto #OBd":toleft}
        r(a)

        a = sp(a,'"codigo #OBd">',1)
        r(a)

        a = sp(a,"</span>",1)
        oleft=a[0]

        oleft_dict={"codigo #OBd":oleft}

        major_list = [bkc_dict, toleft_dict, oleft_dict]
        # print(major_list)

        super_list.append(major_list)






    # this is the semicol identifier for the semicol functions ..
    if ';"'in a:
        # print('there is a semicol  ')
        semicoltrue(a)
    else:
        # print("no semicol  ")
        semicolFalse(a)

listfilter()

for idx, el in enumerate(super_list):
    print(idx, el)

def ask():

    nome = input("Nome da cor:")
    nome =str(nome)
    nome = nome.lower()

    for idx,el in enumerate(super_list):
        # print(idx, el)
        templ = []
        for subel in el:
            templ.append(subel)

        for i in templ:
            if 'texto #OBd' in i:
                # print(i['texto oleft'])
            #     ####################
                zi=i['texto #OBd']

                if nome in zi.lower():
                    print("")
                    print("Correspondencia de ",nome," em:")
                    print(templ)
                else:
                    pass

    input("#                    #")
    print("")
    ask()
ask()

