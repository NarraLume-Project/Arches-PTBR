label a3s1:
window hide
pause 1.0
play music neuronintro fadein 10.0 volume 0.3
queue music neuronloop volume 0.3
pause 1.0
play ambient heartbeat
show bg closed_eyes5 as original
show bg closed_eyes5 at zooming5 as extra
show bg forest_night_shadows_b at zooming5 as extra2 behind original
with medium_dissolve
pause 1.0
window show
"A dor lateja ritmicamente em sua cabeça como uma batida de tambor pesada, fazendo suas orelhas se colarem firmemente antes de começarem a gemer, então ele range os dentes enquanto sua garganta dolorida protesta contra o som."
window hide
hide original
hide extra
show bg forest_night_shadows_b
with slow_dissolve
pause 1.0
window show
"Eles encaram a cena diante deles, então piscam."
window hide
show bg closed_eyes5 as extra4
with dis
pause 1.0
hide extra4
show bg forest_night_shadows_b
with dis
pause 1.0
window show
"Mas isso não os ajuda a entender o que está à sua frente."
"Na verdade, parece piorar as coisas."
"{i}Quem está entendendo o que está diante de quem?{/i}"
"Esses pensamentos intrusivos sobre não existir."
"{i}Quem está tendo esses pensamentos?{/i}"
window hide
stop ambient fadeout 6.0
hide bg forest_night_shadows_b
show bg forest_night_shadows_a
hide extra3
hide extra2
hide extra
with medium_dissolve
pause 0.5
show bri neutral red3 at left
show expression AlphaMask("foliage3", At("bri neutral red3", left)) as mask
with dissolve
window show
b "\"Viu? Você está voltando a si.\""
hide mask
hide bri
with dissolve
"O medo sobe em sua garganta, algo profundo em seu cérebro dizendo para fugir daquela voz, escapar dela."
"Mas ele ainda está muito confuso para entender quem ou o que ele é agora, porque ainda se sente como nada."
"Mas ele também está consciente o suficiente para saber que ele é, de fato, algo."
window hide
play ambient heartbeat
show camforest
show bg forest_night_shadows_b at zooming5 as extra2 behind camforest
show camforest at zooming5 as extra
with medium_dissolve
pause 1.0
window show
"Ele lembra que é alguém chamado Cameron."
"Ele lembra de sua situação, e lembra que foi drogado com cogumelos e Xanax."
"Sua viagem atingiu o pico vertiginoso, seu senso de si mesmo tão completamente dizimado que ele não tem certeza se algum dia se sentirá o mesmo novamente."
"O terror e tortura dos últimos dois dias culminaram nisso, o momento em que sua mente cede e quebra, e Cameron não consegue mais distinguir o que é real do que não é."
"... Mas há algo mais também."
"Apesar da terrível perda de quem ele era, Cameron, essa amalgamação que ele chama de Cameron, está sentindo as coisas ainda mais vividamente do que há alguns minutos atrás, quando ele contatou Dev."
"Cameron vê o que está à sua frente, mas está vendo muito mais."
hide camforest
hide extra
hide extra2
show bg hollow_visions
show bri evilgrin red at left:
    xoffset -150
show brianshadow2 at left:
    xoffset -150
show black as temp behind bri:
    alpha 0.6
show dev angry s red at center:
    flip
    xoffset 200
show devshadow at center:
    xoffset 200
show cam horror red at twelve
show camshadow at twelve
show blood08:
    alpha 0.5
with dis3
"Em sua mente, ele olha {i}para frente{/i}, e vê uma miríade de pessoas à sua frente, embora sejam todas as mesmas pessoas: Devon, Brian e ele mesmo, presos em um redemoinho violento de garras e dentes, sangue e vísceras horríveis e irreconhecíveis."
show black
with dis2
"É confuso, ver tantas versões de si mesmo e de seu namorado, e ele vira a cabeça para olhar para longe, não querendo ver aquela violência."
hide bg hollow_visions
hide black
hide bri
hide dev
hide cam
hide camshadow
hide devshadow
hide brianshadow2
hide blood08
show bg forest_night_shadows_a behind extra2:
    zoom 1.02
    truecenter
show bri evilgrin red3 at left
show brianshadow2 at left
show expression AlphaMask("foliage3", At("bri evilgrin red3", left)) as mask
show cam horror red3 at center
show camshadow at center
show expression AlphaMask("foliage3", At("cam horror red3", center)) as mask2
show blood08:
    alpha 0.5
hide black
with dis2
"Então, percebendo algo sobre seu ombro, ele olha {i}para trás{/i}, e desta vez vê uma versão de si mesmo, junto com Brian."
"Ele vê seu corpo inconsciente sendo pressionado contra a árvore por um tempo antes de desmoronar no chão."
window hide
pause 0.5
stop ambient fadeout 6.0
scene bg forest_night_shadows_a:
    zoom 1.02
    truecenter
with medium_dissolve
pause 0.5
window show
c "\"Que diabos?\""
show cam sad_alt red3 at right
show expression AlphaMask("foliage3", At("cam sad_alt red3", right)) as mask2
with dissolve
"Sua voz é baixa, rouca e quase inaudível."
"Brian ri, assustando o coiote com suas visões de violência."
show bri evilgrin red3 at left,jumping
show expression AlphaMask("foliage3", At("bri evilgrin red3", left)) as mask at jumping
show cam shocked red3 at jumping
show expression AlphaMask("foliage3", At("cam shocked red3", right)) as mask2 at jumping
b "\"Eu te enforquei até você apagar, isso que foi!\""
show cam worried_alt red3
show expression AlphaMask("foliage3", At("cam worried_alt red3", right)) as mask2
with dis
"Cameron pisca para o urso, então de volta para a floresta."
c "\"Eu pensei que tinha morrido.\""
show bri smirk2 red3
show expression AlphaMask("foliage3", At("bri smirk2 red3", left)) as mask
with dis
b "\"Heh, ainda não, garoto. Temos algumas coisas para fazer primeiro, e você provavelmente quer ver seu namorado também, né? Não sei se você vai conseguir falar com ele já que ele está desmaiado.\""
show cam confused a red3
show expression AlphaMask("foliage3", At("cam confused a red3", right)) as mask2
with dis
c "\"Desmaiado?\""
show bri smirk red3
show expression AlphaMask("foliage3", At("bri smirk red3", left)) as mask
with dis
b "\"Isso.\""
show cam scared red3
show expression AlphaMask("foliage3", At("cam scared red3", right)) as mask2
with dis
c "\"Espera, com o quê?\""
show bri smirk2 red3
show expression AlphaMask("foliage3", At("bri smirk2 red3", left)) as mask
with dis
b "\"Relaxa, é só Rohypnol. Claro, eu dei uma boa dose, mas eles estão com algumas décadas porque foram proibidos nos EUA nos anos 90, e sabe, quando os comprimidos ficam velhos, não funcionam tão bem--\""
"Brian continua falando sobre Rohypnol e como costumava ser a principal droga de estupro no país."
show cam serious a red3
show expression AlphaMask("foliage3", At("cam serious a red3", right)) as mask2
with dis
"Cameron observa a boca do urso se mover em ondas e ondulações, dentes amarelos saindo por trás dos lábios enquanto a saliva se acumula e forma espuma nos cantos."
"{i}Quem está vendo isso?{/i}"
"Cameron se tranquiliza automaticamente."
"Eu estou {i}vendo isso, e{/i} eu {i}preciso salvar o Devon.{/i}"
"Ele não está tão convencido da primeira parte, no entanto."
window hide
show forest_night_shadows_b as extrabg:
    zoom 1.02
    truecenter
show black:
    alpha 0.6
