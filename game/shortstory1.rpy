label shortstory1:
$ quick_menu = False
stop music
stop background
pause 2.0
nvl clear
window hide
pause 1.0
$ renpy.music.set_volume(0.3, delay=3, channel=u'ambient')
play ambient wind4 fadein 6.0
pause 2.0
play ambient2 ticktock fadein 6.0
scene black with medium_dissolve
pause 2.0
scene bg forest_stormy with medium_dissolve:
    xzoom -1.0
pause 1.0
$ quick_menu = True
window show
"A primeira vez que vi algo “sério” foi no dia em que completei oito anos."
"Minha mãe tinha me comprado um daqueles videogames portáteis antigos e alguns jogos para acompanhar."
"Mesmo sendo de uma geração ultrapassada, e todos os meus amigos tendo a versão mais nova, eu ainda estava feliz por tê-lo. Era legal apenas {i}ter{/i} algo meu."
"Eu estava sozinho; minha mãe me deixou faltar à escola naquele dia como parte do meu presente de aniversário."
"Eu estava naquele sofá pequeno, meio escorregado para baixo o máximo que podia, quase deitado com as costas no assento e a cabeça apoiada nele."
"Estava jogando um jogo que nem lembro mais, só olhando para a tela."
"Então vi um reflexo estranho no plástico da tela; fácil de notar porque ela não era iluminada como a do modelo novo."
"Enfim, havia o reflexo de algo muito alto e escuro no canto ao meu lado."
"Tudo o que consegui pensar foi que minha mãe tinha pendurado um de seus casacos longos ou vestidos no abajur que ficava ali."
stop ambient2 fadeout 3.0
$ renpy.music.set_volume(0.0, delay=3, channel=u'ambient')
"Mas isso não fazia sentido, então olhei para cima e para a direita."
show black with dis3
"E então,{w=0.5} eu o vi.{cps=3}..{/cps}{w=0.4} um rosto olhando para mim."
play ambient2 darkambient01 volume 0.3
"Dois olhos amarelos com pupilas estreitas,{w=0.5} sem focinho,{w=0.5} rosto achatado,{w=0.5} e as bordas da boca curvadas em um sorriso.{w=0.5} Seus dentes eram longos e afiados, todos eles."
"Não lembro de ver orelhas,{w=0.5} acho que não tinha."
"Só sei que não era uma pessoa,{w=0.5} era uma coisa.{cps=3}..{/cps}{w=0.4} uma criatura."
"Os olhos amarelos se destacavam na pelagem preta e embaraçada que cobria seu rosto."
"Eu só conseguia ver as bordas da boca porque ele usava o que acho que era um casaco de chuva, ou algo assim. Havia um grande colarinho virado para cima, cobrindo a metade inferior do rosto."
"E era alto.{w=0.5} Seus ombros e a parte de trás da cabeça e pescoço encostavam no teto, então ele olhava diretamente para mim."
"O resto do corpo estava encolhido no canto ao lado do sofá,{w=0.5} com os braços estendidos para os lados e pressionados contra as paredes,{w=0.5} como se estivesse se apoiando."
"O que pareciam ser garras longas e pretas saíam das aberturas das mangas, cravadas nas paredes."
"E pelos poucos segundos em que fiquei olhando, ele não se moveu, nem um pouco — como se estivesse preso em um quadro estático."
"É estranho ver algo que você sabe que não deveria existir. Tipo, há um momento extra em que seu cérebro absorve o que está vendo."
"Então, em vez de fazer você reagir imediatamente,{w=0.5} como seria ao ver uma aranha,{w=0.5} há essa pausa extra onde o cérebro está analisando."
stop ambient2 fadeout 3.0
"Tipo 'sim, isso está realmente acontecendo, e realmente não deveria, mas aqui está.'"
window hide
pause 2.0
$ renpy.music.set_volume(0.5, delay=6, channel=u'ambient')
pause 2.0
hide black with leftwipefast
play ambient2 distantthunder
pause 0.5
window show
"É difícil lembrar o que aconteceu depois. Só corri, ou melhor, me arrastei de quatro tentando fugir dali."
"Não ouvi nada, não senti ele se mover e estava com muito medo de olhar para trás."
"Caí na grama molhada, porque estava nublado e chuviscando como sempre, e depois na calçada de paralelepípedos que serpenteava pelo trailer park."
"Continuei correndo por aquela calçada, me afastando o máximo possível daquela coisa que não entendia."
"O que me perturba até hoje, mais do que quando a vi pela primeira vez, é que, quando estava a uns três trailers de distância, olhei para trás — sem esperar ver nada, mas vi."
play music mines02 fadein 3.0
play sound horrorsting01
play sound2 horrorsting01
"Ali, enquadrado na pequena janela do nosso trailer, estava a criatura de rosto achatado, ainda com a mesma expressão, o colarinho ainda erguido, como congelada no tempo."
"As persianas, que sempre estavam tortas e desalinhadas, estavam se mexendo — balançando suavemente atrás de sua cabeça enquanto ele sorria para mim com aqueles olhos amarelos."
"Fiquei sentado na entrada do parque, tremendo na chuva."
"Depois de um momento, uma vizinha saiu correndo do trailer para ver se eu estava bem."
"Disse a ela que estava, mas não consegui explicar por que ela me viu correndo do trailer, ou por que não conseguia voltar para lá."
"Então, ela me levou para o trailer dela."
"Acho que ela pensou que talvez alguém tivesse invadido e me assustado, porque então a polícia chegou, depois minha mãe, e acho que ela teve problemas por me deixar sozinho."
stop music fadeout 6.0
$ renpy.music.set_volume(1.0, delay=6, channel=u'ambient')
"Quando a polícia foi embora, levei uma baita bronca, mas estava feliz por ter gente por perto."
"Claro, não pude contar o que aconteceu, porque não poderia ter acontecido."
"Mas aconteceu. E então aconteceu de novo, e de novo, e de novo..."
play sound2 windchimes fadein 7 volume 0.5
window hide
pause 7.0
stop sound2
stop ambient2
stop ambient
scene black
pause 4.0

