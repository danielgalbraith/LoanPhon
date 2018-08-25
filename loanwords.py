cons = {'m','F','n','n`','J','N','N\\','p','b','p_d','b_d','t','d','t`','d`','c','J\\','k','g','q','G\\','>\\','?','p\\','B','f','v','T','D','s','z','S','Z','s`','z`','C','j\\','x','G','X','R','X\\','?\\','H\\','<\\','h','h\\','B_o','v\\','r\\','r\\`','j','M\\','B\\','r','R\\','4','r`','K','K\\','l','l`','L','L\\','l\\','W','w','H','s\\','z\\','x\\','ts','dz','tS','dZ','ts\\','dz\\','tK','kp','gb','Nm','O\\','|\\','!\\','=\\','|\\|\\','b_<','d_<','J\\_<','g_<','G\\_<','p_>','t_>','k_>','s_>'}
vow = {'i','y','1','}','M','u','I','Y','I\\','U`','U','e','2','@\\','8','7','o','E','9','@','3','3\\','V','O','{','6','a','&','A','Q'}

#cons_dia = ['_0','=','_?\\','_}','_a','_d','_G','_h','_j','_l','_m','_N','_n','_o','_r','_v','_w','_+','_-']
#vow_dia = ['_"','_/','_0','_\\','`','~','_A','_B','_B_L','_c','_F','_H','_H_T','_k','_L','_M','_O','_o','_q','_R','_R_F','_r','_T','_t','_X','_x']

en_dict = {'m':'m','n':'n','N':'N','p':'p','t':'t','tS':'tS','k':'k','b':'b','d':'d','g':'g','dZ':'tS','f':'f','T':'t','s':'s','S':'S','h':'h','v':'b','D':'d','z':'z','Z':'S','r\\':'r','l':'l','j':'j','w':'w','{':'a','A':'a','Q':'o','O:':'o','I':'i','E':'e','V':'a','U':'u','eI':'ej','@U':'o','i:':'i','u:':'u','aI':'aj','OI':'oja','aU':'aw','Er\\':'er','Ar\\':'ar','Or\\':'or','Ir\\':'ir','E@r\\':'er','u@r\\':'ur','@':'a','@r\\':'ar','i':'i'}
fr_dict = {'m':'m','n':'n','J':'J','p':'p','t':'t','k':'k','b':'b','d':'d','g':'g','f':'f','s':'s','S':'S','v':'b','z':'z','Z':'S','l':'l','j':'j','R':'r','H':'w','w':'w','i':'i','y':'i','u':'u','e':'e','2':'e','E':'e','E:':'e','a':'a','9':'o','@':'a','o':'o','O':'o','A':'a','E~':'an','9~':'an','O~':'on','A~':'on'}
es_dict = {'m':'m','n':'n','J':'J','p':'p','t':'t','k':'k','tS':'tS','b':'b','B':'b','d':'d','D':'d','g':'g','G':'g','f':'f','T':'s','s':'s','j\\':'j','x':'h','X':'h','l':'l','r':'r','4':'r','L':'j','a':'a','e':'e','i':'i','o':'o','u':'u','ai':'aj','au':'aw','ei':'ej','eu':'ew','oi':'oja','w':'u','j':'j'}
de_dict = {'m':'m','n':'n','N':'N','p':'p','t':'t','k':'k','b':'b','d':'d','g':'g','pf':'f','ts':'s','tS':'tS','s':'s','S':'S','z':'z','f':'f','v':'b','C':'S','x':'h','h':'h','j':'j','l':'l','r':'r','I':'i','i:':'i','Y':'u','y:':'i','U':'u','u:':'u','e:':'e','2:':'e','@':'a','o:':'o','E':'e','9':'o','O':'o','a':'a','a:':'a','OY':'oja','aI':'aj','aU':'aw','Ir':'ir','i:r':'ir','Yr':'ur','y:r':'ir','Ur':'ur','u:r':'ur','Er':'er','E:r':'er','e:r':'er','9r':'or','2:r':'er','Or':'or','o:r':'or','ar':'ar','a:r':'ar'}
dictnames = {'en':en_dict,'fr':fr_dict,'es':es_dict,'de':de_dict}

out_codas = {'n','N','m','p','t','k','s','w','j','l','r'}

def translate(word):
    """Function that takes XSAMPA of word, where every phoneme is followed by '.', consults a dictionary where the keys are the input language phonemes and the values are output language phonemes, and returns a string of the output word in the '.'-separated XSAMPA."""
    outword = ""
    phons = get_phons(word)
    global dictname
    for phon in phons:
        # Catch stress:
        if phon[0] == '*':
            outword += '*' + dictname[phon[1:]] + '.'
        else:
            outword += dictname[phon] + '.'
    return outword 

def get_phons(word):
    """Function that takes XSAMPA of word, where every phoneme is followed by '.', and returns a list of the phonemes without the '.' separator and without newline character."""
    phons = word.split('.')
    if phons[-1] == '\n':
        phons.pop()
    return phons