with fast_dissolve
pause 1.0
centertext "Eu."
centertext "Mim."
centertext "Cameron."
centertext "Conceitos simples que não são mais tão simples."
centertext "Assim como no ensino médio, ele parou de existir."
centertext "É diferente desta vez, porém."
centertext "O Xanax certamente está suprimindo o pânico que ele deveria estar sentindo agora, mas desta vez, sua perspectiva é de um ângulo completamente diferente."
centertext "A amalgamação de Cameron ainda existe, mas as fronteiras se dissolveram, e ele parece estar se infiltrando em tudo."
centertext "Apesar de já saber que é insignificante, ele ainda está\n maravilhado com o quão pequeno 'Cameron' é comparado ao mundo."
centertext "Até os insetos rastejando sob as folhas fazem Cameron\n se sentir pequeno; um mundo inteiro sobre o qual ele não sabe nada."
centertext "Mas entrelaçar sua identidade com o universo\n significa que ele também está entrelaçado com Brian."
centertext "O urso está faltando partes de si mesmo, meio que como Artie, pedaços\n quebrados e buracos irregulares marcando a paisagem de sua vida."
centertext "Cameron quase sente pena dele, que talvez se as coisas tivessem\n sido um pouco diferentes, as chances um pouco mais a favor de Brian,\n ele poderia ter sido uma pessoa muito diferente."
pause 1.0
hide black
hide extrabg
with fast_dissolve
window show
"O que é realmente perturbador, porém, é a afeição genuína que ele tem por Cameron, seu desejo de acariciar e segurar o coiote, mas..."
"Há um ódio lá também, uma repulsa pelo que Cameron é."
"Jovem, atraente e um viado..."
"Não apenas {i}queer{/i} como Brian se considera ser, mas um viado."
"O tipo de queer que age fofo antes de foder os homens de verdade que deveriam estar fazendo todo o foda."
"Então é bom punir Cameron, mas é ainda melhor vê-lo sofrer, ver a maneira como seu corpo se contorce, sua boca aberta por ar, seus olhos arregalados e temerosos."
"Cameron sente-se recuar ao entender o processo de pensamento de Brian, uma maneira de pensar que ele nunca consideraria."
"Mas esse processo de pensamento não é o que faz de Brian a pessoa terrível que ele é."
"Cameron sabe que a maioria não tem escolha em como seus interesses sexuais e fetiches se desenvolvem, então os pensamentos em si não são exatamente malignos, pelo menos não para Cameron."
"Cameron conheceu alguns caras da faculdade que tinham interesses semelhantes aos de Brian."
"Durante seu primeiro ano namorando Devon, o urso timidamente perguntou se ele poderia fechar gentilmente os dentes no pescoço do coiote e rosnar."
"Foi emocionante e intenso, e Cameron adorou a adrenalina."
"Mas então Devon teve um pesadelo sobre arrancar a garganta de Cameron, e isso foi o fim daquilo."
"Então, para Cameron, Brian não é tão estranho."
"O que torna Brian diferente não é que ele tenha fetiches."
"Ele não é louco."
"Ele não é um psicopata."
"Não, a verdadeira raiz do mal de Brian é clara."
"Ele é egoísta, e nunca está satisfeito com o que consegue."
"Egoísta o suficiente para colocar dezenas de jovens em torturas horríveis até que finalmente morressem."
"Tudo enquanto tinha a capacidade de se controlar completamente."
"Tudo enquanto tinha acesso total a alternativas como role-play."
"Mas não é o suficiente para Brian."
"Ele sempre precisa de mais."
"Tudo para sua fugaz gratificação sexual alimentada por drogas porque em algum momento, Brian decidiu que isso o fazia se sentir bem, então foda-se esse mundo que o faz se sentir mal."
"Mas ele encontrou alguma liberação em estrangular Cameron, e agora seu foco está voltando para uma vaga ideia de como usar as habilidades de Cameron."
"Algo para impedi-lo de passar o resto da eternidade com suas vítimas o torturando."
"Cameron poderia estragar o final para Brian, deixá-lo saber que quando todos morrem, eles simplesmente deixam de ser o que eram."
"Isso é tudo."
"Fantasmas, demônios, poltergeists?"
"Criações dos vivos... e seja lá o que estiver em Echo."
show cam worried a l red3
show expression AlphaMask("foliage3", At("cam worried a l red3", right)) as mask2
with dis
"Cameron recua neste ponto, ficando sobrecarregado por todos os pensamentos vindos do velho urso, incapaz de entendê-los sem mais contexto."
show cam worried_alt red3
show expression AlphaMask("foliage3", At("cam worried_alt red3", right)) as mask2
with dis
"Olhando {i}para frente{/i}, ele vislumbra os vários cenários novamente, e a única constante é a morte."
"A maioria envolve ele morrendo, e uma boa parte envolve Devon morrendo também."
"Cameron imagina que isso é indicativo do que é mais provável que aconteça."
"Mas alguns, apenas dois, de fato, mostram Cameron e Devon sobrevivendo, com Brian vivendo ou morrendo."
"Cameron não se importa muito com o último, contanto que possa tirar Devon e a si mesmo de Echo vivos."
"Eles podem lidar com Brian depois."
"Cameron nem se importa muito se ele não conseguir, especialmente neste estado de espírito, mas ele não aceitará não poder salvar Devon."
"De repente, lembrando do que fez antes, Cameron tenta sutilmente esfregar o bolso e fica surpreso que a chave ainda está lá."
show cam worried a red3
show expression AlphaMask("foliage3", At("cam worried a red3", right)) as mask2
with dis
"Brian sabe?"
"Bem, ele sabe o que Cameron havia planejado, mas em sua própria empolgação, e especialmente porque está drogado, ele está hiperfocado em outras coisas."
"Ele também não percebeu a chave sendo tirada do bolso."
"Isso, e a memória de Brian é terrível."
"Décadas de drogas em doses neurotóxicas desmantelaram quem ele costumava ser."
"Ele nem parece se lembrar por que estrangulou Cameron em primeiro lugar."
show bri smirk2 red3
show expression AlphaMask("foliage3", At("bri smirk red3", left)) as mask
with dis
b "\"...tive que fazer conexões em Sonora. A coisa era vendida sem receita lá, então era fácil de conseguir, mas passar pela porra da fronteira é um problema completamente diferente--\""
show bri serious red3
show expression AlphaMask("foliage3", At("bri serious red3", left)) as mask
with dis
"Brian de repente para de falar, os olhos estreitando."
"O pulso de Cameron acelera enquanto ele se pergunta se Brian acabou de se lembrar de seu plano."
stop music fadeout 10.0
play ambient crickets fadein 10.0
show cam surprised a red3
show expression AlphaMask("foliage3", At("cam surprised a red3", right)) as mask2
with dis
c "\"O que foi?\""
"Sua voz ainda está áspera do enforcamento, uma dor profunda começando a emanar do centro de seu pescoço."
b "\"Eu não sei, só gosto mais de você quando está sorrindo, mas se eu estou te enchendo o saco, é só dizer.\""
"Leva alguns segundos para Cameron entender do que Brian está falando, então mais alguns para escanear os pensamentos do urso."
"Na mente de Brian, seu sorriso tem muito a ver com o quão interessante a explicação excessiva do urso sobre Rohypnol é, então Cameron rapidamente coloca um em seu rosto."
show cam smile c red3
show expression AlphaMask("foliage3", At("cam smile c red3", right)) as mask2
with dis
play music zen fadein 5.0 volume 0.2
c "\"Ah, desculpe, é realmente interessante. Eu só estou tão sobrecarregado com as drogas e--\""
show bri angry red3
show expression AlphaMask("foliage3", At("bri angry red3", left)) as mask
with dis
b "\"Cala a boca.\""
show cam worried a red3
show expression AlphaMask("foliage3", At("cam worried a red3", right)) as mask2
with dis
"Cameron cala a boca."
"Brian começa a mexer a mandíbula, como se estivesse mastigando algo, antes de cerrar os punhos."
show bri angry fists red3
show expression AlphaMask("foliage3", At("bri angry fists red3", left)) as mask
show cam horrified red3
show expression AlphaMask("foliage3", At("cam horrified red3", right)) as mask2
with dis
"Cameron se tensiona, preparando-se para ser atingido novamente."
b "\"Você é bonitinho, mas não tanto, e eu não sou tão estúpido. Eu odeio viados como você, bajulando e chupando pau para conseguir o que realmente quer.\""
"A mente de Brian passa por alguns rostos, mas o único definido o suficiente para Cameron compreender é um raposo com um chapéu vermelho."
"Então Brian parece relaxar, mas a raiva ainda está lá, o urso tendo a aprimorado para se tornar mais frio e controlado, o que só o torna ainda mais aterrorizante."
"Claro, estimulantes aumentam a empatia em um cérebro normal, mas se Brian os abusou ao ponto que anfetaminas parecem cafeína, então provavelmente só aumenta sua irritabilidade e raiva."
"Era assim que sua mãe era no final, e sempre confundia Cameron o porquê de alguém querer usar uma droga que os faz sentir pior."
b "\"Tive uma ideia melhor.\""
window hide
show cam scared red3
show expression AlphaMask("foliage3", At("cam scared red3", right)) as mask2
with dis
pause 0.5
hide bri
hide cam
hide mask
hide mask2
with vpunch
window show
"Cameron suspira quando Brian o agarra pela orelha."
c "\"Não, não! Pare, eu posso andar com você.\""
c "\"Eu não vou tentar correr--{w=0.4}{nw}"
extend" AI!\" with vpunch
"Cameron sente a diversão do urso com seu medo de ser puxado pela orelha novamente, e o coiote rapidamente suplica, percebendo que isso pode desviar os interesses de Brian de usar Cameron para tortura em vez de suas habilidades."
"A dor foi cegante, mas não é nada, absolutamente nada comparado ao que este urso fez com os outros."
"Cameron consegue se acomodar em uma caminhada tropeçando enquanto Brian o puxa, curvado e tentando ver o chão no escuro, enquanto tenta seguir cuidadosamente os movimentos brutos e imprevisíveis do urso."
"A cada minuto ou mais, Cameron olha {i}para frente{/i}, e vê o cenário que está buscando, ainda ao alcance, então ele continua andando."
"Enquanto isso, uma van emerge das árvores, estacionada um pouco longe da estrada."
show bri horror red3 at left
show expression AlphaMask("foliage3", At("bri horror red3", left)) as mask
with dissolve
"Brian congela, encarando."
"Então ele solta uma risada surpresa."
stop music fadeout 10.0
show bri evilgrin red3
show expression AlphaMask("foliage3", At("bri evilgrin red3", left)) as mask
with dis
b "\"Bem, eu estarei danado. O filho da puta escapou!\""
show cam confused c red3
show expression AlphaMask("foliage3", At("cam confused c red3", center)) as mask2
with dis
c "\"Quem?\""
"O coiote faz uma careta enquanto Brian continua segurando-o pela orelha."
"Cameron espera que ele esteja falando sobre Devon, mesmo que possa sentir a presença do urso mais jovem logo à frente deles."
"O coiote ficaria feliz em estar errado sobre suas habilidades, especialmente se isso significar que Devon escapou."
"Mas Cameron sabe."
show bri evilgrin3 red3
show expression AlphaMask("foliage3", At("bri evilgrin3 red3", left)) as mask
with dis
b "\"Aquele gato! Eu juro que atirei nele duas vezes também. Mas então, ele não fez aquela coisa estranha de se contorcer que as pessoas fazem quando você dá o tiro fatal, então devo ter errado na segunda vez.\""
b "\"Pensei que talvez eu tivesse matado ele com o primeiro.\""
show cam worried_alt red3
show expression AlphaMask("foliage3", At("cam worried_alt red3", center)) as mask2
with dis
"Cameron olha para onde Brian está encarando e vê o local onde Arturo deve ter estado."
show cam sad red3
show expression AlphaMask("foliage3", At("cam sad red3", center)) as mask2
with dis
"Manchas escuras cobrem as folhas, junto com o que parece ser vômito, e Cameron sente seu próprio estômago revirar com a visão."
"É difícil conectar seu amigo extrovertido e despreocupado àquela bagunça, e Cameron sente a culpa se misturar à sua miséria ao perceber que o que está acontecendo com Artie é culpa deles."
"Mas ele sabe que Artie está longe agora, a quilômetros de distância, e Cameron silenciosamente incentiva o gato a continuar, a fazer o que puder para salvá-los e a si mesmo, mesmo que ele claramente esteja em péssimo estado."
"Cameron espera que Artie possa ouvi-lo, mesmo que esteja acordado agora."
show bri lookdown red3
show expression AlphaMask("foliage3", At("bri lookdown red3", left)) as mask
with dis
"Cameron sente outra mudança sinistra na motivação do urso."
"Brian não acha que Artie chegará à rodovia, e ele sabe que deveria procurar pelo gato."
"Mas tudo está tão fodido desde o início: três jovens que provavelmente têm famílias e grupos de amigos próximos, todos os três feridos, espancados, e todos os três sabendo muito bem do que Brian é capaz..."
"Não há mais sentido nisso."
"Brian quase havia voltado a pensar que escaparia de tudo isso de alguma forma, mas não."
"Este é o fim."
show bri neutral red3
show expression AlphaMask("foliage3", At("bri neutral red3", left)) as mask
with dis
b "\"Bem... Acho que é isso, então. Sabia que estava chegando perto há um tempo. Tipo, sabia disso quando deixei o telefone do garoto tocando no meu trailer.\""
show cam worried a red3
show expression AlphaMask("foliage3", At("cam worried a red3", center)) as mask2
with dis
"A calma com que Brian aceita seu fim iminente faz Cameron querer tentar escapar novamente."
"Por que esse urso não pode simplesmente acabar com isso sem levá-los junto?"
"É o fim para ele, não para eles."
show cam smile a red3
show expression AlphaMask("foliage3", At("cam smile a red3", center)) as mask2
with dis
c "\"Posso ver o Devon?\""
"Cameron sorri sem entusiasmo, esperando que isso possa influenciar o urso, mas ele não está prestando atenção no coiote."
"Brian balança a cabeça para a versão sóbria de si mesmo, a versão que realmente planejava deixar Cameron ir, porque por que ele acrescentaria a seus problemas matando o coiote se ele pudesse tirá-los todos?"
"É por isso que ele tentou ser legal com ele, e então é claro que as coisas saíram do controle."
"Cameron começa a tremer ao sentir a excitação e a empolgação de Brian."
"Ele está pensando em Cameron, em seu saquinho cheio de sais de banho, e em quanto tempo pode levar para encontrá-los em--"
show cam scared red3
show expression AlphaMask("foliage3", At("cam scared red3", center)) as mask2
with dis
stop music fadeout 10.0
"Cameron empalidece mentalmente, incerto sobre o que é aquele lugar sombrio cheio de morte, mas sabe que não quer ir para lá."
c "\"Para onde você está me levando?\""
show bri angry red3
show expression AlphaMask("foliage3", At("bri angry red3", left)) as mask
with dis
b "\"Você é o psíquico. Descubra.\""
hide bri
hide mask
hide mask2
hide cam
with dissolve
"Mantendo sua pegada no coiote, Brian puxa Cameron em direção à van."
window hide
pause 0.5
scene black with medium_dissolve
pause 1.0
play music lingeringintro fadein 15.0 volume 0.3
queue music lingeringloop volume 0.3
scene bg outskirts_night with medium_dissolve
pause 0.5
window show
"Não demora muito para Artie perceber que as luzes ao longo da rodovia estão na verdade muito mais longe do que ele pensava."
"Ele não tem ideia de quanto tempo está andando, mas parece pelo menos uma hora, e a estrada está talvez um pouco mais perto."
"Neste ponto, ele está tão fraco, seus movimentos tão descoordenados, que no fundo ele sabe que seu corpo está prestes a desistir."
"Cada tontura, cada onda de ansiedade, aterroriza o gato que ele possa ter outra convulsão, e se tiver, sabe que não vai se levantar novamente."
c "\"{i}Artie, por favor...{/i}\""
a "\"C-C-Cam?\""
"Artie olha ao redor, esperançoso."
"Ele provavelmente começaria a chorar agora se Cameron simplesmente aparecesse, mesmo que fosse só porque ele não estaria mais sozinho."
"Mas então Artie vê um par de faróis mais perto que os outros."
"E eles ficam cada vez mais perto."
"Artie nota que as luzes estão vindo direto para ele, e ele não se incomoda em sair da estrada, sentindo que isso deve ser uma situação de luz-no-fim-do-túnel."
window hide
pause 0.5
play background engine fadein 5.0
show headlights with medium_dissolve
pause 0.5
window show
"E então as luzes diminuem e Artie ouve o som de um motor."
unk "\"Que PORRA você tá fazendo parado no meio da PORRA da ESTRADA como um IDIOTA!\""
"As orelhas de Artie se contraem, reconhecendo a voz de algum lugar em seu passado, no que poderia muito bem ser outra vida."
"É difícil dizer porque estão gritando com ele."
play sound cardoor3
"Uma porta de carro se abre e Artie apenas fica parado, perdido na luz."
unk "\"Eu disse pra vocês irem se foder! Primeiro a porra do bar tá fechado por causa de algum resfriado, e agora vocês ainda tão aqui pra me encher? Eu só quero beber um POUCO pra relaxar!\""
"Arturo franze a testa, nunca tendo ouvido aquela palavra em particular ser usada daquela maneira."
"Uma figura começa a se materializar na frente de Arturo, e finalmente ele o reconhece."
window hide
pause 0.5
scene duke_car
with medium_dissolve
pause 0.5
window show
Weasel "\"O que aconteceu com você?\""
"O doninha o encara, então inclina a cabeça para o lado, apertando os olhos antes de estender a mão e girar Arturo levemente pelo ombro."
#show duk angry dark with dis
Weasel "\"Merda, não tem como! Ele não poderia ser tão fodendo...\""
"O doninha se interrompe, então olha para o rosto de Artie."
Weasel "\"Quem fez isso?\""
"Artie relutantemente abre a boca, por algum motivo sentindo-se quase envergonhado por sua condição."
a "\"U-u-u-urso...\""
"O doninha o encara com um olhar estranho."
#show duk neutral dark with dis
Weasel "\"Bar? Sim, eu estava no bar. Está fechado.\""
a "\"U-u-urso.\""
#show duk angry dark with dis
Weasel "\"Urso? Brian?\""
"Arturo acena com a cabeça e imediatamente se arrepende ao quase cair."
#show duk neutral dark with dis
Weasel "\"Caramba, você tá bem fodido, não tá?\""
"Arturo encara de volta para o doninha e percebe sua expressão, como se estivesse tentando decidir algo."
"Não é a reação certa para a situação, e Artie de repente sente que pode estar em perigo, mas não tem ideia do porquê."
"Tudo o que ele lembra é que esse velho havia derrubado Devon com dois socos, então combinado com seu estado atual, ele não pode fazer nada."
"Então, o doninha parece sair do que quer que estivesse pensando."
#show duk smirk dark with dis
Weasel "\"Bem, eu estarei danado. É isso então, não é? Aquele filho da puta idiota. Tá bem, entra. Vamos pro hospital.\""
#hide duk with dissolve
show duke_car2 with dis2
"Arturo tropeça para frente, e assim que o doninha percebe que ele está tendo problemas para se mover, ele ajuda Arturo a entrar."
"Enquanto faz isso, o doninha suga o ar, fazendo uma careta."
Weasel "\"Jesus Cristo, isso tá realmente me fazendo não querer fazer o que eu vou ter que fazer depois disso. Mas sabe, tudo tem que acabar eventualmente.\""
"Arturo não tem certeza sobre o que o velho doninha está falando, mas se ele está o levando para o hospital, então pelo menos está no caminho certo."
a "\"A-a-a-amigos...\""
Weasel "\"Sim, sim, vou chamar a polícia de Payton... depois de te deixar lá. Tenho que me certificar de que posso voltar antes deles, porém.\""
"Arturo decide que é o doninha que está agindo estranho."
"Mas, enquanto o estranho doninha começa a fazer uma baliza para dirigir de volta para a rodovia, Arturo está apenas grato."
stop background fadeout 7.0
stop music fadeout 10.0
"Ele fez o que pôde, e agora o resto é com Deus."
"Ele só pode rezar."
"Então ele reza por Devon, Cameron, Maria e por si mesmo, porque se sobreviver, ele sabe que a estrada à sua frente é longa, fraturada e quebrada."
window hide
stop ambient fadeout 6.0
pause 0.5
scene black with medium_dissolve
pause 0.5
play background roughdrive fadein 10.0
pause 1.0
scene van_night at car with medium_dissolve:
    zoom 1.02
    truecenter
