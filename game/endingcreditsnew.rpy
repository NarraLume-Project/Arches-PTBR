label endingcreditsnew:
window hide
pause 1.0
scene black
with medium_dissolve
pause 1.0

show text "{font=ui/LinLibertine_R.ttf}{size=60}Fim" with medium_dissolve

pause 5

hide text with medium_dissolve
show text "{font=ui/LinLibertine_R.ttf}{size=35}Criado e Escrito por" as title:
    yalign 0.475
show text "{font=ui/LinLibertine_R.ttf}{size=60}Howly" as credit:
    yalign 0.525
with medium_dissolve

pause 5

hide title
hide credit
with medium_dissolve
show text "{font=ui/LinLibertine_R.ttf}{size=35}Arte de Sprites e Design de Personagens" as title:
    yalign 0.475
show text "{font=ui/LinLibertine_R.ttf}{size=60}PaintFox" as credit:
    yalign 0.525
with medium_dissolve

pause 5

hide title
hide credit
with medium_dissolve
show text "{font=ui/LinLibertine_R.ttf}{size=35}Música por" as title:
    yalign 0.40
show text "{font=ui/LinLibertine_R.ttf}{size=60}Anthemics" as credit:
    yalign 0.45
show text "{font=ui/LinLibertine_R.ttf}{size=38}Masterizado por" as title2:
    yalign 0.55
show text "{font=ui/LinLibertine_R.ttf}{size=60}Frozen Measure" as credit2:
    yalign 0.60
with medium_dissolve

pause 5

hide title
hide credit
hide title2
hide credit2
with medium_dissolve
show text "{font=ui/LinLibertine_R.ttf}{size=38}Arte de Cenários" as title:
    yalign 0.475
show text "{font=ui/LinLibertine_R.ttf}{size=60}Kardamon" as credit:
    yalign 0.525
with medium_dissolve

pause 5

hide title
hide credit
with medium_dissolve
show text "{font=ui/LinLibertine_R.ttf}{size=38}Ilustrações" as title:
    yalign 0.475
show text "{font=ui/LinLibertine_R.ttf}{size=60}PaintFox" as credit:
    yalign 0.525
with medium_dissolve

pause 5

hide title
hide credit
with medium_dissolve
show text "{font=ui/LinLibertine_R.ttf}{size=35}Arte Adicional" as title:
    yalign 0.40
show text "{font=ui/LinLibertine_R.ttf}{size=60}PaintFox" as credit1:
    yalign 0.45
show text "{font=ui/LinLibertine_R.ttf}{size=60}Kardamon" as credit2:
    yalign 0.51
show text "{font=ui/LinLibertine_R.ttf}{size=60}Orion" as credit3:
    yalign 0.57
with medium_dissolve

pause 5

hide title
hide credit1
hide credit2
hide credit3
with medium_dissolve
show text "{font=ui/LinLibertine_R.ttf}{size=35}Programação" as title1:
    yalign 0.35
show text "{font=ui/LinLibertine_R.ttf}{size=60}Howly" as credit1:
    yalign 0.40
show text "{font=ui/LinLibertine_R.ttf}{size=38}Programação Adicional" as title2:
    yalign 0.5
show text "{font=ui/LinLibertine_R.ttf}{size=60}Orion" as credit2:
    yalign 0.55
show text "{font=ui/LinLibertine_R.ttf}{size=60}Skar" as credit3:
    yalign 0.61
show text "{font=ui/LinLibertine_R.ttf}{size=60}Wattson" as credit4:
    yalign 0.67
with medium_dissolve

pause 5

hide title1
hide title2
hide credit1
hide credit2
hide credit3
hide credit4
with medium_dissolve
show text "{font=ui/LinLibertine_R.ttf}{size=35}Animação do Splash e Menu Principal" as title:
    yalign 0.475
show text "{font=ui/LinLibertine_R.ttf}{size=60}Gumdrop Studios" as credit:
    yalign 0.525
with medium_dissolve

pause 5

hide title
hide credit
with medium_dissolve
show text "{font=ui/LinLibertine_R.ttf}{size=35}Efeitos Sonoros" as title:
    yalign 0.475
show text "{font=ui/LinLibertine_R.ttf}{size=60}Soundblocks" as credit:
    yalign 0.525
with medium_dissolve

pause 5

hide title
hide credit
with medium_dissolve
show text "{font=ui/LinLibertine_R.ttf}{size=35}Agradecimentos Especiais" as title:
    yalign 0.38
show text "{font=ui/LinLibertine_R.ttf}{size=60}Zeke" as credit1:
    yalign 0.43
show text "{font=ui/LinLibertine_R.ttf}{size=60}Redd" as credit2:
    yalign 0.49
show text "{font=ui/LinLibertine_R.ttf}{size=60}McSkinny" as credit3:
    yalign 0.55
show text "{font=ui/LinLibertine_R.ttf}{size=60}Blaidd Llwyd" as credit4:
    yalign 0.615
with medium_dissolve

pause 5

hide title
hide credit1
hide credit2
hide credit3
hide credit4
with medium_dissolve
show text "{font=ui/LinLibertine_R.ttf}{size=35}Feito com a engine de novel visual" as title:
    yalign 0.475
show text "{font=ui/LinLibertine_R.ttf}{size=60}RenPy" as credit:
    yalign 0.525
with medium_dissolve

pause 5

hide title
hide credit
with medium_dissolve

pause 0.1
show eplogo with Dissolve(3.0):
    truecenter
pause 3.0
hide eplogo with Dissolve(3.0)