def fix_biphons(inlist):
    """Function that takes as input a list of words in the '.'-separated XSAMPA; for each word, calls get_phons() to get the list of phonemes; iterates over the phonemes, and for each instance of a phoneme consisting of more than one segment, replaces the phoneme at that index with the vowel only, and appends the additional segment(s) immediately following the vowel; returns an output list whose elements are each word in the '.'-separated XSAMPA with the additional segments."""
    outlist = []
    for word in inlist:
        phons = get_phons(word)
        for i, phon in enumerate(phons):
            if len(phon) > 1 and phon[-1] in cons and phon != 'tS':
                # Catch stress:
                if phon[0] == '*':
                    phons[i] = '*' + phon[1]
                else:
                    phons[i] = phon[0]
                phons.insert(i+1, phon[-1])
            # Catch triphthongs:
            elif phon[-2:] == 'ja' or phon[-2:] == 'wa':
                phons[i] = phon[:-2]
                phons.insert(i+1, phon[-2])
                phons.insert(i+2, 'a')
            else:
                continue
        outlist.append('.'.join(phons))
    return outlist

def epenthesis(inlist):
    """Function that takes as input a list of words in the '.'-separated XSAMPA; for each word, calls get_phons() to get the list of phonemes; iterates over the phonemes, and for each instance of an environment for epenthesis, inserts an epenthetic 'a' at the appropriate index; returns an output list whose elements are each word in the '.'-separated XSAMPA with the additional epenthetic vowels."""
    outlist = []
    for word in inlist:
        phons = get_phons(word)
        if len(phons) > 1:
            for i, phon in enumerate(phons):
                # If initial CC, insert epenthetic 'a' -> CaC
                if i == 0:
                    if phon in cons and phons[i+1] in cons:
                        phons.insert(i+1, 'a')     
                # If statements for medial clusters:
                    # If CCV, if C-1 not legit coda, epenthesise 'a' -> CaCV:
                    # If VCC, if C not legit coda, epenthesise 'a' -> VCaC:
                    # If CCC, if C-1 legit coda -> CCaC, else -> CaCC:
                elif i > 0 and i < len(phons)-1:
                    if phon in cons and phons[i-1] in cons and phons[i+1] in vow:
                        if phons[i-1] not in out_codas:
                            phons.insert(i, 'a')
                    elif phon in cons and phons[i-1] in vow and phons[i+1] in cons:
                        if phon not in out_codas:
                            phons.insert(i+1, 'a')
                    elif phon in cons and phons[i-1] in cons and phons[i+1] in cons:
                        if phons[i-1] in out_codas:
                            phons.insert(i+1, 'a')
                        else:
                            phons.insert(i, 'a')
                    else:
                        continue
                # If statements for final clusters:
                    # If VC, if C not legit coda, epenthesise 'a' -> VCa:
                    # If CC, if C-1 legit coda, epenthesise 'a' -> CCa:
                        # Else, if C legit coda -> CaC, else -> CaCa:
                else:
                    if phon in cons and phons[i-1] in vow:
                        if phon not in out_codas or phon in {'y','w'} and phons[i-1] in {'o','*o','u','*u','i','*i'}:
                            phons.append('a')
                    elif phon in cons and phons[i-1] in cons:
                        if phons[i-1] in out_codas:
                            phons.append('a')
                        else:
                            if phon in out_codas:
                                phons.insert(i, 'a')
                            else:
                                phons.insert(i, 'a')
                                phons.append('a')
                    else:
                        continue
        outlist.append('.'.join(phons) + '.')
    return outlist

def assim_rules(inlist):
    """Function that takes as input a list of words in the '.'-separated XSAMPA; for each word, calls get_phons() to get the list of phonemes; iterates over the phonemes, and for each instance of an environment for assimilation, changes the phoneme at the appropriate index; returns an output list whose elements are each word in the '.'-separated XSAMPA with the assimilations."""
    outlist = []
    for word in inlist:
        phons = get_phons(word)
        if len(phons) > 1:
            for i, phon in enumerate(phons):
                if phon == 'm' and phons[i+1] in {'n','t','d','tS'}:
                    phons[i] = 'n'
                elif phon == 'm' and phons[i+1] == 'J' or phon == 'n' and phons[i+1] == 'J':
                    phons[i] = 'J'
                elif phon == 'n' and phons[i+1] in {'m','p','b'}:
                    phons[i] = 'm'
                elif phon == 'n' and phons[i+1] == 'j':
                    phons[i] = ''
                    phons[i+1] = 'J'
                elif phon == 'l' and phons[i+1] == 'r':
                    phons[i] = 'r'
                elif phon == 'r' and phons[i+1] == 'l':
                    phons[i] = 'l'
                else:
                    continue
        outlist.append('.'.join(phons))
    return outlist

# Main body of script
outputlines = []
langcode = input("Enter language code for input file: ")
infile = langcode + "-in"
dictname = dictnames[langcode]

# Open input file and read lines:
with open(infile,'r') as f:
    lines = f.readlines()
    for line in lines:
        outputlines.append(translate(line) + '\n')  # Add translated line to list of output lines
outputlines = fix_biphons(outputlines)    # Fix phonemes consisting of more than one segment
outputlines = epenthesis(outputlines)    # Apply epenthesis rules
outputlines = assim_rules(outputlines)    # Apply assimilation rules

# Open output file and write output lines to file:
with open('out.txt','w') as f2:
    for oline in outputlines:
        print(oline)
        f2.write(oline + '\n')