pause 1.0
window show
"Devon sente seu corpo balançando e tremendo em uma superfície metálica dura, ocasionalmente inclinando de um lado para o outro, sentindo como se estivesse deitado em um carro fazendo curvas fechadas."
"O urso abre os olhos, gemendo."
c "\"Dev?\""
d "\"Nnh, Cam?\""
"É Cameron dirigindo?"
"O coiote tem seu próprio sedã que dirige, mas geralmente se estão juntos, é no jipe de Devon."
"A princípio, ele pensa que talvez tenha dado o volante ao coiote para que ele mesmo possa descansar, mas eles vieram no Jeep, e Cameron não sabe dirigir manual, certo?"
"{i}Vamos lá, pare de assumir coisas{/i}."
"Ultimamente, Cameron parece se irritar sempre que ele faz isso."
"Ultimamente, como em desde que chegaram em Echo."
c "\"Devon? Eu estou aqui. Como você está?\""
"A voz gentil e preocupada de Cameron está claramente mascarando algo tenso e desesperado por baixo."
d "\"Cameron? O-O que foi? O que há de errado?\""
b "\"Eu te disse, ele tá todo drogado.\""
c "\"Mas ele mal consegue falar.\""
d "\"Cam?\""
b "\"Exatamente, eu já te disse que dei Rohypnol pra ele. É como desmaiar. Enfim, tá passando. Ele só tá cansado.\""
c "\"Isso é sangue?{w=0.3} Por que ele está sangrando!?\""
b "\"Fez isso consigo mesmo. Imagina a bagunça que teríamos se ele não estivesse drogado, né? Nunca confie num urso pra ficar quieto quando você acorrenta ele.\""
c "\"Devon, você pode me ouvir? Você está bem?\""
d "\"Sim, sim...\""
window hide
scene bg black with medium_dissolve
stop background fadeout 6.0
window show
"Então, ele está voltando a dormir novamente."
"Mais sons de dirigir em uma estrada ruim, cascalho rangendo sob as rodas e batendo no assoalho."
window hide
play ambient crickets fadein 5.0
scene van_night with medium_dissolve:
    zoom 1.02
    truecenter
pause 1.0
window show
"Quando ele acorda novamente, parou e Devon percebe que as portas da van estão abertas."
b "\"Parece que passou bem na hora.\""
c "\"Posso ir até ele... Por favor?\""
"Devon vê que uma das orelhas de Cameron está torcida na mão do urso mais velho, a cabeça do coiote inclinada para o lado, fazendo caretas enquanto tenta olhar melhor para Devon."
"O urso mais jovem fica muito quieto, vendo seu melhor amigo sendo segurado pela pior pessoa que ele já conheceu."
"Uma de suas orelhas macias e sensíveis que Devon havia brincado incontáveis vezes no passado agora está torcida firmemente sobre si mesma."
"Na outra pata de Brian, ele segura uma espingarda."
"Além de tudo, Brian parece mais irritado que o normal."
"Na verdade, ele está olhando para Cameron com uma expressão de total desprezo, enquanto Cameron não está prestando atenção nele, olhando intensamente para Devon."
b "\"Claro. Fodendo típico. Que bom que guardei isso.\""
"Ele de repente agarra o coiote pelos ombros e o vira para enfrentá-lo, para ficar de costas para Devon."
"Mesmo assim, não há confusão sobre o que acontece com Cameron em seguida."
"Brian se vira levemente para longe de Cameron, então gira e envia o dorso de sua pata pelo focinho do coiote."
window hide None
play sound "<from 0.11>sounds/punch.ogg"
with vpunch
stop ambient
play music solderingloop fadein 5.0 volume 0.3
pause 0.5
window show
"O som é tão alto que Devon é chocado para acordar, a adrenalina compensando o sedativo."
"A princípio, Devon se recusa a acreditar no que acabou de ver, que um som como aquele poderia ter sido feito com o focinho de Cameron."
"A cabeça do coiote se inclina para a direita antes dele instantaneamente começar a desmoronar, mas Brian o segura."
d "\"Ei!\""
"Devon grita automaticamente, chocado com o que acabou de ver."
"Ele nunca tinha visto alguém ser atingido com tanta força em toda a sua vida."
"No silêncio que se segue, o som distinto de algo pequeno batendo nas paredes da van, como se uma conta de plástico tivesse sido jogada contra as paredes de metal."
"Devon o ouve cair ao seu lado, e olhando para baixo, vê algo longo girando no lugar antes de finalmente parar."
"É fino, branco, e começa largo, mas afina até uma ponta afiada."
"Devon só tem um momento para se concentrar nisso antes que ele grunha quando Cameron cai em cima dele, Brian tendo o empurrado."
play sound thud
scene catastrophic_failure1:
    zoom 1.02
    truecenter
"Enquanto olha para baixo para o coiote e vê o sangue começando a escorrer de sua boca, Devon percebe que a coisa branca é um dos dentes de Cameron, e a raiva chocada supera o medo." with vpunch
scene catastrophic_failure2 with dis:
    zoom 1.02
    truecenter
d "\"EEEEEEI!\""
"Todo o senso parece ter deixado Devon, tudo o que ele está sentindo e pensando se condensando naquela única palavra que ele grita para expressar sua raiva."
scene catastrophic_failure1 with dis:
    zoom 1.02
    truecenter
d "\"Cam?{w=0.3} CAM!\""
"O pânico o faz respirar rápido, embora ele tente evitar que seu peito se mova para não balançar a cabeça de Cameron."
"Brian o havia atingido com tanta força que definitivamente poderia tê-lo matado."
"O que torna tudo ainda mais aterrorizante é a maneira como o corpo de Cameron ficou mole."
"Foi tão reminiscente do colapso repentino de Artie quando ele havia repentinamente perdido a vida."
"Mas Cameron está respirando, embora de uma maneira terrível e bufante."
d "\"Cammy, querido, você pode me ouvir?\""
"O pânico em sua voz diminui para um gemido quase lamentável enquanto ele encara o coiote se contorcendo, seus olhos meio abertos e sua cabeça virando lentamente de um lado para o outro."
b "\"Ops, exagrei um pouco nele, heh. Porra, isso doeu!\""
"Brian balança a pata que usou para bater em Cameron, como se bater no focinho do coiote a tivesse feito arder."
"A raiva de Devon cresce mais uma vez."
scene catastrophic_failure2 with dis:
    zoom 1.02
    truecenter
d "\"BRIAN!{w=0.3} Eu vou te matar!\""
"Brian parece surpreso por apenas um segundo, então continua sorrindo, gostando da reação, como se estivesse assistindo a um show."
"Isso só deixa Devon com mais raiva."
d "\"Vou arrancar cada dente da sua cabeça! Vou arrancar sua garganta, eu vou... vou...\""
"A voz de Devon enfraquece, quebra, então some sob a aparente alegria do urso mais velho com a fúria do urso mais jovem."
stop music fadeout 10.0
play ambient crickets fadein 10.0
"Percebendo que as orelhas de Cameron estão se contraindo com seus gritos, Devon volta sua atenção para o coiote enquanto ele solta um gemido baixo e rouco."
scene catastrophic_failure1 with dis:
    zoom 1.02
    truecenter
d "\"Cameron, querido, você pode me ouvir, certo? Cameron?\""
"Enquanto isso, sangue escorre do nariz e da boca do coiote, infiltrando-se na pele do estômago e do lado de Devon."
"Devon tenta manter seus soluços e suspiros no mínimo enquanto a cabeça de Cameron continua repousando sobre seu diafragma."
"Os olhos de Cameron tremem, então ele pisca, e Devon vê a luz da consciência reentrar em seus olhos."
d "\"Cam!\""
c "\"... Devon?\""
#NOTE: SONG EDIT
play music sagebrushcut fadein 20.0 volume 0.3
"Cameron grunhe baixinho, levantando a cabeça levemente."
"Brian já parece entediado com a catástrofe que acabou de criar, e agora continua olhando por cima do ombro para a escuridão que se estende atrás dele, mudando impacientemente."
b "\"Tá bem, seja rápido, coiote. Precisamos nos mover.\""
scene catastrophic_failure2 with dis:
    zoom 1.02
    truecenter
d "\"Não toque nele!{w=0.3} Você poderia ter quebrado o pescoço dele!\""
"A voz de Devon quebra e fica rouca novamente."
scene catastrophic_failure1 with dis:
    zoom 1.02
    truecenter
