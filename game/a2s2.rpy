label a2s2:
play background wind2 fadein 5.0
"Devon encara, sentindo-se estranhamente distante da situação."
"Sua mente ainda está sobrecarregada com o que acabou de acontecer com Cameron."
"É nisso que ele quer se concentrar, mas a espingarda agora chama sua atenção, e por um momento, Devon pensa em simplesmente fugir."
"Se ele aplicar lógica a essa situação, ele supõe que o outro urso não atiraria, mas algo em seus olhos..."
"...Algo está errado."
"Então, Devon diz o que espera que deixe claro para o outro urso que eles não são uma ameaça."
show dev scream l dark4 at seven
show expression AlphaMask("foliage2", At("dev scream l dark4", seven)) as mask
with dissolve
d "\"Precisamos de ajuda. {w=0.3}Estamos perdidos e nosso amigo está inconsciente.\""
"O urso de aparência velha o observa por vários segundos."
"Devon ouve o farfalhar de folhas mortas e vegetação ao seu lado enquanto Arturo se mexe."
"De repente, o urso balança a espingarda para apontar para a direita de Devon."
unk "\"Não se mexa, garoto!\""
show art scared a l dark4 at jumping,thirteen
show expression AlphaMask("foliage2", At("art scared a l dark4", thirteen)) as mask3 at jumping
a "\"Ei, ei, ei! Me desculpe, não atire!\""
"Artie parece aterrorizado, sua voz tensa e aguda."
"O urso mais velho encara Artie por vários segundos antes de apontar a espingarda para o chão, mas apenas ligeiramente."
show art scared l dark4
show expression AlphaMask("foliage2", At("art scared l dark4", thirteen)) as mask3
with dis
"O urso gesticula em direção ao coiote."
unk "\"Vocês fizeram algo com ele?\""
show dev fear l dark4
show expression AlphaMask("foliage2", At("dev fear l dark4 ", seven)) as mask
with dis
d "\"O quê? Fazer algo? Não, estamos tentando ajudá-lo.\""
d "\"Algo.{cps=3}..{/cps}{w=0.4} o atacou.{w=0.3} Precisamos conseguir ajuda para ele.\""
"O urso mais velho faz uma careta."
unk "\"O que você quer dizer com 'alguma coisa'?\""
"Dev hesita, pelo menos até que a arma seja apontada em sua direção."
show dev scream l dark4
show expression AlphaMask("foliage2", At("dev scream l dark4 ", seven)) as mask
with dis
d "\"Não,{w=0.3} espere!\""
unk "\"Não vou esperar. Vocês aparecem na minha propriedade fazendo todo tipo de barulho, e estão aí com um coiote desmaiado.\""
show art confused l dark4
show expression AlphaMask("foliage2", At("art confused l dark4", thirteen)) as mask3
with dis
a "\"Ei, nós não fizemos nada com ele. Estamos tentando ajudar--\""
"O urso rosna."
unk "\"Não me importo se estão tentando ajudá-lo ou tentando foder ele. Eu quero saber a verdade, não essa história de 'alguma coisa' aconteceu.\""
"O impasse continua por mais alguns segundos antes de Dev intervir novamente."
show dev surprised h l dark4
show expression AlphaMask("foliage2", At("dev surprised h l dark4", seven)) as mask
with dis
d "\"Era algo escuro, como uma sombra. Eu chamei de algo porque não tive chance de ver direito, mas pulou nele e desapareceu.\""
"Devon percebe o que está dizendo enquanto fala, e meio que espera ser baleado por dizer algo tão estúpido."
d "\"Juro por Deus, foi isso que aconteceu.\""
"Os olhos do urso mais velho se voltam para Artie, e o gato rapidamente apoia a declaração ridícula."
show art scared a l dark4
show expression AlphaMask("foliage2", At("art scared a l dark4", thirteen)) as mask3
with dis
a "\"É, foi isso que aconteceu. Eu não sei que porra era aquela, mas estava lá. Era escuro e tinha olhos vermelhos ou algo do tipo. Acho que nem deveríamos estar aqui agora.\""
"Devon, mais uma vez, quer dizer a Artie para calar a boca, que falar mais só vai piorar a situação."
"Mas, em vez de ficar com raiva novamente, uma expressão estranha surge no rosto do outro urso, uma que Devon não consegue decifrar."
"Então ele finalmente fala, colocando casualmente a espingarda sobre o ombro."
unk "\"E pulou nele, aquele coiote aí?\""
d "\"Sim.\""
unk "\"Tá bem, então acho que vocês estão usando drogas, ou algo do tipo?\""
show dev embarrassed l dark4
show expression AlphaMask("foliage2", At("dev embarrassed l dark4", seven)) as mask
with dis
d "\"N—Não.\""
unk "\"Usar drogas no calor nunca é uma ideia inteligente.\""
d "\"Nós não estávamos...\""
"Devon deixa a frase incompleta, percebendo que isso não importa no momento."
d "\"Precisamos conseguir ajuda para ele. Ele não está acordando.\""
"Devon se ajoelha, colocando Cameron no chão enquanto o segura, precisando descansar os braços cansados."
"Há uma pausa em que o outro urso apenas os observa, uma pausa tão longa que Dev abre a boca para falar novamente."
"Mas é finalmente quando o urso mais velho parece sair do transe."
window hide
pause 0.5
scene brian with medium_dissolve
pause 0.5
window show
unk "\"Merda, {w=0.3}claro!{w=0.3} Desculpe pela arma e tudo mais. É que sempre aparecem uns malucos na minha propriedade de vez em quando.\""
"Devon olha para o urso que de repente ficou amigável."
"No fundo da mente, ele acha que quase consegue ouvir sirenes."
"Sirenes muito familiares."
unk "\"Essa porra nem está carregada!\""
"O urso grunhe enquanto traz a espingarda para frente, apontando-a para o chão antes que ela pareça se partir ao meio quando o coronha cai."
play sound pumpback
"O urso se vira para mostrar que os canos estão vazios."
window hide
scene bg forest_day
show dev surprised p l dark4
show expression AlphaMask("foliage2", At("dev surprised p l dark4",center)) as mask
with leftwipe
window show
"Isso realmente faz Devon se sentir um pouco melhor, mesmo que a arma tenha sido apontada para eles minutos atrás."
play sound pumpforward
"O urso então a fecha com um estalo."
unk "\"Então! Acho que a melhor opção é chamar as autoridades para que possam enviar ajuda.\""
show dev shocked h l dark4
show expression AlphaMask("foliage2", At("dev shocked h l dark4",center)) as mask
with dis
d "\"Você sabe como podemos fazer isso? Não tem sinal aqui.\""
unk "\"Claro que não! Mas tem sinal logo fora da cidade, a leste. Funciona sempre que eu vou lá para fazer uma ligação.\""
"O coração de Dev dispara no peito com a ideia de que pode haver uma saída rápida para essa situação."
show dev worried h l dark4
show expression AlphaMask("foliage2", At("dev worried h l dark4",center)) as mask
with dis
"Ele olha na direção leste, pronto para partir imediatamente."
unk "\"Espera aí, é um pouco longe, e é um ponto bem específico. Posso dar uma carona rápida. Não mais que cinco minutos.\""
"O urso mais velho se afasta e começa a se dirigir para a trailer."
show art glare l dark4 at thirteen
show expression AlphaMask("foliage2", At("art thinking l dark4", thirteen)) as mask3
with dissolve
"Artie olha para ele, claramente desconfortável com tudo isso."
"Dev também está hesitante, é claro que estaria."
"Qualquer um estaria. Mas depois de tudo pelo que passaram..."
show dev embarrassed l dark4
show expression AlphaMask("foliage2", At("dev embarrassed l dark4",center)) as mask
with dis
"Devon olha para Cameron, o coiote ainda respirando calmamente, agora parecendo quase em paz."
"Ainda assim, o medo aperta o peito do urso."
"O fato de Cameron {i}ainda{/i} não estar acordando está aumentando lentamente sua preocupação ao ponto do pânico novamente."
"Então, ele cerra os dentes e segue o urso mais velho."
"Ele meio que espera que Artie não o siga, mas ele segue, e os quatro desaparecem mais fundo na floresta."
window hide
pause 0.5
stop ambient fadeout 5.0
stop background fadeout 5.0
#leva eles para a van com uma garrafa de água
#ataca Dev e Artie
#algema Dev na van
#Atira em Artie