play music sil_pre fadein 10.0
scene shortstory1nvl with medium_dissolve
pause 2.0
nvl show fast_dissolve
story "{w=1.0}Eles não podem te tocar, {w=0.7}não podem te machucar.{cps=2}..{/cps}{w=0.5} pelo menos não fisicamente."
story "Mentalmente é outra história, o que faz sentido porque tudo isso é mental."
story "Eu já estava bem fodido muito antes daquela coisa que vi no trailer, o que pode explicar por que a vi."
story "Mas foi continuar vendo ela que me traumatizou;{p}Eu nunca sabia se estava voltando para um trailer vazio, ou um trailer com um monstro de casaco de chuva dentro."
nvl clear
story "Eventualmente, percebi que ela não realmente me notava, acho.{w} Na primeira vez, ela definitivamente quis que eu percebesse sua presença."
story "Hoje em dia, ela só aparece de vez em quando, e é basicamente um recorte de papelão de um personagem assustador de filme de terror."
story "Sim, ainda é assustador quando está ao pé da sua cama às 2 da manhã, mas você aprende a conviver com isso."
nvl clear
play music2 silog fadein 10.0
story "Logo, o monstro de casaco de chuva com garras virou um homem que andava pela nossa cozinha."
story "Ele estava com raiva, {w=0.5}xingando, {w=0.5}jogando coisas, {w=0.5}mas eu estava bem com tudo, porque ele NUNCA me notava."
story "O mesmo não posso dizer da próxima coisa, outra criatura de rosto achatado, mas essa se movia de quatro, com cotovelos e pernas em ângulo, como uma aranha."
story "Ele subia na minha cama, {w=0.5}passava sobre o meu rosto, {w=0.5}e sussurrava coisas para mim."
nvl clear
story "Foi aí que ficou realmente difícil, e as coisas desmoronaram depois da primeira vez que tentei cetamina."
story "Na maior parte da minha adolescência, fui mais de maconha e opioides.{w} Nada tipo heroína, mas um comprimido de vez em quando para acompanhar a maconha e relaxar de verdade."
story "Meu amigo, bem, ele adorava coisas mais intensas, coisas que REALMENTE faziam você sentir algo, ou nada, que era o que ele me prometeu antes de eu usar."
story "Você vai sentir apenas calma."
nvl clear
story "E então.{cps=3}.. {/cps}{w=0.4}enquanto eu estava sentado na sala do meu amigo, {p=0.7}um urso quebrou a janela."
play sound sil_trans
story "Ele estava com uma máscara de esqui{w=0.5} e tinha uma arma, {w=0.7}e eu gritei, {w=0.5}e corri, {w=0.7}e.{cps=2}.. {/cps}{w=0.3}liguei para o 911."
story "E claro que não era real.{w} Eu estava tão fora de mim que pensei estar vendo outra pessoa fazer tudo aquilo."
nvl clear
story "Não sou mais amigo daquele cara, mas foi um ponto de virada para mim."
story "Eu sabia que as drogas pioravam essas alucinações."
story "Eu sabia que quanto mais tempo ficava em um lugar, mais elas apareciam."
nvl clear
story "E eu sabia que elas não eram reais."
story "Eu sabia porque.{cps=3}.. {/cps}{w=0.3}por que haveria uma criatura com garras de 30 cm em um casaco de chuva com 3 metros de altura?"
story "Bem, {w=0.6}aposto que algo assim nunca existiu naquele trailer."
story "Aposto que nada parecido jamais existiu."