"Brian se arrepia, finalmente reagindo, mas Devon volta sua atenção para Cameron, continuando a tentar gentilmente persuadi-lo a um estado de consciência."
d "\"Vamos, querido, você pode me ouvir? Você pode entender o que estou dizendo?\""
window hide
scene van_night with leftwipe
window show
"Lentamente, Cameron levanta a cabeça, uma mistura de sangue e saliva conectando seu lábio à pele de Devon em um fio longo."
c "\"Estou bem. Estou bem.\""
"Cameron parece confuso enquanto murmura, tentando se levantar instavelmente."
d "\"Não! Fique parado.\""
b "\"Não, levanta. Eu não te disse o que faria com seu urso se você não--\""
d "\"Então faça! Venha aqui e faça, seu covarde! Seu lixo--\""
c "\"Devon.\""
"A voz de Cameron é calma, embora quieta e fraca, e o urso fica em silêncio enquanto se concentra novamente no coiote."
"Ele tem a cabeça levantada, tentando se concentrar no rosto de Devon."
c "\"Quem está sentindo isso agora?\""
"A pergunta pega o urso de surpresa."
d "\"O quê?\""
c "\"As minas, isso mesmo. Eu estou indo para as minas, e vou voltar por você.\""
"Cameron coloca uma pata em seu focinho, fazendo caretas enquanto fecha os olhos com força."
d "\"O quê? Que minas? Fique aqui.\""
"Os olhos de Devon se enchem de lágrimas, vendo que o coiote está mal coerente, mal capaz de entender o que está acontecendo."
"Então Cameron se inclina para beijar o urso, novamente pegando Devon de surpresa."
"Ele imediatamente sente o cheiro e o gosto do sangue de Cameron, fazendo o nojo subir em sua garganta."
"Isso lembra ele de seus pesadelos de predação, mas Cameron insiste, então Devon apenas se concentra em não vomitar."
"Ele não quer sentir a lacuna onde o canino inferior esquerdo de Cameron costumava estar, a irregularidade de seu focinho já inchado."
"Enquanto ele se força a beijar de volta, sente algo mais pressionar contra seus lábios."
"Algo duro e de forma estranha, e Devon abre a boca, permitindo que o sangue inunde sua boca, mas com ele vem algo mais, e Devon percebe de uma vez que é a chave."
"Devon manobra a chave em sua boca o mais sutilmente que pode, ouvindo Brian suspirar impacientemente atrás de Cameron."
"Ela desliza sob sua língua facilmente, pequena em sua boca comparativamente grande."
"Cameron sussurra no ouvido de Devon."
c "\"Nós vamos voltar para casa juntos. Eu prometo.\""
d "\"Mas para onde você está indo? Por que as minas? Querido, por favor?\""
stop music fadeout 15.0
play ambient crickets fadein 15.0
"Devon não consegue manter o pânico choroso fora de sua voz, soando como um filhote, mas conseguindo manter as palavras claras com a pequena chave sob sua língua."
"Devon apenas encara Cameron enquanto ele se afasta, lágrimas escorrendo por suas bochechas enquanto seu coiote rasteja fracamente até seus pés e se apoia na parede da van."
b "\"Ah, você tá bem.\""
"Ele volta seu olhar para o urso furioso e choroso."
b "\"Fique quieto, garoto. Voltamos daqui a pouco. Eu prometo.\""
window hide
pause 0.5
scene black with medium_dissolve
pause 1.0
scene mines with medium_dissolve
pause 0.5
window show
"Ser nocauteado, recuperar a consciência, tropeçar no escuro, tudo enquanto está em uma quantidade desconhecida de cogumelos é... angustiante."
"Essa é a única palavra que Cameron sente ser apropriada para esta situação: angustiante."
"O mundo é mais sonho do que seus sonhos."
"Essa combinação de fatores desorientadores deixa Cameron se debatendo através de uma série de eventos imediatamente após ele ter alcançado o velho urso."
"Brian agarrou sua pata, e de repente eles estavam se movendo rapidamente pelo deserto antes que Cameron seja puxado para um lugar que é frio e escuro, iluminado fracamente por uma lanterna elétrica antiga, sua alça pendurada no cano da espingarda de Brian."
"Se Cameron pensou que sua percepção de tempo estava fodida com maconha, agora está torcida sobre si mesma."
"Ele está exausto, sem comer uma refeição adequada em bem mais de um dia, e sua garganta está tão seca que ele acha que pode estar disposto a beber a água drogada de Brian."
stop ambient fadeout 5.0
"Cada vez que Brian vira uma curva primeiro, ou seu volume o obscurece, a luz da lanterna desaparece e deixa Cameron na escuridão."
"Cada vez que isso acontece, arcos vermelhos brilhantes enchem sua visão."
window hide
pause 0.5
play ambient mines02 fadein 3.0 volume 0.3
scene black with medium_dissolve
pause 1.0
#scene bg closed_eyes5 with slow_dissolve:
#    zoom 1.02
#    truecenter
scene mine_blur:
    alpha 0.5
    zoom 1.02
    truecenter
show black behind mine_blur
show lamp:
    zoom 1.02
    truecenter
with slow_dissolve
pause 1.0
window show
"{i}Quem está na escuridão?{/i}"
show cam confused b mine at right behind lamp with dissolve
c "\"Eu estou. Eu estou na escuridão.\""
"{i}Tudo está na escuridão{/i}."
show cam worried b mine at right with dis
c "\"Não, só eu.\""
show bri vaguestare mine at left behind lamp with dissolve
show cam shocked b mine at jumping
b "\"Pare de lutar contra isso. Só vai piorar.\""
"Cameron se surpreende com o aparecimento repentino do urso."
c "\"Onde eu estou?\""
show bri serious mine with dis
"Brian suspira profundamente novamente."
b "\"Não importa.\""
c "\"Mas--\""
hide cam
hide bri
scene black:
    zoom 1.02
    truecenter
play sound thud
"Cameron se encolhe quando algo o cutuca com força no esterno, torcendo-se sobre si mesmo, sentindo um buraco negro se abrir em seu peito." with vpunch
"Ele suga o resto de seu corpo e atenção para dentro dele enquanto o canino se encolhe no chão duro de terra, gemendo e grunhindo."
"Finalmente, o ar volta aos seus pulmões, e enquanto isso acontece, ele ouve um som de bufada novamente."
"Depois de um tempo, Cameron olha para cima de sua posição no chão para ver Brian de joelhos, parecendo cheirar o coronha de sua espingarda."
"Então Cameron percebe o pó branco, e ele entende o que está acontecendo."
play background droneandvoice fadein 15.0
"Cameron ouve uma voz familiar, uma que ele tem certeza de que está ouvindo, e não imaginando."
window hide
scene mine_blur:
    zoom 1.02
    truecenter
show lamp:
    zoom 1.02
    truecenter
