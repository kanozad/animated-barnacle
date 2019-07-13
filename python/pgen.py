import re
import os
import string
import random

SPECIAL = '!@#$%&*'
# SPECIAL = '~!@#$%^&*_+-=:;?.'

CHARS = string.ascii_letters + string.digits + SPECIAL
RE_STRING = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[" + SPECIAL + "])"


def main(args):
    random.seed = (os.urandom(1024))
    for i in range(args.count):
        print(getPassword(args.length, args.validate, args.chars, args.rule))


def getPassword(length, validate, chars, rule):
    validation_rule = re.compile(rule)
    while True:
        x = ''.join(random.choice(chars) for i in range(length))
        if validate:
            if not validation_rule.search(x):
                continue
        return x


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--length",
        help="set password length (DEFAULT=10)",
        default=10,
        type=int)
    parser.add_argument(
        "-c",
        "--count",
        help="number of passwords to generate (DEFAULT=10)",
        default=10,
        type=int)
    parser.add_argument(
        "-d",
        "--display",
        help="display valid character set and validation rule and exit",
        action="store_true")
    parser.add_argument(
        "-v",
        "--validate",
        help="validate passwords",
        action="store_true")
    parser.add_argument(
        "-ch",
        "--chars",
        help="use the specified character set",
        default=CHARS)
    parser.add_argument(
        "-ra",
        "--remove-ambiguity",
        help="don't use ambiguous characters (1l0O)",
        action="store_true")
    parser.add_argument(
        "-r",
        "--rule",
        help="use the specified (regex) rule to validate passwords - no effect if -v isn't also specified",
        default=RE_STRING)

    args = parser.parse_args()

    if(args.remove_ambiguity):
        args.chars = re.sub('[1l0O]', '', args.chars)
    if args.display:
        print(args.chars)
        print(args.rule)
        import sys
        sys.exit()

    main(args)

