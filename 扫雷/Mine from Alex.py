import pygame
import time
import random
import sys

display_width = 700
display_height = 500

FPS = 60

size = [20,20]
pygame.init()
pygame.mixer.init()

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Mine clearance')

clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
purple = (120,65,255)
bluegreen = (40,164,159)
grey = (192,192,192)
light_grey = (214,214,214)

red = (170,0,0)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (34,177,76)
light_green = (0,255,0)

global youwin
mine_number = str("Mine number:")
youwin = str("You win!")


global gametime
global gameclock
gametime = str("Time:")
gameclock = 0

lossquit = str("QUIT")

score_a = random.randint(-1,5)
score_b = random.randint(-1,5)
score_c = random.randint(-1,5)
score_d = random.randint(-1,5)
score_e = random.randint(-1,5)
score_f = random.randint(-1,5)
score_g = random.randint(-1,5)
score_h = random.randint(-1,5)
score_i = random.randint(-1,5)
score_j = random.randint(-1,5)
score_k = random.randint(-1,5)
score_l = random.randint(-1,5)
score_m = random.randint(-1,5)
score_n = random.randint(-1,5)
score_o = random.randint(-1,5)
score_p = random.randint(-1,5)
score_q = random.randint(-1,5)
score_r = random.randint(-1,5)
score_s = random.randint(-1,5)
score_t = random.randint(-1,5)
score_u = random.randint(-1,5)
score_v = random.randint(-1,5)
score_w = random.randint(-1,5)
score_x = random.randint(-1,5)
score_y = random.randint(-1,5)
score_z = random.randint(-1,5)
score_bc = random.randint(-1,5)
score_bd = random.randint(-1,5)
score_aa = random.randint(-1,5)
score_ab = random.randint(-1,5)
score_ac = random.randint(-1,5)
score_ad = random.randint(-1,5)
score_ia = random.randint(-1,5)
score_ib = random.randint(-1,5)
score_ic = random.randint(-1,5)
score_id = random.randint(-1,5)
score_ja = random.randint(-1,5)
score_jb = random.randint(-1,5)
score_jc = random.randint(-1,5)
score_jd = random.randint(-1,5)
score_ae = random.randint(-1,5)
score_af = random.randint(-1,5)
score_ag = random.randint(-1,5)
score_be = random.randint(-1,5)
score_bf = random.randint(-1,5)
score_bg = random.randint(-1,5)
score_ce = random.randint(-1,5)
score_cf = random.randint(-1,5)
score_cg = random.randint(-1,5)
score_de = random.randint(-1,5)
score_df = random.randint(-1,5)
score_dg = random.randint(-1,5)
score_ee = random.randint(-1,5)
score_ef = random.randint(-1,5)
score_eg = random.randint(-1,5)
score_fe = random.randint(-1,5)
score_ff = random.randint(-1,5)
score_fg = random.randint(-1,5)
score_ge = random.randint(-1,5)
score_gf = random.randint(-1,5)
score_gg = random.randint(-1,5)
score_he = random.randint(-1,5)
score_hf = random.randint(-1,5)
score_hg = random.randint(-1,5)
score_ie = random.randint(-1,5)
score_if = random.randint(-1,5)
score_ig = random.randint(-1,5)
score_je = random.randint(-1,5)
score_jf = random.randint(-1,5)
score_jg = random.randint(-1,5)
score_ah = random.randint(-1,5)
score_ai = random.randint(-1,5)
score_aj = random.randint(-1,5)
score_bh = random.randint(-1,5)
score_bi = random.randint(-1,5)
score_bj = random.randint(-1,5)
score_ch = random.randint(-1,5)
score_ci = random.randint(-1,5)
score_cj = random.randint(-1,5)
score_dh = random.randint(-1,5)
score_di = random.randint(-1,5)
score_dj = random.randint(-1,5)
score_eh = random.randint(-1,5)
score_ei = random.randint(-1,5)
score_ej = random.randint(-1,5)
score_fh = random.randint(-1,5)
score_fi = random.randint(-1,5)
score_fj = random.randint(-1,5)
score_gh = random.randint(-1,5)
score_gi = random.randint(-1,5)
score_gj = random.randint(-1,5)
score_hh = random.randint(-1,5)
score_hi = random.randint(-1,5)
score_hj = random.randint(-1,5)
score_ih = random.randint(-1,5)
score_ii = random.randint(-1,5)
score_ij = random.randint(-1,5)
score_jh = random.randint(-1,5)
score_ji = random.randint(-1,5)
score_jj = random.randint(-1,5)



'''
print(score_a)
print(score_b)
print(score_c)
print(score_d)
print(score_e)
print(score_f)
print(score_g)
print(score_h)
print(score_i)
print(score_j)
print(score_k)
print(score_l)
print(score_m)
print(score_n)
print(score_o)
print(score_p)
print(score_q)
print(score_r)
print(score_s)
print(score_t)
print(score_u)
print(score_v)
print(score_w)
print(score_x)
print(score_y)
print(score_z)
print(score_bc)
print(score_bd)
print(score_aa)
print(score_ab)
print(score_ac)
print(score_ad)
print(score_ia)
print(score_ib)
print(score_ic)
print(score_id)
print(score_ie)
print(score_if)
print(score_ig)
print(score_ih)
print(score_ii)
print(score_ij)
print(score_ae)
print(score_af)
print(score_ag)
print(score_ah)
print(score_ai)
print(score_aj)
print(score_be)
print(score_bf)
print(score_bg)
print(score_bh)
print(score_bi)
print(score_bj)
print(score_ce)
print(score_cf)
print(score_cg)
print(score_ch)
print(score_ci)
print(score_cj)
print(score_de)
print(score_df)
print(score_dg)
print(score_dh)
print(score_di)
print(score_dj)
print(score_ee)
print(score_ef)
print(score_eg)
print(score_eh)
print(score_ei)
print(score_ej)
print(score_fe)
print(score_ff)
print(score_fg)
print(score_fh)
print(score_fi)
print(score_fj)
print(score_ge)
print(score_gf)
print(score_gg)
print(score_gh)
print(score_gi)
print(score_gj)
print(score_he)
print(score_hf)
print(score_hg)
print(score_hh)
print(score_hi)
print(score_hj)
print(score_ja)
print(score_jb)
print(score_jc)
print(score_jd)
print(score_je)
print(score_jf)
print(score_jg)
print(score_jh)
print(score_ji)
print(score_jj)

'''

global minefindb 
global minefindc 
global minefindd
global minefinde
global minefindf
global minefinda
global minefindg
global minefindh
global minefindi
global minefindj
global minefindk
global minefindl
global minefindm
global minefindn
global minefindo
global minefindp
global minefindq
global minefindr
global minefinds
global minefindt
global minefindu
global minefindv
global minefindw
global minefindx
global minefindy
global minefindz
global minefindbc
global minefindbd
global minefindaa
global minefindab
global minefindac
global minefindad
global minefindia
global minefindib
global minefindic
global minefindid
global minefindja
global minefindjb
global minefindjc
global minefindjd
global minefindae
global minefindaf
global minefindag
global minefindbe 
global minefindbf
global minefindbg
global minefindce 
global minefindcf 
global minefindcg 
global minefindde
global minefinddf
global minefinddg
global minefindee
global minefindef
global minefindeg
global minefindfe
global minefindff
global minefindfg
global minefindge
global minefindgf
global minefindgg
global minefindhe
global minefindhf
global minefindhg
global minefindie
global minefindif
global minefindig
global minefindje
global minefindjf
global minefindjg
global minefindah
global minefindai
global minefindaj
global minefindbh
global minefindbi 
global minefindbj 
global minefindch
global minefindci 
global minefindcj
global minefinddh
global minefinddi
global minefinddj
global minefindeh
global minefindei
global minefindej
global minefindfh
global minefindfi
global minefindfj
global minefindgh
global minefindgi
global minefindgj
global minefindhh
global minefindhi
global minefindhj
global minefindii
global minefindih
global minefindij
global minefindjh
global minefindji
global minefindjj



minefindb = 0
minefindc = 0
minefindd = 0
minefinde = 0
minefindf = 0
minefinda = 0
minefindg = 0
minefindh = 0
minefindi = 0
minefindj = 0
minefindk = 0
minefindl = 0
minefindm = 0
minefindn = 0
minefindo = 0
minefindp = 0
minefindq = 0
minefindr = 0
minefinds = 0
minefindt = 0
minefindu = 0
minefindv = 0
minefindw = 0
minefindx = 0
minefindy = 0
minefindz = 0
minefindbc = 0
minefindbd = 0
minefindaa = 0
minefindab = 0
minefindac = 0
minefindad = 0
minefindia = 0
minefindib = 0
minefindic = 0
minefindid = 0
minefindja = 0
minefindjb = 0
minefindjc = 0
minefindjd = 0
minefindae = 0
minefindaf = 0
minefindag = 0
minefindbe = 0
minefindbf = 0
minefindbg = 0
minefindce = 0
minefindcf = 0
minefindcg = 0
minefindde = 0
minefinddf = 0
minefinddg = 0
minefindee = 0
minefindef = 0
minefindeg = 0
minefindfe = 0
minefindff = 0
minefindfg = 0
minefindge = 0
minefindgf = 0
minefindgg = 0
minefindhe = 0
minefindhf = 0
minefindhg = 0
minefindie = 0
minefindif = 0
minefindig = 0
minefindje = 0
minefindjf = 0
minefindjg = 0
minefindah = 0
minefindai = 0
minefindaj = 0
minefindbh = 0
minefindbi = 0
minefindbj = 0
minefindch = 0
minefindci = 0
minefindcj = 0
minefinddh = 0
minefinddi = 0
minefinddj = 0
minefindeh = 0
minefindei = 0
minefindej = 0
minefindfh = 0
minefindfi = 0
minefindfj = 0
minefindgh = 0
minefindgi = 0
minefindgj = 0
minefindhh = 0
minefindhi = 0
minefindhj = 0
minefindih = 0
minefindii = 0
minefindij = 0
minefindjh = 0
minefindji = 0
minefindjj = 0




global scoreb 
global scorec 
global scored
global scoree
global scoref
global scorea
global scoreg
global scoreh
global scorei
global scorej
global scorek
global scorel
global scorem
global scoren
global scoreo
global scorep
global scoreq
global scorer
global scores
global scoret
global scoreu
global scorev
global scorew
global scorex
global scorey
global scorez
global scorebc
global scorebd
global scoreaa
global scoreab
global scoreac
global scoread
global scoreia
global scoreib
global scoreic
global scoreid
global scoreja
global scorejb
global scorejc
global scorejd
global scoreae
global scoreaf
global scoreag
global scorebe 
global scorebf
global scorebg
global scorece 
global scorecf 
global scorecg 
global scorede
global scoredf
global scoredg
global scoreee
global scoreef
global scoreeg
global scorefe
global scoreff
global scorefg
global scorege
global scoregf
global scoregg
global scorehe
global scorehf
global scorehg
global scoreie
global scoreif
global scoreig
global scoreje
global scorejf
global scorejg
global scoreah
global scoreai
global scoreaj
global scorebh
global scorebi 
global scorebj 
global scorech
global scoreci 
global scorecj
global scoredh
global scoredi
global scoredj
global scoreeh
global scoreei
global scoreej
global scorefh
global scorefi
global scorefj
global scoregh
global scoregi
global scoregj
global scorehh
global scorehi
global scorehj
global scoreih
global scoreii
global scoreij
global scorejh
global scoreji
global scorejj




scorea = 0
scoreb = 0
scorec = 0
scored = 0
scoree = 0
scoref = 0
scoreg = 0
scoreh = 0
scorei = 0
scorej = 0
scorek = 0
scorel = 0
scorem = 0
scoren = 0
scoreo = 0
scorep = 0
scoreq = 0
scorer = 0
scores = 0
scoret = 0
scoreu = 0
scorev = 0
scorew = 0
scorex = 0
scorey = 0
scorez = 0
scorebc = 0
scorebd = 0
scoreaa = 0
scoreab = 0
scoreac = 0
scoread = 0
scoreia = 0
scoreib = 0
scoreic = 0
scoreid = 0
scoreja = 0
scorejb = 0
scorejc = 0
scorejd = 0
scoreae = 0
scoreaf = 0
scoreag = 0
scorebe = 0
scorebf = 0
scorebg = 0
scorece = 0
scorecf = 0
scorecg = 0
scorede = 0
scoredf = 0
scoredg = 0
scoreee = 0
scoreef = 0
scoreeg = 0
scorefe = 0
scoreff = 0
scorefg = 0
scorege = 0
scoregf = 0
scoregg = 0
scorehe = 0
scorehf = 0
scorehg = 0
scoreie = 0
scoreif = 0
scoreig = 0
scoreje = 0
scorejf = 0
scorejg = 0
scoreah = 0
scoreai = 0
scoreaj = 0
scorebh = 0
scorebi = 0
scorebj = 0
scorech = 0
scoreci = 0
scorecj = 0
scoredh = 0
scoredi = 0
scoredj = 0
scoreeh = 0
scoreei = 0
scoreej = 0
scorefh = 0
scorefi = 0
scorefj = 0
scoregh = 0
scoregi = 0
scoregj = 0
scorehh = 0
scorehi = 0
scorehj = 0
scoreih = 0
scoreii = 0
scoreij = 0
scorejh = 0
scoreji = 0
scorejj = 0


if score_a == -1:
    scoreb += 1
    scorec += 1
    scored += 1
    scoree += 1
    scoref += 1
    scorey += 1
    scorez += 1
    scorebc += 1
    
if score_b == -1:
    scored += 1
    scoree += 1
    scorea += 1
    scorey += 1
    scorez += 1
    
if score_c == -1:
    scored += 1
    scoref += 1
    scorea += 1
    scores += 1
    scoret += 1
    scorez += 1
    scorebc += 1
    scorebd += 1
    
if score_d == -1:
    scorea += 1
    scoreb += 1
    scorec += 1
    scoree += 1
    scoref += 1
    scoreg += 1
    scoreh += 1
    scorei += 1
    
if score_e == -1:
    scoreb += 1
    scorea += 1
    scored += 1
    scoreg += 1
    scorei += 1
    
if score_f == -1:
    scorea += 1
    scorec += 1
    scored += 1
    scoreg += 1
    scoreh += 1
    scorer += 1
    scores += 1
    scoret += 1
    
if score_g == -1:
    scorei += 1
    scoreh += 1
    scored += 1
    scoree += 1
    scoref += 1
    scorej += 1
    scorek += 1
    scorel += 1
    
if score_h == -1:
    scored += 1
    scoreg += 1
    scoref += 1
    scorej += 1
    scorek += 1
    scores += 1
    scoreq += 1
    scorer += 1
    
if score_i == -1:
    scored += 1
    scoree += 1
    scoreg += 1
    scorek += 1
    scorel += 1
    