with slow_dissolve
pause 0.5
window show
dy "\"Não cheire. Você está tentando revestir sua cavidade nasal, não seus pulmões.\""
show cam sad b mine at right behind lamp with dissolve
c "\"É assim que meus amigos faziam.\""
dy "\"Então seus amigos são idiotas.\""
"Brian olha para cima de sua linha de sais de banho desaparecendo."
show bri neutral mine at left behind lamp with dissolve
b "\"Com quem você tá falando?\""
show cam horrified b mine with dis
"Cameron tenta silenciosamente calar Dylan, mas Brian já os ouviu."
"Além disso, Brian não parece bravo ou chateado, mas seu olhar contínuo exige uma resposta."
show cam worried b mine with dis
c "\"Hum, o nome dele é Dylan. Ele é meu ex. Desculpe, nós não nos damos bem.\""
show bri smirk mine with dis
b "\"Tá tendo síndrome do terceiro homem? Sempre que eu fico muito fodido com muitas drogas por muito tempo, uma pessoa sempre aparece. Acabo tendo uma conversa com ela e tudo.\""
"Brian reajusta a maneira como está segurando sua lanterna e arma e agarra o braço de Cameron com a outra."
show bri confused mine with dis
b "\"Ouvi dizer que acontece com pessoas em situações de sobrevivência também. Enfim, eu sempre tô muito delirante pra lembrar quem é o terceiro homem.\""
show cam worried b mine with dis
c "\"Sim...\""
"Cameron não consegue entender como Dylan não é real, mas este urso pesadelo aparentemente é."
"Ele está sendo enganado?"
show bri angry mine with dis
b "\"Tá bem, aqui está o acordo: eu paro de te bater enquanto você estiver sorrindo, entendeu?\""
show cam confused b mine with dis
c "\"Hã?\""
show bri angry fists mine with dis
"Brian cerra os punhos significativamente."
show cam scared b mine with dis
"Cameron faz uma careta, então rapidamente estica a boca em um grande sorriso, mesmo que doa ao ponto de lágrimas se acumularem em seus olhos."
show cam happy b mine with dis
c "\"Ah! Desculpe, eu não percebi o que você estava falando por um segundo. Eu lembro agora!\""
show bri smirk2 mine with dis
b "\"Claro que lembra. Viado patético.\""
show cam grinning b mine with dis
"Brian continua a inspecionar Cameron enquanto o coiote permanece quieto, mantendo um sorriso colado em seu rosto."
"Essa experiência é demais."
"Tudo isso é demais."
"Ele só quer que pare, e fará o que este urso, esta fonte de seu tormento, quiser se isso impedi-lo de ser machucado novamente."
show bri surprised mine with dis
b "\"Acho que eu realmente te espanquei, hein? Hmm--\""
hide bri
show bri angry mine at center behind cam
with dissolve
show cam surprised mine at jumping
"Cameron se encolhe quando o urso agarra seu focinho dolorido em uma pata enorme."
c "\"Espera, por favor não--\""
show cam scared b mine at jumping
c "\"Agh!\""
"Cameron se encolhe com força, mas tenta o seu melhor para ficar parado."
show bri confused mine
with dis
b "\"É, quebrou seu dente também. Inchando um pouco, mas você tá mais bonito com seu rosto todo fodido assim. Pena que vai ficar bem feio até amanhã de manhã, não que vá importar.\""
dy "\"É difícil olhar para você agora, com essa cicatriz estúpida.\""
show cam sad b mine with dis
"Brian solta e pega seu ombro, ao mesmo tempo em que olha para a camisa de Cameron."
show bri smirk2 mine with dis
b "\"Você é de Bridgetown? Cidade madeireira? Ou você só pegou isso no brechó?\""
b "\"Eu sempre digo, quando você tá comprando no brechó, NUNCA pegue roupas que tenham algo a ver com um lugar. Porra, só alguns anos atrás, peguei um moletom da Weston no Exército da Salvação e--\""
show cam worried b mine with dis
"Cameron acompanha em silêncio."
"Enquanto isso, aquela terceira presença se transformou em algo mais, um pouco mais familiar."
"Brian está ficando tagarela novamente da segunda dose que tomou."
b "\"--Enfim, ouvi dizer que a cidade tá cheia de Antifa e tudo mais. Um verdadeiro inferno liberal se é que já existiu um.\""
"Sua mãe, seguindo atrás deles, está segurando sua pata."
"Olhando para trás, ele não consegue vê-la claramente, mas sabe que é ela."
show cam sad b mine with dis
c "\"É... está tudo bem. Muitas vezes são grupos de fora que vêm para a cidade causando problemas.\""
"Ele até soa como ela, defendendo a cidade onde ambos cresceram apesar de seus problemas, apesar de suas ruas se tornarem um palco para as guerras culturais do país se desenrolarem fisicamente."
"Mesmo enquanto sofriam nos arredores do que deveria ser um bastião liberal iluminado pelas luzes da tolerância e do bem-estar, mas em vez disso brilhando laranja de carros queimando e granadas de atordoamento."
"E ainda assim, eles a defendiam, porque ambos acreditavam em seus princípios fundamentais."
"Agora, porém..."
hide bri with dissolve
show cam worried b mine with dis
"Cameron olha para trás enquanto também olha {i}para trás{/i}."
"Ele é mais alto que ela, e é lembrado de como ela era pequena, como ela pareceria pequena para ele agora se tivesse sobrevivido."
"Ele a teria salvado também, se ela pudesse ter aguentado só um pouco mais..."
"Mas quanto mais?"
"Quatro, cinco anos? Ela poderia ter aguentado tanto tempo?"
"Não, não com seu vício e a quantidade que ela estava usando."
"E embora Cameron não queira admitir, foi sua morte que o levou a fazer a primeira mudança séria em sua vida."
"Sua mãe não era uma boa mãe."
"Considerando tudo, ela nunca deveria ter tido filhos."
"Mas como ele pode julgar?"
"Ela ainda era uma adolescente, animada e apaixonada, vivendo em uma van Chevy dos anos 70, mas tudo isso chegou ao fim quando ele nasceu em dezembro de 1995."
"No ano seguinte, seu pai abusivo, provavelmente esquizofrênico, foi embora e cometeu suícidio em algum momento em meados dos anos 2000."
"Mas, por alguns meses em 1995, seus pais realmente queriam fazer uma boa vida para ele, e aquele sentimento de amor daquele momento sobrecarrega Cameron."
show cam sad b mine with dis
"Eles queriam que ele fosse feliz, bem-sucedido, e eles realmente pensaram que ele seria aquele que quebraria o ciclo familiar de abandonar os estudos e ficar sem dinheiro."
"E mesmo que quisessem isso para ele, eles especialmente queriam que ele fosse feliz, tivesse uma vida familiar e uma infância que ambos os pais só foram capazes de ver outras crianças desfrutarem."
"Eles tentaram."
"Mas é a história de amor mais típica para pessoas como eles."
"Porque eventualmente, como em todas aquelas outras histórias, as coisas quebram, e então as coisas se acomodam."
"Ele fez exatamente o mesmo antes de Devon."
"Ela deveria ter tomado mais precauções."
"Ela o deixava sozinho no trailer frequentemente, seus medicamentos e drogas recreativas livremente disponíveis para ele experimentar enquanto ela estava no trabalho."
"Ele se tornou um viciado como ela, e ele veio a entender a bagagem que vem com esse rótulo, que não é apenas sobre um desejo, ou uma vontade por algo."
"Todo mundo tem esses sentimentos."
"Não, é sobre quem você é como pessoa: um mentiroso, um ladrão, um trapaceiro."
"Alguém disposto a fazer qualquer coisa para conseguir o que quer que seja que seu vício exija, qualquer coisa para se sentir bem."
"Seja pateticamente verificando todos os dispensadores de moedas em um cassino depois de gastar suas economias, ou pateticamente vasculhando o carpete por qualquer droga da qual você esteja começando a ficar sem."
"A única coisa que o salvou daquela vida, e da morte, foi a insistência de sua mãe em que ele mantivesse suas notas altas."
"Claro, Devon o salvou também, mas ele nunca teria conhecido o urso sem boas notas e uma pontuação decente no ACT."
"E apesar de ela ter perdido o contato com a vida em seu último ano, aquele hábito de disciplina acadêmica que ela havia incutido nele permaneceu."
"Foi isso que lhe rendeu uma bolsa de estudos parcial para a Universidade de Pueblo."
"E foi isso que o tirou dos parques de trailers ao redor de Bridgetown, e para a principal universidade do estado."
"Algumas escolas em seu próprio estado tinham ofertas melhores, mas Pueblo era a mais prestigiada das escolas para as quais foi aceito."
"{i}Uma das 100 melhores escolas com os melhores programas de enfermagem e engenharia da região!{/i}"
"Isso, e na época, Cameron queria estar longe de Bridgetown, mesmo que isso significasse o deserto."
"E então ele conheceu Devon."
show cam crying b mine with dis
"Ela não era uma boa mãe..."
"... Mas ela era uma ótima pessoa, uma pessoa maravilhosa, e ela fez o melhor que pôde com o que tinha na época."
"Ela o trouxe para uma vida caótica e instável, uma vida que ela salvou várias vezes, e enquanto ele ocasionalmente desejava que sua mãe tivesse apenas deixado ele morrer..."
"... Agora, Cameron está apenas agradecido."
"Enquanto a maior parte de sua vida foi difícil, os últimos cinco anos foram melhores do que ele ousaria sonhar que fosse possível."
"Sua vida era perfeita até ontem, quando chegaram aqui."
"Lágrimas escorrem por seu rosto, conflitado sobre como deveria se sentir, mas apenas sabendo que sente falta dela, que a ama, e que espera que ela esteja bem, onde quer que esteja."
"Essa terceira pessoa aperta sua pata tranquilizadoramente."
"Cameron aperta de volta, e é confortado pela sensação de que por este momento, ele está isolado de Brian e da cidade, e é apenas ele e sua mãe caminhando por essas minas."
"Ela diz a ele que está orgulhosa por ele ter se formado no ensino médio e na faculdade, e está feliz que ele encontrou Devon."
show cam sad b mine with dis
"Ela realmente ficaria orgulhosa dele se soubesse o que ele estudou?"
"Se ela ainda estivesse por perto..."
c "\"--Eu teria me formado em administração, ou algo assim.\""
show bri angry mine at left behind lamp with dissolve
b "\"No que você se formou?\""
show cam worried b mine with dis
"\"{i}Sorria{/i}.\""
"Uma voz gentil atrás dele, quase inaudível, e carregada na brisa suave que fica mais fraca quanto mais fundo eles vão nesses túneis."
show cam grinning b mine with dis
c "\"Ah, teoria musical.\""
show bri vaguestare mine with dis
b "\"E o que diabos você pode fazer com isso?\""
show cam smile b mine with dis
c "\"Ensinar.\""
"A resposta automática, aquela que ele havia preparado para todos os seus amigos céticos que estavam indo para áreas relacionadas a STEM."
b "\"Você é professor?\""
show cam smile b mine with dis
c "\"Não, mas esse era o meu plano.\""
show bri serious mine with dis
b "\"Algum plano.\""
show cam grinning b mine with dis
c "\"Quer dizer, eu não entrei em nenhuma dívida, então tive liberdade financeira depois que me formei.\""
show bri smirk mine with dis
b "\"Sabe, você é bem coerente pra alguém que tá naquela quantidade de cogumelos. A maioria das pessoas enlouqueceria.\""
show cam happy b mine with dis
c "\"Ah, eu estou, eu definitivamente estou, é... eu não sei. Tenho mais controle do que na primeira vez que experimentei.\""
"Na verdade, Cameron sente que está enlouquecendo agora, rindo mesmo que isso faça cada parte de seu corpo doer."
show bri serious mine with dis
b "\"Xanax é como mágica quando você está em pânico. Enfim, o que você faz pra viver, valeu a pena?\""
"Pelo tom na voz de Brian, ele já sabe a resposta para isso."
show cam confused b mine with dis
c "\"Hum... Atendimento ao cliente... Para Hulian.\""
show bri angry mine with dis
b "\"Triste, trabalhando para um país que bombardeamos duas vezes. Nos anos 80, costumávamos bater em pessoas por trabalhar para empresas como essa.\""
show cam confused b mine with dis
"Cameron fica sem palavras, mas apenas por um momento."
show cam smile b mine with dis
c "\"Ah... Ok.\""
"Hulian, a atual líder do mercado em fabricação de smartphones, é taiwanesa, e o coiote assume que o urso está pensando em um certo outro país na mesma região."
"De qualquer forma, é um comentário estranho e perturbador."
"Mas isso é apenas Brian, e às vezes com Brian, é melhor para Cameron apenas manter a boca fechada e continuar sorrindo."
show bri confused mine with dis
b "\"Então por que música? Você canta?\""
"Cameron deseja que o urso pare de fazer perguntas, puxando conversa como se isso fosse uma parte rotineira de suas vidas."
"Mas o coiote assume que sais de banho deixam qualquer um tagarela."
c "\"Ah, tipo--\""
b "\"O que você quer dizer com 'tipo'? Ou você canta, ou não.\""
show cam confused b mine with dis
c "\"Bem, sim, quero dizer, eu canto, mas não sou muito bom--\""
show bri evilgrin3 mine with dis
b "\"Quer dizer, você melhor ser se passou quatro anos aprendendo. Que tal você cantar, e eu decido.\""
"Está ficando mais difícil manter a farsa alegre enquanto Cameron sente a excitação cruel e maliciosa subindo dentro de Brian novamente."
"A segunda dose está fazendo mais do que apenas fazê-lo falar demais."
show cam grinning b mine with dis
c "\"Ah, claro, só preciso pensar em uma para cantar. Alguma que você queira ouvir? Eu conheço muito grunge dos anos 90 e rock alternativo.\""
show bri smirk mine with dis
b "\"Heh, você é um estereótipo ambulante, não é? Você escreve suas próprias músicas?\""
show cam smile b mine with dis
c "\"Eu definitivamente tentei.\""
"Um leve tremor de irritação percorre o ar."
show bri vaguestare mine with dis
b "\"Sabe, uma coisa que realmente me irrita é quando alguém age como um bundinha humilde demais. Ou você faz, ou não faz. Ou você é bom nisso, ou não é. Ou você oferece algo diferente, ou você não oferece.\""
show bri evilgrin2 mine with dis
b "\"Então qual porra é?\""
show cam happy b mine with dis
c "\"Eu faço! Eu posso! Ah, só me dá um segundo.\""
"Os cantos do focinho de Cameron se curvam levemente para baixo, sua compostura quase desmoronando."
"Ele está fazendo o melhor que pode nas circunstâncias atuais, mas precisa de ajuda."
"{i}Devon, onde você está?{/i}"
show bri smirk mine with dis
"A atitude de Brian muda de um extremo para o outro, fazendo Cameron sentir uma espécie de chicotada emocional, mas contanto que isso o impeça de ser atingido, ou mais importante, morto, ele está bem com isso."
hide bri
hide cam
with dissolve
"Tentativamente, Cameron começa a cantar, escolhendo a música que lhe deu mais atenção."
"Aquela que foi tocada em rotação moderada em faculdades do Mountain West, junto com algumas no Noroeste."
"Uma música sobre seu ex, Dylan, sobre seu amor e ódio mútuos, sobre o abuso que costumavam infligir um ao outro, físico e mental, e finalmente, sobre seu término."
"Sua voz está áspera e quebrada, e enquanto parte disso é porque ele não está aquecido, é principalmente por ter sua garganta esmagada."
"Desidratação, e gritar também não ajuda."
"Mas além de se assustar cada vez que Brian o puxa em uma direção diferente, Cameron encontra a melodia e o ritmo."
"Enquanto faz isso, ele se torna um pouco mais ousado, cantando mais alto até que sua voz ecoa pelos túneis."
"É muito estranho com seu focinho inchado e dente faltando."
"Brian ainda não diz nada, e Cameron percebe que ele está ouvindo atentamente."
"Enquanto isso deixa o coiote nervoso, ele sabe que é melhor do que o urso estar com raiva, e principalmente, ele só precisa continuar cantando."
"Devon está nas minas com eles, e ele precisa de direções."
"Cameron só deseja que não pareça que ele está levando Devon para seu próprio fim."
stop ambient fadeout 6.0
stop background fadeout 6.0
window hide
pause 0.5
scene black with medium_dissolve
pause 1.0
play ambient2 crickets fadein 5.0
pause 1.0
scene mines with medium_dissolve
pause 0.5
window show
"Encontrar a entrada não foi difícil."
"Enquanto a entrada principal havia sido bloqueada com vergalhões antes de ser preenchida e selada com concreto, ele sabia sobre a entrada lateral dos fóruns sobrenaturais que pesquisou antes de vir aqui."
"Isso, e o sangue de Cameron estava espalhado aqui e ali, e o cheiro dele o impulsionou."
"Claro, levou direto para aquela entrada."
"Ele começou a destravar as algemas no segundo em que pensou que Brian poderia estar fora de alcance auditivo."
"Ele tinha se atrapalhado com a chave minúscula e escorregadia, antes de libertar seus pulsos, revelando pele quebrada com pelos embolados e cobertos de sangue."
stop ambient2 fadeout 5.0
"Agora, Devon se move pelas minas em completa escuridão."
window hide
pause 0.5
play ambient mines01 fadein 6.0 volume 0.5
scene bg black with medium_dissolve
pause 0.5
window show
"É quase sufocante, quase induzindo ao pânico, mas o cheiro de Cameron misturado com o odor fétido de Brian empurra o urso mais jovem mais fundo nos túneis."
show dev angry s dark5 with dissolve
"O ar parece tenso, como se a mina em si estivesse determinada a ver o que acontece a seguir."
"Ele não vai cair em outro abismo."
"Quando Lupita morreu, tinha sido um acidente, um que aconteceu depois que um tornado destruiu sua cidade, nivelando o quarteirão do outro lado da rua, mas deixando sua casa praticamente intacta."
"Como um garoto de 12 anos, ele simplesmente não pensou que isso poderia acontecer."
"Eles haviam sobrevivido ao desastre real, mas assim que o alívio começou a surgir, e sua guarda começou a baixar, aconteceu."
"Ele se sentiu impotente naquela situação, e sabia que sua morte tinha acontecido por causa dele."
"Mas desta vez é diferente."
"Ele não podia lutar contra o que levou Lupita, mas pode lutar contra o que está levando Cameron."
show dev worried s dark5 with dis
d "\"Droga...\""
"Depois de cerca de dez minutos, porém, Devon começa a ficar mais agitado, incapaz de ouvi-los mais, e pelo cheiro, Devon pode dizer que perdeu o rastro."
show dev frustrated s dark5 with dis
d "\"Merda... Merda, merda, merda!\""
"Ele assobia pelos dentes, tentando ficar quieto caso Brian esteja de alguma forma por perto, à espreita."
"E então, de alguma forma, ele ouve a voz cantando de Cameron."
show dev shocked dark5 with dis
"Devon fica completamente imóvel."
"Ele reconheceria a voz de seu namorado em qualquer lugar, é claro, mas o estilo de Cameron é diferente, tendo as qualidades de um cantor dos anos 50 enquanto retém uma aspereza semelhante ao grunge."
"O coiote foi fortemente influenciado pelos musicais em preto e branco que sua mãe costumava assistir tarde da noite."
"Ele ficou envergonhado disso depois de ser criticado em uma de suas aulas de performance vocal, e estava tentando mudar sua técnica quando Devon o conheceu."
"Mas Devon sempre gostou da voz de Cameron, e foi devido ao incentivo de Devon que Cameron se inclinou para seu estilo."
"Ele conhece a música também, aquela sobre o ex de Cameron, aquela que ele não gosta de ouvir porque é violenta e cruel."
"Ele nunca perguntou a Cameron sobre isso porque assumiu que o coiote traria isso em seu próprio tempo."
"Agora, ele precisa ter certeza de que terá essa chance."
show dev angry s dark5 with dis
"Devon começa a se mover o mais rápido que pode enquanto fica quieto."
"Ele bate o nariz em algumas paredes, e raspa os cotovelos e ombros, mas continua se movendo, simplesmente tentando forçar seu caminho na direção da voz."
"Então, assim que ele acha que está a algumas curvas de distância, ela para."
"Então Cameron grita, e Devon desiste de todas as tentativas de furtividade."
show dev angry yelling s dark5 at jumping
d "\"Cam!{w=0.3} BRIAN!\""
"Ele chama para deixar Brian saber que ele está lá, pelo menos para distraí-lo do coiote."
"Então ele avança pela escuridão, tentando encontrar o que tem certeza que é a última curva."
"Por que Brian trouxe Cameron aqui, ele não sabe."
"Ele nem sabe o que vai fazer quando os encontrar."
stop ambient fadeout 6.0
"Bem, qualquer coisa."
"Ele fará qualquer coisa."
window hide
pause 0.5
play background droneandvoice fadein 15.0
scene black with medium_dissolve
scene mine_blur:
    zoom 1.02
    truecenter
show lamp:
    zoom 1.02
    truecenter