scene bg black with medium_dissolve
pause 1.0
window show
"A agonia de Cameron parecia que poderia durar para sempre."
"A sensação de sufocamento continuando sem fim."
"Mas depois de um tempo imensurável, os dedos sobre sua boca e narinas se dissolveram na escuridão."
"Assim como as vozes, diminuídas em sussurros indistintos."
"Agora sua respiração vem lenta e constante, mas ele precisa se concentrar nela, inspirar e expirar conscientemente para que não pare."
"Embora a experiência seja aterrorizante, a natureza trabalhosa dela quase garante que ele não vai hiperventilar."
"Depois de um tempo, o terror se dissolve em um desespero vazio e maçante, acompanhado por surtos de pânico cada vez que ele se lembra que está em um lugar que não entende, e que não parece conseguir escapar."
"Então, gradualmente, até isso se dissolve, e como um sonho dentro de um sonho, desaparece..."
play sound distant_gunshot
window hide
pause 0.5
scene mirror1 with medium_dissolve
pause 1.0
window show
"A visão de Cameron está embaçada no início, e permanece assim enquanto seus olhos permanecem quase fechados, sem foco."
"O medo surge em seu peito novamente antes que ele perceba que estava respirando normalmente sem precisar se concentrar nisso."
"É quando ele percebe que o que consegue ver é um pouco estranho."
"Parece com..."
window hide
scene mirror4 with medium_dissolve
pause 0.5
window show
"...ele mesmo."
"Cameron encara, ainda se sentindo grogue e confuso, tentando entender o que está vendo."
"É ele, seu reflexo, mas é difícil entender por que isso acontece porque parece que ele está deitado."
scene mirror3 with dis2
"A princípio, o coiote se pergunta se talvez seja o espelho do chão no banheiro e que ele desmaiou."
"Ainda assim, o ângulo está errado, e isso só deixa Cameron mais confuso."
scene mirror2 with dis2
"O coiote fecha os olhos novamente, tentando lembrar o que aconteceu por último."
"Ele também começa a se perguntar por que está deitado em algo macio em vez do piso frio do banheiro."
"Nada faz sentido."
"Então ele faz a única coisa que consegue pensar no momento:"
c "\"D—Dev?\""
"Ele ouve algo se mover ao seu lado."
"Cameron tenta limpar a garganta, mas está seca, então ele engole."
scene mirror3 with dis2
c "\"Dev!\""
unk "\"Merda...\""
window hide
pause 0.5
play music2 zen volume 0
play music zenintro fadein 10.0 volume 0.2
queue music zenloop volume 0.2
scene bg trailer with medium_dissolve
pause 0.5
window show
"Algo é pressionado contra seus lábios e, sentindo que é água, Cameron bebe, engolindo várias vezes antes que seja tirado."
"Cameron então olha ao redor, tendo uma visão completa de seus arredores."
"A voz não parecia ser de Dev, mas Cameron não consegue imaginar de quem mais seria, e uma grande forma marrom e peluda entra em seu campo de visão."
show bri neutral trailsun at left with dissolve
"Cameron encara, primeiro se perguntando o que poderia ter acontecido com Dev."
"Mas então ele percebe o quão estúpido é esse pensamento."
"Este é um urso completamente diferente."
"Ele também percebe que algo está definitivamente errado, que ou ele ainda está sonhando, ou está em uma situação que não consegue nem começar a entender."
show cam scared trailsun at right with dissolve
"Ele rapidamente se senta e o urso mais velho levanta uma pata."
show bri smirk2 trailsun with dis
unk "\"Ei, ei, está tudo bem, garoto. Estou aqui para te ajudar.\""
"A voz é mais aguda do que ele esperaria de uma criatura tão grande, e o coiote sente que já a ouviu antes, mas não consegue lembrar, pelo menos não agora."
show bri confused trailsun with dis
unk "\"Eu sou Brian. E você?\""
show cam worried a trailsun with dis
c "\"Cameron.\""
"Cameron responde automaticamente, mesmo que uma pequena voz no fundo de sua mente diga que isso não está certo."
"Nada disso está certo."
show bri smirk2 trailsun with dis
b "\"Bem, olá, Cameron. Você provavelmente está se perguntando onde diabos está, né?\""
"Embora o comportamento do urso seja amigável o suficiente, sua aparência definitivamente não é."
"Novamente, Cameron tenta desesperadamente lembrar exatamente o que aconteceu por último, e onde exatamente ele pode estar."
show cam serious a trailsun with dis
"Ele concorda de qualquer forma, instintivamente tentando manter a fachada de que está bem, e que não suspeita que tudo está errado."
show bri surprised trailsun with dis
b "\"Bem, é uma história engraçada, mas ouvi uns gritos lá fora e quando saí, encontrei você e seus amigos. Você estava inconsciente, é claro.\""
show cam surprised c trailsun with dis
c "\"Dev? Ele era um urso?\""
"Cameron olha ao redor esperançoso, como se Dev pudesse estar ali com eles."
"É só então que ele percebe que estão em um trailer, e fragmentos do que aconteceu recentemente começam a voltar."
show cam serious a trailsun with dis
"Isso o deixa ainda mais inquieto."
show bri smirk2 trailsun with dis
b "\"Sim, um urso como eu, e também tinha um gato.\""
show cam worried c trailsun with dis
c "\"Artie...\""
"As memórias do último dia e meio voltam ao coiote lentamente, e com elas vem uma sensação de ansiedade e pavor."
"Ou ele está em apuros, ou estava em apuros, e de alguma forma esse urso está aqui tentando ajudá-lo."
b "\"Bem, eu não peguei o nome dele. Ele fugiu assim que eu cheguei.\""
c "\"Onde está Dev? O urso, quero dizer. Ele está aqui?\""
b "\"Sim, sobre isso--\""
"O urso se mexe na cama em que está sentado, fazendo as molas rangirem."
show bri neutral trailsun with dis
b "\"O que aconteceu é que depois que o gato fugiu e você estava inconsciente, seu amigo urso, Devon, certo? Ele decidiu correr para a rodovia para conseguir ajuda para você.\""
show cam worried a trailsun with dis
"Cameron fica quieto enquanto tenta absorver isso."
"As frases do urso fazem sentido, tecnicamente, mas ao mesmo tempo são confusas."
"Por que Devon o deixaria aqui sozinho com esse urso?"
"Agora Cameron se lembra que eles estavam em uma viagem de algum tipo... uma viagem para Echo."
"A voz, o trailer..."
show cam shocked trailsun with dis
"Cameron começa a olhar ao redor novamente, tentando avistar uma espingarda, porque agora ele está começando a perceber quem esse pode ser."
show cam sad trailsun with dis
c "\"Eu não...\""
"Ele para, completamente perdido."
"O que ele quer dizer é que quer ver Dev, mas se o que o urso disse é verdade, não há muito que ele possa fazer."
show cam serious a trailsun with dis
c "\"O Devon sabe que estou aqui?\""
show bri smirk trailsun with dis
b "\"Claro que sabe. Parecia muito preocupado com você. Disse que teria mandado o gato buscar ajuda, mas nem sabemos para onde ele fugiu.\""
show cam confused c trailsun with dis
c "\"Por que ele fugiu?\""
show bri surprised trailsun with dis
b "\"Bem...\""
"Brian pausa, parecendo pensar no passado, e também parecendo hesitante em dizer algo."
show cam surprised a trailsun with dis
"Cameron fica tenso, a sensação de que algo está errado retornando."
show bri confused trailsun with dis
b "\"É meio difícil de explicar, mas algo o assustou.\""
show cam worried c trailsun with dis
"Recordar os eventos dos últimos dias parece ganhar impulso, e agora ele consegue lembrar vagamente o que aconteceu logo antes de acabar aqui."
"Ele estava de pé na floresta, orelhas abaixadas, ouvindo aquele estático horrível, mas o que exatamente aconteceu depois ainda está um pouco nebuloso."
show cam surprised c trailsun with dis
c "\"O que era?\""
show bri neutral trailsun with dis
b "\"Bem, isso pode parecer um pouco louco, mas eu moro aqui há um bom tempo e às vezes tem essa coisa nas árvores que vem atrás de mim...\""
"'Coisa?'"
"Que coisa estranha.{cps=3}..{/cps}{w=0.4} de se dizer."
"Mas então ele se lembra de algo estranho logo antes de perder a consciência: Uma sombra escura caindo sobre ele antes que ele desaparecesse em outro mundo, preso naquele terrível abraço."
show cam worried trailsun with dis
c "\"Uma sombra...\""
"Embora ele diga isso baixinho, o urso claramente o ouve."
"Cameron engole seco, ainda sentindo que essa situação está muito errada, mesmo considerando as circunstâncias."
"Mas Brian sorri de uma maneira quase simpática."
show bri smirk trailsun with dis
b "\"Por acaso parecia estático, ruído branco?\""
show cam serious trailsun with dis
"Cameron olha para o urso cuidadosamente antes de concordar."
show bri smirk2 trailsun with dis
b "\"É, eu já vi isso também. Alguns de nós conseguem ver coisas que outros não podem.\""
"Cameron engole alto."
show cam confused a trailsun with dis
c "\"Você.{cps=3}..{/cps}{w=0.4} Você também vê coisas?\""
b "\"Sim. Sempre pude. Não sei por quê.\""
show cam worried c trailsun with dis
"Por toda a confusão e terror, e de todas as pessoas, esse urso parece entender exatamente pelo que Cameron está passando."
"Ele sente uma súbita sensação de afinidade com o urso."
show cam surprised trailsun with dis
"Então Cameron se lembra do seu telefone, rapidamente o puxando e segurando o botão de ligar."
show bri surprised fists trailsun with dis
"A tela pisca por apenas um momento antes que múltiplas linhas verticais pretas apareçam na tela, que se alargam constantemente antes que a tela inteira fique preta."
show bri surprised trailsun with dis
"Cameron está confuso, então se lembra da queda no lago, e até vê um pouco de umidade ainda sob a tela."
show cam worried a trailsun with dis
c "\"Merda.\""
"Brian grunhe."
show bri lookdown trailsun with dis
b "\"Seu telefone quebrou? Que pena. Não tem sinal aqui de qualquer forma.\""
show cam surprised c trailsun with dis
c "\"Há quanto tempo ele saiu?\""
show bri closedeyes trailsun with dis
b "\"Hm, umas duas, três horas atrás?\""
show cam worried a trailsun with dis
"Ele estava inconsciente por tanto tempo?"
"Ainda assim, a ansiedade está dizendo a Cameron para se mover, para ir."
show cam serious c trailsun with dis
c "\"Acho que devo ir atrás dele. Obrigado pela ajuda, de qualquer forma.\""
"Cameron de repente se levanta, mas uma onda de tontura o atinge."
show cam shocked trailsun with dis
c "\"Ah, merda...\""
show cam sad trailsun with dis
"O coiote se segura na parede, sentindo-se fraco e confuso."
show bri angry trailsun with dis
b "\"Ei, calma aí, garoto. Acho que você não está em condições de sair por aí. Você pode desmaiar de novo, e aquele urso parecia bem insistente em que eu te mantivesse seguro.\""
"Cameron tem que se apoiar levemente na parede, recuperando o fôlego."
"Ele não tinha percebido que ainda está mal."
"Faria sentido já que ele estava desacordado por tanto tempo, é só estranho que parece estar piorando."
"O que quer que aquela criatura tenha feito com ele, parece sério."
"Como se lesse seus pensamentos, o urso menciona a entidade."
show bri vaguestare trailsun with dis
b "\"Além disso, acho que você não deveria sair enquanto aquela criatura sombria ainda está por aí. Já a vi pela janela algumas vezes. Não quero te assustar, mas acho que ela quer você.\""
show cam surprised a r trailsun with dis
"Cameron olha para a janela mais próxima deles."
"Em vez da sombra, ele se surpreende ao ver o Monstro do Casaco de Chuva logo além das árvores, parcialmente escondido em uma posição estranha e agachada."
"Ainda mais estranhos são os movimentos estranhos e espasmódicos que a criatura está fazendo."
"Embora seu rosto esteja quase escondido, Cameron pode dizer que está sendo observado."
"Mesmo depois de tudo pelo que passou, o coiote se vê baixando o olhar rapidamente."
"Mais uma vez, assim como quando tinha oito anos, ele tem medo dessa alucinação."
"Ou melhor, ele tem medo dessa imitação da alucinação, e considerando que está se movendo tão violentamente, é isso que é."
show bri surprised trailsun with dis
b "\"Você a vê?\""
show cam sad trailsun with dis
c "\"Ah, não, quero dizer, é outra coisa.\""
b "\"Ah, o que é? Às vezes eu vejo outras coisas bem perturbadoras naquela floresta. Bem, na maioria dos lugares desta cidade, na verdade.\""
show cam worried c trailsun with dis
c "\"É... algo mais pessoal.\""
"Cameron está dividido entre querer ser cauteloso com esse homem, mas também querer confiar nele."
"Depois do trauma dos últimos dois dias combinado com a sensação de quase ter sido abandonado por seu namorado, o coiote está desesperado por algum tipo de conexão."
show cam serious a trailsun with dis
c "\"Que tipo de coisas você vê?\""
show bri neutral trailsun with dis
"Brian parece hesitante."
b "\"Eh, não quero te assustar mais do que você já está.\""
show cam smile a trailsun with dis
c "\"Estou bem. Só estou me perguntando se talvez vejamos coisas parecidas.\""
"Cameron sorri para ele, e isso parece desconcertar o urso por algum motivo."
show bri smirk trailsun with dis
b "\"Hã, bem...\""
"Então ele parece sair disso."
show bri neutral trailsun with dis
b "\"Para ser honesto, eu vejo pessoas sendo mortas, geralmente. Não sei se é real, tipo do passado, ou se não é. Às vezes, parece que algo está sendo inventado.\""
show cam serious c trailsun with dis
"Cameron pode entender essa sensação."
c "\"Sim, eu...\""
"Outra onda de fraqueza e exaustão."
show cam sad trailsun with dis
c "\"Desculpe, ainda estou muito cansado.\""
show bri surprised trailsun
with dis
"Cameron desliza pela parede para se sentar novamente, ainda se sentindo fora de si."
"Mas pelo menos ele se sente um pouco confortável com esse urso agora."
show bri smirk trailsun with dis
b "\"Faz sentido, depois do que você passou. Quer a minha cama?\""
show cam worried c trailsun with dis
c "\"Estou bem. Só preciso recuperar o fôlego."
"Ele não está {i}tão{/i} confortável assim com ele."
show cam serious a trailsun with dis
c "\"Isso vai soar estranho também, mas eu vejo um monte de coisas nesta cidade, e às vezes parece inventado. Tipo, eu vi um OVNI, tipo uma nave alienígena acima de um corpo hoje.\""
show bri confused trailsun with dis
"Brian encara Cameron."
show bri lookdown trailsun with dis
b "\"Entendo.\""
show cam worried c trailsun with dis
"Assim que estava começando a se sentir confortável, o coiote se sente novamente tenso."
"Ele disse algo errado?"
c "\"Quero dizer, {w=0.3}eu não sei se era um OVNI, {w=0.3}mas parecia--\""
show bri smirk trailsun with dis
b "\"Você está bem, garoto. É só que eu nunca conheci ninguém que tenha visto algo que eu também vi. Foi naquela estrada de terra, certo? Forma circular com um monte de luzes vermelhas?\""
show cam surprised c trailsun with dis
"Cameron se anima."
"Não há dúvida em sua mente agora de que esse urso é definitivamente como ele."
c "\"Sim.{cps=4}..{/cps}{w=0.3} Sim, {w=0.3}em tipo...\""
c "\"Merda,{w=0.3} quando foi que aquele ônibus espacial explodiu? Tipo, em meados dos anos 80, eu acho?\""
show bri surprised fists trailsun with dis
"Desta vez, Brian solta uma risada de surpresa, e talvez um pouco de descrença também."
show bri smirk2 trailsun with dis
b "\"'86, para ser exato. Caramba, isso é loucura. Já conheci algumas pessoas como você, mas você está em um nível totalmente novo, garoto.\""
show cam smile a trailsun with dis
"Cameron encara de volta, brevemente se perguntando se ainda está sonhando com tudo isso."
"É quase muito abrupto tentar entender como ele acabou aqui com esse urso, mas se for um sonho, não é o pior."
c "\"Você pode me ajudar a encontrar o Devon? Talvez você pudesse me levar até a rodovia e poderíamos alcançá-lo.\""
"O urso se recosta, coçando a cabeça."
show bri confused trailsun with dis
b "\"Não sei sobre isso, garoto. Ele saiu em um bom ritmo, e aposto que provavelmente já chegou à rodovia agora. Provavelmente no processo de alertar as autoridades.\""
show cam sad trailsun with dis
"Cameron torce a barra da camisa em suas patas, sentindo um nó de preocupação crescente e doentio no fundo do estômago."
"Ele só quer ir, correr e encontrar Dev e escapar da cidade com ele, mas a ameaça do que está lá fora é muito real, e Cameron não quer repetir o que aconteceu na floresta."
"E aparentemente Dev já escapou sem ele."
"Faz sentido por que ele teve que deixá-lo para trás, mas isso não significa que não dói."
"Só agora as memórias do que aconteceu durante seu desmaio estão voltando, e só agora ele se lembra de como foi estar no inferno."
show cam worried c trailsun with dis
c "\"Aquela criatura sombria pode entrar aqui?\""
show bri neutral trailsun with dis
b "\"Não, parece evitar o trailer. Não sei por quê. Você está bem?\""
"Cameron esfrega os olhos com ambas as patas."
show cam heartbreak trailsun with dis
c "\"Eu não sei.\""
"Seu pesado aumento na respiração faz Brian se agachar na frente dele, batendo em seu ombro com força."
show bri smirk trailsun with dis
b "\"Ei, você está bem. Vou te fazer algo, ok? Que tal um chá? Isso sempre me acalma.\""
stop music fadeout 15.0
stop music2
"Os tapas sacodem o coiote de volta à consciência, e ele concorda, mesmo que só para fazer o urso se concentrar em algo que não ele."
c "\"Ok.\""
show bri smirk2 trailsun with dis
b "\"Ótimo, vou começar a fazer então. Só relaxe por enquanto.\""
window hide
pause 0.5