if score_j == -1:
    scoreg += 1
    scoreh += 1
    scorek += 1
    scoren += 1
    scorem += 1
    scorep += 1
    scoreq += 1
    scorer += 1
    
if score_k == -1:
    scorej += 1
    scoreh += 1
    scoreg += 1
    scorei += 1
    scorel += 1
    scorem += 1
    scoren += 1
    scoreo += 1
    
if score_l == -1:
    scorek += 1
    scoreg += 1
    scorei += 1
    scoren += 1
    scoreo += 1
    
if score_m == -1:
    scorej += 1
    scorek += 1
    scoren += 1
    scorep += 1
    scoreq += 1
    scoreu += 1
    scorev += 1
    scorew += 1
    
if score_n == -1:
    scorem += 1
    scorej += 1
    scorek += 1
    scorel += 1
    scoreo += 1
    scorev += 1
    scorew += 1
    scorex += 1
    
if score_o == -1:
    scoren += 1
    scorek += 1
    scorel += 1
    scorew += 1
    scorex += 1
    
if score_p == -1:
    scorem += 1
    scorej += 1
    scoreq += 1
    scoreu += 1
    scorev += 1
    scorefe += 1
    scorege += 1
    scorehe += 1
    
if score_q == -1:
    scorep += 1
    scorem += 1
    scorej += 1
    scoreh += 1
    scorer += 1
    scoreee += 1
    scorefe += 1
    scorege += 1
    
if score_r == -1:
    scoreq += 1
    scorej += 1
    scoreh += 1
    scores += 1
    scoref += 1
    scorede += 1
    scoreee += 1
    scorefe += 1
    
if score_s == -1:
    scorer += 1
    scoreh += 1
    scoref += 1
    scorec += 1
    scoret += 1
    scorece += 1
    scorede += 1
    scoreee += 1
    
if score_t == -1:
    scores += 1
    scoref += 1
    scorec += 1
    scorebc += 1
    scorebd += 1
    scorebe += 1
    scorece += 1
    scorede += 1
   
if score_u == -1:
    scorep += 1
    scorem += 1
    scorev += 1
    scoreid += 1
    scoreic += 1
    scorege += 1
    scorehe += 1
    scoreie += 1

if score_v == -1:
    scoreu += 1
    scorep += 1
    scorem += 1
    scoren += 1
    scorew += 1
    scoreid += 1
    scoreic += 1
    scoreib += 1

if score_w == -1:
    scorev += 1
    scorem += 1
    scoren += 1
    scoreo += 1
    scorex += 1
    scoreic += 1
    scoreib += 1
    scoreia += 1

if score_x == -1:
    scorew += 1
    scoren += 1
    scoreo += 1
    scoreia += 1
    scoreib += 1
    
if score_y == -1:
    scorez += 1
    scorea += 1
    scoreb += 1
    scoreaa += 1
    scoreab += 1
    
if score_z == -1:
    scorey += 1
    scoreb += 1
    scorea += 1
    scorec += 1
    scorebc += 1
    scoreaa += 1
    scoreab += 1
    scoreac += 1
    
if score_bc == -1:
    scorez += 1
    scorea += 1
    scorec += 1
    scoret += 1
    scorebd += 1
    scoread += 1
    scoreac += 1
    scoreab += 1
    
if score_bd == -1:
    scorebc += 1
    scorec += 1
    scoret += 1
    scoread += 1
    scoreac += 1
    scoreae += 1
    scorebe += 1
    scorece += 1

if score_aa == -1:
    scorey += 1
    scorez += 1
    scoreab += 1

if score_ab == -1:
    scoreaa += 1
    scorey += 1
    scorez += 1
    scorebc += 1
    scoreac += 1

if score_ac == -1:
    scoreab += 1
    scorez += 1
    scorebc += 1
    scorebd += 1
    scoread += 1

if score_ad == -1:
    scoreac += 1
    scorebc += 1
    scorebd += 1
    scoreae += 1
    scorebe += 1

if score_ia == -1:
    scorex += 1
    scorew += 1
    scoreib += 1
    scoreja += 1
    scorejb += 1
    
if score_ib == -1:
    scoreic += 1
    scorev += 1
    scorew += 1
    scorex += 1
    scoreia += 1
    scoreja += 1
    scorejb += 1
    scorejc += 1
    
if score_ic == -1:
    scoreid += 1
    scoreu += 1
    scorev += 1
    scorew += 1
    scoreib += 1
    scorejb += 1
    scorejc += 1
    scorejd += 1
    
if score_id == -1:
    scoreu += 1
    scorev += 1
    scoreic += 1
    scorejc += 1
    scorejd += 1
    scorehe += 1
    scoreie += 1
    scoreje += 1

if score_ja == -1:
    scoreia += 1
    scoreib += 1
    scorejb += 1

if score_jb == -1:
    scoreja += 1
    scoreia += 1
    scoreib += 1
    scoreic += 1
    scorejc += 1

if score_jc == -1:
    scorejb += 1
    scoreib += 1
    scoreic += 1
    scoreid += 1
    scorejd += 1

if score_jd == -1:
    scorejc += 1
    scoreic += 1
    scoreid += 1
    scoreie += 1
    scoreje += 1

if score_ae == -1:
    scoread += 1
    scorebd += 1
    scorebe += 1
    scorebf += 1
    scoreaf += 1
    
if score_af == -1:
    scoreae += 1
    scoreag += 1
    scorebf += 1
    scorebg += 1
    scorebe += 1
    
if score_ag == -1:
    scoreaf += 1
    scorebf += 1
    scorebg += 1
    scoreah += 1
    scorebh += 1

if score_be == -1:
    scoret += 1
    scorebd += 1
    scoread += 1
    scoreaf += 1
    scoreae += 1
    scorebf += 1
    scorecf += 1
    scorece += 1
    
if score_bf == -1:
    scorebe += 1
    scoreae += 1
    scoreaf += 1
    scoreag += 1
    scorebg += 1
    scorecg += 1
    scorece += 1
    scorecf += 1
    
if score_bg == -1:
    scoreag += 1
    scoreaf += 1
    scorebf += 1
    scorecg += 1
    scorecf += 1
    scoreah += 1
    scorebh += 1
    scorech += 1

if score_ce == -1:
    scorecf += 1
    scorebf += 1
    scorebe += 1
    scorebd += 1
    scoret += 1
    scores += 1
    scoredf += 1
    scorede += 1

if score_cf == -1:
    scorecg += 1
    scorebg += 1
    scorebf += 1
    scorebe += 1
    scorece += 1
    scoredg += 1
    scoredf += 1
    scorede += 1

if score_cg == -1:
    scorebg += 1
    scorebf += 1
    scorecf += 1
    scoredg += 1
    scoredf += 1
    scorebh += 1
    scorech += 1
    scoredh += 1

if score_de == -1:
    scoredf += 1
    scorecf += 1
    scorece += 1
    scoret += 1
    scores += 1
    scorer += 1
    scoreef += 1
    scoreee += 1

if score_df == -1:
    scoredg += 1
    scorecg += 1
    scorecf += 1
    scorece += 1
    scorede += 1
    scoreeg += 1
    scoreef += 1
    scoreee += 1

if score_dg == -1:
    scorecg += 1
    scorecf += 1
    scoredf += 1
    scoreeg += 1
    scoreef += 1
    scorech += 1
    scoredh += 1
    scoreeh += 1

if score_ee == -1:
    scoreef += 1
    scoredf += 1
    scorede += 1
    scores += 1
    scorer += 1
    scoreq += 1
    scoreff += 1
    scorefe += 1

if score_ef == -1:
    scoreeg += 1
    scoredg += 1
    scoredf += 1
    scorede += 1
    scoreee += 1
    scorefg += 1
    scoreff += 1
    scorefe += 1

if score_eg == -1:
    scoredg += 1
    scoredf += 1
    scoreef += 1
    scorefg += 1
    scoreff += 1
    scoredh += 1
    scoreeh += 1
    scorefh += 1

if score_fe == -1:
    scoreff += 1
    scoreef += 1
    scoreee += 1
    scorer += 1
    scoreq += 1
    scorep += 1
    scorege += 1
    scoregf += 1

if score_ff == -1:
    scorefg += 1
    scoreeg += 1
    scoreef += 1
    scoreee += 1
    scorefe += 1
    scorege += 1
    scoregf += 1
    scoregg += 1

if score_fg == -1:
    scoreeg += 1
    scoreef += 1
    scoreff += 1
    scoregg += 1
    scoregf += 1
    scoreeh += 1
    scorefh += 1
    scoregh += 1

if score_ge == -1:
    scoregf += 1
    scoreff += 1
    scorefe += 1
    scoreq += 1
    scorep += 1
    scoreu += 1
    scorehe += 1
    scorehf += 1

if score_gf == -1:
    scoregg += 1
    scorefg += 1
    scoreff += 1
    scorefe += 1
    scorege += 1
    scorehg += 1
    scorehf += 1
    scorehe += 1

if score_gg == -1:
    scorefg += 1
    scoreff += 1
    scoregf += 1
    scorehg += 1
    scorehf += 1
    scorefh += 1
    scoregh += 1
    scorehh += 1

if score_he == -1:
    scorehf += 1
    scoregf += 1
    scorege += 1
    scorep += 1
    scoreu += 1
    scoreid += 1
    scoreie += 1
    scoreif += 1

if score_hf == -1:
    scorehg += 1
    scoregg += 1
    scoregf += 1
    scorege += 1
    scorehe += 1
    scoreie += 1
    scoreif += 1
    scoreig += 1

if score_hg == -1:
    scoregg += 1
    scoregf += 1
    scorehf += 1
    scoreif += 1
    scoreig += 1
    scoregh += 1
    scorehh += 1
    scoreih += 1

if score_ie == -1:
    scoreif += 1
    scorehe += 1
    scorehf += 1
    scoreu += 1
    scoreid += 1
    scorejd += 1
    scoreje += 1
    scorejf += 1

if score_if == -1:
    scoreig += 1
    scorehg += 1
    scorehf += 1
    scorehe += 1
    scoreie += 1
    scoreje += 1
    scorejf += 1
    scorejg += 1
   

if score_ig == -1:
    scorehg += 1
    scorehf += 1
    scoreif += 1
    scorejf += 1
    scorejg += 1
    scorehh += 1
    scoreih += 1
    scorejh += 1

if score_je == -1:
    scorejf += 1
    scoreif += 1
    scoreie += 1
    scoreid += 1
    scorejd += 1

if score_jf == -1:
    scorejg += 1
    scoreig += 1
    scoreif += 1
    scoreie += 1
    scoreje += 1

if score_jg == -1:
    scoreig += 1
    scoreif += 1
    scorejf += 1
    scoreih += 1
    scorejh += 1

if score_ah == -1:
    scoreag += 1
    scorebg += 1
    scoreai += 1
    scorebi += 1
    scorebh += 1

if score_ai == -1:
    scoreaj += 1
    scoreah += 1
    scorebi += 1
    scorebj += 1
    scorebh += 1

if score_aj == -1:
    scoreai += 1
    scorebj += 1
    scorebi += 1

if score_bh == -1:
    scorebi += 1
    scoreai += 1
    scoreah += 1
    scoreag += 1
    scorebg += 1
    scorecg += 1
    scoreci += 1
    scorech += 1

if score_bi == -1:
    scorebj += 1
    scoreaj += 1
    scoreai += 1
    scoreah += 1
    scorebh += 1
    scorech += 1
    scoreci += 1
    scorecj += 1
    
if score_bj == -1:
    scoreaj += 1
    scoreai += 1
    scorebi += 1
    scoreci += 1
    scorecj += 1

if score_ch == -1:
    scoreci += 1
    scorebi += 1
    scorebh += 1
    scorebg += 1
    scorecg += 1
    scoredg += 1
    scoredi += 1
    scoredh += 1

if score_ci == -1:
    scorecj += 1
    scorebj += 1
    scorebi += 1
    scorebh += 1
    scorech += 1
    scoredi += 1
    scoredj += 1
    scoredh += 1

if score_cj == -1:
    scorebj += 1
    scorebi += 1
    scoreci += 1
    scoredj += 1
    scoredi += 1

if score_dh == -1:
    scoredi += 1
    scoreci += 1
    scorech += 1
    scorecg += 1
    scoredg += 1
    scoreeg += 1
    scoreei += 1
    scoreeh += 1

if score_di == -1:
    scoredj += 1
    scorecj += 1
    scoreci += 1
    scorech += 1
    scoredh += 1
    scoreei += 1
    scoreeh += 1
    scoreej += 1

if score_dj == -1:
    scorecj += 1
    scoredi += 1
    scoreci += 1
    scoreei += 1
    scoreej += 1

if score_eh == -1:
    scoreei += 1
    scoreeg += 1
    scoredi += 1
    scoredh += 1
    scoredg += 1
    scorefg += 1
    scorefi += 1
    scorefh += 1

if score_ei == -1:
    scoreej += 1
    scoredj += 1
    scoredi += 1
    scoredh += 1
    scoreeh += 1
    scorefi += 1
    scorefj += 1
    scorefh += 1
    
if score_ej == -1:
    scoreei += 1
    scoredi += 1
    scoredj += 1
    scorefj += 1
    scorefi += 1

if score_fh == -1:
    scorefi += 1
    scoreei += 1
    scoreeh += 1
    scoreeg += 1
    scorefg += 1
    scoregg += 1
    scoregi += 1
    scoregh += 1

if score_fi == -1:
    scorefj += 1
    scoreej += 1
    scoreei += 1
    scoreeh += 1
    scorefh += 1
    scoregi += 1
    scoregj += 1
    scoregh += 1

if score_fj == -1:
    scoreej += 1
    scoreei += 1
    scorefi += 1
    scoregi += 1
    scoregj += 1
   
if score_gh == -1:
    scoregi += 1
    scorefi += 1
    scorefh += 1
    scorefg += 1
    scoregg += 1
    scorehg += 1
    scorehi += 1
    scorehh += 1

if score_gi == -1:
    scoregj += 1
    scorefj += 1
    scorefi += 1
    scorefh += 1
    scoregh += 1
    scorehi += 1
    scorehh += 1
    scorehj += 1

if score_gj == -1:
    scorefj += 1
    scorefi += 1
    scoregi += 1   
    scorehj += 1
    scorehi += 1

if score_hh == -1:
    scorehi += 1
    scoregi += 1
    scoregh += 1
    scoregg += 1
    scorehg += 1
    scoreig += 1
    scoreii += 1
    scoreih += 1

if score_hi == -1:
    scorehj += 1
    scoregj += 1
    scoregi += 1
    scoregh += 1
    scorehh += 1
    scoreii += 1
    scoreij += 1
    scoreih += 1

if score_hj == -1:
    scoregj += 1
    scoregi += 1
    scorehi += 1
    scoreij += 1
    scoreii += 1

