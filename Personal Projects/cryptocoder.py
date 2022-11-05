# Casual Coded Correspondence: The Project

#         xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!
    
#     This message has an offset of 10. Can you decode it?

alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = "!,.:?' "
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
decoded_message = ""
for letter in message:
    if not letter in punctuation:
        letter_decoded = alphabet.find(letter)
        decoded_message += alphabet[(letter_decoded + 10) % 26]
    else:
        decoded_message += letter
print(decoded_message)

#Output: hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!

alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = "!,.:?' "
message = "Hey friend, this is pretty cool! I was able to decode the message using alphabet.find and indexing!"
decoded_message = ""
for letter in message:
    if not letter in punctuation:
        letter_decoded = alphabet.find(letter)
        decoded_message += alphabet[(letter_decoded - 10) % 26]
    else:
        decoded_message += letter
print(decoded_message)

# Output: puo vhyudt, jxyi yi fhujjo seeb! p mqi qrbu je tusetu jxu cuiiqwu kiydw qbfxqruj.vydt qdt ydtunydw!


#
# Define functions to automate this process
#

alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = "!,.:?' "
message = ""

def decoder(message, offset):
    decoded_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_decoded = alphabet.find(letter)
            decoded_message += alphabet[(letter_decoded + offset) % 26]
        else:
            decoded_message += letter
    return decoded_message

def coder(message, offset):
    coded_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_coded = alphabet.find(letter)
            coded_message += alphabet[(letter_coded - offset) % 26]
        else:
            coded_message += letter
    return coded_message

#Unknown offset of the cypher, brute force through using a range of numbers
def decoder(message, offset):
    decoded_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_decoded = alphabet.find(letter)
            decoded_message += alphabet[(letter_decoded + offset) % 26]
        else:
            decoded_message += letter
    return decoded_message

message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

for i in range(0,31):
    print(decoder(message, int(i)))

# Output:
# vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.
# wigjonylm bupy lyhxylyx uff iz nbymy ifx wcjbylm um ivmifyny. qy'ff bupy ni lyuffs mnyj oj iol augy cz qy quhn ni eyyj iol gymmuaym muzy.
# xjhkpozmn cvqz mziyzmzy vgg ja ocznz jgy xdkczmn vn jwnjgzoz. rz'gg cvqz oj mzvggt nozk pk jpm bvhz da rz rvio oj fzzk jpm hznnvbzn nvaz.
# ykilqpano dwra najzanaz whh kb pdaoa khz yeldano wo kxokhapa. sa'hh dwra pk nawhhu opal ql kqn cwia eb sa swjp pk gaal kqn iaoowcao owba.
# zljmrqbop exsb obkaboba xii lc qebpb lia zfmebop xp lyplibqb. tb'ii exsb ql obxiiv pqbm rm lro dxjb fc tb txkq ql hbbm lro jbppxdbp pxcb.
# amknsrcpq fytc pclbcpcb yjj md rfcqc mjb agnfcpq yq mzqmjcrc. uc'jj fytc rm pcyjjw qrcn sn msp eykc gd uc uylr rm iccn msp kcqqyecq qydc.
# bnlotsdqr gzud qdmcdqdc zkk ne sgdrd nkc bhogdqr zr narnkdsd. vd'kk gzud sn qdzkkx rsdo to ntq fzld he vd vzms sn jddo ntq ldrrzfdr rzed.
### ********** This is the one!!! offset is 7 ********** computers have rendered all of these old ciphers as obsolete. we'll have to really step up our game if we want to keep our messages safe.
# dpnqvufst ibwf sfoefsfe bmm pg uiftf pme djqifst bt pctpmfuf. xf'mm ibwf up sfbmmz tufq vq pvs hbnf jg xf xbou up lffq pvs nfttbhft tbgf.
# eqorwvgtu jcxg tgpfgtgf cnn qh vjgug qnf ekrjgtu cu qduqngvg. yg'nn jcxg vq tgcnna uvgr wr qwt icog kh yg ycpv vq mggr qwt oguucigu uchg.
# frpsxwhuv kdyh uhqghuhg doo ri wkhvh rog flskhuv dv revrohwh. zh'oo kdyh wr uhdoob vwhs xs rxu jdph li zh zdqw wr nhhs rxu phvvdjhv vdih.
# gsqtyxivw lezi virhivih epp sj xliwi sph gmtlivw ew sfwspixi. ai'pp lezi xs vieppc wxit yt syv keqi mj ai aerx xs oiit syv qiwwekiw weji.
# htruzyjwx mfaj wjsijwji fqq tk ymjxj tqi hnumjwx fx tgxtqjyj. bj'qq mfaj yt wjfqqd xyju zu tzw lfrj nk bj bfsy yt pjju tzw rjxxfljx xfkj.
# iusvazkxy ngbk xktjkxkj grr ul znkyk urj iovnkxy gy uhyurkzk. ck'rr ngbk zu xkgrre yzkv av uax mgsk ol ck cgtz zu qkkv uax skyygmky yglk.
# jvtwbalyz ohcl yluklylk hss vm aolzl vsk jpwolyz hz vizvslal. dl'ss ohcl av ylhssf zalw bw vby nhtl pm dl dhua av rllw vby tlzzhnlz zhml.
# kwuxcbmza pidm zmvlmzml itt wn bpmam wtl kqxpmza ia wjawtmbm. em'tt pidm bw zmittg abmx cx wcz oium qn em eivb bw smmx wcz umaaioma ainm.
# lxvydcnab qjen anwmnanm juu xo cqnbn xum lryqnab jb xkbxuncn. fn'uu qjen cx anjuuh bcny dy xda pjvn ro fn fjwc cx tnny xda vnbbjpnb bjon.
# mywzedobc rkfo boxnobon kvv yp droco yvn mszrobc kc ylcyvodo. go'vv rkfo dy bokvvi cdoz ez yeb qkwo sp go gkxd dy uooz yeb wocckqoc ckpo.
# nzxafepcd slgp cpyopcpo lww zq espdp zwo ntaspcd ld zmdzwpep. hp'ww slgp ez cplwwj depa fa zfc rlxp tq hp hlye ez vppa zfc xpddlrpd dlqp.
# oaybgfqde tmhq dqzpqdqp mxx ar ftqeq axp oubtqde me aneaxqfq. iq'xx tmhq fa dqmxxk efqb gb agd smyq ur iq imzf fa wqqb agd yqeemsqe emrq.
# pbzchgref unir eraqrerq nyy bs gurfr byq pvcuref nf bofbyrgr. jr'yy unir gb ernyyl fgrc hc bhe tnzr vs jr jnag gb xrrc bhe zrffntrf fnsr.
# qcadihsfg vojs fsbrsfsr ozz ct hvsgs czr qwdvsfg og cpgczshs. ks'zz vojs hc fsozzm ghsd id cif uoas wt ks kobh hc yssd cif asggousg gots.
# rdbejitgh wpkt gtcstgts paa du iwtht das rxewtgh ph dqhdatit. lt'aa wpkt id gtpaan hite je djg vpbt xu lt lpci id ztte djg bthhpvth hput.
# secfkjuhi xqlu hudtuhut qbb ev jxuiu ebt syfxuhi qi eriebuju. mu'bb xqlu je huqbbo ijuf kf ekh wqcu yv mu mqdj je auuf ekh cuiiqwui iqvu.
# tfdglkvij yrmv iveuvivu rcc fw kyvjv fcu tzgyvij rj fsjfcvkv. nv'cc yrmv kf ivrccp jkvg lg fli xrdv zw nv nrek kf bvvg fli dvjjrxvj jrwv.
# ugehmlwjk zsnw jwfvwjwv sdd gx lzwkw gdv uahzwjk sk gtkgdwlw. ow'dd zsnw lg jwsddq klwh mh gmj ysew ax ow osfl lg cwwh gmj ewkksywk ksxw.
# vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.
# wigjonylm bupy lyhxylyx uff iz nbymy ifx wcjbylm um ivmifyny. qy'ff bupy ni lyuffs mnyj oj iol augy cz qy quhn ni eyyj iol gymmuaym muzy.
# xjhkpozmn cvqz mziyzmzy vgg ja ocznz jgy xdkczmn vn jwnjgzoz. rz'gg cvqz oj mzvggt nozk pk jpm bvhz da rz rvio oj fzzk jpm hznnvbzn nvaz.
# ykilqpano dwra najzanaz whh kb pdaoa khz yeldano wo kxokhapa. sa'hh dwra pk nawhhu opal ql kqn cwia eb sa swjp pk gaal kqn iaoowcao owba.
# zljmrqbop exsb obkaboba xii lc qebpb lia zfmebop xp lyplibqb. tb'ii exsb ql obxiiv pqbm rm lro dxjb fc tb txkq ql hbbm lro jbppxdbp pxcb.