nvl hide dissolve
scene black
with fast_dissolve
pause 2.0
stop music fadeout 8.0
stop music2 fadeout 8.0
centertext "{cps=40}Eu a criei, {w=0.5}e ela me segue,{w=0.5} e eu a ignoro, {p=0.7}mesmo que ela esteja ficando estranhamente insistente.{cps=2}.."
pause 3.0
window hide
$ fade_inout_chapter("Outubro 2019", color="#FFFFFF", size=50)
play background roofrain fadein 6.0
pause 12
scene shortstory1front
show shortstory01_01 behind shortstory1front
show shortstory01_02 behind shortstory1front
show shortstory1back behind shortstory1front
show rain behind shortstory1front
with slow_dissolve
pause 1.0
window show
$ quick_menu = True
dev "Tudo bem, amor?"
"Dev, de alguma forma, já está sem camisa."
dev "Um pouco ansioso, hein?"
"Não respondo à pergunta enquanto tiro minha camisa e as patas de Dev imediatamente começam a explorar meus lados."
"Ele está um pouco bêbado, então acho que isso não vai levar a lugar nenhum."
"Só queríamos sair da festa. Nós vagamos pela floresta perto da casa, Dev estava procurando por orbes ou algo assim."
"Começou a chover, então corremos para o carro e decidimos esperar Jason sair para irmos embora."
"Espero que seja logo, porque essa coisa.{cps=2}..{/cps}{w=0.3} está do lado de fora da janela."
"Ela está nos vendo.{w=0.3} Não gosto disso,{w=0.3} até hoje."
dev "Tem alguém lá fora, ou algo assim?"
window hide
scene black with fast_dissolve
pause 0.5
window show
"Dev olha para trás, direto para a criatura, e um calafrio percorre minhas costas enquanto ele encara ela cara a cara."
"Ela está sorrindo para ele com os dentes afiados, curvada porque é muito alta."
"Mas, como sempre, Dev não reage. Porque ele é normal."
dev "Você está vendo coisas de novo, Cam? Só porque você me disse que parou não significa que não pode voltar."
"{i}Você ia adorar isso, não é?{/i}"
cam "Não! {w=0.3}Tudo livre de fantasmas."
dev "Bem, seja lá o que VOCÊ acha que eles são. Você está vendo coisas de novo?"
"Eu suspiro profundamente."
cam "Bem,{w=0.3} isso nunca desaparece.{w=0.3} Só melhora às vezes, comparado a outras."
"Dev esfrega o braço, seu peito largo se erguendo, então estremecendo quando passo minhas patas por seus músculos, apertando-os."
window hide
pause 0.5
play ambient2 timedthunder
scene shortstory3front
show shortstoryflash
show shortstory1back behind shortstory3front,shortstoryflash
show rain behind shortstory3front,shortstoryflash
with medium_dissolve
pause 0.5
window show
dev "Não quero te chatear, {w=0.4}mas..."
"Fechei os olhos, esperando ficar chateado. Ele já sabe que não gosto quando ele me trata como se eu fosse algum vidente."
"Sou só um garoto estúpido que vê coisas horríveis e inúteis."
dev ".{cps=2}..{/cps}{w=0.5}Mas você me diria se visse algo que... fosse importante para mim."
"Pisquei, pensei e então entendi sobre quem ele estava falando."
cam "Ah! {w=0.5}Bem, {w=0.3}sim, {w=0.3}claro que diria.{w=0.3} É que eu não vejo pessoas."
cam "Só coisas.{w=0.3} E coisas ruins."
"Dev ficou quieto enquanto eu acariciava seu estômago, brincando com a pelagem grossa natural dos ursos, algo que eu gosto."
"Me sinto estranho fazendo isso enquanto esperamos nosso amigo."
"Quer dizer, é nosso carro, mas temos 25 anos e estamos agindo como se não pudéssemos esperar, precisamos fazer isso antes de ir para casa."
"Normalmente, Dev só gosta de carícias assim, onde pode me sentir, mas ele só grunhe quando abro seu zíper com hesitação."
"Ele não me impede, então continuo."
dev "Bem, eu devia ter visitado Echo hoje, mas Larry teve uns problemas, então acabamos nessa festa ruim, e só vou ter outra chance daqui a meses."
"Encolho os ombros, querendo manter a conversa leve."
cam "Já vi piores.{cps=2}..{/cps}{w=0.3} Festas, {w=0.3}quero dizer."
dev "Da próxima vez, não levo Larry. Vou só eu e quem mais quiser ir."
"Aceno para ele continuar. Dev suspira frustrado, seu peito se expandindo contra mim novamente."
"Ele segura minhas patas e nos abraça, pressionando nossos corpos."
dev "Obviamente, quero que você vá, mas não quero que você se sinta como uma ferramenta, ou algo que estou usando. Acho que pode ser uma boa experiência para todos."
"Olho para ele."
cam "Não morreram tipo dez pessoas lá?"
dev "Bem, não isso, mas como as coisas mudam se virmos algo."
cam "E o que isso significa?"
dev "Que.{cps=3}..{/cps}{w=0.3} há algo mais, {w=0.3}um lugar para onde vamos depois de morrer."
"Penso muito, tentando escolher as palavras com cuidado."
cam "Mas como sabemos? Ver algo não significa nada. Aprendi isso com o tempo."
dev "Só--"
"Dev suspira, não irritado, só cansado, provavelmente com dificuldade para pensar direito por causa do álcool."
dev "Só preciso da sua ajuda por alguns dias."
dev "Quero saber, {w=0.4}preciso saber onde ela está."
"{i}{cps=30}Em lugar nenhum.{w=0.3} Ela está morta, {w=0.4}então não está em lugar nenhum.{w=0.3} Sinto muito.{i}"
"Não quero fazer isso. É uma péssima ideia, mas isso é importante para Dev, sempre foi."
"Então, agora que ele finalmente me pede para ir, só posso dizer:"
window hide
pause 0.5
scene black with fast_dissolve
pause 2.0
window show
cam "{cps=40}Claro."
"Ele sorri e solta um suspiro, como se estivesse aliviado."
"Não tinha ideia de que ele estava tão tenso com isso, mas minhas reações anteriores sobre a cidade devem ter mostrado que eu não era exatamente fã de ir."
"Mas, {w=0.3}posso aguentar alguns dias de desconforto se Dev encontrar sua resposta, o que eu realmente espero que ele encontre."
dev "Obrigado."
cam "Sem problemas, cara."
window hide
$ quick_menu = False
with Dissolve(0.5)
pause 2.0
centertext "{cps=30}Tento não me assustar, {w=0.5}porque, assim que eu disse isso, {p=0.5}pela primeira vez na vida, {w=0.5}vi a criatura de papelão se mover."
stop background fadeout 3.0
stop ambient2 fadeout 3.0
play sound thunder
pause 1.0
scene white
pause 2.0
scene black with fast_dissolve
pause 7.0
return MainMenu