scene bg black with transition_fade
play background sirens fadein 10.0
window show
"O vento chicoteia violentamente no rosto de Devon."
"É forte o suficiente que ele mal consegue respirar."
"O som sinistro das sirenes era realmente a única coisa que garantia que ele estaria em casa o mais rápido possível."
"Ele sempre levou seus avisos a sério, porque o que eles alertavam sempre o aterrorizava."
"Então agora, nessa névoa de dor e horror, ele se pergunta por que não ouviu os avisos."
"Os tornados de um quilômetro de largura que varrem as planícies de seu estado natal evocam um medo primordial nele que poucas outras coisas fazem."
"Ele sentiu esse medo momentos antes de seu mundo se tornar um flash vermelho de dor..."
play sound distant_gunshot
"Antes de ver Artie cair sem vida no chão ao mesmo tempo que um estalo ecoava pelo ar."
"Antes de ser obrigado a beber da garrafa de água que o outro urso trouxe de seu trailer."
"E antes de suas patas serem firmemente amarradas acima de sua cabeça."
$ renpy.music.play("<from 15>ambient/wind.ogg", channel='sound',fadein=6.0)
$ renpy.music.set_volume(0.3, delay=4, channel="sound")
"Enquanto Devon volta a si brevemente no brilho vermelho deste contêiner de metal em que está, ao som de correntes de metal e a sensação de calor apertado, ele sabe que deveria estar fazendo algo."
"Ele deveria estar ajudando alguém, alguém com quem ele se importa profundamente."
"{cps=25}Lupita... {w=0.5}Artie... {w=0.5}Cameron...{/cps}"
"Cameron."
$ renpy.music.set_volume(0.6, delay=2, channel=u'sound')
d "\"Cameron...\""
"Sua voz está rouca, seca, à beira de quebrar."
"Seu peito parece estar sendo esmagado."
"Devon afunda de volta na escuridão, mesmo enquanto sua mente se agita em terror."
"Mesmo enquanto o tornado F5 continua a avançar direto para ele."
window hide
stop background fadeout 5.0
stop sound fadeout 5.0