#Test the offset to verify our brute force worked:
print(decoder(message, 7))

#######################################################################################
############################# Move on to stronger ciphers #############################
#######################################################################################


alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = "!,.:?' "

def keyword_decoder(message, keyword):
    letter_place = 0
    keyword_final = ''
    for i in range(0,len(message)):
        if message[i] in punctuation:
            keyword_final += message[i]
        else:
            keyword_final += keyword[letter_place]
            letter_place = (letter_place+1)%len(keyword)
    decoded_message = ''
    for i in range(0,len(message)):
        if not message[i] in punctuation:
            pl = alphabet.find(message[i]) - alphabet.find(keyword_final[i])
            decoded_message += alphabet[pl % 26]
        else:
            decoded_message += message[i]
    return decoded_message

def keyword_encoder(message, keyword):
    letter_place = 0
    keyword_final = ''
    for i in range(0,len(message)):
        if message[i] in punctuation:
            keyword_final += message[i]
        else:
            keyword_final += keyword[letter_place]
            letter_place = (letter_place+1)%len(keyword)
    encoded_message = ''
    for i in range(0,len(message)):
        if not message[i] in punctuation:
            pl = alphabet.find(message[i]) - alphabet.find(keyword_final[i])
            decoded_message += alphabet[pl % 26]
        else:
            decoded_message += message[i]
    return decoded_message


def keyword_encoder(message, keyword):
    letter_place = 0
    keyword_final = ''
    for i in range(0,len(message)):
        if message[i] in punctuation:
            keyword_final += message[i]
        else:
            keyword_final += keyword[letter_place]
            letter_place = (letter_place+1)%len(keyword)
    encoded_message = ''
    for i in range(0,len(message)):
        if message[i] in punctuation:
            encoded_message += message[i]
        else:
            pl = alphabet.find(message[i]) + alphabet.find(keyword_final[i])
            encoded_message += alphabet[pl % 26]
    #Uncomment to see the keyword placement
    print(keyword_final)
    return encoded_message

message = "This is a test of the encoder. By encoding this, you can see a few things: Whether you can decode with the decoder, and if punctuation effects your message!"
keyword = "bigkeywordtoday"

encoded_message = keyword_encoder(message, keyword)
print(encoded_message)

print(keyword_decoder(encoded_message, keyword))