if score_ih == -1:
    scoreii += 1
    scorehi += 1
    scorehh += 1
    scorehg += 1
    scoreig += 1
    scorejg += 1
    scoreji += 1
    scorejh += 1

if score_ii == -1:
    scoreij += 1
    scorehj += 1
    scorehi += 1
    scorehh += 1
    scoreih += 1
    scorejj += 1
    scoreji += 1
    scorejh += 1

if score_ij == -1:
    scorehj += 1
    scorehi += 1
    scoreii += 1
    scorejj += 1
    scoreji += 1

if score_jh == -1:
    scorejg += 1
    scoreig += 1
    scoreih += 1
    scoreji += 1
    scoreii += 1
    
if score_ji == -1:
    scorejj += 1
    scoreij += 1
    scoreii += 1
    scoreih += 1
    scorejh += 1

if score_jj == -1:
    scoreij += 1
    scoreii += 1
    scoreji += 1

global minenumber
minenumber = 0


if score_a == -1:
    scorea = "M"
    minenumber += 1
    minefinda = -1
if score_b == -1:
    scoreb = "M"
    minenumber += 1
    minefindb = -1
if score_c == -1:
    scorec = "M"
    minenumber += 1
    minefindc = -1
if score_d == -1:
    scored = "M"
    minenumber += 1
    minefindd = -1
if score_e == -1:
    scoree = "M"
    minenumber += 1
    minefinde = -1
if score_f == -1:
    scoref = "M"
    minenumber += 1
    minefindf = -1
if score_g == -1:
    scoreg = "M"
    minenumber += 1
    minefindg = -1
if score_h == -1:
    scoreh = "M"
    minenumber += 1
    minefindh = -1
if score_i == -1:
    scorei = "M"
    minenumber += 1
    minefindi = -1
if score_j == -1:
    scorej = "M"
    minenumber += 1
    minefindj = -1
if score_k == -1:
    scorek = "M"
    minenumber += 1
    minefindk = -1
if score_l == -1:
    scorel = "M"
    minenumber += 1
    minefindl = -1
if score_m == -1:
    scorem = "M"
    minenumber += 1
    minefindm = -1
if score_n == -1:
    scoren = "M"
    minenumber += 1
    minefindn = -1
if score_o == -1:
    scoreo = "M"
    minenumber += 1
    minefindo = -1
if score_p == -1:
    scorep = "M"
    minenumber += 1
    minefindp = -1
if score_q == -1:
    scoreq = "M"
    minenumber += 1
    minefindq = -1
if score_r == -1:
    scorer = "M"
    minenumber += 1
    minefindr = -1
if score_s == -1:
    scores = "M"
    minenumber += 1
    minefinds = -1
if score_t == -1:
    scoret = "M"
    minenumber += 1
    minefindt = -1
if score_u == -1:
    scoreu = "M"
    minenumber += 1
    minefindu = -1
if score_v == -1:
    scorev = "M"
    minenumber += 1
    minefindv = -1
if score_w == -1:
    scorew = "M"
    minenumber += 1
    minefindw = -1
if score_x == -1:
    scorex = "M"
    minenumber += 1
    minefindx = -1
if score_y == -1:
    scorey = "M"
    minenumber += 1
    minefindy = -1
if score_z == -1:
    scorez = "M"
    minenumber += 1
    minefindz = -1
if score_bc == -1:
    scorebc = "M"
    minenumber += 1
    minefindbc = -1
if score_bd == -1:
    scorebd = "M"
    minenumber += 1
    minefindbd = -1
if score_aa == -1:
    scoreaa = "M"
    minenumber += 1
    minefindaa = -1
if score_ab == -1:
    scoreab = "M"
    minenumber += 1
    minefindab = -1
if score_ac == -1:
    scoreac = "M"
    minenumber += 1
    minefindac = -1
if score_ad == -1:
    scoread = "M"
    minenumber += 1
    minefindad = -1
if score_ia == -1:
    scoreia = "M"
    minenumber += 1
    minefindia = -1
if score_ib == -1:
    scoreib = "M"
    minenumber += 1
    minefindib = -1
if score_ic == -1:
    scoreic = "M"
    minenumber += 1
    minefindic = -1
if score_id == -1:
    scoreid = "M"
    minenumber += 1
    minefindid = -1
if score_ja == -1:
    scoreja = "M"
    minenumber += 1
    minefindja = -1
if score_jb == -1:
    scorejb = "M"
    minenumber += 1
    minefindjb = -1
if score_jc == -1:
    scorejc = "M"
    minenumber += 1
    minefindjc = -1
if score_jd == -1:
    scorejd = "M"
    minenumber += 1
    minefindjd = -1
if score_ae == -1:
    scoreae = "M"
    minenumber += 1
    minefindae = -1
if score_af == -1:
    scoreaf = "M"
    minenumber += 1
    minefindaf = -1
if score_ag == -1:
    scoreag = "M"
    minenumber += 1
    minefindag = -1
if score_be == -1:
    scorebe = "M"
    minenumber += 1
    minefindbe = -1
if score_bf == -1:
    scorebf = "M"
    minenumber += 1
    minefindbf = -1
if score_bg == -1:
    scorebg = "M"
    minenumber += 1
    minefindbg = -1
if score_ce == -1:
    scorece = "M"
    minenumber += 1
    minefindce = -1
if score_cf == -1:
    scorecf = "M"
    minenumber += 1
    minefindcf = -1
if score_cg == -1:
    scorecg = "M"
    minenumber += 1
    minefindcg = -1
if score_de == -1:
    scorede = "M"
    minenumber += 1
    minefindde = -1
if score_df == -1:
    scoredf = "M"
    minenumber += 1
    minefinddf = -1
if score_dg == -1:
    scoredg = "M"
    minenumber += 1
    minefinddg = -1
if score_ee == -1:
    scoreee = "M"
    minenumber += 1
    minefindee = -1
if score_ef == -1:
    scoreef = "M"
    minenumber += 1
    minefindef = -1
if score_eg == -1:
    scoreeg = "M"
    minenumber += 1
    minefindeg = -1
if score_fe == -1:
    scorefe = "M"
    minenumber += 1
    minefindfe = -1
if score_ff == -1:
    scoreff = "M"
    minenumber += 1
    minefindff = -1
if score_fg == -1:
    scorefg = "M"
    minenumber += 1
    minefindfg = -1
if score_ge == -1:
    scorege = "M"
    minenumber += 1
    minefindge = -1
if score_gf == -1:
    scoregf = "M"
    minenumber += 1
    minefindgf = -1
if score_gg == -1:
    scoregg = "M"
    minenumber += 1
    minefindgg = -1
if score_he == -1:
    scorehe = "M"
    minenumber += 1
    minefindhe = -1
if score_hf == -1:
    scorehf = "M"
    minenumber += 1
    minefindhf = -1
if score_hg == -1:
    scorehg = "M"
    minenumber += 1
    minefindhg = -1
if score_ie == -1:
    scoreie = "M"
    minenumber += 1
    minefindie = -1
if score_if == -1:
    scoreif = "M"
    minenumber += 1
    minefindif = -1
if score_ig == -1:
    scoreig = "M"
    minenumber += 1
    minefindig = -1
if score_je == -1:
    scoreje = "M"
    minenumber += 1
    minefindje = -1
if score_jf == -1:
    scorejf = "M"
    minenumber += 1
    minefindjf = -1
if score_jg == -1:
    scorejg = "M"
    minenumber += 1
    minefindjg = -1
if score_ah == -1:
    scoreah = "M"
    minenumber += 1
    minefindah = -1
if score_ai == -1:
    scoreai = "M"
    minenumber += 1
    minefindai = -1
if score_aj == -1:
    scoreaj = "M"
    minenumber += 1
    minefindaj = -1
if score_bh == -1:
    scorebh = "M"
    minenumber += 1
    minefindbh = -1
if score_bi == -1:
    scorebi = "M"
    minenumber += 1
    minefindbi = -1
if score_bj == -1:
    scorebj = "M"
    minenumber += 1
    minefindbj = -1
if score_ch == -1:
    scorech = "M"
    minenumber += 1
    minefindch = -1
if score_ci == -1:
    scoreci = "M"
    minenumber += 1
    minefindci = -1
if score_cj == -1:
    scorecj = "M"
    minenumber += 1
    minefindcj = -1
if score_dh == -1:
    scoredh = "M"
    minenumber += 1
    minefinddh = -1
if score_di == -1:
    scoredi = "M"
    minenumber += 1
    minefinddi = -1
if score_dj == -1:
    scoredj = "M"
    minenumber += 1
    minefinddj = -1
if score_eh == -1:
    scoreeh = "M"
    minenumber += 1
    minefindeh = -1
if score_ei == -1:
    scoreei = "M"
    minenumber += 1
    minefindei = -1
if score_ej == -1:
    scoreej = "M"
    minenumber += 1
    minefindej = -1
if score_fh == -1:
    scorefh = "M"
    minenumber += 1
    minefindfh = -1
if score_fi == -1:
    scorefi = "M"
    minenumber += 1
    minefindfi = -1
if score_fj == -1:
    scorefj = "M"
    minenumber += 1
    minefindfj = -1
if score_gh == -1:
    scoregh = "M"
    minenumber += 1
    minefindgh = -1
if score_gi == -1:
    scoregi = "M"
    minenumber += 1
    minefindgi = -1
if score_gj == -1:
    scoregj = "M"
    minenumber += 1
    minefindgj = -1
if score_hh == -1:
    scorehh = "M"
    minenumber += 1
    minefindhh = -1
if score_hi == -1:
    scorehi = "M"
    minenumber += 1
    minefindhi = -1
if score_hj == -1:
    scorehj = "M"
    minenumber += 1
    minefindhj = -1
if score_ih == -1:
    scoreih = "M"
    minenumber += 1
    minefindih = -1
if score_ii == -1:
    scoreii = "M"
    minenumber += 1
    minefindii = -1
if score_ij == -1:
    scoreij = "M"
    minenumber += 1
    minefindij = -1
if score_jh == -1:
    scorejh = "M"
    minenumber += 1
    minefindjh = -1
if score_ji == -1:
    scoreji = "M"
    minenumber += 1
    minefindji = -1
if score_jj == -1:
    scorejj = "M"
    minenumber += 1
    minefindjj = -1



'''
if score_a != -1 and score_b != -1 and score_c != -1 and score_d != -1 and score_e != -1 and score_f != -1 and score_g != -1 and score_h != -1 and score_i != -1:
    score_a = random.randint(-1,8)
    score_b = random.randint(-1,8)
    score_c = random.randint(-1,8)
    score_d = random.randint(-1,8)
    score_e = random.randint(-1,8)
    score_f = random.randint(-1,8)
    score_g = random.randint(-1,8)
    score_h = random.randint(-1,8)
    score_i = random.randint(-1,8)
'''

tta = False
ttb = False
ttc = False
ttd = False
tte = False
ttf = False
ttg = False
tth = False
tti = False
ttj = False
ttk = False
ttl = False
ttm = False
ttn = False
tto = False
ttp = False
ttq = False
ttr = False
tts = False
ttt = False
ttu = False
ttv = False
ttw = False
ttx = False
tty = False
ttz = False
ttbc = False
ttbd = False
ttaa = False
ttab = False
ttac = False
ttad = False
ttia = False
ttib = False
ttic = False
ttid = False
ttja = False
ttjb = False
ttjc = False
ttjd = False
ttae = False
ttaf = False
ttag = False
ttbe = False
ttbf = False
ttbg = False
ttce = False
ttcf = False
ttcg = False
ttde = False
ttdf = False
ttdg = False
ttee = False
ttef = False
tteg = False
ttfe = False
ttff = False
ttfg = False
ttge = False
ttgf = False
ttgg = False
tthe = False
tthf = False
tthg = False
ttie = False
ttif = False
ttig = False
ttje = False
ttjf = False
ttjg = False
ttah = False
ttai = False
ttaj = False
ttbh = False
ttbi = False
ttbj = False
ttch = False
ttci = False
ttcj = False
ttdh = False
ttdi = False
ttdj = False
tteh = False
ttei = False
ttej = False
ttfh = False
ttfi = False
ttfj = False
ttgh = False
ttgi = False
ttgj = False
tthh = False
tthi = False
tthj = False
ttih = False
ttii = False
ttij = False
ttjh = False
ttji = False
ttjj = False
show = False


#scorea,scoreb,scorec,scored,scoree,scoref,scoreg,scoreh,scorei
if scorea == 0:
    scorea = " "
if scoreb == 0:
    scoreb = " "
if scorec == 0:
    scorec = " "
if scored == 0:
    scored = " "
if scoree == 0:
    scoree = " "
if scoref == 0:
    scoref = " "
if scoreg == 0:
    scoreg = " "
if scoreh == 0:
    scoreh = " "
if scorei == 0:
    scorei = " "
if scorej == 0:
    scorej = " "
if scorek == 0:
    scorek = " "
if scorel == 0:
    scorel = " "
if scorem == 0:
    scorem = " "
if scoren == 0:
    scoren = " "
if scoreo == 0:
    scoreo = " "
if scorep == 0:
    scorep = " "
if scoreq == 0:
    scoreq = " "
if scorer == 0:
    scorer = " "
if scores == 0:
    scores = " "
if scoret == 0:
    scoret = " "
if scoreu == 0:
    scoreu = " "
if scorev == 0:
    scorev = " "
if scorew == 0:
    scorew = " "
if scorex == 0:
    scorex = " "
if scorey == 0:
    scorey = " "
if scorez == 0:
    scorez = " "
if scorebc == 0:
    scorebc = " "
if scorebd == 0:
    scorebd = " "
if scoreaa == 0:
    scoreaa = " "
if scoreab == 0:
    scoreab = " "
if scoreac == 0:
    scoreac = " "
if scoread == 0:
    scoread = " "
if scoreia == 0:
    scoreia = " "
if scoreib == 0:
    scoreib = " "
if scoreic == 0:
    scoreic = " "
if scoreid == 0:
    scoreid = " "
if scoreja == 0:
    scoreja = " "
if scorejb == 0:
    scorejb = " "
if scorejc == 0:
    scorejc = " "
if scorejd == 0:
    scorejd = " "
if scoreae == 0:
    scoreae = " "
if scoreaf == 0:
    scoreaf = " "
if scoreag == 0:
    scoreag = " "
if scorebe == 0:
    scorebe = " "
if scorebf == 0:
    scorebf = " "
if scorebg == 0:
    scorebg = " "
if scorece == 0:
    scorece = " "
if scorecf == 0:
    scorecf = " "
if scorecg == 0:
    scorecg = " "
if scorede == 0:
    scorede = " "
if scoredf == 0:
    scoredf = " "
if scoredg == 0:
    scoredg = " "
if scoreee == 0:
    scoreee = " "
if scoreef == 0:
    scoreef = " "
if scoreeg == 0:
    scoreeg = " "
if scorefe == 0:
    scorefe = " "
if scoreff == 0:
    scoreff = " "