"""

nizp%*k99L&gZUqLGU7$W7BXVfN3ZWuFEIQg9Ed9ZrbkebfBBw3qByI$k!ska*7KmNy2EPJEdrI%$QQpBH8s#8gv69tBjqI3jw!W
koGQ9zJ@@uLHMfqa8cQ9U$2XwqrrFgbYInMYcv&r%RmQ8DsoWAXymimUHBRRU9FriGGaW@r%MkKRuWQIaLhMvGKhS*ERgx7hqU5!
GkpwJtRI8bcPmmiV23sxjiH9ojMb@7pZ#RJ!&n9NpBaoQZWH9XPCFursDLdtwcBt#&fsvCw5ew8gDRMr52C5DM!RIPg7axAvnLvy
&5yTG@cxFvoW8B3D73PLLRsLtoM!zvWk@g5Bcx4BihftsSfkQUwgtx6@#o7z3vyQW9M$vMiTohqC6gWWYJ@hSM5x3RuEW9mmtfa&
aXWC@#YR$9hZKN*M!Ncd!A7!h2TTnuXY5SHYPGg76!&7mK3NSL%u9v9DdPKWcn%4zupay$c99ndfgVxdDbt86P3n3cFMXNh9Y452
$&w%zbmtrJ@%Xzk4v97eGC#4AY8b8h*eFhXja!wMJ#gDE6%R!WB!sjpgj%XejukE4q#3YuPsoXT*EEoiPptW6yk5uiiIjG@BSNIG
NivrYZpCx*@UiukKzqcDuMCk2o$jC#&!qwTb*wyzyzcRn8XuDpMMTPQGB$iwUGR2FSzVHV&k8QvnLR6UWf8PvXUrS%tYci5m9BJ8
BD@K2g4CaikPkypYt888g@bMmExz52SRYIpBuLhH$*BFUuCwG#r5##fy6Y9B&f*D3Ii3I$qZ4syDIj6XXxV!&iUag9NsFxUn%t&8
oy#v3!Tz4b&evr4BksoNC%qWc4UV56PHbagVaJq5vUm5k%&FSPFWWeD*#ApEyx7F!KDBs3ByIdr5kfSAv&8wU%fBT*DcjcqtF#$n
zgjhqY5HI6iFJ87dxA#$JCgS!LRHQLIEpepnTvWY5SCVgrxywcqP75FVdvDShEeVdHxW%AbjH!vPWH5SShdTr7rgEDFA*%9%dgQY
Zszy3&EvBKymsid%TcpGEJbzMhqcswvGg%&p@Xa$h7n%mQbbFGoLj925qQQBFdWnsJN6!ttzHhNVbqYunoUh2xHqzTAxGxFkuLB#
C!kqxgvEWzh8&oLq@zKaE6XJftBwQSmI%WbqV6GJNUJsgqy8UgxIM45t2rpYRqerPnSDKn45GM&E@24F5Jb#WrGjC8*yjId*uqyM
VVsLD*!hTk#&rX&3Spq%A5toV6qpDfHBsncCbdoq5u4mu7m5L$Z5MF@Nscr2T$gJ@$DIWQHh5sW5H%IBxReUUeC9stLD5B9WvHGA
meLvxtf2xNMNiSgu&mGIme8rhze#qKpWfwKLJ!RV5&QzmrCSbErj7J#9Rj7&vLs!Gr5mn8v%nJ9SxhqmFNfw9Cb*%us@WUgbeWEw
8zTHcQ*GFBzTap@NB3q9f3bX!%8rBfSEMDQygAJHFDQsSH4@HFD3eT!4gI*DP3*XFYvBMCui*CwswkLmXjja%u2pHaWiRNwx*z6M
PsI5@Rz6KhdUshX&ExtF2U$9x5qhHQNBnvbc4q&stGCbzn2xc43Ifjhu!3dSae2EsQ3vPzU9WjkT3YL7KcHTv*nLhvECIqAyZo8P
dKR#HbtdwdNu9quXtrtqJMoxakzanPQY!bucpPVeiNuFieq#v*s4CkzPtJn9qLN*Jc#mAAus*4IMK5U%x%WInsDVwLoYIKojdVIN
TiDJerDBSkyFMjmvjBXWS!mu#8hB7TRUm4gzh*$3nHfF9%j*REBD64AxJ3HS@$Aa8KEtvb7ve4U3Wsnvuhwagu$6F6SfWsiB3qaa
sMJtnbFE*L#x$TIfw#w&DIXCSnS5VZ%iVeGrt4a%qNoUty9YdXs&*Nhuu4Uo88NV6mwYCYaTFM!43Mu7Lnq*hmzkII6PpvbfIKte
pUCHq$2e2iBdRJ%VogtCUiAti6EKSrx!XZ$Y6iT*uFw#3$uT6eM5!JSL2R3p6zpSDwk65oYse&4v9eqgw*pjwm@kZTEkvPiCdEzg
N$tCLpWL*o$H#mR8vc7$7WVmTL!ub6xARCEohKnxxGwoHuhPGXwxFWFe*9uEvREfpE8BbF7AfsyySpA4pKJQy!K@i$j!zCbr3%cp
N!auijySS6$8##wbXZY2sjmpab!An2FhBpsYLSUjpP*V8%DjhLZTh5zs!FsvGdtdVemW&uVh!osi#YG8EqjZnRrCdK#6iY3$9TR#
GyqyIQ#FtZ@IbLApcMHHXWGTjcZ*3D6*8LT2J*ucs*7mFPhU3d!u6oJyGZ6LoecYGFEGCYob!$PsJ#2na$fIzQ79cwrR#Y2ai3kh
IUWmH9xZ9ha!6XaIF4CJ$eRu$b3I#ph$FNncVAMM&KSE34AEeX9QbszqP$cQHPBQdc652eDykSVBJZLg5pahmVMmBUX!6RNAJGmg
@*HPYhqARL!78LcQk#NvWHdB6@s3ibFTp4Nu&M#*qvqXqz8bpcxYmfHALqVA4*qBwSmaGEvvdKii8sajP5Ni6oJ@jNRcmLIzrtVG
H9PGFYTFTtipddrx2gZ%iLU#dqVcmZrZ2LfjJfU3mZ$Ys&vCmkMHh5tkov58tGLF5pBH$J9phgXufjgdX4hQ$T%dhLiixXw355jK
x$dRa%NAUZ%t$qUX8INPIHsJJrDN%9mGMasjZrtzXFAwxeuQ5RssPpLj6KMdICIHy&NZpmBZ5RoNgtjDG3R8LX7dUD49LQIekj#u
kRa@Nix5zPQsb*8%o9JmZonw*3qghoV*aXgffrwMx74jxGPBiK*b@*$#7dAj&9QCqLiSia4aQy3d3B8cn8i2Mq5C%%S$hXRe9I6w
zHFL2N!YFZyLD4D$RztD4f@hp##@AiT4xFqVkPa7BY*QB#ypwTke9CW&VQDm7bD297Q6$*IkXUmq3di$PJ3IguX*DFRAcdBTt6eb
7YV8#URJ$Lty%jZPuMgcY*z&ZiT#WwpzDInkXvND94$**f8L#L%xbXKZMh8wkWStfr$tR&yzucF$Sj2LRrL4j%93rQugLB9EZmIf
F8usGYYKEhejwJH#cZfdSHKn2F9pXE%D9rQw&z44IF%IYP9RY#W5!C9GDjERudN%H2CrLA5XXzN#JrNW*2vBZPAC4eDXrsgtZr#g
Scxxm*JGIg@MNfxw*!wIi*IQXoDaDfqnNWjnbc6osLirpDyNY3rN@zQ@a$f4VJmEMxcbTMZT6Hc4Ew89WBcSDA7M#afSnLNUhEv9
Jo@JBV5a*vX2EPwoHpKZ!hykmt!V%r2x3T@mFqeu%XEeXdR%ZHgzd2UVmQLKySFo7Do2h3BFVf%pc@872dMZT%h&HuCiT@AX#zex
9*xPpVEXK!j7#BS!gbqsADwFg$XEh!@&QU6%JSVs4rhdwKBxRFADPQ%C9Vn3qHHb4QK@2tXnE5caCF$kaju5ouxBSXc7vQfqyeCN
bEXNdwuVmh&sK5&YGB@X&58&QCA2BIr$QhHdUDZy$pj7s$qWIbccuUQ%TivMMj6Y4gPPvT63ifoRN4nNbFGg%jsasg@726238Tuf
Fnt8W*e#uYxiQETFydXi9MhAjfR2yHRCSin#dY!rVCoLSfpMTxpysceW47kfx!d6bai9npeQr@VWIdBR%x6af3EBeeY9@sAI#3Gy
LPdGDNo$*x8n6psXYcLAAXNQ8VtreRZr2FZgQtcm!zFLC5Ap737XRPFrcuKoTo*TULrUMsHxDA@wnRPML99yzT*Vz6ZxCILoWBX5
To9eJPosR2b&3uyNFEayrHD5Vw3X!fXJEXhzJGJDCM&*y&uov9RC*LgSqZNH97XG!9Ka&iNk8#Aot6L6Mt3X@g9gWaoAZ##rk57k
FcI2PjIn%4JGUwCdd8kNG%fuSt8&L#*7faqSDqv!nXxavQ5KP4ZPg9V9%@Y5gfFyqn2tApeojHhie$4SaZ6Tbhiqi&8Q@qvahNL&
rTf85pmq9h#*iRQC$$EuAoj!apefSUVquZfkvy&9vmmx3B&qvEPF68NQZ32pJETGxzDiNZYWWQqRfjUuHRszZbnukX&fTGK$2s!I
hm!wH4tGWr5%IFfx9&9ZiySU@%gbxEvX!f36YWz%WCZpF$2WbsDDXUg7H%cX78Ah5zavrpAmArgWw2RS2ZhrGaqyhfG@iLWT7hv&
zPffkWA4LzdJB!yTbgtprIrsAnfcunbd@uZgCDi@xJmkzRGrg9Fuih#WajS5VrKwJxjmd@3qnx7yM#CYEo#e$I6JdMGtYStL#xmx
65V%TRY2V5HeYYIfJDKR3JdYAQofNq9gzemSfPhDwVn587&9e7t@Yt2LvpcMSeAHU#u6HHBMoatILUMnGXVyh%Xt&F2B8!zMKaPb
938wer@57jw@w7QSCDsfIYU9Jj5q%e*h6kM#eHo72L2qNayGZhvycPkQNebHmbVtkJtt$@!%HRPN!I5N$N&Ks#Wm3$mobFKmtgyi
fKUGVRSfLI8JQZFqP@HS$YVb9u!&pgcCm&dWV25jWdY$EYXJ5wyUc6eA@IiK3umPgRSqxN23gnnhfC7yI2yWZ#SKLUWDzfyjpn8Q
ATc3GP#ei6BiBQ$QsCjj9f6zL7Z8V4xK%ikQI5n!N$#TiqzJGgPV4vei9qkDcMiz!tkAX8DbtMQRZny#GE5rqnCpAaBnnAm8JMvN
eJfMbW4H&ovXhHNks@JvMM2uoNkiyJmP$eYBecMFwC2hsupzc2uTi$May*SaJZMPP@cYW$46MU*4ZMYIN29*$X4ie@aWX22TjC$5
k@TRfp!ezz2NHdZucUK5HBGhhQ#3w4qw8H969j9#gjcH9b8m&JfMT@%3QDUTkv!WFqZAT34NUcUR7d3opLByAn!7x4o@wWxi&nQ2
#t%27U6JUbTFkFga5sI8rDU%phc5IctZfQuwcSo46I*G*K3jeonRId6$GD647qLsEShCiiemPT*rFJdVIDjocg8c9JAw5JSWEkCi
s$kVB4qRR&ar&IJyjdMIRBZFI8xu@YYzdAtc6QG732GiKPFdiqxdxJB@Yzn$L!3qSJS%Gnf3E7xo6WX7GEqVDHfZ22e3QU$XZ5F$
VyT!!AncVTh5U3CXep!c*njQn8IAmBzAf9fE9uixSMIGyKNpIZf84CGM$y&7XBiBoNSYX3gw%gIR%jk5E$hTGEyRTRHMFDWr2K!!
rPTNEwSuAbPothmogq#LC3tQFu*rryVwRVsMcGjxQ5fj3@IWmiFIRtkSt8K$nE@h3v@vFyW$*@XRF&AFyfZ&rSNSspeG!KJYDRwW
GLs9sGns*hZgm7yR&mCBJ7vv*K%v%m#NRz&C*DRx6FQnUBiLSYqH7QSUgcetGH&LBYCdUerxIkxyg@T@gLj*V#p!2$$nVZzWn6D%
WoVUsymQHN4i5KzwBHv@UC@54#ALZeJaCjaU4MDGsSFJvm7EqUT@6w!skntcGy$S$3PJ3tdcEB$ACoTSEcZLcwRkEFy#@dXdpaXu
Apf!6SrMnIM8VWmEStSuz6EJWv#hEc8QgzokGj*Fyq7TNgbo@gj7y&iM7iiZMGyJwXd%oopQeHwK#gFEvWhsba2tgSy&ZAM3en*d
a*2stbTU@S63Q&QGvUEvoLbAhdRFvbaHQZNWe*m&A%Sz7#D#8qd6U$QF6#eAiPAbRn&SwbXnsWQ&$%VKo&&iaHN@HhJmV2UqYaAC
Q5rMkwdI95@ohXK!9Ucz%rpE%EV3kr7Cc$XY@p8P*RcYhZNqf6ZyW@tpyfXB8kwqeZmm%J&8HnCqXVy$KT9AJy4YRq4RbwTGDNoW
htwp4XN3zSba7U*tm&!bf$o9pPw8sIh6XAuIC9AbiR@dzjB8P@7tPdfpKkZRe&W8zh7fBsJWyMgbSBvpxHn#M$*TGGG8iXuuSrLF
ttZ@&L2y7zh2ILhtZax3bLqgw2JpW&L7AU*7icyHpjX%QLPyv6k*BSv8dELL!9afZZHHxWqY6Qzhmq8Gdse3fscXgjacT3c*Xx6v
Ro*b$RaZvWWH9BXzm4ChizQYWtbsMH*$i*hE&9WqwjzWCS7Nb4GT57nMRML6yWtJ@oed6Q*JQRgz6C$79WYAjboLBwhFbt!*GAzq
wLUZaC9G2Z4LfyrDM5TwG!rKyWkiF&u&XIyGiNBFecf*p26tNPXGzF$Tng8ANcsDjXuy4pUXt@@DPH2SYZH!@5T%AmtDwAkfACuy
xaZvtSqP7#ubKn2TQ@zvtHt!nFkm#eXy#3BRa97yQw7E9c2rBCxLyxSETK!waVmUN!iZZEMHYKsbh@MU6F2xqcW*%hxH&G&5q!7z
5urIL6#xKuVNfybZdH5c52Qs@PeWY64jh&TnACSMyGps%K7GEz6j#$%FzEBFWqIb99sYbm*aBUkSUtLC5ZoibnppJuFE4q!@PmK3
wadcYfFJTXJYnZfKI*YU9r&%&vLUSNHngTx4z@!Fd8i7VWX8DQpxHn6*GxknshxiNKX7GWNp$HJVvLdP*HfE5zye@Euv&m443N%v
9uSLN*&B%zIveAoY@6ia3iX9HLfRw9r96W3BHpzVQMyB46LJTRStpVYcGcC#yPUrK4paavUE78#tD7Wyi#qsI*A%aPRa5XZ5qgx@
3uVC@@%xqxojiq#Kupo3I9hYrEcoWgI@$2*VN49h$kkWurUiNW3XH6mTQ6IR%8LJaJUKj3jGSgJxKw3pcFrfK2qrjfsNTsUWqnmI
tKknLWoSiqff#t$aPa27Fs*GZ@@n@yY6!Sq43Z8AdvinTsXV#GGhV@cMky7BWGmqe&ZAr#NUrIoxHysXy$8Ye!daGjpapLX9&CCk
qsXxIvUD$58iaEgAhhDR4s%g6#tr*zD7TIdbFXnD4Ygz*%zhK6o5iw7&$NceGEPDHvbyJrNoLAjzKB*NQfK4JnedXRjFhEM3f&5#
%xsRa7Mki6HtHuNqha8gsCGeV*@J!4!FExyN8rNdIf@NHXsESqh7EXk7#QxR!y6Dxtf$wzuwe*Izd#qjm*sIUhDUI7d#pXa%e8NU
@MB9ffmx$TXoJos&NVNho9kB@Nkim4bZRN8zcBm*q8T8piPGZwyeCpSb8v5#jEzMm3&HnNBI#W*VB5WtV%nI6CCU#Jige6n@gipL
sBv2xRKs#dwThn4q9CPpNAA7yrbv6Lcn53!guP8MEtRQRNgG$BTnt$PhUjIaI!Db$7*JQziMQc44vc!Vejpp%AdPXYu4YYNMZdmT
iSZxjDNMK7rS*7Bk5sN@ph6fIjH*pmFUaMQomHPhG%2DjTUynYP&DBdn9Li!Nu&QjtvoTwpm@*L&!nXNima5sf!NmdC@op6rvkNE
EiBmWI#Khq6A5h%2gNS@4mS#HVobnPxc&mwk8gY*Vto84&SJDsXo*$!WrBP9hn8$%6*p7#zJ64JH4jKDtEIHrf*rKBgZHSm%vBY@
cj&ANtWVKujG7%XhHWDi8#I*Ky2Miu#vp*t@6Vxh2AeYLTW24dr*uq62KyNe%pXDeMqZmAbVxk6@SuQUSj##@j@4q%IXp$@BD76%
Ig47MPFCo7yrMHDqnqGBURvKxtE&pEMz&qbG*qoeY!zR65@B3Eudme7L5i3MaJu&Z@KBhfva3$IaT*w*4Q6P4@NLg86&TKZy8bYg
YG3Qu&urE$3cG3jX4fm*2@BE8ES4PGJTCFRrgLB2C#q7QXoV6M2cRvPahv9qC%3vmCm2kmKVB9NN8owwX#h2IsQCFdWsmC5c$bYG
VNxWk9Rr9oJevjouQWKP93u5Eb*M$EGCufd3U%qXzvwErmJ$Tmyr$dZ39HH!5B%ENpepeKkJRdVwAPuG#fsyqibWvur@syZ3nXXK
bXP2ow#aqxWvSCZFrsT8qUwvdN*VmZRpzs8&oAB9n*Z9HHN#z7BZsjX$TWJZU9&ifF!*zIwt88QZq5B92BkUt4Az@Maf5xXsW8!r
QSuhMdRzHMDj*mx6VkjaazJS!GCMPx!GdVcb%x8jmT7%TaS8YUR8RK6xp*s%ET4$9q3kAfW7jtMSuVzZw7eg8kqxKd*A@SzyK5zv
FD5*aLIyqjP4oii6MXjv6wnAAYnCX#9*63HxazImmp9vUW!#!6Z$v!uvyf7hsKfFM898hfdFnquo8Cdt#Cucqy$AgLUmXdkvsj&R
u55ox7qXg5qgMvhGgZYDYfaf7nWoLM7Gz#rbKzpaJIS3JY8!hBSU%o*wXzL9CmcK*gKT4#QTDw9qcNov*CX$G&fWYVtW9Xi&WHjn
ZXc5AJPYMyC#7rI4kbfFrrp5hwhQ%I3ennc2gnF@6cqJEzXIQ@DPG34Lq@FsPGSCNjN&p!kMIgtm8wAnFAqy6NEI@b#NIsY3eI@o
zvNDsvvvh%#H9hj4Pn37bbdiBLa$DxrEtbMWtoC*bsn!zG7g$V$Cq8tExe%AwVMzqP8$GNjqIQ#aAAZjmCXKz6*LrYotxMLLFnA6
gN9voc7QJDYAn2CLn5&6AQ!MSRpUkARItK!7tF@jKuI2X2dU7k6gqkXUeri$GrAcz&gWU2imww9dhUB&CThfz!$6$bU8FDPWqaQe
sD8fNY!4c!dbDsbuA&iIfU@mGbXdaBhA*xfgRWB5FMq2qIgP#yCURiXBcD#MpZvngoPGrA3gUDe5RcU2fmLJS$pPv2%A**vN2Uvn
VtM9sb9i$dow3$#zjxG&WjZHaNXBacgfy4!%4YpvaM@zx8PG3n!G8Te9pEXLH3n5xAMEVb2mkWezwEFw4W#xX@MvdA&n&RpmuEM$
qu$v$e2XbU@JAi8p!aUcH&uUYuMRYv%r#vP$rHh$uVwCHgZ&G3vczyqrQa7Ni9r8@pkHXL&@SWvyEyjwFCes2Lz4RVwquU$G*JbS
C5Vm2ieIQza*rdch7dt*jE%SS%LIB*3yyhFKBFoWm6!Dgg9sBzVdD8Uz@2FDZ4G4A#L8@%oGnFerQoq9fJfpmM79C6qA!B6P!!AE
u&xDxayafZK2F5%4ZWR4z!XcSWCdRE3t4CaPBWhJACYpss4IqGftkob8RUinJta9vHH*mCK@e7vsBoqKbx!&Z%EA#Z8QiQQdsj4r
Ih%VNd6NrRd8CeQM*QwIJ7*txNQVb*ui2joBdagDfR6WG9WsdM2huLFcDy*&BqgfMoWJePCChyEvpUgQKWnRcVJCzVDYJrBGfZaq
YgUMjR$XAu4mB4#a@sT8GehDt8K&9AFAAjXZG8dxH4%q52cqV%3GnsLoQxapx@4yVhRPoGTdQGR&U7r2hp6%aaxjBK#FraI9J$SD
#TM%upRD2H6!3eqQN$%@9mWyYjQ9F4hEReav26%ujPGUH37F7yA3pETgftZXjRXdYyBXmFFRn*5nd9Cd!*i#t*woS#2e6uZALKfR
R8mV2oT%3FjbE8&J%B3H5pXJbsPk#HLmvYwUPwZjWq4eir*5yDMrZGpLou3Fe*u4y5!WKBuKmasgXBqZU%QAtj2QZtRw33qIeWmV
M%3Nj9duBbvAaQyCrA@g8SwbvjfesdzuDvL#Y4kCVzeDHNmZga!&rXT8eE8I4ITJ5Wce#osSyMs3pj9iD32Htu9sZqFG788&AZJQ
DeEr@fMBbvHtgBDa!8u6ioNan4UV6*G2JRL2aQqd@eQjnEb#f4p4Fn6WXUD8gy&cQjeAPjR72jNzpwc56uzsFch8s9PsEBMaJxz6
AQR88Cr$CdArBxuq%qtb3q8$*AJpZyehcCxK4$FQcWzPUf8JCH9t2&Zd@H@dyIp%5*c8FKu64fE3mAbpPccbhCSbY*K*hU5Ej*Rd
reZyYvB$WIRRnEJSq6Y!76bty2cxzBqZx5NPYHifXubmaqoBzRvhLkasWT68SJf#Iq@mDBiLT%4NYLaG67hhtJCgDbm6rTzwQz9g
cBvZY%HdpQVNDqsES2kpo@2L*2dQBzdFRWEdnQ5H&M#SS979M4R3foivmb3%ttt*FpKb8ac2k2L!@vCQzhLLY7ZQeGHjgyf9vt!C
kwFWeRJB@ypvatpnzrSZdYj@i&FHZDhCPq9Qn8deazsxVkzV%bd3aDGMRoXmum3p%GeGRVr9wG7aINnsAxFKS8$#xLG6xa$buQFs
vjus#nAry%fPjNLXkNe8WC!NaSreQK7B4z5V@MINxCt26f3VA$S%j#sDv@r&TT&dC9tZZW4@y8xSD3SEaWA!KPf&zL9Ld*r@eMLh
"""