pause 6.0
play music zenintro fadein 10.0 volume 0.2
queue music zenloop volume 0.2
scene bg trailer with medium_dissolve
pause 0.5
window show
"Cameron se senta à mesa enquanto o urso se ocupa perto do fogão com as costas voltadas para o coiote."
show cam worried a r trailsun at right with dissolve
"Novamente, o coiote contempla sair, seja pedindo a Brian novamente, ou simplesmente saindo pela porta."
show cam serious c r trailsun with dis
"Outro olhar para a janela confirma que o Monstro do Casaco de Chuva ainda está lá fora, desta vez em pé no alto das árvores, empoleirado em um galho, ainda observando."
show cam worried c r trailsun with dis
"Cameron rapidamente desvia o olhar novamente."
"Ele sente profundamente que, se sair, outra coisa terrível vai acontecer."
"Embora ele acredite na história do urso sobre o que aconteceu, algo sobre este trailer é extremamente desconfortável, deixando-o ainda mais ansioso."
"Ele acha que isso deve ter algo a ver com sua criação, o espaço longo e estreito parecendo familiar da pior maneira possível."
"É como ficar doente de repente."
"E ser lembrado de todos os sentimentos horríveis que se tem quando está especialmente doente."
"Enquanto isso, Brian está tagarelando sobre como a camomila é particularmente eficaz quando se trata de ansiedade, e Cameron se pergunta vagamente por que ele está se movendo tanto se está apenas fazendo chá."
"Principalmente, porém, Cameron está tentando pensar com clareza, alinhar seus pensamentos corretamente através da névoa que ainda sente nublar seu cérebro."
"Isso está deixando-o extremamente cansado, e algumas vezes o coiote está convencido de que ainda está sonhando."
"É quase como se estivesse chapado novamente, mas sem nenhum dos aspectos positivos de estar chapado."
"Sua ansiedade já está se acalmando, no entanto, apesar da preocupação de que o que estava na floresta possa ter causado algum tipo de dano ao seu cérebro."
"Ele concentra seus pensamentos em Devon, tentando pensar com clareza."
"O urso realmente o deixaria sozinho assim?"
"Ele poderia pelo menos ter deixado uma mensagem, para que ele soubesse que era isso que ele queria, que Cameron está seguro nesta situação."
"Mas..."
show cam disappointed trailsun with dis
"Cameron também sabe que isso não teria sido muito prático."
"Se Devon estava realmente com pressa, o que ele definitivamente estaria, ele o teria deixado para trás se soubesse que era o melhor, e se soubesse que a situação era segura."
"Não há realmente uma maneira de ele ter deixado uma mensagem, exceto talvez um texto, mas sem telefone e sem sinal..."
"Se esse Brian realmente quer ajudá-los, ele deveria ter ido para a rodovia em vez disso."
"Ele deve ter um carro, certo?"
"Não é como se ele pudesse simplesmente sobreviver aqui em um trailer velho."
"Cameron ajusta seu rosto em um sorriso agradável, sabendo que parecia deixar o urso mais velho à vontade sempre que fazia isso."
show cam grinning c trailsun with dis
c "\"Você tem um carro?\""
"Brian, aparentemente absorto no que está fazendo, olha para trás."
show bri smirk trailsun at left with dissolve
b "\"Ah, bem, eu meio que divido uma caminhonete com outro cara na cidade. Ele está fora da cidade com essa caminhonete agora. Claro que ele estaria, né?\""
show cam smile a trailsun with dis
c "\"Ah, ok.\""
"Brian sorri para ele novamente."
b "\"Posso ver por que o Daniel gosta de você. Você é um garoto simpático.\""
c "\"Ah, você quer dizer o Devon?\""
show bri smirk2 trailsun with dis
b "\"Merda, sim. O cérebro não lembra mais das coisas como costumava.\""
c "\"Tudo bem.\""
show cam worried a trailsun with dis
"Cameron encara a mesa, sentindo que essa troca foi muito estranha, mas é difícil pensar através da nebulosidade."
"Apesar da ansiedade amortecida, a sensação está o preocupando cada vez mais."
show cam sad trailsun with dis
c "\"Eu estou, uh.{cps=3}..{/cps}{w=0.4} me sentindo muito estranho. Estou tão cansado.\""
show bri serious trailsun with dis
b "\"Bem, considerando o que aconteceu com você, isso faz sentido. Sem querer me intrometer, mas você usa alguma droga?\""
show cam serious c trailsun with dis
c "\"Não, pelo menos não mais... Quero dizer, fumei maconha tipo, horas atrás, mas isso já deveria ter passado.\""
show bri neutral trailsun with dis
"Brian encolhe os ombros."
b "\"As pessoas sempre dizem que maconha não é grande coisa, mas provavelmente foi o que mais me ferrou quando eu experimentei.\""
"Cameron ouve o som de líquido sendo derramado em uma xícara."
show cam disappointed trailsun with dis
c "\"Sim, eu não.{cps=4}..{/cps}{w=0.4} acho que não gosto.\""
c "\"Mas eu não deveria ainda estar chapado, certo?\""
b "\"Não deveria, mas depois da primeira vez que fumei, me senti chapado por {i}anos{/i} depois, mesmo quando não estava usando.\""
"Cameron sente um arrepio de preocupação sob a névoa."
show cam confused c trailsun with dis
c "\"Anos?\""
show bri surprised trailsun with dis
b "\"Sim. É, uh, como se chama... Despersonalização? Me fez sentir como se minhas próprias patas não fossem minhas, e tudo parecia estranho e distorcido, como se houvesse um filtro na frente dos meus olhos.\""
show cam sad trailsun with dis
"Cameron lembra vagamente de alguns de seus próprios amigos descrevendo exatamente a mesma coisa, mesmo quando a viagem deveria ter acabado."
"Ele mesmo experimentou isso enquanto estava sob a influência de vários dissociativos."
"Ter a mesma experiência enquanto deveria estar sóbrio é quase aterrorizante, no entanto."
c "\"Maconha faz isso?\""
"Sua preocupação e pânico rompem a superfície por um segundo e ele sente que, naquele momento, emergiu das profundezas lamacentas de sua confusão antes de escorregar de volta."
"Ele não pode viver em um sonho pelo resto da vida."
"Mas o que é sua vida, sentado aqui em um trailer com um urso velho e um pouco fedido?"
b "\"Bem, isso passou assim que parei de pensar nisso.\""
"Como ele chegou aqui mesmo?"
"Onde está o Dev?"
show cam scared trailsun with dis
c "\"Ah, merda...\""
"Cameron de repente agarra a mesa, as patas tremendo como se estivesse saindo de seu corpo de alguma forma, e ele precisa se segurar em algo para permanecer no lugar."
show bri smirk2 trailsun with dis
b "\"Eeei, você está bem, garoto. Aqui, uh...\""
hide bri with dissolve
"Brian caminha até a geladeira, abre o congelador, puxa a forma de gelo e deixa cair alguns cubos na caneca, o gelo tilintando alto."
"Ele mexe por alguns momentos, então se vira para o coiote trêmulo."
show bri smirk2 trailsun at left with dissolve
b "\"Espero que não se importe com o gelo, mas deve estar fresco o suficiente para beber agora.\""
show cam worried a trailsun
show bri neutral trailsun
with dis
"Ainda confuso e aterrorizado, e apenas querendo algo para fazer, para se concentrar, Cameron estica a pata para a caneca que o urso está segurando."
"Ele a pega com uma pata trêmula, engolindo tudo de uma vez."
"Está cheia de mel e com o gosto forte de gengibre, e é diferente de qualquer chá de camomila que ele já tomou antes."
"A quantidade de mel é surpreendente e ele brevemente se pergunta se é uma coisa de urso, mesmo que Devon nunca tenha tido muita afinidade com isso."
"Ainda assim, Cameron não sente o sabor completo da mistura até terminar, e quando expira, um gosto estranho e terroso misturado com algo que Cameron só pode descrever como terra permanece na parte de trás de sua língua."
show cam sad trailsun with dis
"Cameron franze a testa para o chá bizarro e terrível."
"Ele não pode evitar fazer uma careta enquanto olha para a caneca, um globo grosso e redondo de mel permanecendo na base enquanto partículas escuras se acumulam lentamente ao redor dele."
"É perturbador o suficiente para que seu ataque de pânico seja interrompido antes que possa realmente começar."
show bri smirk trailsun with dis
"Brian ri."
b "\"Desculpe por isso. Gosto de adicionar raiz de kava para aliviar a ansiedade também. Devia ter te avisado.\""
"Cameron achou que o gosto era de alguma forma familiar, mas supõe que qualquer tipo de raiz teria um gosto terroso e amargo."
show cam confused c trailsun with dis
c "\"Ah, tudo bem, só não estava esperando. Eu li sobre kava algumas vezes quando estava procurando maneiras de ajudar com a ansiedade. Nunca experimentei, no entanto.\""
show bri smirk2 trailsun with dis
b "\"Bem, prepare-se para mudar sua vida. Isso me tirou de todos os meus remédios calmantes. Tenho alguns comprimidos sobrando se precisar de algo mais forte, no entanto.\""
show cam serious a trailsun with dis
c "\"Xanax? Uh, vou esperar e ver.\""
"Embora isso fosse bom, Cameron já se sente como se fosse cair no sono, então não parece a melhor ideia."
"Embora ele acredite em grande parte na história desse urso, ele não quer estar completamente alheio ao que está acontecendo agora."
b "\"Acho que você já teve alguma experiência com isso antes, né?\""
show cam worried a trailsun with dis
c "\"Uh...\""
"Cameron franze a testa para a mesa, sem saber o que dizer."
"Ele não quer realmente discutir seu passado com um estranho, mesmo que o cara pareça entender."
show bri surprised trailsun with dis
"Brian levanta as patas, como se estivesse mostrando que está desarmado."
b "\"Ei, eu não julgo, garoto. Eu estava nesse estilo de vida pela maior parte da minha vida antes de começar a mudar as coisas.\""
"Embora Cameron ainda esteja cauteloso, ele não quer parecer suspeito."
"Não parece a melhor ideia estragar as coisas entre ele e a única outra pessoa com ele no meio do deserto."
show cam serious c trailsun with dis
c "\"Sim, eu usei um pouco de tudo no ensino fundamental e médio. A única coisa que viciei foi opioides, no entanto.\""
show bri smirk2 trailsun with dis
b "\"Oof, você e metade do país, garoto. Essa é difícil.\""
"O cansaço está começando a se estabilizar, se não recuar ligeiramente, e Cameron sente uma sensação estranha, mas bem-vinda, de empatia por esse urso."
"Deve ser o kava fazendo efeito."
"O rosto de Brian parece um pouco mais definido e claro, e há uma calorosidade em seus olhos."
show cam smile c trailsun with dis
c "\"Foi minha primeira droga também. Experimentei tudo o resto porque estava tentando encontrar algo menos viciante e prejudicial.\""
"Brian balança a cabeça."
b "\"Esse é o problema com isso. Não há muita coisa por aí que faça você se sentir tão bem. É o que me disseram, pelo menos.\""
"Brian ri."
show bri smirk trailsun with dis
b "\"Eu tomei apenas um dos hidros do meu pai e acabei vomitando por horas. Acho que tive sorte de não conseguir mantê-los no estômago.\""
"Cameron pensa nisso, em como teria sido bom se ele tivesse ficado violentamente doente sempre que tentasse opioides, ou qualquer droga, por falar nisso."
show cam grinning a trailsun with dis
c "\"Sim, eu diria que isso é sorte. Parei na faculdade e não usei mais desde então, no entanto.\""
show bri smirk2 trailsun with dis
b "\"Bom para você.\""
show bri neutral trailsun with dis
"Brian olha para Cameron, começando a franzir a testa."
show cam smile a trailsun with dis
"As orelhas de Cameron se contraem quando ele sente uma mudança repentina no humor."
b "\"Agora, não quero trazer isso de novo, mas suas, uh, visões ficaram mais intensas quando você usou heroína?\""
show cam serious a trailsun with dis
"A princípio, Cameron quer corrigir o urso e dizer que nunca usou heroína, mas então para enquanto pensa."
"Claro, suas 'visões' pioravam quando ele estava sob certas drogas, incluindo opioides, mas ele assumiu na época que estavam apenas agitando suas alucinações já presentes."
"Foi só hoje que ele fez a conexão entre o uso de drogas e alucinações... ou visões."
show cam confused c trailsun with dis
c "\"Sim, na verdade, e algumas vezes com outras coisas também. Isso acontece com você?\""
show bri angry trailsun with dis
b "\"Definitivamente.\""
show cam smile a trailsun with dis
"Novamente, sentimentos de empatia crescem no peito do coiote."
"Há outros como ele, exatamente como ele."
show cam disappointed trailsun with dis
c "\"Talvez eu não esteja ficando louco, então. Eu fico indo e voltando nisso.\""
show bri confused trailsun with dis
stop music fadeout 15.0
"Brian ri um pouco."
b "\"Bem, não louco normal, de qualquer forma, certo? Diga...\""
show bri neutral trailsun with dis
"Brian olha cuidadosamente para Cameron novamente e o coiote está quase distraído pelo brilho que parece estar emanando dos olhos do urso."
show cam serious a trailsun with dis
"Estranhamente, o pelo intensamente vívido e definido parece estar ondulando, como se estivesse soprando ao vento, mesmo estando dentro de casa."
"Isso é kava?"
show bri serious trailsun with dis
b "\"Você já tentou algo mais psicodélico, como ácido, ou cogumelos?\""
show cam worried a trailsun with dis
"Cameron se mexe desconfortavelmente com a última palavra."
c "\"Sim, ambos. Ácido foi tranquilo, mas nada estranho aconteceu. Cogumelos só me deixaram louco e eu vi todo tipo de coisa.\""
show bri lookdown trailsun with dis
b "\"Hm, isso é uma pena. Esse pode ser um verdadeiro abridor de olhos.\""
show cam worried c trailsun with dis
c "\"Ah.\""
"Cameron não tem certeza do que mais dizer, se sentindo um pouco desconfortável novamente."
b "\"Mas sim, a maioria das drogas faz você ver mais coisas. As únicas que não fazem são os estimulantes. É por isso que tantas pessoas aqui se viciaram em metanfetamina.\""
"Brian ri novamente, mas desta vez soa um pouco sombrio, sinistro."
show bri confused trailsun with dis
b "\"O único problema com isso é que a metanfetamina ainda faz você ver merda, mas só porque te deixa louco.\""
"{i}Arcos e semicírculos...{/i}"
c "\"Sim.\""
hide bri with dissolve
"Cameron olha de volta para a mesa."
"Ele se pergunta sobre sua mãe novamente, e se talvez ela fosse como ele."
"Talvez ela tenha tomado os estimulantes porque estava apenas tentando parar as visões, mas acabou começando uma onda de alucinações e delírios."
"Cameron observa o veio da madeira na mesa se mover e mudar levemente, como ondas em um oceano."
window hide
play music amygdala fadein 10.0 volume 0.3
play ambient wind2 fadein 6.0
scene bg trailer
show bg trailer as trailer at drugtripbg
show cam surprised c trailsun at right
show cam surprised c trailsun as extra2 at drugtrip3 behind cam:
    xpos 1420