show bri vaguestare mine behind lamp at left
show cam surprised b mine behind lamp at right
with medium_dissolve
window show
"Brian parece um pouco mais distraído, começando a escanear a parede do túnel antes que seus olhos se fixem no que parece ser uma grande rachadura do teto ao chão."
show cam happy b mine with dis
"Cameron aumenta um pouco seu canto, sabendo que este é seu destino, o fim da estrada."
show bri confused mine with dis
"O velho urso olha para ele, parecendo irritado."
"Isso, por algum motivo, é o que tira Brian de seu hiperfoco induzido por estimulantes."
show bri horror mine
show cam shocked b mine with dis
with dis
stop background fadeout 15.0
"Brian finalmente percebe o que está acontecendo."
"Só agora o velho urso se lembra do plano de Cameron de pegar a chave."
"Até Cameron havia esquecido."
"Mas agora, uma pata enorme voa para seu bolso, cavando dentro e percebendo que é tarde demais antes de girar em Cameron."
play music drowning fadein 3.0
show bri rage mine with dis
b "\"Ah, seu viadinho!\""
show cam scared at jumping
hide bri
hide cam
with dissolve
"Cameron se vira e corre, tentando aproveitar Brian soltando-o por aqueles poucos segundos."
hide lamp
play sound punch
scene mine_blur red:
    zoom 1.02
    truecenter
show lamp red:
    alpha 0.7
    zoom 1.02
    truecenter

show redarch_05 behind lamp:
    alpha 0.4
    yoffset 500
    zoom 1.05
show redarch_04 behind lamp:
    alpha 0.4
    yoffset 500
    zoom 0.85
show redarch_03 behind lamp:
    alpha 0.4
    yoffset 500
    zoom 0.62
show redarch_02 behind lamp:
    alpha 0.4
    yoffset 500
    zoom 0.4
show redarch_01 behind lamp:
    alpha 0.4
    yoffset 500
    zoom 0.2

show redarch_05 as extra1 behind lamp at drugtriparch01:
    yoffset 500
    zoom 1.05
show redarch_04 as extra2 behind lamp at drugtriparch02:
    yoffset 500
    zoom 0.85
show redarch_03 as extra3 behind lamp at drugtriparch03:
    yoffset 500
    zoom 0.62
show redarch_02 as extra4 behind lamp at drugtriparch04:
    yoffset 500
    zoom 0.4
show redarch_01 as extra5 behind lamp at drugtriparch05:
    yoffset 500
    zoom 0.2
show bg black:
    zoom 1.3
    truecenter
"Algo bate nas costas de Cameron, logo à direita, e parece uma bola de canhão sendo esmagada através de seu corpo." with hpunch
"Cameron é lançado para frente contra a parede do túnel diretamente à sua frente, e ele tenta se segurar nela, escorregando levemente enquanto olha para cima na escuridão."
window hide
pause 0.5
hide bg black with medium_dissolve
pause 2.0
window show
"É tão escuro que Cameron não consegue dizer se o teto está a alguns metros acima dele, ou se é simplesmente um espaço sem fim cheio de arcos brilhantes que se estendem para sempre."
"Seus olhos ficam arregalados, sua respiração vazando de seu focinho em um suspiro lento e agudo, não querendo acreditar que a dor que sente se espalhando por suas entranhas é real."
"Então, ele está no chão, se contorcendo e gemendo incontrolavelmente enquanto dores elétricas se espalham como teias de aranha por seu corpo."
"Os golpes que Brian havia desferido antes não são nada comparados a isso."
"Cameron se debate no chão, desesperado para encontrar uma saída do inferno."
"Ele está no inferno."
"{i}Quem está no inferno?{/i}"
"Ele tem que estar."
"O que são esses arcos vermelhos, e por que chamas estão se espalhando de suas entranhas para seus pulmões?"
show bri lookdown red at left behind lamp
with dissolve
window show
b "\"Droga. Você provavelmente só vai urinar sangue depois dessa.\""
"A voz falsamente preocupada de Brian tira Cameron de volta à situação em que está, e no fundo de sua mente, ele percebe que sua viagem está começando a descer."
"A dor ainda está presente, porém, e não está diminuindo."
"Como ele pode sentir dor se ele não é nada?"
"Ele está finalmente respirando novamente, mas cada expiração é acompanhada por um gemido ofegante, lágrimas involuntárias rolando por seu rosto."
"Brian se inclina sobre ele e o coiote se encolhe."
c "\"Não,{w=0.3} pare!{w=0.3} Por favor!\""
show bri neutral red with dis
"Brian pausa, então apenas agarra Cameron pelo braço e o puxa para cima."
hide bri with dissolve
"Cameron solta um grito rouco e sem fôlego enquanto seu corpo dolorido é forçado a se mover novamente."
"Ecoa ao redor deles antes de ser interrompido quando um braço enorme aperta a garganta de Cameron."
d "\"Cam!{w=0.3} BRIAN!\" with vpunch
"A voz de Devon está muito perto, talvez apenas um túnel ou dois de distância."
"Brian murmura baixinho ao ouvido de Cameron."
b "\"Cala a porra da boca agora, ou eu oblitero seu outro rim, entendeu?\""
"Cameron sente a ameaça pairando sobre o lado esquerdo de suas costas desta vez, e ele rapidamente fecha o focinho, mesmo que gemidos ainda forcem sua saída, abafados atrás de seus lábios."
"Isso parece pelo menos satisfazer Brian, e ele solta o enforcamento antes de empurrar Cameron para frente."
"A princípio, Cameron fica surpreso que o urso não o tenha atingido novamente de qualquer maneira, mas Brian está distraído novamente."
"Devon está muito perto, e alguns planos terríveis passam pela cabeça do urso mais velho que fazem o abdômen já dolorido de Cameron se contorcer com náusea e medo."
"Brian considera esperar e emboscar Dev, mas rapidamente descarta a ideia ao perceber que Cameron pode tentar avisar Devon fazendo barulho assim que ele os alcançar."
"É exatamente o que Cameron faria, mesmo que isso significasse ser espancado até a morte por Brian."
"Decidindo novamente que nada importa mais, ele empurra Cameron para frente através da abertura estreita, a passagem ficando mais apertada até que Brian tem que se virar de lado e lutar para passar, e então se abre."
window hide
pause 0.5
scene black with leftwipe
pause 0.5
scene bg hollow_visions with leftwipe:
    zoom 1.02
    truecenter
pause 0.5
window show
"Cameron sente o cheiro da morte."
"Ele instintivamente recua, direto para Brian."
show cam terror b red with dissolve
c "\"Não.{cps=3}..{/cps}{w=0.4} Não...{w=0.3} Não,{w=0.2} não,{w=0.2} não,{w=0.2} por favor não faça isso!\""
c "\"Eu não posso...{w=0.3} Eu não posso--\""
"Ele não consegue terminar sua frase."
"As vítimas de Brian sentiram dores que ainda parecem inimagináveis para o coiote."
hide cam with dissolve
"Sabendo que Devon está logo atrás deles, Cameron faz um último esforço para se virar e desviar de Brian, mas o urso é grande demais, e ele facilmente agarra o coiote e o joga mais para dentro da cavidade."
play sound thud
"Cameron se levanta imediatamente, tentando suprimir seus gemidos e choramingos." with hpunch
show cam shocked b red at twelve,jumping
c "\"Brian, só espera um segundo. Pensa nisso. Eu posso {i}ajudar{/i} você. Por que você me trouxe aqui em primeiro lugar?\""
show bri neutral red at left with dissolve
"Brian dá a Cameron um olhar impassível, mas ele pausa, e isso dá ao coiote alguma esperança."
"E algum tempo."
show cam scared b red with dis
c "\"Deixa eu falar com eles. Deixa eu ver se posso argumentar com eles. Nós dois sabemos que isso, tudo isso, acabou.\""
show bri vaguestare red with dis
"Cameron sente uma ligeira mudança nas intenções de Brian enquanto o urso começa a considerar seriamente o raciocínio de Cameron."
show cam horror b red with dis
c "\"Eu sei que você precisa da minha ajuda. Eu posso senti-los. Eles querem você, Brian, e estão esperando por você!\""
show cam worried b red with dis
show bri confused red with dis
c "\"Eu sei como pode ser, andando em círculos pela maior parte da sua vida, cometendo os mesmos erros estúpidos e sabendo o que você precisa fazer para melhorar, e simplesmente nunca fazendo.\""
show cam worried b red with dis
show bri smirk red with dis
c "\"Mas eu finalmente fiz, e minha vida estava quase perfeita.\""
"{i}Até te conhecer{/i}."
show cam surprised b red with dis
c "\"Então vamos fazer isso. Vamos acabar com esse pesadelo agora mesmo.\""
show bri closedeyes red with dis
"Brian respira fundo e segura."
"Toda a mina, toda a cidade, parece segurar a respiração com ele, e Cameron começa a entender o quão profundamente entrelaçado este urso está com este lugar, esta entidade que parece puxar todas as cordas."
"Cameron pode sentir a entidade monolítica se mover e girar, como se também sentisse um fim inevitável."
"Brian está perto de aceitar a oferta do coiote."
"Mas não está destinado a ser, e Cameron, é claro, sabe disso."
"Um barulho vindo da entrada anuncia a chegada de Devon."
show bri angry fists red with dis
b "\"Acho que ele finalmente chegou, hein? Que bom que trouxe minha espingarda calibre 10. Sempre quer ter certeza que tem bom poder de fogo quando ursos estão envolvidos, né?\""
hide bri with dis
play sound pumpback
show cam scared b red with dis
"Cameron observa horrorizado enquanto o velho urso abre a espingarda antes de inserir um cartucho."
play sound pumpforward
hide cam
hide bri
with dis
"A mente de Cameron está em branco enquanto ele automaticamente avança sobre o urso enorme, agarrando o cano da espingarda enquanto Brian rosna de raiva."
"\"{i}Tudo está desmoronando. Você está em espiral.\""
window hide
pause 0.5
scene bg black with leftwipe
window show
"Devon enfia seu volume através da passagem estreita, se espremendo para a cavidade do outro lado."
window hide
scene bg hollow:
    zoom 1.02
    truecenter
show dev angry s mines at left
with leftwipe
pause 0.5
window show
"Quando ele tropeça no espaço aberto, Devon avista Cameron imediatamente, o coiote sendo balançado para lá e para cá enquanto luta com Brian pela espingarda."
stop music fadeout music fadeout 10.0
"Cameron está coberto de sangue, lágrimas embolando os pelos em suas bochechas."
"A situação já é terrível, mas novamente, seu medo por Cameron se transforma em raiva de Brian ao ver o urso desferindo chutes cruéis e esmagadores na parte inferior do corpo do coiote."
"Devon percebe que é isso, e ele não tem tempo para pensar."
play music terrorbelowthesurface
hide dev with dis
show bg hollow at zooming6 as extra
"Devon avança por trás do urso mais velho e morde profundamente o lado do pescoço de Brian."
"Aparentemente, morder alguém além de si mesmo é muito mais eficaz, e ele sente seus caninos afundarem profundamente na carne sob a pele grossa."
"O velho está coberto por uma camada de proteção, assim como ele mesmo, mas o urso mais velho claramente tem muito mais."
"Ainda assim, Brian grita, agudo e cheio de fúria."
"Então, Cameron é finalmente sacudido da espingarda, e Brian agarra o cano com ambas as patas antes de bater com a coronha da espingarda no estômago de Devon."
play sound thud2
"O urso mais jovem engasga e se dobra, mas consegue agarrar a espingarda, segurando firmemente o estoque." with vpunch
"Brian, claramente ciente de quão ruim a situação pode se tornar para ele, solta a espingarda para que possa jogar um cotovelo no rosto de Devon, batendo no lado esquerdo de seu focinho e rosto."
"Isso o atordoa e dá ao urso maior tempo para jogar um joelho para cima na forma curvada de Devon, uma polegada acima do umbigo, quase exatamente o local que ele havia atingido antes."
play sound punch
"Devon sente como se suas entranhas fossem achatadas contra sua coluna antes de se liquefazerem, a força realmente o levantando do chão por meio segundo." with hpunch
"Mesmo que ele pouse em seus pés, ele imediatamente afunda em seus joelhos, seu focinho aberto enquanto continua uma batalha com seus próprios pulmões, tudo enquanto ainda tenta segurar a espingarda."
show bri rage mines with dissolve
b "\"Você é um homem morto andando, garoto! Bem, de joelhos, de qualquer maneira. Que surpresa!\""
"Brian procura tremulamente o estoque da espingarda, escondido em algum lugar sob o volume de Devon enquanto simultaneamente tenta evitar a ponta do cano, caso Devon consiga encontrar o gatilho."
"O ataque foi suficiente para abalar Brian, mesmo que tenha sido breve."
"Devon amaldiçoa a si mesmo, tentando se mover, sabendo que provavelmente não pode vencer, mas ele precisa fazer algo, talvez machucar Brian tanto que Cameron possa pelo menos fugir."
"{i}Levanta!{/i}"
"Mas ele não consegue respirar, então não há muito que ele possa fazer para se defender, muito menos se levantar."
"Então, Devon mantém seu aperto na espingarda mesmo quando Brian começa a tentar arrancá-la de seu aperto enfraquecido, e ele está começando a conseguir."
d "\"Cam... corre...\""
"Devon rouqueja, nem mesmo tendo certeza de onde Cameron está agora, assumindo que ele ainda pode estar no chão depois de ser chutado tantas vezes."
play sound thud
show bri horror mines at jumping
"Brian guincha."
"Olhando para cima de sua posição dobrada, Devon vê Brian na sua frente, também dobrado, o urso velho agarrando entre as pernas."
hide bri
with dissolve
show cam shocked b mines with dis
"Enquanto Brian afunda mais, Cameron aparece, abaixando um pé."
show cam happy b mines with dis
"O coiote sorri com alívio e alegria ao ver Devon, e vendo que ele pegou a espingarda."
"Cameron parece tão certo de que eles venceram que ele não vê a rápida recuperação de Brian, o urso velho forçando-se para cima, vingança assassina em seus olhos enquanto corre em direção a Cameron com outro grito animal."
show bri rage mines at left,jumping
show cam scared b mines at jumping
"Devon só pode assistir enquanto o urso enorme avança sobre Cameron."
c "\"Não!\""
"O coiote muito menor só pode gritar em pânico antes que Brian esmague-o contra a parede."
hide cam
hide bri
play sound punch2
show blood06:
    zoom 1.02
    truecenter
