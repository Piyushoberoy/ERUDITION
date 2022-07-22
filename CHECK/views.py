from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from gingerit.gingerit import GingerIt

def CHECK(request):
    if request.method=="POST":
        return render(request,'CHECK/CHECK.html')
    return redirect("/")

def CORRECT(request):
    txt = request.POST.get('text', 'This feature will be available soon.')
    parser = GingerIt()
    x = parser.parse(txt)['result']
    y = parser.parse(txt)['text']
    # z = parser.parse(txt)['corrections']
    # print(z)
    # for a in z:
    #     d=a
    #     for key in d:
    #         if key=='start':
    #             r=d[key]
    #             e=txt[r]
    #             print(e)

    out = {'text': x,'org':y}
    return render(request,'CHECK/CORRECT.html',out)

#Correction
'''
def Analyse1(request):
    txt = request.GET.get('text', 'default')
    S= txt.split('.')
    n = ''
    for a in S:
        a = a.strip()
        n += a.capitalize() + '. '
    n = n[:-2]
    print(n)
    l = txt.split()
    N=''
    for A in l:
        if A=='yes':
            A=A.strip()
            N+=A+', '
        

        #else:
        #    N+=A+' '
    #print(N)
    NW=''
    ''    x=int(input("Please enter number of places in text:"))
        lst=[]
        for a in range(0,x):
            y=input('Enter place in your text:')
            lst.append(y)
        print(lst)
    ''
    for B in l:
        print(B)
        y=B[:1]
        Y=B[1:2]
        if 'a' in y or 'e' in y or 'i' in y or 'o' in y or 'u' in y:
            if 'am' in B or 'are' in B or 'is' in B or 'in' in B or 'on' in B or 'boys' in B or 'girls' in B or 'i' in B or 'I' in B:
                NW+=B+' '
                ''d = PyDictionary()
                x = input('Enter word:')
                meanings = d.meaning(x)
                try:
                    if 'Noun' in meanings and 'Verb' in meanings:
                        print('do everything')
                    elif 'Noun' in meanings:
                        print('do something')
                    elif 'Verb' in meanings:
                        print('do something else')
                except:
                    y = x.capitalize()
                    print(y)
                ''
            #elif B in lst:
            #    print(123)
            else:
                NW=NW+'an '+B+' '

        else:
            nlp = spacy.load("en_core_web_sm")
            nlp_var = nlp(B)
            for i in nlp_var.ents:
                print(i, i.label_, i.label)
                if 'ORG' in i.label_ or 'PERSON' in i.label_:
                    B.capitalize()
                print(i)
            NW=NW+B+' '
    print(NW)

    ''
    #SPLIT COMMAND DEVELOP BY PIYUSH
    s=''
    l=[]
    for a in txt:
        if a==' ' or a=='\n':
            l.append(s)
            s=''
        else:
            if a=='\r':
                pass
            else:
                s+=a
    print(l)
    for A in l:
        if '.' in A:
    ''
'''