with medium_dissolve
pause 0.5
window show
"E então isso o atinge. Atinge ele com força."
"O gosto residual do chá, por que era familiar, por que as coisas estão se movendo de maneiras inexplicáveis, por que tudo está se sentindo mais estragado a cada segundo."
"Ele já esteve aqui antes."
hide cam
hide extra2
play sound chair
"Um momento parece desaparecer da memória de Cameron porque a próxima coisa que ele sabe é que já está de pé, a cadeira deslizando para trás dele."
show cam scared trailsun at right
show cam scared trailsun as extra2 at drugtrip3 behind cam:
    xpos 1420
with dissolve
"Ele encara Brian com olhos arregalados, boca aberta, mas parece que não consegue dizer nada."
"Ele não consegue pensar no que dizer se o urso fez o que ele acha que fez."
show bri lookdown trailsun
show bri lookdown trailsun as extra at drugtrip2 behind bri
with dissolve
"Brian encara de volta, observando Cameron cuidadosamente de uma maneira que diz ao coiote que o urso não está surpreso com essa reação, e isso deixa Cameron ainda mais assustado."
"A iluminação aconchegante e sonhadora do trailer se torna mais sinistra: vermelha e perigosa, e o urso na frente dele parece se distorcer--"
window hide
pause 0.5
scene trailer_vision
show trailer_vision as trailer at drugtripbg
show bri evilgrin3 red2
show bri evilgrin3 red2 as extra at drugtrip2 behind bri
show cam scared red2 at right
show cam scared red2 as extra2 at drugtrip3 behind cam:
    xpos 1420