"Devon ouve um som de esmagamento assim que consegue seu primeiro pequeno gole de ar, assim que ouve o próprio ar de Cameron sair em um gemido quase uivante." with hpunch
"E então, ainda mais cruelmente do que Devon havia atacado Brian, o urso velho começa a atacar Cameron."
window hide
play sound punch
show blood07 with vpunch:
    zoom 1.02
    truecenter
pause 0.5
play sound punch3
show blood08 with vpunch:
    zoom 1.02
    truecenter
window show
"Brian o bate para lá e para cá com golpes direcionados ao rosto do coiote antes que Cameron desabe."
"Lá, Brian começa a rasgar e arranhar o coiote com suas garras."
"Devon começa a se mover, mas é lento, e ele só deseja que seus pulmões comecem a funcionar."
"Cameron tenta rastejar para longe de Brian, e Devon vê o horror refletido nos olhos de seu namorado."
play sound bite
show blood03:
    zoom 1.02
    truecenter
"Então Brian desce sobre ele novamente, e Cameron joga seu cotovelo esquerdo de volta no rosto do urso, apenas para Brian afundar seus dentes no antebraço e cotovelo de Cameron." with hpunch
"Cameron solta um guincho e se enrola ao redor do focinho de Brian, arranhando e mordendo com suas garras e dentes."
"Mas então, Brian torce e rasga, e Cameron solta um som uivante, seu corpo se contorcendo violentamente."
show blood03_2 with dis2:
    zoom 1.02
    truecenter
"Ele está de costas agora, e fica quieto, encarando em choque a parede em que está deitado perpendicularmente, seus olhos começando a revirar enquanto Brian sacode a cabeça e um esmagamento vem do braço de Cameron."
"O coiote não consegue fazer nenhum som agora, o ar aparentemente tirado dele pela dor."
"Devon nunca ouviu Cameron fazer aqueles sons de dor selvagem, não assim."
"A espingarda havia se aberto em algum momento durante a luta, e Devon deixa cair a arma estranha, muito intencionado em salvar Cameron para descobrir agora."
"E vê-lo em tanta agonia que ele não consegue respirar, nem mesmo vocalizar mais, dá a Devon o empurrão final que ele precisa."
play sound punch
hide blood06
hide blood07
hide blood08
hide blood03
hide blood03_2
hide black
"Ele avança sobre Brian e a força derruba o urso velho do coiote." with hpunch
"Devon nunca seriamente atacou alguém em toda a sua vida."
"Mas é algo que vem naturalmente para ele e Brian, e enquanto ele havia atacado brincando pessoas no passado, incluindo Cameron, esta é a primeira vez que ele traz suas garras, dentes e músculos para uso total."
"Montando o urso mais velho, Devon ruge para Brian antes de mergulhar."
"Primeiro, ele morde o pescoço de Brian novamente, mas desta vez pela frente enquanto suas patas rasgam e arranham o couro do urso maior."
"Brian parece se concentrar por um segundo antes de enterrar seu punho no estômago de Devon com um baque profundo e abafado."
"Mas o urso mais jovem está tensionado desta vez, e o punho não vai além de seus músculos estomacais."
"Ainda assim, o poder de Brian é quase sobrenatural, e Devon se inclina para frente e grunhe, uma dor se formando no fundo de sua barriga, mas isso só o faz morder com mais força."
"Devon pode sentir que ele realmente atordou o urso velho, pelo menos por agora, e enquanto Brian leva seu punho de volta, ele recorre a empurrões em pânico em vez de realmente tentar lutar."
"Quando Brian finalmente tenta arranhar o rosto e os olhos de Devon, o urso mais jovem se inclina para trás e esmaga sua cabeça no focinho de Brian."
play sound thud8
show blood06:
    zoom 1.02
    truecenter
"O som que faz indica um focinho quebrado, e Brian solta outro gemido agudo antes de gritar e tentar avançar para morder o pescoço de Devon." with vpunch
"Devon se inclina para trás, apenas evitando os dentes antes de esmagar sua cabeça uma segunda vez no rosto de Brian."
play sound punch2
show blood02:
    zoom 1.02
    truecenter
"Então, enquanto Brian fica atordoado, Devon ataca seu focinho três vezes, com toda a força, tentando infligir cada pedaço de agonia em Brian que o urso velho havia dado a todos eles." with hpunch
"Isso seria impossível, porém."
"Ainda assim, Devon sente uma satisfação selvagem ao ver pelo menos dois dos dentes amarelos do urso velho rolarem para fora de seu focinho."
"Brian uiva e rola violentamente, finalmente desalojando o urso ligeiramente menor."
stop music fadeout 15.0
"Devon arqueja por ar, observando enquanto Brian surge a alguns metros de distância, agachado e também arquejando por ar."
b "\"Você vai... Você!\""
"Brian mal consegue formar palavras, mas não apenas porque está sem fôlego."
window hide
play ambient mines03 fadein 6.0
play ambient2 wind2
scene black with fast_dissolve
window show
"Seu ódio amargo é evidente, tão bravo que apenas saliva espumosa voa de seus lábios enquanto ele cospe."
"Mas então os olhos de Brian piscam para a direita, e Devon lembra de uma vez que ele deixou a arma lá, tendo se concentrado em ajudar Cameron."
"O urso velho se move novamente rápido como um raio, e ele dispara para a direita, e Devon percebe que Cameron está lá também."
d "\"Cameron, cuidado!\""
scene bg hollow_visions with dis2
play music solderingloop fadein 15.0 volume 0.3
"Cameron, deitado em agonia após o ataque brutal de Brian, sabe que algo está profundamente errado com seu corpo."
"O esmagamento contra a parede da câmara havia feito isso."
"A verdadeira dor, porém, emana de seu braço esquerdo, e Cameron sabe que está mutilado, quebrado e inútil."
"Mas ele ainda pode usar as pernas, e Cameron se força a se levantar e começar a se mover para a espingarda, ouvindo os rosnados e grunhidos dos ursos atrás dele."
"Ele faz o seu melhor para ficar quieto, mas grunhidos abafados e pequenos guinchos forçam sua saída de sua garganta."
"Assim que ele toca a espingarda, porém, ele ouve Devon gritar."
d "\"Cameron, o--\"" 
scene blood04 with dis2
"E novamente, o pesadelo que é Brian está rasgando seu corpo, prendendo-o contra a parede, e Cameron grita de terror enquanto o urso enorme começa a tentar morder seu pescoço."
"O coiote em pânico só consegue levantar o braço não quebrado."
"É talvez apenas três segundos antes que Devon esteja lá, mas parece uma eternidade, Cameron considerando o quão ruim pode ser morrer por ter sua garganta rasgada."
"O braço direito de Cameron também está rasgado, mas como Brian não está sacudindo a cabeça desta vez, seus ossos pelo menos permanecem intactos."
play sound thud
scene bg hollow_visions:
    zoom 1.02
    truecenter
"Então, Devon arranca o urso maior dele." with vpunch
"Cameron tenta se levantar, rastejar, mas é inútil, seu corpo muito espancado e quebrado para fazer qualquer coisa além de se arrastar para longe."
"Então ele ouve o guincho alto de Brian novamente, e desta vez, é genuinamente aterrorizado."
"Cameron olha e vê o urso velho agora de costas com seu braço em uma espécie de chave por Devon."
"Devon está deitado de costas, o braço de Brian puxado em direção a seu peito, os quadris de Devon perto do ombro do urso mais velho enquanto suas pernas se travam juntas nos tornozelos."
"Devon grunhe e se esforça com toda a sua força, seu corpo enorme e poderoso arqueando em direção ao teto."
"Devon está determinado a realmente machucar Brian desta vez, querendo ter certeza de que ele paga o urso velho de volta pelo dente e braço de Cameron."
"Então, com a parte do dente vingada, Devon se concentra em destruir o braço do outro urso."
window hide
scene black with fast_dissolve
window show
"Ossos de urso são especialmente difíceis de quebrar."
"Devon nunca quebrou um osso em sua vida."
"Mas o urso mais jovem sabe uma coisa ou duas sobre aplicar força."
"Seu pai assistia MMA o tempo todo, e enquanto ele sabe pouco sobre luta, ele sabe por que chaves de braço podem ser tão devastadoras."
"Mas mesmo enquanto ele se inclina para trás, dobrando o braço do urso maior sobre sua coxa interna, apenas alguns estalos são ouvidos, mas nada sério."
"Devon precisa que o braço tenha menos resistência, e mais distância do fulcro."
"Destravando as pernas, ele leva apenas um segundo para chutar o focinho do urso velho."
play sound thud8
"Por apenas um segundo, Brian fica mole, e Devon trava seus tornozelos novamente antes de levantar o braço mole para longe de seu peito, e se enrolar."
"Então, ele puxa o braço novamente, arqueando com força enquanto torce seu corpo."
d "\"Torque!\""
"\"{i}Agora você está pensando como um engenheiro!{/i}\""
window hide
play sound crack
play sound2 punch2 volume 0.6
scene bg hollow:
    zoom 1.02
    truecenter
show blood05:
    zoom 1.02
    truecenter
with vpunch
pause 0.3
hide blood05 with dis2
pause 0.5
window show
"Enquanto o bordão de um dos antigos professores de Devon vem à mente, um estalo divide o ar, e os gritos de Brian de alguma forma alcançam um novo tom, em pânico."
"Devon olha para o lado e vê que Cameron se arrastou alguns metros de distância, deixando um rastro escuro, horrível e sangrento atrás dele."
"Há muito sangue, e Devon entra em pânico, pensando que o coiote está sangrando até a morte pelo pescoço."
"Devon tropeça até ele, pairando suas patas sobre a cabeça do coiote."
d "\"Querido, seu pescoço! Deixa eu ver!\""
c "\"Ele-- Ele não me pegou. Vamos!\""
"Cameron não está em condições de correr, então ele geme quando Devon o levanta em seus braços, o urso começando a tropeçar em direção à saída."
"Devon olha para baixo para o coiote em seus braços, apenas agora vendo como são terríveis os ferimentos de Cameron."
"E então ele olha para trás, chocado ao ver Brian em pé."
"Como o urso velho conseguiu se levantar sem fazer barulho está além de Devon."
play sound thud
d "\"UNGH!\"" with hpunch
"A coronha da espingarda, impulsionada pelo corpo enorme do urso velho, bate em seu lado, espalhando uma dor doentia em ondas através de seu corpo."
scene bg hollow_visions with dis2:
    zoom 1.02
    truecenter