if scorefg == 0:
    scorefg = " "
if scorege == 0:
    scorege = " "
if scoregf == 0:
    scoregf = " "
if scoregg == 0:
    scoregg = " "
if scorehe == 0:
    scorehe = " "
if scorehf == 0:
    scorehf = " "
if scorehg == 0:
    scorehg = " "
if scoreie == 0:
    scoreie = " "
if scoreif == 0:
    scoreif = " "
if scoreig == 0:
    scoreig = " "
if scoreje == 0:
    scoreje = " "
if scorejf == 0:
    scorejf = " "
if scorejg == 0:
    scorejg = " "
if scoreah == 0:
    scoreah = " "
if scoreai == 0:
    scoreai = " "
if scoreaj == 0:
    scoreaj = " "
if scorebh == 0:
    scorebh = " "
if scorebi == 0:
    scorebi = " "
if scorebj == 0:
    scorebj = " "
if scorech == 0:
    scorech = " "
if scoreci == 0:
    scoreci = " "
if scorecj == 0:
    scorecj = " "
if scoredh == 0:
    scoredh = " "
if scoredi == 0:
    scoredi = " "
if scoredj == 0:
    scoredj = " "
if scoreeh == 0:
    scoreeh = " "
if scoreei == 0:
    scoreei = " "
if scoreej == 0:
    scoreej = " "
if scorefh == 0:
    scorefh = " "
if scorefi == 0:
    scorefi = " "
if scorefj == 0:
    scorefj = " "
if scoregh == 0:
    scoregh = " "
if scoregi == 0:
    scoregi = " "
if scoregj == 0:
    scoregj = " "
if scorehh == 0:
    scorehh = " "
if scorehi == 0:
    scorehi = " "
if scorehj == 0:
    scorehj = " "
if scoreih == 0:
    scoreih = " "
if scoreii == 0:
    scoreii = " "
if scoreij == 0:
    scoreij = " "
if scorejh == 0:
    scorejh = " "
if scoreji == 0:
    scoreji = " "
if scorejj == 0:
    scorejj = " "
number = 0


#colorchoice = [0,255,34,177,76]
#r,g,b= colorchoice[0],colorchoice[0],colorchoice[0]

def explosion(x=500, y=211):

    explode = True

    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()

        startPoint = x,y

        colorChoices = [red, light_red, yellow, light_yellow, green, light_green, purple]

        magnitude = 1

        while magnitude < 100:

            exploding_bit_x = x +random.randrange(-1*magnitude,magnitude)
            exploding_bit_y = y +random.randrange(-1*magnitude,magnitude)

            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0,7)],(exploding_bit_x, exploding_bit_y),random.randrange(1,6))
            magnitude += 1

            pygame.display.update()
            clock.tick(FPS)
            
        explode = False


def button(text, x, y, width, height,inactive_color, active_color,back_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
            pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
            if click[0] == 1 and action != None and click[-1] == 1:
                showallfinally()

            if click[0] == 1 and action != None:
                if action == "a":
                    global tta
                    tta = True
                    global number
                    number = scorea
                    clickevent()
                    #print(cur)
                if action == "b":
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    global ttb
                    ttb = True
                    number = scoreb
                    clickevent()
                    #print(cur)
                if action == "c":
                    global ttc
                    ttc = True
                    number = scorec
                    clickevent()
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    #print(cur)
                if action == "d":
                    global ttd
                    ttd = True
                    number = scored
                    clickevent()
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    #print(cur)
                if action == "e":
                    global tte
                    tte = True
                    number = scoree
                    clickevent()
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    #print(cur)
                if action == "f":
                    global ttf
                    ttf = True
                    number = scoref
                    clickevent()
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    #print(cur)
                if action == "g":
                    global ttg
                    ttg = True
                    number = scoreg
                    clickevent()
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    #print(cur)
                if action == "h":
                    global tth
                    tth = True
                    number = scoreh
                    clickevent()
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    #print(cur)
                if action == "i":
                    global tti
                    tti = True
                    number = scorei
                    clickevent()
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    #print(cur)
                if action == "j":
                    global ttj
                    ttj = True
                    number = scorej
                    clickevent()
                if action == "k":
                    global ttk
                    ttk = True
                    number = scorek
                    clickevent()
                if action == "l":
                    global ttl
                    ttl = True
                    number = scorel
                    clickevent()
                if action == "m":
                    global ttm
                    ttm = True
                    number = scorem
                    clickevent()
                if action == "n":
                    global ttn
                    ttn = True
                    number = scoren
                    clickevent()
                if action == "o":
                    global tto
                    tto = True
                    number = scoreo
                    clickevent()
                if action == "p":
                    global ttp
                    ttp = True
                    number = scorep
                    clickevent()
                if action == "q":
                    global ttq
                    ttq = True
                    number = scoreq
                    clickevent()
                if action == "r":
                    global ttr
                    ttr = True
                    number = scorer
                    clickevent()
                if action == "s":
                    global tts
                    tts = True
                    number = scores
                    clickevent()
                if action == "t":
                    global ttt
                    ttt = True
                    number = scoret
                    clickevent()
                if action == "u":
                    global ttu
                    ttu = True
                    number = scoreu
                    clickevent()
                if action == "v":
                    global ttv
                    ttv = True
                    number = scorev
                    clickevent()
                if action == "w":
                    global ttw
                    ttw = True
                    number = scorew
                    clickevent()
                if action == "x":
                    global ttx
                    ttx = True
                    number = scorex
                    clickevent()
                if action == "y":
                    global tty
                    tty = True
                    number = scorey
                    clickevent()
                if action == "z":
                    global ttz
                    ttz = True
                    number = scorez
                    clickevent()
                if action == "bc":
                    global ttbc
                    ttbc = True
                    number = scorebc
                    clickevent()
                if action == "bd":
                    global ttbd
                    ttbd = True
                    number = scorebd
                    clickevent()
                if action == "aa":
                    global ttaa
                    ttaa = True
                    number = scoreaa
                    clickevent()
                if action == "ab":
                    global ttab
                    ttab = True
                    number = scoreab
                    clickevent()
                if action == "ac":
                    global ttac
                    ttac = True
                    number = scoreac
                    clickevent()
                if action == "ad":
                    global ttad
                    ttad = True
                    number = scoread
                    clickevent()
                if action == "ia":
                    global ttia
                    ttia = True
                    number = scoreia
                    clickevent()
                if action == "ib":
                    global ttib
                    ttib = True
                    number = scoreib
                    clickevent()
                if action == "ic":
                    global ttic
                    ttic = True
                    number = scoreic
                    clickevent()
                if action == "id":
                    global ttid
                    ttid = True
                    number = scoreid
                    clickevent()
                if action == "ja":
                    global ttja
                    ttja = True
                    number = scoreja
                    clickevent()
                if action == "jb":
                    global ttjb
                    ttjb = True
                    number = scorejb
                    clickevent()
                if action == "jc":
                    global ttjc
                    ttjc = True
                    number = scorejc
                    clickevent()
                if action == "jd":
                    global ttjd
                    ttjd = True
                    number = scorejd
                    clickevent()
                if action == "ae":
                    global ttae
                    ttae = True
                    number = scoreae
                    clickevent()
                if action == "af":
                    global ttaf
                    ttaf = True
                    number = scoreaf
                    clickevent()
                if action == "ag":
                    global ttag
                    ttag = True
                    number = scoreag
                    clickevent()
                if action == "be":
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    global ttbe
                    ttbe = True
                    number = scorebe
                    clickevent()
                if action == "bf":
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    global ttbf
                    ttbf = True
                    number = scorebf
                    clickevent()
                if action == "bg":
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    global ttbg
                    ttbg = True
                    number = scorebg
                    clickevent()
                if action == "ce":
                    global ttce
                    ttce = True
                    number = scorece
                    clickevent()
                if action == "cf":
                    global ttcf
                    ttcf = True
                    number = scorecf
                    clickevent()
                if action == "cg":
                    global ttcg
                    ttcg = True
                    number = scorecg
                    clickevent()
                if action == "de":
                    global ttde
                    ttde = True
                    number = scorede
                    clickevent()
                if action == "df":
                    global ttdf
                    ttdf = True
                    number = scoredf
                    clickevent()
                if action == "dg":
                    global ttdg
                    ttdg = True
                    number = scoredg
                    clickevent()
                if action == "ee":
                    global ttee
                    ttee = True
                    number = scoreee
                    clickevent()
                if action == "ef":
                    global ttef
                    ttef = True
                    number = scoreef
                    clickevent()
                if action == "eg":
                    global tteg
                    tteg = True
                    number = scoreeg
                    clickevent()
                if action == "fe":
                    global ttfe
                    ttfe = True
                    number = scorefe
                    clickevent()
                if action == "ff":
                    global ttff
                    ttff = True
                    number = scoreff
                    clickevent()
                if action == "fg":
                    global ttfg
                    ttfg = True
                    number = scorefg
                    clickevent()
                if action == "ge":
                    global ttge
                    ttge = True
                    number = scorege
                    clickevent()
                if action == "gf":
                    global ttgf
                    ttgf = True
                    number = scoregf
                    clickevent()
                if action == "gg":
                    global ttgg
                    ttgg = True
                    number = scoregg
                    clickevent()
                if action == "he":
                    global tthe
                    tthe = True
                    number = scorehe
                    clickevent()
                if action == "hf":
                    global tthf
                    tthf = True
                    number = scorehf
                    clickevent()
                if action == "hg":
                    global tthg
                    tthg = True
                    number = scorehg
                    clickevent()
                if action == "ie":
                    global ttie
                    ttie = True
                    number = scoreie
                    clickevent()
                if action == "if":
                    global ttif
                    ttif = True
                    number = scoreif
                    clickevent()
                if action == "ig":
                    global ttig
                    ttig = True
                    number = scoreig
                    clickevent()
                if action == "je":
                    global ttje
                    ttje = True
                    number = scoreje
                    clickevent()
                if action == "jf":
                    global ttjf
                    ttjf = True
                    number = scorejf
                    clickevent()
                if action == "jg":
                    global ttjg
                    ttjg = True
                    number = scorejg
                    clickevent()
                if action == "ah":
                    global ttah
                    ttah = True
                    number = scoreah
                    clickevent()
                if action == "ai":
                    global ttai
                    ttai = True
                    number = scoreai
                    clickevent()
                if action == "aj":
                    global ttaj
                    ttaj = True
                    number = scoreaj
                    clickevent()
                if action == "bh":
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    global ttbh
                    ttbh = True
                    number = scorebh
                    clickevent()
                if action == "bi":
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    global ttbi
                    ttbi = True
                    number = scorebi
                    clickevent()
                if action == "bj":
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    global ttbj
                    ttbj = True
                    number = scorebj
                    clickevent()
                if action == "ch":
                    global ttch
                    ttch = True
                    number = scorech
                    clickevent()
                if action == "ci":
                    global ttci
                    ttci = True
                    number = scoreci
                    clickevent()
                if action == "cj":
                    global ttcj
                    ttcj = True
                    number = scorecj
                    clickevent()
                if action == "dh":
                    global ttdh
                    ttdh = True
                    number = scoredh
                    clickevent()
                if action == "di":
                    global ttdi
                    ttdi = True
                    number = scoredi
                    clickevent()
                if action == "dj":
                    global ttdj
                    ttdj = True
                    number = scoredj
                    clickevent()
                if action == "eh":
                    global tteh
                    tteh = True
                    number = scoreeh
                    clickevent()
                if action == "ei":
                    global ttei
                    ttei = True
                    number = scoreei
                    clickevent()
                if action == "ej":
                    global ttej
                    ttej = True
                    number = scoreej
                    clickevent()
                if action == "fh":
                    global ttfh
                    ttfh = True
                    number = scorefh
                    clickevent()
                if action == "fi":
                    global ttfi
                    ttfi = True
                    number = scorefi
                    clickevent()
                if action == "fj":
                    global ttfj
                    ttfj = True
                    number = scorefj
                    clickevent()
                if action == "gh":
                    global ttgh
                    ttgh = True
                    number = scoregh
                    clickevent()
                if action == "gi":
                    global ttgi
                    ttgi = True
                    number = scoregi
                    clickevent()
                if action == "gj":
                    global ttgj
                    ttgj = True
                    number = scoregj
                    clickevent()
                if action == "hh":
                    global tthh
                    tthh = True
                    number = scorehh
                    clickevent()
                if action == "hi":
                    global tthi
                    tthi = True
                    number = scorehi
                    clickevent()
                if action == "hj":
                    global tthj
                    tthj = True
                    number = scorehj
                    clickevent()
                if action == "ih":
                    global ttih
                    ttih = True
                    number = scoreih
                    clickevent()
                if action == "ii":
                    global ttii
                    ttii = True
                    number = scoreii
                    clickevent()
                if action == "ij":
                    global ttij
                    ttij = True
                    number = scoreij
                    clickevent()
                if action == "jh":
                    global ttjh
                    ttjh = True
                    number = scorejh
                    clickevent()
                if action == "ji":
                    global ttji
                    ttji = True
                    number = scoreji
                    clickevent()
                if action == "jj":
                    global ttjj
                    ttjj = True
                    number = scorejj
                    clickevent()
            if click[-1] == 1 and action != None:
                if action == "a":
                    tta = "MINE"
                    
                    
                if action == "b":
                    ttb = "MINE"
                    
                    #print(cur)
                if action == "c":
                    ttc = "MINE"
                    
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    #print(cur)
                if action == "d":
                    ttd = "MINE"
                   
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    #print(cur)
                if action == "e":
                    tte = "MINE"
    
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    #print(cur)
                if action == "f":
                    ttf = "MINE"
    
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    #print(cur)
                if action == "g":
                    ttg = "MINE"
  
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    #print(cur)
                if action == "h":
                    tth = "MINE"
     
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    #print(cur)
                if action == "i":
                    tti = "MINE"
  
                    #pygame.draw.rect(gameDisplay, back_color, (x, y, width, height))
                    #print(cur)
                if action == "j":
                    ttj = "MINE"
            
                if action == "k":
                    ttk = "MINE"
              
                if action == "l":
                    ttl = "MINE"
                    clickevent()
                if action == "m":
                    ttm = "MINE"
                    clickevent()
                if action == "n":
                    ttn = "MINE"
                    clickevent()
                if action == "o":
                    tto = "MINE"
                    clickevent()
                if action == "p":
                    ttp = "MINE"
                    clickevent()
                if action == "q":
                    ttq = "MINE"
                    clickevent()
                if action == "r":
                    ttr = "MINE"
                    clickevent()
                if action == "s":
                    tts = "MINE"
                    clickevent()
                if action == "t":
                    ttt = "MINE"
                    clickevent()
                if action == "u":
                    ttu = "MINE"
                    clickevent()
                if action == "v":
                    ttv = "MINE"
                    clickevent()
                if action == "w":
                    ttw = "MINE"
                    clickevent()
                if action == "x":
                    ttx = "MINE"
                    clickevent()
                if action == "y":
                    tty = "MINE"
                    clickevent()
                if action == "z":
                    ttz = "MINE"
                    clickevent()
                if action == "bc":
                    ttbc = "MINE"
                    clickevent()
                if action == "bd":
                    ttbd = "MINE"
                    clickevent()
                if action == "aa":
                    ttaa = "MINE"
                    clickevent()
                if action == "ab":
                    ttab = "MINE"
                    clickevent()
                if action == "ac":
                    ttac = "MINE"
                    clickevent()
                if action == "ad":
                    ttad = "MINE"
                    clickevent()
                if action == "ia":
                    ttia = "MINE"
                    clickevent()
                if action == "ib":
                    ttib = "MINE"
                    clickevent()
                if action == "ic":
                    ttic = "MINE"
                    clickevent()
                if action == "id":
                    ttid = "MINE"
                    clickevent()
                if action == "ja":
                    ttja = "MINE"
                    clickevent()
                if action == "jb":
                    ttjb = "MINE"
                    clickevent()
                if action == "jc":
                    ttjc = "MINE"
                    clickevent()
                if action == "jd":
                    ttjd = "MINE"
                    clickevent()
                if action == "ae":
                    ttae = "MINE"
                    clickevent()
                if action == "af":
                    ttaf = "MINE"
                    clickevent()
                if action == "ag":
                    ttag = "MINE"
                    clickevent()
                if action == "be":
                    ttbe = "MINE"
                    clickevent()
                if action == "bf":
                    ttbf = "MINE"
                    clickevent()
                if action == "bg":
                    ttbg = "MINE"
                    clickevent()
                if action == "ce":
                    ttce = "MINE"
                    clickevent()
                if action == "cf":
                    ttcf = "MINE"
                    clickevent()
                if action == "cg":
                    ttcg = "MINE"
                    clickevent()
                if action == "de":
                    ttde = "MINE"
                    clickevent()
                if action == "df":
                    ttdf = "MINE"
                    clickevent()
                if action == "dg":
                    ttdg = "MINE"
                    clickevent()
                if action == "ee":
                    ttee = "MINE"
                    clickevent()
                if action == "ef":
                    ttef = "MINE"
                    clickevent()
                if action == "eg":
                    tteg = "MINE"
                    clickevent()
                if action == "fe":
                    ttfe = "MINE"
                    clickevent()
                if action == "ff":
                    ttff = "MINE"
                    clickevent()
                if action == "fg":
                    ttfg = "MINE"
                    clickevent()
                if action == "ge":
                    ttge = "MINE"
                    clickevent()
                if action == "gf":
                    ttgf = "MINE"
                    clickevent()
                if action == "gg":
                    ttgg = "MINE"
                    clickevent()
                if action == "he":
                    tthe = "MINE"
                    clickevent()
                if action == "hf":
                    tthf = "MINE"
                    clickevent()
                if action == "hg":
                    tthg = "MINE"
                    clickevent()
                if action == "ie":
                    ttie = "MINE"
                    clickevent()
                if action == "if":
                    ttif = "MINE"
                    clickevent()
                if action == "ig":
                    ttig = "MINE"
                    clickevent()
                if action == "je":
                    ttje = "MINE"
                    clickevent()
                if action == "jf":
                    ttjf = "MINE"
                    clickevent()
                if action == "jg":
                    ttjg = "MINE"
                    clickevent()
                if action == "ah":
                    ttah = "MINE"
                    clickevent()
                if action == "ai":
                    ttai = "MINE"
                    clickevent()
                if action == "aj":
                    ttaj = "MINE"
                    clickevent()
                if action == "bh":
                    ttbh = "MINE"
                    clickevent()
                if action == "bi":
                    ttbi = "MINE"
                    clickevent()
                if action == "bj":
                    ttbj = "MINE"
                    clickevent()
                if action == "ch":
                    ttch = "MINE"
                    clickevent()
                if action == "ci":
                    ttci = "MINE"
                    clickevent()
                if action == "cj":
                    ttcj = "MINE"
                    clickevent()
                if action == "dh":
                    ttdh = "MINE"
                    clickevent()
                if action == "di":
                    ttdi = "MINE"
                    clickevent()
                if action == "dj":
                    ttdj = "MINE"
                    clickevent()
                if action == "eh":
                    tteh = "MINE"
                    clickevent()
                if action == "ei":
                    ttei = "MINE"
                    clickevent()
                if action == "ej":
                    ttej = "MINE"
                    clickevent()
                if action == "fh":
                    ttfh = "MINE"
                    clickevent()
                if action == "fi":
                    ttfi = "MINE"
                    clickevent()
                if action == "fj":
                    ttfj = "MINE"
                    clickevent()
                if action == "gh":
                    ttgh = "MINE"
                    clickevent()
                if action == "gi":
                    ttgi = "MINE"
                    clickevent()
                if action == "gj":
                    ttgj = "MINE"
                    clickevent()
                if action == "hh":
                    tthh = "MINE"
                    clickevent()
                if action == "hi":
                    tthi = "MINE"
                    clickevent()
                if action == "hj":
                    tthj = "MINE"
                    clickevent()
                if action == "ih":
                    ttih = "MINE"
                    clickevent()
                if action == "ii":
                    ttii = "MINE"
                    clickevent()
                if action == "ij":
                    ttij = "MINE"
                    clickevent()
                if action == "jh":
                    ttjh = "MINE"
                    clickevent()
                if action == "ji":
                    ttji = "MINE"
                    clickevent()
                if action == "jj":
                    ttjj = "MINE"
                    clickevent()            
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

def buttonquit(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "lossquit":
                pygame.quit()
                sys.exit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))
 