with medium_dissolve
pause 0.5
window show
"--em um demônio."
show cam horror red2 with dis
c "\"Não! {w=0.3}Não, {w=0.2}não, {w=0.2}não, {w=0.3}o que você me deu!?\""
"Cameron olha desesperadamente para a caneca de café."
b "\"Você precisa se acalmar, entendeu?\""
show cam terror red2 at jumping
c "\"O que você me deu!?\""
show bri evilgrin red2
show bri evilgrin red2 as extra at drugtrip2 behind bri
with dis
b "\"Acho que você já sabe a resposta para isso, então por que não se senta e se controla.\""
"O rosto do urso está tão distorcido, mas Cameron honestamente não consegue dizer se é real ou não."
c "\"Era psilocibina?{w=0.3} Você me drogou com cogumelos!?\""
"Brian não diz nada, e ele está certo de que Cameron sabe."
"Ele nunca poderia esquecer essa sensação."
c "\"Meu deus,{w=0.3} por quê!?{w=0.4} Isso arruinou minha vida!\""
"Cameron está ofegante, os sons de sua respiração quase abafando o urso."
b "\"Sente-se, e eu vou explicar--\""
"Mas Cameron não tem intenção de se sentar."
"As sensações e visuais são tão ruins quanto da última vez, se não piores, e ele está apenas no começo."
"O medo e o pânico atingem um nível vertiginoso, e Cameron está correndo ao redor da mesa para a porta."
scene bs
play sound mugbreak
"Então ele está de costas, seu peito, coluna e a parte de trás da cabeça doendo." with vpunch
window hide
scene black
show psilocybin_red2
show psilocybin behind psilocybin_red2
show psilocybin_red2 at drugtrip2 as extra1:
    alpha 0.7