show text "{font=ui/LinLibertine_R.ttf}{size=38}Agradecemos a todos os nossos patrocinadores e\n a todos que tornaram este projeto possível..." with medium_dissolve

pause 11

hide text with medium_dissolve

pause 2.0

show logo with slow_dissolve:
    truecenter
    zoom 0.5
pause
stop music2 fadeout 8.0
pause 2.0
hide logo with slow_dissolve
pause 5.0
$ persistent.altnavi = True
$ persistent.removeload = False
$ persistent.shortstory1 = False
$ persistent.shortstory2 = False
$ persistent.act_2 = True
$ persistent.musicon = True
$ persistent.goingincircles = True
return "main_menu2"

#####################

$ fade_inout_card("{font=ui/LinLibertine_R.ttf}Fim", color="#FFFFFF", size=60)
pause 9

$ fade_inout_title("{font=ui/LinLibertine_R.ttf}Criado e Escrito por", color="#FFFFFF", size=38)
$ fade_inout_name_01("{font=ui/LinLibertine_R.ttf}Howly", color="#FFFFFF", size=60)
pause 9

$ fade_inout_title("{font=ui/LinLibertine_R.ttf}Arte de Sprites e Design de Personagens", color="#FFFFFF", size=38)
$ fade_inout_name_01("{font=ui/LinLibertine_R.ttf}PaintFox", color="#FFFFFF", size=60)
pause 9

$ fade_inout_title("{font=ui/LinLibertine_R.ttf}Música por", color="#FFFFFF", size=38)
$ fade_inout_name_01("{font=ui/LinLibertine_R.ttf}Anthemics", color="#FFFFFF", size=60)
pause 9

$ fade_inout_title("{font=ui/LinLibertine_R.ttf}Arte de Cenários", color="#FFFFFF", size=38)
$ fade_inout_name_01("{font=ui/LinLibertine_R.ttf}Kardamon", color="#FFFFFF", size=60)
pause 9

$ fade_inout_title("{font=ui/LinLibertine_R.ttf}Ilustrações", color="#FFFFFF", size=38)
$ fade_inout_name_01("{font=ui/LinLibertine_R.ttf}PaintFox", color="#FFFFFF", size=60)
pause 9

$ fade_inout_add("{font=ui/LinLibertine_R.ttf}Arte Adicional", color="#FFFFFF", size=38)
$ fade_inout_add01("{font=ui/LinLibertine_R.ttf}PaintFox", color="#FFFFFF", size=60)
$ fade_inout_add02("{font=ui/LinLibertine_R.ttf}Orion", color="#FFFFFF", size=60)
pause 9

$ fade_inout_prog_card("{font=ui/LinLibertine_R.ttf}Programação", color="#FFFFFF", size=38)
$ fade_inout_prog01("{font=ui/LinLibertine_R.ttf}Howly", color="#FFFFFF", size=60)
$ fade_inout_addprog_card("{font=ui/LinLibertine_R.ttf}Programação Adicional", color="#FFFFFF", size=38)
$ fade_inout_addprog01("{font=ui/LinLibertine_R.ttf}Orion", color="#FFFFFF", size=60)
$ fade_inout_addprog02("{font=ui/LinLibertine_R.ttf}Skar", color="#FFFFFF", size=60)
$ fade_inout_addprog03("{font=ui/LinLibertine_R.ttf}Wattson", color="#FFFFFF", size=60)
pause 9

$ fade_inout_title("{font=ui/LinLibertine_R.ttf}Animação do Splash e Menu Principal", color="#FFFFFF", size=38)
$ fade_inout_name_01("{font=ui/LinLibertine_R.ttf}Gumdrop Studios", color="#FFFFFF", size=60)
pause 9

$ fade_inout_title("{font=ui/LinLibertine_R.ttf}Efeitos Sonoros", color="#FFFFFF", size=38)
$ fade_inout_name_01("{font=ui/LinLibertine_R.ttf}Soundblocks", color="#FFFFFF", size=60)
pause 9

$ fade_inout_thanks("{font=ui/LinLibertine_R.ttf}Agradecimentos Especiais", color="#FFFFFF", size=38)
$ fade_inout_thanks01("{font=ui/LinLibertine_R.ttf}Zeke", color="#FFFFFF", size=60)
$ fade_inout_thanks02("{font=ui/LinLibertine_R.ttf}Redd", color="#FFFFFF", size=60)
$ fade_inout_thanks03("{font=ui/LinLibertine_R.ttf}McSkinny", color="#FFFFFF", size=60)
$ fade_inout_thanks04("{font=ui/LinLibertine_R.ttf}Blaidd Llwyd", color="#FFFFFF", size=60)
pause 9

$ fade_inout_title("{font=ui/LinLibertine_R.ttf}Feito com a engine de novel visual", color="#FFFFFF", size=38)
$ fade_inout_name_01("{font=ui/LinLibertine_R.ttf}Renpy", color="#FFFFFF", size=60)
pause 9

pause 0.1
show eplogo with Dissolve(3.0):
    truecenter
pause 3.0
hide eplogo with Dissolve(3.0)

$ fade_inout_title("{font=ui/LinLibertine_R.ttf}Agradecemos a todos os nossos patrocinadores e", color="#FFFFFF", size=38)
$ fade_inout_name_01("{font=ui/LinLibertine_R.ttf}todos que tornaram este projeto possível...", color="#FFFFFF", size=38)
pause 11

show logo with medium_dissolve:
    truecenter
    zoom 0.5
pause
stop music2 fadeout 8.0
pause 2.0
hide logo with medium_dissolve
pause 5.0
return "main_menu2"