def clickevent():
    if number == "M":
        showall()


smallfont = pygame.font.SysFont("comicsansms", 15)
medfont = pygame.font.SysFont("comicsansms", 20)
largefont = pygame.font.SysFont("comicsansms", 60)



def buttons(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "Quit":
                pygame.quit()
                sys.exit()
                quit()

            if action == "Controls":
                game_controls()

            if action == "Play":
                game_control()
            
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_buttons(text,black,x,y,width,height)

def game_controls():

    
    gcont = True

    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()


        gameDisplay.fill(white)
        message_to_screen("Controls",
                          black,
                          -100,
                          "large")

        message_to_screen("Click Right to put flag on mine",
                         bluegreen,
                         -30,
                          "medium")

        message_to_screen("Click left to show whether a mine or not",
                          bluegreen,
                          10,
                          "medium")
        
        message_to_screen("If shows blank, you can click the box around it",
                          bluegreen,
                          50,
                          "medium")
        
        message_to_screen("Click left to cancel the flag",
                          bluegreen,
                          90,
                          "medium")
        
        message_to_screen("Good luck!",
                          bluegreen,
                          130,
                          "medium")

        buttons("Play", 211,442,60,30, grey, light_grey, action="Play")
        buttons("Quit", 421,442,60,30, grey, light_grey, action="Quit")
        
      
        pygame.display.update()
        clock.tick(FPS)

def game_intro():

    
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()


        gameDisplay.fill(white)
        message_to_screen("Welcome to Mine Clearance!",
                          black,
                          -100,
                          "large")

        message_to_screen("The objective is to find mine",
                         bluegreen,
                         -30,
                         "medium")

        message_to_screen("Don't click mine",
                          bluegreen,
                          10,
                          "medium")
        
        message_to_screen("Find out all the mines and you will win",
                          bluegreen,
                          50,
                          "medium")
        
        message_to_screen("Good Luck!",
                          bluegreen,
                          90,
                          "medium")
        
        message_to_screen("Build by AlexTao",
                          bluegreen,
                          130,
                          "small")

        buttons("Play", 211,442,60,30, grey, light_grey, action="Play")
        buttons("Controls", 316,442,60,30, grey, light_grey, action="Controls")
        buttons("Quit", 421,442,60,30, grey, light_grey, action="Quit")
        
      
        pygame.display.update()
        clock.tick(FPS)


def text_objects(text,color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def text_to_buttons(msg, color, buttonsx, buttonsy, buttonswidth, buttonsheight, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = ((buttonsx+(buttonswidth/2)), buttonsy+(buttonsheight/2))
    gameDisplay.blit(textSurf, textRect)


def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)
                
        
def showall():

    global tta
    global ttb
    global ttc
    global ttd
    global tte
    global ttf
    global ttg
    global tth
    global tti
    global ttj
    global ttk
    global ttl
    global ttm
    global ttn
    global tto
    global ttp
    global ttq
    global ttr
    global tts
    global ttt
    global ttu
    global ttv
    global ttw
    global ttx
    global tty
    global ttz
    global ttbc
    global ttbd
    global ttaa
    global ttab
    global ttac
    global ttad
    global ttia
    global ttib
    global ttic
    global ttid
    global ttja
    global ttjb
    global ttjc
    global ttjd
    global ttae
    global ttaf
    global ttag
    global ttbe
    global ttbf
    global ttbg
    global ttce
    global ttcf
    global ttcg
    global ttde
    global ttdf
    global ttdg
    global ttee
    global ttef
    global tteg
    global ttfe
    global ttff
    global ttfg
    global ttge
    global ttgf
    global ttgg
    global tthe
    global tthf
    global tthg
    global ttie
    global ttif
    global ttig
    global ttje
    global ttjf
    global ttjg
    global ttah
    global ttai
    global ttaj
    global ttbh
    global ttbi
    global ttbj
    global ttch
    global ttci
    global ttcj
    global ttdh
    global ttdi
    global ttdj
    global tteh
    global ttei
    global ttej
    global ttfh
    global ttfi
    global ttfj
    global ttgh
    global ttgi
    global ttgj
    global tthh
    global tthi
    global tthj
    global ttih
    global ttii
    global ttij
    global ttjh
    global ttji
    global ttjj

    global show



    tta = True
    ttb = True
    ttc = True
    ttd = True
    tte = True
    ttf = True
    ttg = True
    tth = True
    tti = True
    ttj = True
    ttk = True
    ttl = True
    ttm = True
    ttn = True
    tto = True
    ttp = True
    ttq = True
    ttr = True
    tts = True
    ttt = True
    ttu = True
    ttv = True
    ttw = True
    ttx = True
    tty = True
    ttz = True
    ttbc = True
    ttbd = True
    ttaa = True
    ttab = True
    ttac = True
    ttad = True
    ttia = True
    ttib = True
    ttic = True
    ttid = True
    ttja = True
    ttjb = True
    ttjc = True
    ttjd = True
    ttae = True
    ttaf = True
    ttag = True
    ttbe = True
    ttbf = True
    ttbg = True
    ttce = True
    ttcf = True
    ttcg = True
    ttde = True
    ttdf = True
    ttdg = True
    ttee = True
    ttef = True
    tteg = True
    ttfe = True
    ttff = True
    ttfg = True
    ttge = True
    ttgf = True
    ttgg = True
    tthe = True
    tthf = True
    tthg = True
    ttie = True
    ttif = True
    ttig = True
    ttje = True
    ttjf = True
    ttjg = True
    ttah = True
    ttai = True
    ttaj = True
    ttbh = True
    ttbi = True
    ttbj = True
    ttch = True
    ttci = True
    ttcj = True
    ttdh = True
    ttdi = True
    ttdj = True
    tteh = True
    ttei = True
    ttej = True
    ttfh = True
    ttfi = True
    ttfj = True
    ttgh = True
    ttgi = True
    ttgj = True
    tthh = True
    tthi = True
    tthj = True
    ttih = True
    ttii = True
    ttij = True
    ttjh = True
    ttji = True
    ttjj = True

    global youloss
    youloss = str("You loss! Try again!")

    show = True

def showallfinally():

    global tta
    global ttb
    global ttc
    global ttd
    global tte
    global ttf
    global ttg
    global tth
    global tti
    global ttj
    global ttk
    global ttl
    global ttm
    global ttn
    global tto
    global ttp
    global ttq
    global ttr
    global tts
    global ttt
    global ttu
    global ttv
    global ttw
    global ttx
    global tty
    global ttz
    global ttbc
    global ttbd
    global ttaa
    global ttab
    global ttac
    global ttad
    global ttia
    global ttib
    global ttic
    global ttid
    global ttja
    global ttjb
    global ttjc
    global ttjd
    global ttae
    global ttaf
    global ttag
    global ttbe
    global ttbf
    global ttbg
    global ttce
    global ttcf
    global ttcg
    global ttde
    global ttdf
    global ttdg
    global ttee
    global ttef
    global tteg
    global ttfe
    global ttff
    global ttfg
    global ttge
    global ttgf
    global ttgg
    global tthe
    global tthf
    global tthg
    global ttie
    global ttif
    global ttig
    global ttje
    global ttjf
    global ttjg
    global ttah
    global ttai
    global ttaj
    global ttbh
    global ttbi
    global ttbj
    global ttch
    global ttci
    global ttcj
    global ttdh
    global ttdi
    global ttdj
    global tteh
    global ttei
    global ttej
    global ttfh
    global ttfi
    global ttfj
    global ttgh
    global ttgi
    global ttgj
    global tthh
    global tthi
    global tthj
    global ttih
    global ttii
    global ttij
    global ttjh
    global ttji
    global ttjj



    tta = True
    ttb = True
    ttc = True
    ttd = True
    tte = True
    ttf = True
    ttg = True
    tth = True
    tti = True
    ttj = True
    ttk = True
    ttl = True
    ttm = True
    ttn = True
    tto = True
    ttp = True
    ttq = True
    ttr = True
    tts = True
    ttt = True
    ttu = True
    ttv = True
    ttw = True
    ttx = True
    tty = True
    ttz = True
    ttbc = True
    ttbd = True
    ttaa = True
    ttab = True
    ttac = True
    ttad = True
    ttia = True
    ttib = True
    ttic = True
    ttid = True
    ttja = True
    ttjb = True
    ttjc = True
    ttjd = True
    ttae = True
    ttaf = True
    ttag = True
    ttbe = True
    ttbf = True
    ttbg = True
    ttce = True
    ttcf = True
    ttcg = True
    ttde = True
    ttdf = True
    ttdg = True
    ttee = True
    ttef = True
    tteg = True
    ttfe = True
    ttff = True
    ttfg = True
    ttge = True
    ttgf = True
    ttgg = True
    tthe = True
    tthf = True
    tthg = True
    ttie = True
    ttif = True
    ttig = True
    ttje = True
    ttjf = True
    ttjg = True
    ttah = True
    ttai = True
    ttaj = True
    ttbh = True
    ttbi = True
    ttbj = True
    ttch = True
    ttci = True
    ttcj = True
    ttdh = True
    ttdi = True
    ttdj = True
    tteh = True
    ttei = True
    ttej = True
    ttfh = True
    ttfi = True
    ttfj = True
    ttgh = True
    ttgi = True
    ttgj = True
    tthh = True
    tthi = True
    tthj = True
    ttih = True
    ttii = True
    ttij = True
    ttjh = True
    ttji = True
    ttjj = True

def game_control():

    control = True
    
    global minenumber
    global minefindb 
    global minefindc 
    global minefindd
    global minefinde
    global minefindf
    global minefinda
    global minefindg
    global minefindh
    global minefindi
    global minefindj
    global minefindk
    global minefindl
    global minefindm
    global minefindn
    global minefindo
    global minefindp
    global minefindq
    global minefindr
    global minefinds
    global minefindt
    global minefindu
    global minefindv
    global minefindw
    global minefindx
    global minefindy
    global minefindz
    global minefindbc
    global minefindbd
    global minefindaa
    global minefindab
    global minefindac
    global minefindad
    global minefindia
    global minefindib
    global minefindic
    global minefindid
    global minefindja
    global minefindjb
    global minefindjc
    global minefindjd
    global minefindae
    global minefindaf
    global minefindag
    global minefindbe 
    global minefindbf
    global minefindbg
    global minefindce 
    global minefindcf 
    global minefindcg 
    global minefindde
    global minefinddf
    global minefinddg
    global minefindee
    global minefindef
    global minefindeg
    global minefindfe
    global minefindff
    global minefindfg
    global minefindge
    global minefindgf
    global minefindgg
    global minefindhe
    global minefindhf
    global minefindhg
    global minefindie
    global minefindif
    global minefindig
    global minefindje
    global minefindjf
    global minefindjg
    global minefindah
    global minefindai
    global minefindaj
    global minefindbh
    global minefindbi 
    global minefindbj 
    global minefindch
    global minefindci 
    global minefindcj
    global minefinddh
    global minefinddi
    global minefinddj
    global minefindeh
    global minefindei
    global minefindej
    global minefindfh
    global minefindfi
    global minefindfj
    global minefindgh
    global minefindgi
    global minefindgj
    global minefindhh
    global minefindhi
    global minefindhj
    global minefindjh
    global minefindji
    global minefindjj
    
    while control:
        gameDisplay.fill(bluegreen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        buttonquit("",50,350,50,30, yellow, light_yellow, action = "lossquit")

        
        button("",400,379,20,20, black, grey, green, action = "a")
        button("",400,400,20,20, black, grey, green, action = "b")
        button("",400,358,20,20, black, grey, green, action = "c")
        button("",379,379,20,20, black, grey, green, action = "d")
        button("",379,400,20,20, black, grey, green, action = "e")
        button("",379,358,20,20, black, grey, green, action = "f")
        button("",358,379,20,20, black, grey, green, action = "g")
        button("",358,358,20,20, black, grey, green, action = "h")
        button("",358,400,20,20, black, grey, green, action = "i")
        button("",337,358,20,20, black, grey, green, action = "j")
        button("",337,379,20,20, black, grey, green, action = "k")
        button("",337,400,20,20, black, grey, green, action = "l")
        button("",316,358,20,20, black, grey, green, action = "m")
        button("",316,379,20,20, black, grey, green, action = "n")
        button("",316,400,20,20, black, grey, green, action = "o")
        button("",316,337,20,20, black, grey, green, action = "p")
        button("",337,337,20,20, black, grey, green, action = "q")
        button("",358,337,20,20, black, grey, green, action = "r")
        button("",379,337,20,20, black, grey, green, action = "s")
        button("",400,337,20,20, black, grey, green, action = "t")
        button("",295,337,20,20, black, grey, green, action = "u")
        button("",295,358,20,20, black, grey, green, action = "v")
        button("",295,379,20,20, black, grey, green, action = "w")
        button("",295,400,20,20, black, grey, green, action = "x")
        button("",421,400,20,20, black, grey, green, action = "y")
        button("",421,379,20,20, black, grey, green, action = "z")
        button("",421,358,20,20, black, grey, green, action = "bc")
        button("",421,337,20,20, black, grey, green, action = "bd")
        button("",442,400,20,20, black, grey, green, action = "aa")
        button("",442,379,20,20, black, grey, green, action = "ab")
        button("",442,358,20,20, black, grey, green, action = "ac")
        button("",442,337,20,20, black, grey, green, action = "ad")
        button("",274,400,20,20, black, grey, green, action = "ia")
        button("",274,379,20,20, black, grey, green, action = "ib")
        button("",274,358,20,20, black, grey, green, action = "ic")
        button("",274,337,20,20, black, grey, green, action = "id")
        button("",253,400,20,20, black, grey, green, action = "ja")
        button("",253,379,20,20, black, grey, green, action = "jb")
        button("",253,358,20,20, black, grey, green, action = "jc")
        button("",253,337,20,20, black, grey, green, action = "jd")
        button("",442,316,20,20, black, grey, green, action = "ae")
        button("",442,295,20,20, black, grey, green, action = "af")
        button("",442,274,20,20, black, grey, green, action = "ag")
        button("",421,316,20,20, black, grey, green, action = "be")
        button("",421,295,20,20, black, grey, green, action = "bf")
        button("",421,274,20,20, black, grey, green, action = "bg")
        button("",400,316,20,20, black, grey, green, action = "ce")
        button("",400,295,20,20, black, grey, green, action = "cf")
        button("",400,274,20,20, black, grey, green, action = "cg")
        button("",379,316,20,20, black, grey, green, action = "de")
        button("",379,295,20,20, black, grey, green, action = "df")
        button("",379,274,20,20, black, grey, green, action = "dg")
        button("",358,316,20,20, black, grey, green, action = "ee")
        button("",358,295,20,20, black, grey, green, action = "ef")
        button("",358,274,20,20, black, grey, green, action = "eg")
        button("",337,316,20,20, black, grey, green, action = "fe")
        button("",337,295,20,20, black, grey, green, action = "ff")
        button("",337,274,20,20, black, grey, green, action = "fg")
        button("",316,316,20,20, black, grey, green, action = "ge")
        button("",316,295,20,20, black, grey, green, action = "gf")
        button("",316,274,20,20, black, grey, green, action = "gg")
        button("",295,316,20,20, black, grey, green, action = "he")
        button("",295,295,20,20, black, grey, green, action = "hf")
        button("",295,274,20,20, black, grey, green, action = "hg")
        button("",274,316,20,20, black, grey, green, action = "ie")
        button("",274,295,20,20, black, grey, green, action = "if")
        button("",274,274,20,20, black, grey, green, action = "ig")
        button("",253,316,20,20, black, grey, green, action = "je")
        button("",253,295,20,20, black, grey, green, action = "jf")
        button("",253,274,20,20, black, grey, green, action = "jg")
        button("",442,253,20,20, black, grey, green, action = "ah")
        button("",442,232,20,20, black, grey, green, action = "ai")
        button("",442,211,20,20, black, grey, green, action = "aj")
        button("",421,253,20,20, black, grey, green, action = "bh")
        button("",421,232,20,20, black, grey, green, action = "bi")
        button("",421,211,20,20, black, grey, green, action = "bj")
        button("",400,253,20,20, black, grey, green, action = "ch")
        button("",400,232,20,20, black, grey, green, action = "ci")
        button("",400,211,20,20, black, grey, green, action = "cj")
        button("",379,253,20,20, black, grey, green, action = "dh")
        button("",379,232,20,20, black, grey, green, action = "di")
        button("",379,211,20,20, black, grey, green, action = "dj")
        button("",358,253,20,20, black, grey, green, action = "eh")
        button("",358,232,20,20, black, grey, green, action = "ei")
        button("",358,211,20,20, black, grey, green, action = "ej")
        button("",337,253,20,20, black, grey, green, action = "fh")
        button("",337,232,20,20, black, grey, green, action = "fi")
        button("",337,211,20,20, black, grey, green, action = "fj")
        button("",316,253,20,20, black, grey, green, action = "gh")
        button("",316,232,20,20, black, grey, green, action = "gi")
        button("",316,211,20,20, black, grey, green, action = "gj")
        button("",295,253,20,20, black, grey, green, action = "hh")
        button("",295,232,20,20, black, grey, green, action = "hi")
        button("",295,211,20,20, black, grey, green, action = "hj")
        button("",274,253,20,20, black, grey, green, action = "ih")
        button("",274,232,20,20, black, grey, green, action = "ii")
        button("",274,211,20,20, black, grey, green, action = "ij")
        button("",253,253,20,20, black, grey, green, action = "jh")
        button("",253,232,20,20, black, grey, green, action = "ji")
        button("",253,211,20,20, black, grey, green, action = "jj")

        
        
        if tta == True:
            pygame.draw.rect(gameDisplay, white, (400,379,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorea), True, green, white)
            gameDisplay.blit(text, (405, 379))

        if ttb == True:
            pygame.draw.rect(gameDisplay, white, (400,400,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreb), True, green, white)
            gameDisplay.blit(text, (405, 400))

        if ttc == True:
            pygame.draw.rect(gameDisplay, white, (400,358,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorec), True, green, white)
            gameDisplay.blit(text, (405, 358))

        if ttd == True:
            pygame.draw.rect(gameDisplay, white, (379,379,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scored), True, green, white)
            gameDisplay.blit(text, (384, 379))

        if tte == True:
            pygame.draw.rect(gameDisplay, white, (379,400,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoree), True, green, white)
            gameDisplay.blit(text, (384, 400))

        if ttf == True:
            pygame.draw.rect(gameDisplay, white, (379,358,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoref), True, green, white)
            gameDisplay.blit(text, (384, 358))

        if ttg == True:
            pygame.draw.rect(gameDisplay, white, (358,379,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreg), True, green, white)
            gameDisplay.blit(text, (363, 379))

        if tth == True:
            pygame.draw.rect(gameDisplay, white, (358,358,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreh), True, green, white)
            gameDisplay.blit(text, (363, 358))

        if tti == True:
            pygame.draw.rect(gameDisplay, white, (358,400,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorei), True, green, white)
            gameDisplay.blit(text, (363, 400))

        if ttj == True:
            pygame.draw.rect(gameDisplay, white, (337,358,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorej), True, green, white)
            gameDisplay.blit(text, (342, 358))

        if ttk == True:
            pygame.draw.rect(gameDisplay, white, (337,379,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorek), True, green, white)
            gameDisplay.blit(text, (342, 379))

        if ttl == True:
            pygame.draw.rect(gameDisplay, white, (337,400,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorel), True, green, white)
            gameDisplay.blit(text, (342, 400))

        if ttm == True:
            pygame.draw.rect(gameDisplay, white, (316,358,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorem), True, green, white)
            gameDisplay.blit(text, (321, 358))

        if ttn == True:
            pygame.draw.rect(gameDisplay, white, (316,379,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoren), True, green, white)
            gameDisplay.blit(text, (321, 379))

        if tto == True:
            pygame.draw.rect(gameDisplay, white, (316,400,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreo), True, green, white)
            gameDisplay.blit(text, (321, 400))

        if ttp == True:
            pygame.draw.rect(gameDisplay, white, (316,337,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorep), True, green, white)
            gameDisplay.blit(text, (321, 337))

        if ttq == True:
            pygame.draw.rect(gameDisplay, white, (337,337,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreq), True, green, white)
            gameDisplay.blit(text, (342, 337))

        if ttr == True:
            pygame.draw.rect(gameDisplay, white, (358,337,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorer), True, green, white)
            gameDisplay.blit(text, (363, 337))

        if tts == True:
            pygame.draw.rect(gameDisplay, white, (379,337,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scores), True, green, white)
            gameDisplay.blit(text, (384, 337))

        if ttt == True:
            pygame.draw.rect(gameDisplay, white, (400,337,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoret), True, green, white)
            gameDisplay.blit(text, (405, 337))

        if ttu == True:
            pygame.draw.rect(gameDisplay, white, (295,337,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreu), True, green, white)
            gameDisplay.blit(text, (300, 337))

        if ttv == True:
            pygame.draw.rect(gameDisplay, white, (295,358,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorev), True, green, white)
            gameDisplay.blit(text, (300, 358))

        if ttw == True:
            pygame.draw.rect(gameDisplay, white, (295,379,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorew), True, green, white)
            gameDisplay.blit(text, (300, 379))

        if ttx == True:
            pygame.draw.rect(gameDisplay, white, (295,400,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorex), True, green, white)
            gameDisplay.blit(text, (300, 400))

        if tty == True:
            pygame.draw.rect(gameDisplay, white, (421,400,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorey), True, green, white)
            gameDisplay.blit(text, (426, 400))

        if ttz == True:
            pygame.draw.rect(gameDisplay, white, (421,379,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorez), True, green, white)
            gameDisplay.blit(text, (426, 379))

        if ttbc == True:
            pygame.draw.rect(gameDisplay, white, (421,358,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorebc), True, green, white)
            gameDisplay.blit(text, (426, 358))

        if ttbd == True:
            pygame.draw.rect(gameDisplay, white, (421,337,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorebd), True, green, white)
            gameDisplay.blit(text, (426, 337))

        if ttaa == True:
            pygame.draw.rect(gameDisplay, white, (442,400,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreaa), True, green, white)
            gameDisplay.blit(text, (447, 400))

        if ttab == True:
            pygame.draw.rect(gameDisplay, white, (442,379,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreab), True, green, white)
            gameDisplay.blit(text, (447, 379))

        if ttac == True:
            pygame.draw.rect(gameDisplay, white, (442,358,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreac), True, green, white)
            gameDisplay.blit(text, (447, 358))

        if ttad == True:
            pygame.draw.rect(gameDisplay, white, (442,337,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoread), True, green, white)
            gameDisplay.blit(text, (447, 337))

        if ttia == True:
            pygame.draw.rect(gameDisplay, white, (274,400,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreia), True, green, white)
            gameDisplay.blit(text, (279, 400))

        if ttib == True:
            pygame.draw.rect(gameDisplay, white, (274,379,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreib), True, green, white)
            gameDisplay.blit(text, (279, 379))

        if ttic == True:
            pygame.draw.rect(gameDisplay, white, (274,358,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreic), True, green, white)
            gameDisplay.blit(text, (279, 358))

        if ttid == True:
            pygame.draw.rect(gameDisplay, white, (274,337,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreid), True, green, white)
            gameDisplay.blit(text, (279, 337))

        if ttja == True:
            pygame.draw.rect(gameDisplay, white, (253,400,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreja), True, green, white)
            gameDisplay.blit(text, (258, 400))

        if ttjb == True:
            pygame.draw.rect(gameDisplay, white, (253,379,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorejb), True, green, white)
            gameDisplay.blit(text, (258, 379))

        if ttjc == True:
            pygame.draw.rect(gameDisplay, white, (253,358,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorejc), True, green, white)
            gameDisplay.blit(text, (258, 358))

        if ttjd == True:
            pygame.draw.rect(gameDisplay, white, (253,337,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorejd), True, green, white)
            gameDisplay.blit(text, (258, 337))

        if ttae == True:
            #if number == -1:
                #scorea = "M"
            pygame.draw.rect(gameDisplay, white, (442,316,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreae), True, green, white)
            gameDisplay.blit(text, (447, 316))

        if ttaf == True:
            #if number == -1:
                #scorea = "M"
            pygame.draw.rect(gameDisplay, white, (442,295,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreaf), True, green, white)
            gameDisplay.blit(text, (447, 295))

        if ttag == True:
            #if number == -1:
                #scorea = "M"
            pygame.draw.rect(gameDisplay, white, (442,274,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreag), True, green, white)
            gameDisplay.blit(text, (447, 274))

        if ttbe == True:
            pygame.draw.rect(gameDisplay, white, (421,316,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorebe), True, green, white)
            gameDisplay.blit(text, (426, 316))

        if ttbf == True:
            pygame.draw.rect(gameDisplay, white, (421,295,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorebf), True, green, white)
            gameDisplay.blit(text, (426, 295))

        if ttbg == True:
            pygame.draw.rect(gameDisplay, white, (421,274,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorebg), True, green, white)
            gameDisplay.blit(text, (426, 274))

        if ttce == True:
            pygame.draw.rect(gameDisplay, white, (400,316,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorece), True, green, white)
            gameDisplay.blit(text, (405, 316))

        if ttcf == True:
            pygame.draw.rect(gameDisplay, white, (400,295,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorecf), True, green, white)
            gameDisplay.blit(text, (405, 295))

        if ttcg == True:
            pygame.draw.rect(gameDisplay, white, (400,274,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorecg), True, green, white)
            gameDisplay.blit(text, (405, 274))

        if ttde == True:
            pygame.draw.rect(gameDisplay, white, (379,316,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorede), True, green, white)
            gameDisplay.blit(text, (384, 316))

        if ttdf == True:
            pygame.draw.rect(gameDisplay, white, (379,295,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoredf), True, green, white)
            gameDisplay.blit(text, (384, 295))

        if ttdg == True:
            pygame.draw.rect(gameDisplay, white, (379,274,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoredg), True, green, white)
            gameDisplay.blit(text, (384, 274))

        if ttee == True:
            pygame.draw.rect(gameDisplay, white, (358,316,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreee), True, green, white)
            gameDisplay.blit(text, (363, 316))

        if ttef == True:
            pygame.draw.rect(gameDisplay, white, (358,295,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreef), True, green, white)
            gameDisplay.blit(text, (363, 295))

        if tteg == True:
            pygame.draw.rect(gameDisplay, white, (358,274,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreeg), True, green, white)
            gameDisplay.blit(text, (363, 274))

        if ttfe == True:
            pygame.draw.rect(gameDisplay, white, (337,316,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorefe), True, green, white)
            gameDisplay.blit(text, (342, 316))

        if ttff == True:
            pygame.draw.rect(gameDisplay, white, (337,295,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreff), True, green, white)
            gameDisplay.blit(text, (342, 295))

        if ttfg == True:
            pygame.draw.rect(gameDisplay, white, (337,274,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorefg), True, green, white)
            gameDisplay.blit(text, (342, 274))

        if ttge == True:
            pygame.draw.rect(gameDisplay, white, (316,316,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorege), True, green, white)
            gameDisplay.blit(text, (321, 316))

        if ttgf == True:
            pygame.draw.rect(gameDisplay, white, (316,295,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoregf), True, green, white)
            gameDisplay.blit(text, (321, 295))

        if ttgg == True:
            pygame.draw.rect(gameDisplay, white, (316,274,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoregg), True, green, white)
            gameDisplay.blit(text, (321, 274))

        if tthe == True:
            pygame.draw.rect(gameDisplay, white, (295,316,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorehe), True, green, white)
            gameDisplay.blit(text, (300, 316))

        if tthf == True:
            pygame.draw.rect(gameDisplay, white, (295,295,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorehf), True, green, white)
            gameDisplay.blit(text, (300, 295))

        if tthg == True:
            pygame.draw.rect(gameDisplay, white, (295,274,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorehg), True, green, white)
            gameDisplay.blit(text, (300, 274))

        if ttie == True:
            pygame.draw.rect(gameDisplay, white, (274,316,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreie), True, green, white)
            gameDisplay.blit(text, (279, 316))

        if ttif == True:
            pygame.draw.rect(gameDisplay, white, (274,295,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreif), True, green, white)
            gameDisplay.blit(text, (279, 295))

        if ttig == True:
            pygame.draw.rect(gameDisplay, white, (274,274,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreig), True, green, white)
            gameDisplay.blit(text, (279, 274))

        if ttje == True:
            pygame.draw.rect(gameDisplay, white, (253,316,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreje), True, green, white)
            gameDisplay.blit(text, (258, 316))

        if ttjf == True:
            pygame.draw.rect(gameDisplay, white, (253,295,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorejf), True, green, white)
            gameDisplay.blit(text, (258, 295))

        if ttjg == True:
            pygame.draw.rect(gameDisplay, white, (253,274,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorejg), True, green, white)
            gameDisplay.blit(text, (258, 274))

        if ttah == True:
            #if number == -1:
                #scorea = "M"
            pygame.draw.rect(gameDisplay, white, (442,253,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreah), True, green, white)
            gameDisplay.blit(text, (447, 253))

        if ttai == True:
            #if number == -1:
                #scorea = "M"
            pygame.draw.rect(gameDisplay, white, (442,232,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreai), True, green, white)
            gameDisplay.blit(text, (447, 232))

        if ttaj == True:
            #if number == -1:
                #scorea = "M"
            pygame.draw.rect(gameDisplay, white, (442,211,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreaj), True, green, white)
            gameDisplay.blit(text, (447, 211))

        if ttbh == True:
            pygame.draw.rect(gameDisplay, white, (421,253,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorebh), True, green, white)
            gameDisplay.blit(text, (426, 253))

        if ttbi == True:
            pygame.draw.rect(gameDisplay, white, (421,232,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorebi), True, green, white)
            gameDisplay.blit(text, (426, 232))

        if ttbj == True:
            pygame.draw.rect(gameDisplay, white, (421,211,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorebj), True, green, white)
            gameDisplay.blit(text, (426, 211))

        if ttch == True:
            pygame.draw.rect(gameDisplay, white, (400,253,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorech), True, green, white)
            gameDisplay.blit(text, (405, 253))

        if ttci == True:
            pygame.draw.rect(gameDisplay, white, (400,232,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreci), True, green, white)
            gameDisplay.blit(text, (405, 232))

        if ttcj == True:
            pygame.draw.rect(gameDisplay, white, (400,211,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorecj), True, green, white)
            gameDisplay.blit(text, (405, 211))

        if ttdh == True:
            pygame.draw.rect(gameDisplay, white, (379,253,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoredh), True, green, white)
            gameDisplay.blit(text, (384, 253))

        if ttdi == True:
            pygame.draw.rect(gameDisplay, white, (379,232,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoredi), True, green, white)
            gameDisplay.blit(text, (384, 232))

        if ttdj == True:
            pygame.draw.rect(gameDisplay, white, (379,211,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoredj), True, green, white)
            gameDisplay.blit(text, (384, 211))

        if tteh == True:
            pygame.draw.rect(gameDisplay, white, (358,253,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreeh), True, green, white)
            gameDisplay.blit(text, (363, 253))

        if ttei == True:
            pygame.draw.rect(gameDisplay, white, (358,232,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreei), True, green, white)
            gameDisplay.blit(text, (363, 232))

        if ttej == True:
            pygame.draw.rect(gameDisplay, white, (358,211,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreej), True, green, white)
            gameDisplay.blit(text, (363, 211))

        if ttfh == True:
            pygame.draw.rect(gameDisplay, white, (337,253,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorefh), True, green, white)
            gameDisplay.blit(text, (342, 253))

        if ttfi == True:
            pygame.draw.rect(gameDisplay, white, (337,232,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorefi), True, green, white)
            gameDisplay.blit(text, (342, 232))

        if ttfj == True:
            pygame.draw.rect(gameDisplay, white, (337,211,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorefj), True, green, white)
            gameDisplay.blit(text, (342, 211))

        if ttgh == True:
            pygame.draw.rect(gameDisplay, white, (316,253,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoregh), True, green, white)
            gameDisplay.blit(text, (321, 253))

        if ttgi == True:
            pygame.draw.rect(gameDisplay, white, (316,232,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoregi), True, green, white)
            gameDisplay.blit(text, (321, 232))

        if ttgj == True:
            pygame.draw.rect(gameDisplay, white, (316,211,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoregj), True, green, white)
            gameDisplay.blit(text, (321, 211))

        if tthh == True:
            pygame.draw.rect(gameDisplay, white, (295,253,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorehh), True, green, white)
            gameDisplay.blit(text, (300, 253))

        if tthi == True:
            pygame.draw.rect(gameDisplay, white, (295,232,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorehi), True, green, white)
            gameDisplay.blit(text, (300, 232))

        if tthj == True:
            pygame.draw.rect(gameDisplay, white, (295,211,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorehj), True, green, white)
            gameDisplay.blit(text, (300, 211))

        if ttih == True:
            pygame.draw.rect(gameDisplay, white, (274,253,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreih), True, green, white)
            gameDisplay.blit(text, (279, 253))

        if ttii == True:
            pygame.draw.rect(gameDisplay, white, (274,232,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreii), True, green, white)
            gameDisplay.blit(text, (279, 232))

        if ttij == True:
            pygame.draw.rect(gameDisplay, white, (274,211,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreij), True, green, white)
            gameDisplay.blit(text, (279, 211))

        if ttjh == True:
            pygame.draw.rect(gameDisplay, white, (253,253,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorejh), True, green, white)
            gameDisplay.blit(text, (258, 253))

        if ttji == True:
            pygame.draw.rect(gameDisplay, white, (253,232,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scoreji), True, green, white)
            gameDisplay.blit(text, (258, 232))

        if ttjj == True:
            pygame.draw.rect(gameDisplay, white, (253,211,20,20))
            basicfont = pygame.font.SysFont(None, 26)
            text = basicfont.render(str(scorejj), True, green, white)
            gameDisplay.blit(text, (258, 211))

        if tta == "MINE":
            pygame.draw.rect(gameDisplay, red, (400,379,20,20))
            if score_a == -1:
                minefinda = 0

        if ttb == "MINE":
            pygame.draw.rect(gameDisplay, red, (400,400,20,20))
            if score_b == -1:
                minefindb = 0

        if ttc == "MINE":
            pygame.draw.rect(gameDisplay, red, (400,358,20,20))
            if score_c == -1:
                minefindc = 0

        if ttd == "MINE":
            pygame.draw.rect(gameDisplay, red, (379,379,20,20))
            if score_d == -1:
                minefindd = 0


        if tte == "MINE":
            pygame.draw.rect(gameDisplay, red, (379,400,20,20))
            if score_e == -1:
                minefinde = 0


        if ttf == "MINE":
            pygame.draw.rect(gameDisplay, red, (379,358,20,20))
            if score_f == -1:
                minefindf = 0


        if ttg == "MINE":
            pygame.draw.rect(gameDisplay, red, (358,379,20,20))
            if score_g == -1:
                minefindg = 0
            
        if tth == "MINE":
            pygame.draw.rect(gameDisplay, red, (358,358,20,20))
            if score_h == -1:
                minefindh = 0

        if tti == "MINE":
            pygame.draw.rect(gameDisplay, red, (358,400,20,20))
            if score_i == -1:
                minefindi = 0
            
        if ttj == "MINE":
            pygame.draw.rect(gameDisplay, red, (337,358,20,20))
            if score_j == -1:
                minefindj = 0

      

        if ttk == "MINE":
            pygame.draw.rect(gameDisplay, red, (337,379,20,20))
            if score_k == -1:
                minefindk = 0


            
      

        if ttl == "MINE":
            pygame.draw.rect(gameDisplay, red, (337,400,20,20))
            if score_l == -1:
                minefindl = 0


     

        if ttm == "MINE":
            pygame.draw.rect(gameDisplay, red, (316,358,20,20))
            if score_m == -1:
                minefindm = 0


 

        if ttn == "MINE":
            pygame.draw.rect(gameDisplay, red, (316,379,20,20))
            if score_n == -1:
                minefindn = 0


 
        if tto == "MINE":
            pygame.draw.rect(gameDisplay, red, (316,400,20,20))
            if score_o == -1:
                minefindo = 0


 

        if ttp == "MINE":
            pygame.draw.rect(gameDisplay, red, (316,337,20,20))
            if score_p == -1:
                minefindp = 0


 
        if ttq == "MINE":
            pygame.draw.rect(gameDisplay, red, (337,337,20,20))
            if score_q == -1:
                minefindq = 0


 
        if ttr == "MINE":
            pygame.draw.rect(gameDisplay, red, (358,337,20,20))
            if score_r == -1:
                minefindr = 0


 
        if tts == "MINE":
            pygame.draw.rect(gameDisplay, red, (379,337,20,20))
            if score_s == -1:
                minefinds = 0


 
        if ttt == "MINE":
            pygame.draw.rect(gameDisplay, red, (400,337,20,20))
            if score_t == -1:
                minefindt = 0


 
        if ttu == "MINE":
            pygame.draw.rect(gameDisplay, red, (295,337,20,20))
            if score_u == -1:
                minefindu = 0


 
        if ttv == "MINE":
            pygame.draw.rect(gameDisplay, red, (295,358,20,20))
            if score_v == -1:
                minefindv = 0



        if ttw == "MINE":
            pygame.draw.rect(gameDisplay, red, (295,379,20,20))
            if score_w == -1:
                minefindw = 0


   
        if ttx == "MINE":
            pygame.draw.rect(gameDisplay, red, (295,400,20,20))
            if score_x == -1:
                minefindx = 0


 
        if tty == "MINE":
            pygame.draw.rect(gameDisplay, red, (421,400,20,20))
            if score_y == -1:
                minefindy = 0



        if ttz == "MINE":
            pygame.draw.rect(gameDisplay, red, (421,379,20,20))
            if score_z == -1:
                minefindz = 0


 
        if ttbc == "MINE":
            pygame.draw.rect(gameDisplay, red, (421,358,20,20))
            if score_bc == -1:
                minefindbc = 0



        if ttbd == "MINE":
            pygame.draw.rect(gameDisplay, red, (421,337,20,20))
            if score_bd == -1:
                minefindbd = 0


 
        if ttaa == "MINE":
            pygame.draw.rect(gameDisplay, red, (442,400,20,20))
            if score_aa == -1:
                minefindaa = 0


 
        if ttab == "MINE":
            pygame.draw.rect(gameDisplay, red, (442,379,20,20))
            if score_ab == -1:
                minefindab = 0


 
        if ttac == "MINE":
            pygame.draw.rect(gameDisplay, red, (442,358,20,20))
            if score_ac == -1:
                minefindac = 0


 
        if ttad == "MINE":
            pygame.draw.rect(gameDisplay, red, (442,337,20,20))
            if score_ad == -1:
                minefindad = 0


 
        if ttia == "MINE":
            pygame.draw.rect(gameDisplay, red, (274,400,20,20))
            if score_ia == -1:
                minefindia = 0


 
        if ttib == "MINE":
            pygame.draw.rect(gameDisplay, red, (274,379,20,20))
            if score_ib == -1:
                minefindib = 0


 
        if ttic == "MINE":
            pygame.draw.rect(gameDisplay, red, (274,358,20,20))
            if score_ic == -1:
                minefindic = 0


 
        if ttid == "MINE":
            pygame.draw.rect(gameDisplay, red, (274,337,20,20))
            if score_id == -1:
                minefindid = 0


 
        if ttja == "MINE":
            pygame.draw.rect(gameDisplay, red, (253,400,20,20))
            if score_ja == -1:
                minefindja = 0


 
        if ttjb == "MINE":
            pygame.draw.rect(gameDisplay, red, (253,379,20,20))
            if score_jb == -1:
                minefindjb = 0


 
        if ttjc == "MINE":
            pygame.draw.rect(gameDisplay, red, (253,358,20,20))
            if score_jc == -1:
                minefindjc = 0


 
        if ttjd == "MINE":
            pygame.draw.rect(gameDisplay, red, (253,337,20,20))
            if score_jd == -1:
                minefindjd = 0


 
        if ttae == "MINE":
            #if number == -1:
                #scorea = "M"
            pygame.draw.rect(gameDisplay, red, (442,316,20,20))
            if score_ae == -1:
                minefindae = 0


 
        if ttaf == "MINE":
            #if number == -1:
                #scorea = "M"
            pygame.draw.rect(gameDisplay, red, (442,295,20,20))
            if score_af == -1:
                minefindaf = 0



        if ttag == "MINE":
            #if number == -1:
                #scorea = "M"
            pygame.draw.rect(gameDisplay, red, (442,274,20,20))
            if score_ag == -1:
                minefindag = 0


 
        if ttbe == "MINE":
            pygame.draw.rect(gameDisplay, red, (421,316,20,20))
            if score_be == -1:
                minefindbe = 0


 
        if ttbf == "MINE":
            pygame.draw.rect(gameDisplay, red, (421,295,20,20))
            if score_bf == -1:
                minefindbf = 0


 
        if ttbg == "MINE":
            pygame.draw.rect(gameDisplay, red, (421,274,20,20))
            if score_bg == -1:
                minefindbg = 0


 
        if ttce == "MINE":
            pygame.draw.rect(gameDisplay, red, (400,316,20,20))
            if score_ce == -1:
                minefindce = 0


 
        if ttcf == "MINE":
            pygame.draw.rect(gameDisplay, red, (400,295,20,20))
            if score_cf == -1:
                minefindcf = 0


 
        if ttcg == "MINE":
            pygame.draw.rect(gameDisplay, red, (400,274,20,20))
            if score_cg == -1:
                minefindcg = 0


 
        if ttde == "MINE":
            pygame.draw.rect(gameDisplay, red, (379,316,20,20))
            if score_de == -1:
                minefindde = 0


 
        if ttdf == "MINE":
            pygame.draw.rect(gameDisplay, red, (379,295,20,20))
            if score_df == -1:
                minefinddf = 0



        if ttdg == "MINE":
            pygame.draw.rect(gameDisplay, red, (379,274,20,20))
            if score_dg == -1:
                minefinddg = 0


 
        if ttee == "MINE":
            pygame.draw.rect(gameDisplay, red, (358,316,20,20))
            if score_ee == -1:
                minefindee = 0



        if ttef == "MINE":
            pygame.draw.rect(gameDisplay, red, (358,295,20,20))
            if score_ef == -1:
                minefindef = 0


 
        if tteg == "MINE":
            pygame.draw.rect(gameDisplay, red, (358,274,20,20))
            if score_eg == -1:
                minefindeg = 0


 
        if ttfe == "MINE":
            pygame.draw.rect(gameDisplay, red, (337,316,20,20))
            if score_fe == -1:
                minefindfe = 0



        if ttff == "MINE":
            pygame.draw.rect(gameDisplay, red, (337,295,20,20))
            if score_ff == -1:
                minefindff = 0


 
        if ttfg == "MINE":
            pygame.draw.rect(gameDisplay, red, (337,274,20,20))
            if score_fg == -1:
                minefindfg = 0


 
        if ttge == "MINE":
            pygame.draw.rect(gameDisplay, red, (316,316,20,20))
            if score_ge == -1:
                minefindge = 0


 
        if ttgf == "MINE":
            pygame.draw.rect(gameDisplay, red, (316,295,20,20))
            if score_gf == -1:
                minefindgf = 0



        if ttgg == "MINE":
            pygame.draw.rect(gameDisplay, red, (316,274,20,20))
            if score_gg == -1:
                minefindgg = 0


 
        if tthe == "MINE":
            pygame.draw.rect(gameDisplay, red, (295,316,20,20))
            if score_he == -1:
                minefindhe = 0


 
        if tthf == "MINE":
            pygame.draw.rect(gameDisplay, red, (295,295,20,20))
            if score_hf == -1:
                minefindhf = 0


 
        if tthg == "MINE":
            pygame.draw.rect(gameDisplay, red, (295,274,20,20))
            if score_hg == -1:
                minefindhg = 0


 
        if ttie == "MINE":
            pygame.draw.rect(gameDisplay, red, (274,316,20,20))
            if score_ie == -1:
                minefindie = 0


 
        if ttif == "MINE":
            pygame.draw.rect(gameDisplay, red, (274,295,20,20))
            if score_if == -1:
                minefindif = 0


 
        if ttig == "MINE":
            pygame.draw.rect(gameDisplay, red, (274,274,20,20))
            if score_ig == -1:
                minefindig = 0


 
        if ttje == "MINE":
            pygame.draw.rect(gameDisplay, red, (253,316,20,20))
            if score_je == -1:
                minefindje = 0


 
        if ttjf == "MINE":
            pygame.draw.rect(gameDisplay, red, (253,295,20,20))
            if score_jf == -1:
                minefindjf = 0


 
        if ttjg == "MINE":
            pygame.draw.rect(gameDisplay, red, (253,274,20,20))
            if score_jg == -1:
                minefindjg = 0


 
        if ttah == "MINE":
            #if number == -1:
                #scorea = "M"
            pygame.draw.rect(gameDisplay, red, (442,253,20,20))
            if score_ah == -1:
                minefindah = 0


 
        if ttai == "MINE":
            #if number == -1:
                #scorea = "M"
            pygame.draw.rect(gameDisplay, red, (442,232,20,20))
            if score_ai == -1:
                minefindai = 0


 
        if ttaj == "MINE":
            #if number == -1:
                #scorea = "M"
            pygame.draw.rect(gameDisplay, red, (442,211,20,20))
            if score_aj == -1:
                minefindaj = 0


 
        if ttbh == "MINE":
            pygame.draw.rect(gameDisplay, red, (421,253,20,20))
            if score_bh == -1:
                minefindbh = 0


 
        if ttbi == "MINE":
            pygame.draw.rect(gameDisplay, red, (421,232,20,20))
            if score_bi == -1:
                minefindbi = 0


 
        if ttbj == "MINE":
            pygame.draw.rect(gameDisplay, red, (421,211,20,20))
            if score_bj == -1:
                minefindbj = 0


 
        if ttch == "MINE":
            pygame.draw.rect(gameDisplay, red, (400,253,20,20))
            if score_ch == -1:
                minefindch = 0


 
        if ttci == "MINE":
            pygame.draw.rect(gameDisplay, red, (400,232,20,20))
            if score_ci == -1:
                minefindci = 0


 
        if ttcj == "MINE":
            pygame.draw.rect(gameDisplay, red, (400,211,20,20))
            if score_cj == -1:
                minefindcj = 0


 
        if ttdh == "MINE":
            pygame.draw.rect(gameDisplay, red, (379,253,20,20))
            if score_dh == -1:
                minefinddh = 0


 
        if ttdi == "MINE":
            pygame.draw.rect(gameDisplay, red, (379,232,20,20))
            if score_di == -1:
                minefinddi = 0


 
        if ttdj == "MINE":
            pygame.draw.rect(gameDisplay, red, (379,211,20,20))
            if score_dj == -1:
                minefinddj = 0


 
        if tteh == "MINE":
            pygame.draw.rect(gameDisplay, red, (358,253,20,20))
            if score_eh == -1:
                minefindeh = 0


 
        if ttei == "MINE":
            pygame.draw.rect(gameDisplay, red, (358,232,20,20))
            if score_ei == -1:
                minefindei = 0


 
        if ttej == "MINE":
            pygame.draw.rect(gameDisplay, red, (358,211,20,20))
            if score_ej == -1:
                minefindej = 0


 
        if ttfh == "MINE":
            pygame.draw.rect(gameDisplay, red, (337,253,20,20))
            if score_fh == -1:
                minefindfh = 0



        if ttfi == "MINE":
            pygame.draw.rect(gameDisplay, red, (337,232,20,20))
            if score_fi == -1:
                minefindfi = 0



        if ttfj == "MINE":
            pygame.draw.rect(gameDisplay, red, (337,211,20,20))
            if score_fj == -1:
                minefindfj = 0


 
        if ttgh == "MINE":
            pygame.draw.rect(gameDisplay, red, (316,253,20,20))
            if score_gh == -1:
                minefindgh = 0



        if ttgi == "MINE":
            pygame.draw.rect(gameDisplay, red, (316,232,20,20))
            if score_gi == -1:
                minefindgi = 0


 
        if ttgj == "MINE":
            pygame.draw.rect(gameDisplay, red, (316,211,20,20))
            if score_gj == -1:
                minefindgj = 0


 
        if tthh == "MINE":
            pygame.draw.rect(gameDisplay, red, (295,253,20,20))
            if score_hh == -1:
                minefindhh = 0


 
        if tthi == "MINE":
            pygame.draw.rect(gameDisplay, red, (295,232,20,20))
            if score_hi == -1:
                minefindhi = 0



        if tthj == "MINE":
            pygame.draw.rect(gameDisplay, red, (295,211,20,20))
            if score_hj == -1:
                minefindhj = 0


 
        if ttih == "MINE":
            pygame.draw.rect(gameDisplay, red, (274,253,20,20))
            if score_ih == -1:
                minefindih = 0



        if ttii == "MINE":
            pygame.draw.rect(gameDisplay, red, (274,232,20,20))
            if score_ii == -1:
                minefindii = 0


 
        if ttij == "MINE":
            pygame.draw.rect(gameDisplay, red, (274,211,20,20))
            if score_ij == -1:
                minefindij = 0


 
        if ttjh == "MINE":
            pygame.draw.rect(gameDisplay, red, (253,253,20,20))
            if score_jh == -1:
                minefindjh = 0


 
        if ttji == "MINE":
            pygame.draw.rect(gameDisplay, red, (253,232,20,20))
            if score_ji == -1:
                minefindji = 0


 
        if ttjj == "MINE":
            pygame.draw.rect(gameDisplay, red, (253,211,20,20))
            if score_jj == -1:
                minefindjj = 0


        basicfont = pygame.font.SysFont(None, 30)
        text = basicfont.render(str(minenumber), True, white, bluegreen)
        gameDisplay.blit(text, (280, 107))
        basicfont = pygame.font.SysFont(None, 25)
        text = basicfont.render(str(mine_number), True, white, bluegreen)
        gameDisplay.blit(text, (165, 108))

        if minefinda == 0 and minefindb == 0 and minefindc == 0 and minefindd == 0 and minefinde == 0 and minefindf == 0 and minefinda == 0 and minefindg == 0 and minefindh == 0 and minefindi == 0 and minefindj == 0 and minefindk == 0 and minefindl == 0 and minefindm == 0 and minefindn == 0 and minefindo == 0 and minefindp == 0 and minefindq == 0 and minefindr == 0 and minefinds == 0 and minefindt == 0 and minefindu == 0 and minefindv == 0 and minefindw == 0 and minefindx == 0 and minefindy == 0 and minefindz == 0 and minefindbc == 0 and minefindbd == 0 and minefindaa == 0 and minefindab == 0 and minefindac == 0 and minefindad == 0 and minefindia == 0 and minefindib == 0 and minefindic == 0 and minefindid == 0 and minefindja == 0 and minefindjb == 0 and minefindjc == 0 and minefindjd == 0 and minefindae == 0 and minefindaf == 0 and minefindag == 0 and minefindbe == 0 and minefindbf == 0 and minefindbg == 0 and minefindce == 0 and minefindcf == 0 and minefindcg == 0 and minefindde == 0 and minefinddf == 0 and minefinddg == 0 and minefindee == 0 and minefindef == 0 and minefindeg == 0 and minefindfe == 0 and minefindff == 0 and minefindfg == 0 and minefindge == 0 and minefindgf == 0 and minefindgg == 0 and minefindhe == 0 and minefindhf == 0 and minefindhg == 0 and minefindie == 0 and minefindif == 0 and minefindig == 0 and minefindje == 0 and minefindjf == 0 and minefindjg == 0 and minefindah == 0 and minefindai == 0 and minefindaj == 0 and minefindbh == 0 and minefindbi == 0 and minefindbj == 0 and minefindch == 0 and minefindci == 0 and minefindcj == 0 and minefinddh == 0 and minefinddi == 0 and minefinddj == 0 and minefindeh == 0 and minefindei == 0 and minefindej == 0 and minefindfh == 0 and minefindfi == 0 and minefindfj == 0 and minefindgh == 0 and minefindgi == 0 and minefindgj == 0 and minefindhh == 0 and minefindhi == 0 and minefindhj == 0 and minefindjh == 0 and minefindjh == 0 and minefindjj == 0:
            basicfont = pygame.font.SysFont(None, 60)
            text = basicfont.render(str(youwin), True, white, bluegreen)
            gameDisplay.blit(text, (200, 150))
            showallfinally()
            explosion()

        if show == True:
            basicfont = pygame.font.SysFont(None, 60)
            text = basicfont.render(str(youloss), True, white, bluegreen)
            gameDisplay.blit(text, (200, 150))

                   
        basicfont = pygame.font.SysFont(None, 25)
        text = basicfont.render(str(gametime), True, white, bluegreen)
        gameDisplay.blit(text, (400, 108))

        global gameclock
        gameclock += 1
        basicfont = pygame.font.SysFont(None, 30)
        text = basicfont.render(str(gameclock//56), True, white, bluegreen)
        gameDisplay.blit(text, (450, 107))


        basicfont = pygame.font.SysFont(None, 30)
        text = basicfont.render(str(lossquit), True, white, bluegreen)
        gameDisplay.blit(text, (51, 320))
        
        
        pygame.display.update()
        clock.tick(FPS)


    pygame.quit()
    sys.exit()
    quit()


game_intro()

game_control()