show psilocybin_red2 at drugtripbg as extra2:
    alpha 0.7
with dissolve
pause 0.5
window show
"Brian está em cima dele, e Cameron está de costas."
"Ele pode ver a caneca de café quebrada no chão a alguns metros de distância."
b "\"Acalme-se. Lembra do que eu disse sobre despersonalização? A única coisa que você pode fazer é não pensar nisso, caso contrário eu vou te nocautear.\""
"Cameron se debate, ofegante."
c "\"Me solta! {w=0.3}Não consigo respirar!\""
"Brian responde apertando seus braços com mais força, colocando mais peso no torso de Cameron."
c "\"Agh! {w=0.4}Pare, {w=0.3}me desculpe, {w=0.2}me desculpe!\""
"Ele nem sabe pelo que está se desculpando, só espera que talvez faça o urso parar."
b "\"Heh, e eu pensei que você era fofo quando estava sorrindo.\""
"Essa afirmação, por algum motivo, é a parte mais assustadora do que está acontecendo agora."
"Ele começa a gritar pela única pessoa em quem consegue pensar agora."
c "\"DEVON! {w=0.3}ME AJUDA! {w=0.3}DEVON!{w=0.3} DEVON!\""
b "\"Cala a porra da boca.\""
"Brian soa genuinamente irritado enquanto se levanta de Cameron."
window hide
scene bg trailer_vision
with medium_dissolve
show bg trailer_vision as trailer at drugtripbg
window show
"O coiote se prepara para gritar novamente, mas vê o pé de Brian se esticar e chutá-lo no lado, enviando-o contra a base do balcão."
"Então, curvando-se sobre ele com ambas as patas na borda do balcão, ele começa a chutar Cameron repetidamente."
"Cameron grita e chia, os golpes fortes o suficiente para que ele se preocupe que o urso definitivamente vai quebrar algo se já não quebrou."
"Ele se debate e rola, tentando escapar."
"Então, um chute o acerta particularmente forte na base do esterno e ele se encolhe violentamente, um ruído alto e semelhante a um sapo escapando de sua garganta."
"Brian pausa enquanto os sons continuam emanando da boca de Cameron."
"Cameron pode ouvir o urso respirando pesadamente sobre ele enquanto Brian observa seus espasmos agonizantes, quase como se estivesse fascinado por isso."
"Depois de quase um minuto, os ruídos terríveis se transformam em suspiros que então se transformam em soluços enquanto Cameron permanece encolhido de lado, um braço em torno de seu meio enquanto o outro está pressionado sobre seus olhos."
"Brian não se move, apenas observa enquanto Cameron chora no chão."
"A princípio, Cameron acha que pode ser melhor apenas manter os olhos fechados e tentar desaparecer na escuridão, talvez acordar novamente, mas em um novo lugar desta vez."
"Qualquer lugar parece melhor do que aqui."
"Mas é quando linhas vermelhas brilhantes, levemente curvadas, começam a se expandir e encolher atrás de suas pálpebras, e Cameron geme com a terrível lembrança do que vai acontecer."
"Ele vai ter uma bad trip, e vai ser terrível."
"Cameron tira a pata dos olhos e descobre que o que vê não é muito melhor."
"O urso enorme está agachado na frente dele, seu pelo agora uma massa retorcida e pulsante que quase parece outra criatura viva cobrindo o urso."
show brianshadow
show bri rage red2 behind brianshadow
show bri rage red2 behind brianshadow as extra at drugtrip2
with dissolve
b "\"Escuta! O que você fizer agora vai determinar o que vai acontecer com você.\""
"{i}Isso é um sonho. Tem que ser um sonho.{/i}"
"Tudo o que aconteceu, não só neste trailer, mas em toda esta cidade."
"Tem que ser um sonho, {w=0.3}uma alucinação, {w=0.3}um truque."
"Isso não pode estar acontecendo."
stop music fadeout 10.0
b "\"Preciso que você converse com algumas pessoas que eu conhecia. Se você for realmente um daqueles psíquicos, se puder resolver meus problemas, eu te solto como se nada tivesse acontecido.\""
window hide
pause 1.0
stop ambient fadeout 6.0
scene black with medium_dissolve
pause 0.5
scene van with medium_dissolve
play background reststop fadein 3.0
pause 2.0
window show
d "\"Cameron?\""
"Devon volta a si novamente, e ele solta o nome sem pensar."
"Ele não tem certeza de quanto tempo passou desde a última vez que acordou."
"Parece que foram horas, possivelmente até dias desde que ele esteve consciente pela última vez."
"Ele estava sonhando."
"Algo sobre insetos rastejando e mordendo seus braços."
"E tornados..."
"\"{i}Uma força giratória...{/i}\""
"Ele percebe então que são seus braços que o trouxeram de volta ao mundo acordado."
"Eles adormeceram, e agora o formigamento é tão ruim que parece que estão cobertos de formigas rastejantes e retorcidas feitas de chumbo derretido."
"O urso grunhe de desconforto e tenta abaixá-los de cima de sua cabeça, mas não consegue."
"Eles param e ele ouve um som de chocalho perto de suas orelhas, que se contraem com o barulho."
#sfx
"Correntes?"
"Devon congela, mantendo os olhos fechados, sem saber se quem fez isso com ele está por perto."
window hide
scene bs with fast_dissolve
pause 1.0
"Embora seja difícil pensar através de toda a nebulosidade, as memórias voltam a ele rapidamente."
"Primeiro, ele se lembra de caminhar mais fundo na floresta antes que o urso estranho entrasse em seu trailer para pegar algo."
"Ele saiu com uma garrafa de água, alegando que era para Cameron."
"Então, depois de caminhar mais para dentro da densa floresta, eles encontraram uma van branca."
"Exatamente o tipo de van que deixaria a maioria das pessoas desconfiadas."
"Devon ficou mais desconfiado, mas nessa altura já era tarde demais."
"O urso mais velho apontou uma arma para eles, uma que não era sua espingarda, e disse a ambos para entrarem na van."
"Artie começou a correr e o outro urso não hesitou em atirar nele, mirando em sua cabeça."
"Devon não tem certeza, mas poderia jurar que viu um jato de algo, seja pelo, sangue, ou pior, saindo da parte de trás da cabeça de Artie antes que ele caísse."
"Os dedos e dedões dos pés de Devon se contraem enquanto ele pensa naquele momento."
"O som. A repentinidade disso."
"Mas principalmente ele se lembra de como Artie caiu."
"Foi instantâneo, como se as cordas que o seguravam tivessem sido cortadas, desmoronando tão rapidamente que Devon tem certeza de que ele foi morto."
"Nesse ponto, Devon fez tudo o que o urso mais velho lhe disse para fazer, incluindo deitar Cameron no chão áspero do deserto..."
"Devon tenta evitar gemer enquanto se pergunta se essa pode ter sido a última vez que viu Cameron."
"E então deitou na van e deixou ele amarrar seus braços."
"Ele pensou em revidar naquele momento, mas foi tão rápido que antes que percebesse, estava preso e foi obrigado a beber da garrafa."
"Agora ele está no centro do tornado."
"\"{i}Uma força giratória...{/i}\""
"Devon cerra os olhos com mais força, sentindo umidade se acumulando nos cantos."
"\"{i}... Ao redor do ponto... É igual à força vezes a distância...{/i}\""
"Mas ele os abre um momento depois, percebendo que seu captador teria visto todos os movimentos que ele fez."
window hide
scene van with fast_dissolve
pause 0.5
window show
"\"{i}... Perpendicular à força...{/i}\""
"Ele está sozinho na van."
"Seus olhos ardem, e o urso percebe que está suando muito."
"Essa caixa de metal em que está preso está quente, quase sufocante."
"Ele se preocupa por um momento que dormiu a noite toda, e agora é o nascer do sol e ele está prestes a cozinhar até a morte nesta van."
"Mas depois de avaliar a luz, ele decide que ainda está por volta do pôr do sol, apenas algumas horas depois do que aconteceu."
"Depois que Artie foi morto."
d "\"Merda.\""
"Devon aperta os olhos novamente, sentindo lágrimas escorrendo e entrando no pelo úmido de suas bochechas."
"Ele se permite esse momento, mas rapidamente se concentra novamente, sabendo que Cameron ainda está lá fora, com aquele urso."
"Isso é o suficiente para provocar uma reação em Devon, uma que se transforma em uma onda em seu peito."
"Uma combinação de adrenalina e terror, mas principalmente fúria."
"Enquanto a brutalidade desse urso do interior evoca medo em Devon, também o deixa com raiva, que alguém, qualquer um, sentiria que tem o direito de fazer o que o urso mais velho fez."
"Ele abre os olhos novamente e observa seus arredores."
"Ele está deitado de costas, braços esticados acima da cabeça."
"Ele pode sentir que é um par de algemas que o mantém no lugar."
"Há espaço suficiente para que, lentamente, ele consiga se virar de bruços."
"A ação é incrivelmente dolorosa, e Devon não pode evitar gemer alto, seus braços parecendo que podem cair enquanto espasmodizam."
"Lentamente, dolorosamente, ele se puxa para uma posição de joelhos, tendo uma visão melhor de seu dilema."
"Ele percebe então que essas algemas são mais como grilhões, destinados a segurar criaturas do tamanho de ursos como ele."
"Elas estão parafusadas no chão da van."
"Devon olha para cima de repente, suas orelhas captando o que soa como um choro fraco fora da van."
d "\"Cameron?\""
"A voz de Devon sai rouca e rachada mais uma vez."
"Era Cameron?"
"Parecia com ele."
"Devon ainda está grogue com o que estava naquela garrafa de água, mas tem certeza de que ouviu o som distinto da voz de seu namorado."
"O fato de agora estar de repente ausente convence Devon de que era definitivamente Cameron."
"Ele se esforça para ouvir por vários segundos a mais, mas não consegue ouvir nada."
"Ele olha para a corrente pesada ligando as algemas de metal em seus pulsos."
"Inquebrável."
"Ainda assim, ele se pega puxando as algemas, esperando que haja algum tipo de folga na corrente e parafusos ligeiramente enferrujados."
d "\"Merda!\""
"Lágrimas enchem os olhos de Devon, a sensação de cair, cair para sempre retornando."
"Ele sentiu isso apenas algumas vezes antes."
"A primeira vez foi enquanto corria para casa, depois de encontrar o corpo de Lupita."
"A última vez foi quando viu Arturo ser baleado."
"E agora, sabendo que seu namorado pode estar à mercê desse urso cujas intenções Devon não consegue nem começar a adivinhar."
"Ele só sabe que são horríveis."
"Mas ver os rostos daquelas pessoas muda algo em Devon."
"Uma calma fria e gelada desce sobre ele, e ele olha para as correntes cuidadosamente."
"Suas aulas de física lhe ensinaram tudo sobre a maneira como a força é exercida pode aparentemente realizar coisas que parecem impossíveis."
stop background fadeout 10.0
"Então, mesmo enquanto seu coração martela em seus ouvidos, e mesmo enquanto seu cérebro está nublado com uma densa névoa de sedação, Devon analisa a corrente e os parafusos que a mantêm no lugar."
"\"{i}Torque.{/i}\""
window hide
pause 0.5

jump a2s3