stop music fadeout 6.0
"Cameron ouve o baque surdo seguido pela vibração através do corpo grosso de Devon."
"Ele sente o urso se encolher enquanto afunda em seus joelhos, curvado sobre Cameron."
window hide
pause 0.5
scene black with medium_dissolve
scene circles with medium_dissolve
pause 0.5
window show
"O urso enorme levanta a espingarda que conseguiu segurar."
"Ele luta para segurá-la apenas com a pata esquerda, e seu braço direito ferido pende antes que ele praticamente o balance para apoiar o cotovelo direito contra a parede, alguns estalos vindo de seu ombro enquanto ele faz isso."
"Ele grita novamente quando isso acontece, mas com seu pulso totalmente funcional, ele agora pode mirar com firmeza, e com o quão estreita a cavidade é, não há para onde ir."
play sound pumpback
b "\"Não.{cps=3}..{/cps}{w=0.4} Não se mexam.{w=0.3} Entenderam?\""
b "\"Acabou. Eu vou matar esse coiote na sua frente, e depois vou arrancar seu braço, garoto!\""
"A expressão de Brian é uma mistura estranha de empolgação e nojo."
b "\"Pena que você não é nem metade tão bonitinho quanto o filhote.\""
window hide
pause 0.5
scene the_divide with medium_dissolve
pause 0.5
window show
"Devon só consegue arfar em resposta, e Cameron se agarra a ele com força enquanto é embalado em seus braços."
b "\"Deus, você arruinou tudo! Ele estava perfeitamente bem até você aparecer. Agora ele tá tão fodido que nem dá mais pra foder!\""
"Cameron começa a tremer e se contorcer, e Devon o segura mais firmemente."
b "\"Deus, você arruinou tudo! Ele estava perfeitamente bem até você aparecer. Agora ele tá tão fodido que nem dá mais pra foder!\""
"A habilidade de Cameron de ver e sentir as coisas está desaparecendo, assim como os efeitos dos cogumelos estão desaparecendo."
"Ainda assim, há apenas um pouco sobrando, e Cameron tenta o seu melhor para usá-lo."
"O corpo de Devon começa a tremer, e Cameron se agarra a ele mais firmemente."
"A voz de Devon, ainda sem fôlego, sussurra no ouvido de Cameron."
d "\"Querido, o que quer que aconteça, apenas finja estar morto, ok? Não importa o quê.\""
scene the_divide2 with dis2
"Mas Cameron de repente se vira--"
window hide None
stop ambient
stop ambient2
play sound shotgun
scene white
pause 0.5
scene bg black with dissolve
pause 2.0
window show
"Devon assiste enquanto o rosto de Cameron se torna um buquê de fitas vermelhas, e o urso tropeça quando o tiro atinge seu braço também."
"O corpo de Cameron se contorce violentamente em seus braços antes de ficar incrivelmente imóvel."
"Devon rapidamente olha para baixo para ver Cameron sem rosto."
window hide
play ambient2 wind2
show blood01 with medium_dissolve
window show
"Tudo que costumava compor seu rosto está espalhado contra as paredes, e ainda escorre de..."
"Cameron se foi."
"Em choque, Devon olha para seu braço e vê os fragmentos brancos de ossos, a princípio pensando que são os seus, mas então ele vê alguns dos dentes afiados de Cameron também embutidos em seu braço."
"Devon se inclina sobre o corpo de Cameron, uma expressão de angústia indescritível em seu rosto enquanto ele começa a soltar um gemido baixo e terrível que aumenta em tom para um uivo ursino--"
window hide
stop ambient2 fadeout 2.0
pause 2.0
play sound reverse fadein 2.0
pause 1.6
scene the_divide2 with dis
play ambient mines03 fadein 2.0
play ambient2 wind2
"Depois de olhar {i}para frente{/i}, Cameron faz a única coisa que consegue pensar."
scene the_divide3 with dis
d "\"Não!\""
"Cameron agarra o cano e empurra para cima."
window hide None
stop ambient
stop ambient2
play sound shotandring
scene white
pause 0.5
scene bg black with dissolve
window show
"O som é tão alto que instantaneamente ensurdece Cameron, e embora o zumbido comece a diminuir, a audição em seu ouvido direito não volta."
d "\"Cameron!{w=0.3} Cameron?\""
c "\"Estou bem! Estou bem.\""
"Cameron olha para onde Brian está, o recuo da espingarda calibre 10 o atingiu com força, diretamente no peito."
"Cameron quase consegue visualizar o choque enviado através daquele coração velho e desgastado, já exausto do estimulante e da luta."
play ambient2 wind2
"O urso velho, ainda em pés instáveis, tropeça um pouco mais antes de bater na parede e deslizar para baixo para sentar."
window hide
scene mines_alt with medium_dissolve:
    zoom 1.02
    truecenter
pause 0.5
window show
play music submergedintro fadein 10.0 volume 0.3
queue music submergedloop volume 0.3
play sound heartattack01 fadein 3.0
queue sound heartattack02 loop
"Brian fica sentado encostado nela, parecendo confuso."
"Ele agarra seu peito, esfregando e fazendo caretas."
"A espingarda está no chão, fora do alcance de Brian, e o urso velho não faz nenhum movimento para pegá-la."
b "\"Porra...\""
"Ele começa a tentar se levantar, mas cai de volta."
b "\"Ah porra.{cps=3}..{/cps}{w=0.4} Ah porra...\""
"Brian agarra seu peito e estômago e geme."
b "\"Ah não, foi isso?{w=0.3} É isso?{w=0.3} Que porra?\""
b "\"Que porra...\""
b "\"Que...\""
play sound2 thud
"Brian cai de volta, seu corpo convulsionando, então ele se debate, como se estivesse tentando escapar de algo." with vpunch
scene bg black:
    zoom 1.02
    truecenter
play sound lantern
play sound2 shatter01
"Ele derruba e esmaga a lanterna elétrica, esmagando-a sob seu peso." with vpunch
stop music fadeout 10.0
play ambient mines03 fadein 10.0 volume 0.4
"Por vários segundos, ambos ouvem os gemidos, arfos e bufadas de Brian antes que fique em silêncio."
"Fica quieto por mais um tempo, Cameron e Devon não ousando se mover."
"Brian parecia invencível por tanto tempo, Cameron não consegue acreditar que pode ter acabado."
"Devon sussurra no ouvido de Cameron."
d "\"Cameron? Como você está se sentindo?\""
"Cameron dá a Devon um olhar que é uma mistura de amor e exasperação, mesmo que Devon não possa ver agora."
"Ambos sabem que ele está muito ferido."
c "\"Eu acho que algo se rompeu. Parece tudo errado.\""
"Cameron coloca sua pata direita em seu próprio torso, fazendo caretas."
d "\"Não se mexa, ok? Eu vou nos tirar daqui. Vou nos tirar daqui em nenhum momento.\""
play sound2 gravel_echo volume 0.5
stop ambient2 fadeout 7.0
stop ambient fadeout 7.0
"Devon começa a cautelosamente seguir em frente, e assim que Cameron percebe quanto tempo isso pode realmente levar, possivelmente muito tempo se houver sangramento interno, sua visão pisca."
window hide
pause 0.5
scene hollow_arch_0 with slow_dissolve2
pause 1.0
play music2 neuroprotection volume 0
play music neuroprotectionintro volume 0.3
queue music neuroprotectionloop volume 0.3
scene bg hollow_arch with slow_dissolve2
show bg hollow_arch_anim
pause 1.0
window show
"Cameron olha para ele, então olha para Devon, fazendo caretas com o rosto ensanguentado e machucado do urso."
"Mas Devon não reage à luz, como se Cameron fosse o único vendo."
"Mas uma viagem de cogumelos não pode emitir luz não importa o quão forte você esteja viajando."
c "\"Eu acho que consigo ver para onde ir. Apenas ande em frente.\""
d "\"Como--\""
"Cameron começa a balançar a cabeça, então para quando seu pescoço envia uma pontada de dor ardente pelas costas."
c "\"Eu não sei, mas eu consigo ver. Vamos só sair daqui... por favor.\""
"Cameron tenta muito não olhar para a forma amassada de Brian contra a parede lateral da cavidade, seus olhos arregalados brilhando do brilho suave."
d "\"Ok. Apenas me diga para onde, ok?\""
"E com certeza, enquanto eles saem, arco após arco aparece, e Cameron está confiante de que eles levarão à saída."
"Esses arcos torturaram sua mãe, mas isso {i}parece{/i} sua mãe, de alguma forma."
window hide
pause 0.5
scene bg black with medium_dissolve
window show
"Enquanto se movem, ambos ouvem sons de farfalhar muito atrás deles nas minas, mas Brian está definitivamente morto, ou pelo menos estava quando eles saíram."
"Então eles continuam se movendo, tentando ficar quietos."
"Então, dentro de uma hora, luz real."
window hide
scene the_arch3 with slow_dissolve
window show
d "\"Luz do dia.\""
"Devon olha para baixo para Cameron e faz caretas assim como Cameron fez quando viu o rosto de Devon."
d "\"Deus, querido, vamos te ajudar, e você vai ficar melhor, ok?\""
c "\"Mas e você? Você se sente bem?\""
"A voz de Cameron está mais fraca do que estava antes, e Cameron sente Devon acelerar seu passo."
d "\"Estou bem.\""
"Devon diz severamente, cerrando a mandíbula, e Cameron fica quieto."
d "\"Cameron, sinto muito.\""
c "\"E essa é a... última vez que você diz isso para mim, ok? Eu não te culpo por nada. Estou tão feliz por ter te conhecido.\""
"Ele ouve o coração do urso, estável pela maior parte da jornada, mas ficando mais rápido conforme eles se aproximam da saída."
d "\"Eu acho que ouço um helicóptero? E talvez um megafone? Merda, vieram nos buscar?\""
c "\"A espingarda estourou minha audição, então eu não... não tenho certeza.\""
window hide
scene the_arch2 with slow_dissolve
show the_arch2_anim
pause 0.5
window show
"Sua viagem está quase terminada, mas essas visões são tão vívidas."
"Cameron olha para este novo arco, e algo sobre ele parece diferente."
c "\"Ah.{cps=3}..{/cps}{w=0.4} Mãe,{w=0.3} eu encontrei.\""
d "\"Hã?\""
c "\"Seu arco.\""
d "\"Você está vendo arcos?\""
c "\"Você sabe como algo pode acontecer que é tão impactante, que divide sua vida em duas? Tipo, você vê a vida como antes, e depois daquele momento. Pode ser bom ou ruim.\""
"Devon hesita, como se quisesse uma resposta para a pergunta que acabou de fazer, mas deixa pra lá, por enquanto."
d "\"Claro.\""
c "\"Eu acho que te conhecer é a boa divisão na minha vida. Eu acho que o que aconteceu aqui, e o que vai acontecer depois, acho que é a divisão ruim.\""
"Sempre foi a morte de sua mãe, e ainda é."
"Uma divisão."
"Mas desta vez, Cameron percebe que foi profundamente afetado mentalmente, e não é algo de que ele possa simplesmente se recuperar."
"Algo está realmente errado com ele."
"Esse tem sido o caso por um longo tempo, mas agora, depois disso, algo foi empurrado para além do limite."
"Então, outra divisão."
d "\"Eu acho que nós vamos ficar bem, Cameron.\""
c "\"Devon, o que quer que aconteça depois disso, eu te amo, e estou tão feliz por ter te conhecido.\""
d "\"Vamos lá, você não precisava dizer essa primeira parte. Nós conseguimos. Ok? É apenas... uma bifurcação na estrada.\""
"Cameron suspira."
c "\"Ah, Devon, Artie está vivo! Ele foi buscar ajuda, eu acho... eu espero.\""
d "\"O quê? Como?\""
c "\"Eu não sei. Ele levou um tiro, mas escapou. Brian estava furioso. Ele está ferido, mas acho que conseguiu.\""
d "\"Ah.{cps=3}..{/cps}{w=0.4} Ah,{w=0.3} isso é...\""
"Os lábios de Devon tremem e seu rosto se contorce levemente enquanto ele tenta não chorar, mas é de um alívio e felicidade incríveis."
"Cameron não lhe diz como pedaços de Artie estão faltando, ou que não consegue mais senti-lo, ambos por causa de seus poderes diminuindo e porque Artie está muito longe, pelo menos é o que ele espera."
"Cameron olha para o arco, parecendo bonito e terrível ao mesmo tempo."
"O Monstro do Casaco de Chuva fica ao lado enquanto eles passam, e desta vez Cameron acha que é sua velha alucinação."
"De papelão, e imóvel, como sempre foi."
"Mas... algo sobre tudo isso, a maneira como ele está vendo as coisas, algo mudou."
"Não são suas habilidades psíquicas, porque agora é sutil e quase imperceptível novamente."
"Não, algo mais aconteceu, e sua mente parece errada."
"Olhar {i}para frente{/i} não está mais claro, mas enquanto Cameron usa o último da psilocibina em seu sistema para espiar em seu futuro, ele fica com medo do que vê."
"Então ele apenas vira seu focinho levemente para Devon."
d "\"Cameron, nós vamos conseguir.\""
"Com base no que viu, Cameron não tem certeza."
"Devon vai ficar, ele conseguiu ver isso, mas ele deveria?"
"Mais do que qualquer coisa, ambos querem ficar juntos, mas se Cameron se tornar um fardo para Devon, ele não sabe como pode ficar."
"Ele apenas espera que Devon ainda possa amá-lo depois dessa terrível mudança, e ele espera que possa lutar contra isso, seja o que for."
"Então, Cameron encosta a cabeça no ombro de Devon, sorrindo de uma maneira feliz, mas amarga."
c "\"Tá bem.\""
d "\"Tá bem,{w=0.3} agora vamos cair fora daqui.\""
window hide
pause 0.5
play sound2 gravel_echo volume 0.5
scene the_arch with slow_dissolve
show the_arch_anim
stop ambient fadeout 10.0
stop music2
stop music fadeout 10.0
pause 1.0
scene white with archtrans
pause 0.5
scene black with slow_dissolve
pause 2.0
jump a3s2