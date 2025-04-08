label a1s1:
    $ quick_menu = False
    $ persistent.act_2 = False
    $ persistent.musicon = False
stop music fadeout 3.5
scene black
with transition_fade
show text "{size=70}Fuja{/size}" with medium_dissolve
pause 2.0
hide text with medium_dissolve
pause 1.0
play background reststop fadein 3.0
scene bg rural_road_day with medium_dissolve
pause 3.0
$ quick_menu = True
window show
"Correr era algo em que ele sempre foi bom. Ele sempre foi o mais rápido da turma."
"Ano passado, ele ficou em segundo lugar na corrida de 200 metros no campeonato estadual."
"Oito meses atrás, um treinador da Universidade de Pueblo o abordou para entrar no time de atletismo após a formatura."
"Mês passado, ele percebeu que era o calouro mais rápido do time."
"Semana passada, ele começou a sair com homens mais velhos que podiam levá-lo aos bares gays de Pueblo."
stop background fadeout 10.0
play music2 soldering volume 0
play music solderingintro fadein 10.0 volume 0.3
queue music solderingloop volume 0.3
"Três dias atrás, um desses homens colocou algo na sua bebida."
"Dois dias atrás, ele acordou amarrado."
"Ontem, ele estava sendo torturado."
"Dez minutos atrás, ele escapou."
"Mas agora, ele está percebendo que não adianta."
"Onde quer que ele olhe, só há deserto ardente. Não há ninguém."
"Suas tentativas de gritar por ajuda importam ainda menos porque sua voz está arruinada. Ele mal consegue sussurrar depois do que o homem lhe fez."
"E agora seus sons vazios e monótonos estão sendo engolidos pelo deserto."
"Enquanto isso, os passos pesados raspando no cascalho atrás dele continuam se aproximando. O homem não está com pressa nenhuma."
"Correr era algo em que ele sempre foi bom."
"Mas agora, quando mais importa, ele não consegue."
"O calouro mais rápido de uma universidade da Divisão 1 não é mais rápido que um velho viciado."
"Ele certamente seria, se tivesse comido algo nos últimos três dias."
"Se suas costelas não estivessem quebradas. Se ele conseguisse enxergar direito."
"O homem lhe deu algo. Disse que era para a dor, mas a dor ainda está lá, e agora ele nem consegue ficar em pé."
"Seu equilíbrio está arruinado, e ele continua tropeçando até ficar de quatro."
"É agora que ele percebe: o homem o deixou escapar de propósito."
"Isso o faz perceber outra coisa: ele vai morrer."
"Cansado da droga, dos últimos três dias de medo e tortura constantes, e de tentar correr, ele desaba."
"Ele fica ali na terra, chorando, embora as lágrimas não saiam."
"Ele já tinha chorado tudo depois de tudo o que o homem lhe fez."
window hide
pause 0.5
scene sunlight with sunlightright
pause 1.0
scene no_help_1 with medium_dissolve
pause 1.0
window show
"A luz acima é ofuscante. Ele se pergunta se isso é Deus."
"Sua mãe é uma católica devota, e mesmo que ele nunca tenha acreditado, ele promete a essa luz que vai se tornar um crente aqui e agora se ela o salvar."
play sound steps
play sound2 steps
"Os passos no cascalho se aproximam."
unk2 "{cps=20}Eu... {w=0.4}preciso.{cps=4}..{/cps}{w=0.4} ir..."
"Sua voz ainda está rouca e fraca."
"Os passos se aproximam ainda mais."
unk2 "{cps=20}Eu... {w=0.4}tenho uma.{cps=4}..{/cps}{w=0.4} reunião..."
"Há uma risada infantil e aguda."
window hide
pause 0.5
scene no_help_2 with medium_dissolve
pause 1.0
window show
unk "\"Acho que te bati uma vez demais. Tudo o que você faz agora é falar dessa merda de pista de corrida.\""
"A figura enorme se aproxima."
unk "\"Você sabe que essa merda não importa mais, né?\""
"Seu peito dói de tristeza e desespero avassaladores. E não é só porque ele está prestes a morrer."
"É porque sua mãe não vai saber o que aconteceu com ele."
"E é porque a última mensagem de texto que ele viu dela dizia \"Te amo, filhote!!!\" com dez emojis de coração e beijo."
"Na época, ele só revirou os olhos e não respondeu."
"Ele pensou que poderia responder no dia seguinte, ou no outro."
"Depois que foi sequestrado, o homem pegou seu telefone e o deixou no balcão."
"Ele ficou lá vibrando sem parar com mensagens, e seu sequestrador só riu quando ele pediu para pelo menos lê-las."
"Agora as lágrimas fluem enquanto o homem se inclina sobre ele com algo pesado na pata."
"Ele espera que sua mãe esteja certa sobre Deus."
"Ele espera poder vê-la do outro lado."
"Só para poder responder de alguma forma."
stop music
stop music2
scene bg black
centered "{cps=1}...{w=1.0}{nw}"
centertext "Mas há apenas..."
window hide
pause 2.0
play background highway fadein 5.0
scene bg outskirts_evening with medium_dissolve
pause 1.0
window show
"Cameron segura o assento com força, os dentes do coiote batendo a cada buraco que atingem."
"Seu namorado, Devon, não parece se importar; o urso tem a pata no volante e o cotovelo pendurado na janela."
"Ele estava cantando alto para a música tocando nos alto-falantes do carro via Bluetooth, e só quando o sinal do celular acabou que Devon finalmente parece notar o desconforto de Cameron."
d "\"Tudo bem, amor?\""
c "\"Acho que você poderia ir mais devagar.\""
d "\"O quê!?\""
"Cameron levanta a voz, gritando sobre o barulho interno do carro."
c "\"Vá mais devagar!\""
d "\"Por quê? Esse tipo de terreno é para o que esse bebê foi feito!\""
c "\"Tá, mas--\""
"A voz de Cameron salta quando atingem outro buraco profundo na estrada destruída."
c "\"Não sabemos o que está depois dessas curvas. E se for um precipício e cairmos num barranco, ou algo assim!?\""
d "\"É para isso que servem as barras de proteção, querido!\""
c "\"E eu acho que vou quebrar um dente!\""
d "\"Ah, qual é. Você tem que admitir que há algo bom em {i}sentir{/i} a estrada.\""
"Cameron não responde e continua segurando o assento."
"Devon diminui um pouco, contornando com mais cuidado as partes mais danificadas da estrada."
c "\"O que aconteceu com a estrada mesmo? Só faz cinco anos, né?\""
d "\"Enchentes repentinas, de acordo com o que li online... Obviamente não tem ninguém para manutenção, então é isso que acontece.\""
c "\"Ah é, eu esqueci como esse estado funciona; seco pra caramba até que uma parede de água mortal desça na estrada durante a temporada de monções.\""
"O coiote fica tenso quando o urso faz outra curva suave, mas ainda repentina."
c "\"E está ainda mais quente do que eu lembrava.\""
d "\"Como você é um coiote, Cameron? Esse é o seu clima!\""
c "\"Você sabe que não pode dizer isso. Só porque eu sou feito para isso não significa que eu tenha que gostar.\""
d "\"Sim, sim, mas você odeia Fort Allen também.\""
c "\"Lá não fica UM CALOR INSUPORTÁVEL, pelo menos. Eu consigo lidar.\""
d "\"Bem, a transferência para Bonneville City está parecendo boa, então você não vai ter que lidar com isso por muito mais tempo.\""
"Cameron encolhe os ombros."
c "\"Um clima mais ameno seria bom, eu acho.\""
"Devon sorri."
d "\"Clima melhor, {w=0.3}cenário melhor, {w=0.3}e pessoas melhores.\""
c "\"Todo mundo é mórmon.\""
d "\"Por isso que são legais!\""
c "\"Os que moram aqui embaixo não são.\""
d "\"Há uma GRANDE diferença entre os fundamentalistas e os--\""
c "\"Normais?{w=0.3} Os que batizam mortos e usam pijamas de Jesus debaixo das roupas?\""
"Dev encolhe os ombros."
d "\"A maioria das religiões é estranha quando você analisa assim.\""
c "\"Só estou dizendo, sejam roupas mágicas ou vestidos de pioneira, elas vieram do mesmo lugar perturbado.\""
"Devon não diz nada, e Cameron percebe o quão irritado ele soa agora."
c "\"Desculpa, só me preocupo como podem nos olhar. É mais difícil avaliar as pessoas quando todas são falsamente legais.\""
d "\"Sim, isso é verdade, mas olha--\""
"Dev acena com a cabeça para a janela de Cameron, e o coiote segue seu olhar."
"A paisagem rochosa e irregular se abre para um vasto azul."
d "\"Isso é o Lago Emma, {w=0.3}o que significa que Echo é--\""
"O urso olha para frente, e a primeira coisa que Cameron vê é uma placa alta e enferrujada com letras no topo que ele não consegue ler de tão longe."
"Abaixo dela há um pequeno prédio decadente, e além dele alguns outros menores e ainda mais decadentes."
"Cameron não tinha certeza do que sentiria quando visse a cidade pela primeira vez."
"Se o coiote realmente for o que Devon acha que ele é, então agora ele sentiria todas as coisas horríveis e malignas que supostamente aconteceram aqui."
"Aqueles pequenos prédios decadentes deveriam estar exalando as memórias de seu passado, que seriam então projetadas em sua mente."
"Mas Cameron sente.{cps=3}.. {/cps}{w=0.3}nada."
"Claro, ele meio que sabia que seria assim, mas ele nunca tinha estado em um lugar famosamente assombrado."
"Não como Echo, pelo menos."
"Então ele ficou um pouco preocupado."
"Dev já pediu a ele no passado para acompanhá-lo em suas \"investigações paranormais\" amadoras."
"Tudo porque o coiote podia \"ver\" coisas."
"Ele lembrava a Dev que a palavra correta era \"alucinar\"."
"As coisas que ele via eram manifestações de sua própria mente."
"Não havia razão para alimentá-la indo a um lugar supostamente assombrado."
"Dev entendeu a mensagem rapidamente e parou de pedir."
"Eles ainda conversavam sobre todos esses interesses que ele tinha, e Cameron percebeu que havia muito mais no interesse de Devon por fantasmas do que apenas diversão boba."
"E mesmo que ele se recusasse a aceitar as bobagens psíquicas de Devon, o urso ainda cuidava dele."
"Ele fez tanto pelo coiote que Cameron às vezes ficava envergonhado só de pensar."
"Então, quando Dev teve essa chance de ir para o lugar que mais queria, Cameron decidiu que tinha que ir também."
"Ele está fazendo isso por Dev, para mostrar sua gratidão por tudo que o urso fez por ele."
"Ainda assim, Devon tentou fazer isso parecer mais um tipo de férias, como se Cameron não fosse fazer nenhuma investigação de verdade."
"Ele precisaria conversar com o urso e deixar claro que estava disposto a fazer isso de verdade, pelo menos dentro do razoável."
"Ele também precisava dizer por que não gostava de fazer isso, e essa parte poderia ser difícil."
c "\"Não parece tão ruim, para uma cidade fantasma, quero dizer.\""
d "\"As aparências enganam. Espera aí. Preciso parar um segundo.\""
c "\"Por quê?\""
d "\"Quero dar uma olhada no lago antes de escurecer, e também preciso fazer um {i}enorme{/i} xixi.\""
"Cameron tenta não suspirar, só querendo chegar à cidade para ter certeza de que não sente nada."
"Para realmente ter certeza de que não há nada com o que se preocupar."
"Ele não está preocupado com fantasmas, mas com seu próprio cérebro e o que ele pode fazer."
"A estrada fica mais lisa e parece mais nova quando chegam ao lago."
window hide
play sound engineoff
pause 0.5
scene black with leftwipe
pause 0.5
scene bg lakeside_evening with leftwipe
stop background fadeout 5.0
pause 1.0
window show
d "\"Eles estavam tentando transformar esse reservatório em um ponto recreativo bem quando tudo aconteceu.\""
play sound cardoor
"Ambos saem, Cameron alongando as pernas com gratidão."
window hide
pause 0.5
play music2 roadside volume 0
play music roadsideintro volume 0.3
queue music roadsideloop volume 0.3
show cam serious c evening at right with Dissolve(1.5)
pause 0.5
window show
c "\"Que pena. Até que parece bonito.\""
show dev h evening at left with dissolve
d "\"Sim, esse lugar teve uma longa série de azar.\""
c "\"'Azar' é uma maneira de dizer--\""
show dev happy evening with dis
d "\"Segura essa ideia, {w=0.3}vou mijar!\""
hide dev with dissolve
show cam annoyed a evening with dis
"Dev sai mancando, claramente tendo segurando até quase não aguentar mais."
"Cameron balança a cabeça, lembrando de todas as paradas que passaram na interestadual."
show cam disappointed evening with dis
"Com um suspiro, Cameron se apoia no Jeep, olhando para o lago."
"Até agora, realmente não está tão ruim."
"Claro, eles ainda não estavam na cidade, mas todos aqueles sonhos que ele teve, todos aqueles sentimentos terríveis... Parecem bobagens agora."
"É só uma pequena cidade abandonada com uma história triste."
"Se seu cérebro fosse manifestar algo disso, esse algo seria apenas... triste."
"Cameron sabe que suas alucinações não são reais. Ele sabe disso desde criança, depois que viu um monstro de capa de chuva em sua casa móvel."
"Ele também sabe que fantasmas não são reais."
"Mas Devon acredita. Ou pelo menos quer acreditar."
"Ele quer tanto, e acha que Cameron pode vê-los."
"Cameron sabe que há algo extremamente errado em usar o que poderia ser um transtorno dessa forma."
"Devon também está ciente disso. {i}Dolorosamente{/i} ciente."
"A ponto de Cameron conseguir dizer dias antes que ele ia perguntar sobre levá-lo nessa viagem."
"E sim, isso é errado. Mas o urso nem acha que Cameron tem uma doença mental, ou pelo menos é assim que parece para o coiote."
"Devon não entende como é lutar com a realidade, ter esses problemas e nunca receber um diagnóstico adequado."
"Cameron só sabe que algo está errado, e sempre esteve."
"E que ele nunca contou a ele como era, então como ele poderia entender?"
"Ele contou um pouco, mas sempre teve no fundo da mente a preocupação de que Dev iria embora se contasse tudo."
"Então Dev pegou esses fragmentos de insight sobre a psique de Cameron e de alguma forma interpretou como ele sendo \"dotado\"."
"Ele não podia culpar o urso; às vezes as coisas que ele vê parecem ter um significado mais profundo, como se houvesse mais do que apenas saúde mental."
"Mas não é essa a natureza de vários transtornos mentais, não reconhecer a doença pelo que é?"
"Já faz mais de cinco anos, e Dev viu Cameron no seu pior, no seu mais louco absoluto, e de alguma forma ele ficou por perto e ainda acreditava que o coiote era só um cara normal com alguns problemas pessoais."
"Cameron se abraça um pouco mais forte, percebendo que agora é a hora de realmente conversar sobre isso."
"E depois disso, eles podem ter um novo começo em Bonneville."
show dev smirk p evening at five behind cam with dissolve
d "\"Ufa, {w=0.3}estou pelo menos três quilos mais leve depois disso.\""
show cam unamused c evening with dis
c "\"Sabe, eu não me importo de fazer xixi na natureza, mas não vou fazer mais do que isso.\""
show dev embarrassed evening with dis
d "\"Sim, eu meio que esperava que houvesse um banheiro químico ou dois por aqui, mas parece que vamos ter que cavar alguns buracos--\""
show cam angry evening at jumping
c "\"DEV!\""
show dev scream evening at jumping
d "\"Uau! {w=0.3}Brincadeira, querido!\""
show dev grin p evening with dis
d "\"Podemos dirigir até o posto de descanso.\""
show cam disgusted evening with dis
c "\"Humph.\""
show dev shocked h evening with dis
d "\"O que foi?\""
"O coiote pausa, tentando entrar no mindset que essa conversa desconfortável vai exigir."
show cam disappointed evening with dis
c "\"Uh.{cps=3}..{/cps}{w=0.4} Só me dá um segundo.\""
stop music fadeout 10.0
stop music2
play background lakesounds fadein 5.0
"Cameron vê a postura do urso mudar instantaneamente."
show dev embarrassed evening with dis
d "\"T-Tudo bem.{w=0.3} Hum, {w=0.3}mas enquanto eu te dou esse segundo, {w=0.3}desculpa por te provocar e ser tão nojento.\""
show dev disappointed evening with dis
d "\"Eu sei que não é onde você quer estar agora, e eu só estava tentando aliviar o clima, e você sabe que é porque eu te amo--\""
show cam frustrated evening with dis
c "\"Jesus Cristo, {w=0.3}para!\""
show dev embarrassed evening with dis
"Devon fica quieto e engole, o som alto sendo quase cômico."
"Há uma pausa, e embora Cameron tente manter uma expressão séria, a tensão parece se quebrar sozinha."
show cam happy eyes evening with dis
c "\"Eu prefiro muito mais ouvir você fazer piadas de cocô do que agir daquele jeito. É tão estranho.\""
show dev skeptical p evening with dis
d "\"O quê, {w=0.3}ser atencioso?\""
show cam smirk c evening with dis
c "\"Mais ou menos. Você é atencioso, só não daquele jeito estranho e ansioso.\""
show dev shocked p evening with dis
d "\"Bem, me processe por tentar ser cuidadoso. Eu só não quero dizer algo estúpido e--\""
"Cameron interrompe o urso, não querendo mais adiar isso."
show cam worried a evening with dis
c "\"Devon, só me escuta um minuto.\""
c "\"Eu sei que você não disse, mas vamos deixar claro que ambos sabemos que eu estou aqui por mais do que companhia. Eu não sou tão burro.\""
show dev disappointed evening with dis
d "\"Ah...\""
show cam worried a evening with dis
c "\"E eu só quero dizer que não acho que isso seja uma boa ideia porque o que eu tenho é... algum tipo de problema, não uma habilidade--\""
show dev surprised p evening with dis
d "\"Eu sei, eu não deveria pensar assim, mas pesquisei e só acho que não combina com você ter um transtorno men--\""
show cam frustrated evening with dis
"Dev se interrompe quando Cameron suspira profundamente."
c "\"Por favor, {w=0.3}não.\""
show dev embarrassed evening with dis
d "\"Eu sinto m--\""
"Dev se interrompe de novo, tentando esconder uma careta."
show cam worried a evening with dis
c "\"Quero dizer, você está certo que não sabemos exatamente qual é o meu problema. Eu só sei que não é bom--\""
c "\"--mas o que importa é se isso ajuda {i}você{/i}, não importa se eu acho que é real ou não. Você fez muito por mim, e eu quero poder fazer algo por você.\""
show dev skeptical p evening with dis
d "\"Não, o que eu penso não importa. O mais importante é--\""
c "\"ENTÃO, {w=0.3}eu vou fazer. {w=0.5}Vou ser seu psíquico no fim de semana.\""
show dev shocked h evening with dis
d "\"Espera, {w=0.3}serião?\""
show cam annoyed evening with dis
c "\"Dev, eu não vou passar o tempo todo fingindo que estamos tendo um bom e inocente momento naquela cidade de assassinatos.\""
d "\"Mas.{cps=3}..{/cps}{w=0.4} Eu não quero te fazer fazer algo que você não--\""
show cam smile c l evening with dis
c "\"Ah, eu quero. Talvez eu não {i}goste{/i}, mas eu quero fazer. Só por você.\""
show dev embarrassed evening with dis
d "\"Cam--\""
c "\"Não, eu tomei minha decisão, e eu vou fazer. Mas só dessa vez.\""
show dev worried p evening with dis
d "\"Se você tem certeza, mas por favor não me coloque na frente do seu--\""
show cam smile talking c evening with dis
c "\"E eu pesquisei naquele fórum que você me mandou alguns anos atrás, então meu sexto sentido está pronto e esperando.\""
"Isso parece finalmente tirar Devon de sua relutância, e um leve aborrecimento por ser interrompido a cada frase."
show dev happy evening with dis
d "\"Espera, {w=0.3}sério!? {w=0.4}Tinha tantas pessoas como você naquele fórum. Você--\""
show cam serious c evening with dis
c "{i}\"Escuta{/i}. Eu quero que você encontre suas respostas, eu REALMENTE quero, mas acho que a pior coisa que eu poderia fazer é mentir para te fazer sentir melhor. Eu vou ser completamente honesto sobre tudo--\""
show cam disappointed evening with dis
"Cameron se apoia no jipe."
c "\"--independente de eu ver algo ou não.\""
show dev h evening with dis
d "\"Claro, é isso que eu quero!\""
c "\"E é por isso que você não deveria estar ficando animado agora. Só estou te dizendo que vou tentar.\""
show dev smirk h evening with dis
"O urso olha para Cameron por alguns segundos, apenas sorrindo."
show cam confused a evening with dis
c "\"...O quê?\""
show dev grin h evening with dis
d "\"Só estou feliz por ter te conhecido, {w=0.3}e que estamos juntos, {w=0.3}e que você está aqui comigo.\""
"Devon envolve Cameron com um braço, puxando-o para seu lado enquanto também se apoia no Jeep."
window hide
pause 0.5
$ renpy.music.set_volume(0.2, delay=3, channel=u'background')
play music2 unfold volume 0
play music unfoldintro fadein 10.0 volume 0.3
queue music unfoldloop volume 0.3
scene lake_emma_1
show lake_emma_1
show lake_emma_2
show lake_emma_3
with medium_dissolve
pause 1.0
window show
d "\"Mas sério, {w=0.3}se você alguma vez sentir que.{cps=3}..{/cps}{w=0.4} sei lá, {w=0.3}você não está a fim, é só me avisar.\""
c "\"Bem, desde que você não esteja esperando nada, acho que vai ficar tudo bem.\""
d "\"Sim.\""
"Devon continua sorrindo e Cameron franze a testa."
c "\"Porque eu estou com a impressão de que você está esperando muito.\""
"Devon pausa, parecendo pensar."
d "\"Bem, também estou feliz que você está sendo mais aberto assim. Eu sempre senti que você não queria falar sobre isso.\""
"Cameron também pensa."
scene lake_emma_2 with dis2
c "\"Acho que eu só não queria ouvir que o que eu vejo deve {i}significar{/i} algo, sabe?\""
d "\"Sim, isso ficaria chato rapidinho, mas já que estamos falando sobre isso agora--\""
d "\"--não significa? Tipo, algumas coisas que você mencionou não fazem sentido, como aquela criatura de capa de chuva, mas e seu antigo amigo que... você sabe?\""
c "\"Levou um tiro na cabeça? Depois que eu alucinei que alguém atirou nele na cabeça?\""
d "\"É, {w=0.3}essa.\""
c "\"É disso que eu estou falando. Você, e todos nós, realmente, gostamos de ver significado em tudo.\""
c "\"Que temos um propósito na vida, {w=0.3}um {i}motivo{/i}.\""
c "\"Razão, {w=0.3}propósito, {w=0.3}e o significado da vida não significam nada para o universo.\""
c "\"Tudo só {i}é{/i}. Se tem significado ou não, cabe a nós.\""
c "\"Sim, é estranho que eu tenha alucinado como ele morreria, mas ele também estava envolvido em coisas que poderiam levar a isso.\""
c "\"Eu sabia que ele estava vendendo drogas de um jeito arriscado, então sabia que sua vida estava em perigo, {i}e{/i} eu estava cheio de cetamina. Toda a razão está aí.\""
d "\"Bem, {w=0.3}eu, {w=0.3}uh--\""
"Dev se mexe, claramente desconfortável e tentando não parecer assim."
d "\"Eu entendo isso, mas há muitos outros exemplos que eu poderia citar. Talvez seja coincidência, mas em algum ponto você não tem que se perguntar se talvez seja outra coisa?\""
"Cameron suspira."
c "\"Claro que eu já pensei nisso, mas o que sempre me preocupa nessas coisas paranormais que você gosta, e na vida após a morte e tudo mais--\""
scene lake_emma_3 with dis2
c "\"--me lembra da minha mãe.\""
"Dev não diz nada, só espera e escuta."
c "\"Sabe, no final, logo antes de eu sair, ela geralmente estava cheia de algo para ficar acordada em seus três empregos, seja anfetaminas ou metanfetamina, ela mal dormia.\""
c "\"Tínhamos um ventilador de caixa no nosso trailer, e um dia, depois que ela ligou, me perguntou se eu conseguia ouvir alguém falando {i}de dentro{/i} do ventilador.\""
"Cameron tinha debatido se contaria a Devon todos os detalhes sobre sua mãe, mas sente que precisa dizer."
"Só para que Devon tenha alguma explicação do porquê."
c "\"Eu disse que não, mas ela sentou ao lado dele e ouviu e eventualmente teve essa enorme epifania de que era Deus.\""
c "\"E ela fez isso por semanas, e era quase tudo o que ela fazia quando estava em casa; ouvindo o ventilador falar com ela.\""
c "\"Eu não sei bem o que ele estava dizendo para ela. Nem acho que eu realmente entendia o que estava acontecendo.\""
c "\"Eu só sabia que às vezes viciados em estimulantes faziam esse tipo de coisa, especialmente quando não dormem, sabe?\""
c "\"Mas então ela começou a procurar por formas específicas; arcos e semicírculos.\""
c "\"Essa voz disse a ela que ela poderia entrar no céu se passasse pelo certo.\""
c "\"Mas a voz também disse que o diabo a enganaria com falsos para dificultar encontrar o 'verdadeiro'.\""
c "\"Ela me mostrou isso, como havia tantos, e sim, eles estavam lá, mas quando você procura por esses padrões, por algo tão simples quanto a forma de um arco--\""
"Cameron traça um dedo ao longo do arco do para-lama em que está apoiado."
c "\"--você vai encontrá-los.\""
c "\"Eventualmente, ela me disse que tudo estava distorcido. Acho que ela estava tão fodida que essas formas simplesmente saltavam para ela, como se seu cérebro as destacasse e ela não conseguisse ignorá-las.\""
c "\"No último dia, ela me disse que até {i}eu{/i} parecia um arco, e que ela achava que eu tinha sido condenado ao inferno.\""
c "\"Ela parecia completamente.{cps=3}..{/cps}{w=0.4} acabada.\""
c "\"Ela me disse que voltaria para me salvar, e então saiu do trailer.\""
c "\"Algumas horas depois, ela se afogou tentando nadar sob uma ponte, e todo mundo no trailer park meio que viu como apenas mais uma viciada delirante se matando acidentalmente.\""
"Cameron tinha contado a Devon que sua mãe se afogou em um rio enquanto usava drogas, mas os detalhes são assustadores, e o urso só envolve Cameron mais forte."
c "\"Mas eu acho que foi um suicídio, que ela estava tão cansada de sua vida de merda que apostou naquela ponte sendo o arco que a levaria ao céu, de um jeito ou de outro.\""
scene black
show lake_emma_2
with dis2
c "\"Então é por isso que eu me preocupo em seguir esses padrões, mesmo que seja algo como procurar por OVNIs, ou fantasmas.\""
c "\"Tipo, sim, a metanfetamina e a falta de sono a levaram ao limite, mas há algo genético aí também?\""
c "\"E se eu tiver predisposição a isso? Eu pensei que as drogas estavam piorando, mas não uso nada desde o segundo mês depois de te conhecer, e ainda vejo coisas às vezes.\""
scene lake_emma_3 with dis2
c "\"Quero dizer, seja o que for que está acontecendo comigo, está estável, mas me pergunto se isso vai durar.\""
"Devon limpa a garganta."
d "\"Eu {i}nunca{/i} deixaria isso acontecer com você. Eu sei que digo merdas sobre isso, mas sei que pode ser perigoso, e estou sempre cuidando de você.\""
scene lake_emma_2 with dis2
c "\"Honestamente, é bom ouvir isso, porque deixar minha mãe sentar ao lado de um ventilador por três horas direto todo dia, alimentando suas ilusões, foi a coisa mais idiota que eu já fiz.\""
c "\"Mas eu estava chapado na minha droga de escolha porque eu simplesmente não me importava. Mas o negócio é que mesmo naquele inferno em que ela estava, {i}ela{/i} se importava.\""
c "\"Eu usei demais algumas vezes, e mesmo que ela estivesse ouvindo seu ventilador, em seu próprio mundo, colando post-its em todas as formas que via--\""
c "\"--ela ainda percebia na hora quando minha respiração não estava certa, e eu acordava com ela esguichando Narcan no meu nariz.\""
"Cameron vê Devon inclinar a cabeça em questionamento."
c "\"Neutraliza overdose de opioides.\""
scene lake_emma_3 with dis2
c "\"Mas o negóio é que, {w=0.4}minha mãe não gostava de opioides porque a deixavam enjoada.\""
c "\"Então isso significa que ela conseguiu esses sprays só para mim, só por precaução, mesmo quando eu achava que ela estava tão absorvida em seu próprio mundo para se importar.\""
c "\"Então dói pensar naquela noite, como eu apenas deixei ela sair do nosso trailer assim.\""
window hide
pause 0.5
stop music fadeout 7.0
stop music2
$ renpy.music.set_volume(1.0, delay=5, channel=u'background')
scene bg lakeside_evening with medium_dissolve
pause 0.5
window show
"Cameron respira fundo mais uma vez."
"Ele não tinha planejado falar sobre essa última parte, mas simplesmente saiu."
show cam sad evening at right with dissolve
c "\"{cps=30}Desculpa, {w=0.3}eu realmente não estava planejando entrar em tudo isso.\""
show dev embarrassed evening at left with dissolve
d "\"Cara, {w=0.3}NÃO se desculpe.\""
show cam disappointed evening with dis
c "\"Mas é parte do porquê eu sou do jeito que sou. Eu sei que meus sintomas não batem perfeitamente com o que você pesquisou na internet, mas são próximos o suficiente.\""
c "\"E honestamente, talvez você esteja certo, talvez haja mais depois que morremos, e de alguma forma eu posso te ajudar a encontrar, mas se as coisas piorarem, e se algo estiver errado comigo, só me traz de volta.\""
show cam worried a evening with dis
c "\"Ver a forma de um arco, lembrar de todos os marcadores que ela colocou neles, é como um lembrete do que aconteceu com ela e do que pode acontecer comigo.\""
hide dev
hide cam
with dissolve
"Sem dizer nada, Devon puxa Cameron para um abraço, e o coiote pressiona sua cabeça contra seu peito."
"Naquele momento, Cameron percebe por que tantas pessoas amam seus terapeutas."
"Ele sempre teve medo de que Devon ficasse muito estranhado com o que aconteceu quando ele era adolescente."
"Que ele finalmente veria todos os esqueletos em seu armário: negligente, negligenciado, abusivo, abusado e tão desesperadamente viciado."
"Assim como sua mãe. A definição de lixo de trailer."
"Cameron foi tudo isso em algum momento de sua vida, mas sabe que não importa para Devon."
window hide
stop background fadeout 6.0
pause 0.5
scene black with leftwipe
pause 0.5
play ambient desertmorning fadein 10.0
scene bg outskirts_evening with leftwipe
pause 0.5
window show
"Depois de um tempo, Devon solta e eles começam a voltar para o Jeep, o urso se sentindo um pouco trêmulo."
"Cameron se abrindo assim foi realmente assustador."
"Devon sabia de pedaços da história de seu coiote, mas ouvir assim, como ele teve uma overdose e quase..."
"Dev estremece."
"Ele só está feliz que o coiote está seguro com ele agora, fora daquele inferno."
"Quando está prestes a entrar no lado dele do Jeep, ele olha para a cidade a cerca de um quilômetro de distância."
"Enquanto Cameron tinha dito que tudo isso o fez se sentir melhor, Devon estava se sentindo mais conflitado do que nunca."
"Tudo o que Cameron acabou de contar praticamente gritava que isso era uma má ideia, que isso não era bom para ele."
"Importa o que {i}ele{/i} pensa sobre as alucinações de Cam?"
"Que sua leitura superficial da literatura de psicologia anormal sobre alucinações o levou a acreditar que Cameron não era mentalmente doente?"
"Não."
"Como ele poderia levá-lo a Echo depois de ouvir isso?"
"Como ele poderia arrastá-lo para essa caçada sem fim pela verdade novamente?"
"No entanto, ao mesmo tempo, Cameron está dizendo que quer fazer isso."
"Dev olha sobre o capô para Cameron, batendo suas garras contra o topo macio do Jeep."
show dev grin p evening at left with dissolve
d "\"Ei, Cam? O que você acha de continuarmos para o norte, dar uma olhada em Deseret? Sabe, ver como Bonneville pode ser. Ver como os mórmons realmente são. Poderia ser divertido.\""
"Enquanto ele diz isso, há um sentimento esmagador em seu peito, temendo que Cameron possa dizer sim, mas ao mesmo tempo esperando que ele o faça."
show dev worried p evening with dis
d "\"Quero dizer, com a forma como as coisas estão, eu nem sei se vamos conseguir cruzar as fronteiras estaduais em algumas semanas. Eles estão começando a fechar tudo.\""
"Mas Cameron olha para ele antes de sorrir."
show cam smirk c evening at right with dissolve
c "\"Ah não, {w=0.3}isso é algo que você quis fazer por anos.\""
show cam smile evening with dis
c "\"Quero dizer, me fode por jogar tudo isso em você LOGO antes de chegarmos lá, mas você sabe que eu sou um procrastinador.\""
c "\"Eu não quero que você se sinta culpado, mas só esteja ciente.\""
c "\"E eu meio que quero enfrentar meus medos de certa forma, sabe? Estou pronto para isso.\""
hide cam with dissolve
play sound cardoor
"E antes que Devon possa dizer qualquer outra coisa, Cameron entra."
show dev embarrassed evening with dis
"Dev olha para o lago, realmente não sabendo o que está prestes a fazer."
"Se ele fosse um bom namorado, ele iria embora desse lugar."
"Cameron gritaria, xingaria e reclamaria que levou dez horas para chegar lá."
"E Devon o calaria com uma daquelas abominações açucaradas do Starbucks."
"E ele nunca mais falaria sobre Echo."
"Ele ouviria Cameron e confiaria nele sobre como realmente era ver coisas horríveis."
"Eles se mudariam, se casariam, teriam uma casa grande, e mais cedo ou mais tarde, Dev teria sua resposta, porque todos têm no final."
hide dev with dissolve
"Quando saem do estacionamento, ele acha que tomou sua decisão."
"Mas mesmo que ele diga a si mesmo que vai virar à esquerda, de volta à estrada de onde vieram--"
"Ele vira à direita."
stop ambient fadeout 3.0
"Porque logo antes de fazer isso, ele vê um flash de rosa em sua mente, flutuando no meio de um lago, e é como se alguém o tivesse atingido com força total no peito."
"Antes que ele perceba, Echo está à frente deles."
window hide
pause 0.5
scene black with medium_dissolve
pause 1.0
play ambient desertmorning fadein 6.0
scene bg motel_afternoon with medium_dissolve
pause 0.5
window show
"Devon franze a testa quando entram no estacionamento do motel, olhando para as paredes cobertas de grafite."
"As caricaturas cartunizadas têm uma forma de baratear essa experiência, como se isso fosse apenas uma atração de casa mal-assombrada estúpida."
stop ambient fadeout 10.0
play music2 monochrome volume 0
play music monochromeintro fadein 3.0 volume 0.3
queue music monochromeloop volume 0.3
$ renpy.music.set_volume(0.5, delay=3, channel=u'background')
show cam worried a sunset at right with dissolve
c "\"Então essa é a 'base', hein?\""
"Devon esfrega a parte de trás da cabeça, sentindo-se autoconsciente depois de falar tanto sobre esse lugar."
show dev worried p sunset at left with dissolve
d "\"Não parecia {i}tão{/i} ruim nas fotos.\""
show dev upset p sunset with dis
d "\"As pessoas nunca têm respeito por coisas assim.\""
show cam smile a l sunset with dis
c "\"Eu não acho que parece ruim. Eu amo arte de rua assim.\""
show cam smile c l sunset with dis
c "\"E isso só me faz sentir menos sozinho, como se muitas pessoas tivessem estado aqui e ficado bem.\""
show dev annoyed p sunset with dis
d "\"Na verdade, fique de olho caso um deles esteja por aí.\""
show cam serious a l sunset with dis
c "\"Todos os grafiteiros que eu conheci eram muito legais.\""
show dev serious h sunset with dis
d "\"Não é {i}legal{/i} fazer isso em um lugar onde um monte de pessoas foram mortas.\""
show cam smirk c sunset with dis
c "\"Bem, muita gente desaprovaria o que {i}nós{/i} estamos fazendo, e eu sei que {i}você{/i} é legal.\""
show cam smile talking c sunset with dis
c "\"Então só.{cps=3}..{/cps}{w=0.4} relaxa um pouco.\""
hide cam with dissolve
play sound slap
show dev shocked h sunset at jumping
d "\"Ai! {w=0.3}Poxa...\""
"Cameron passa pelo urso, dando um tapa forte em sua bunda enquanto passa."
show dev skeptical p sunset with dis
"Devon levanta uma sobrancelha, sem saber o que fazer com o alto astral de Cameron."
"Eles acabaram de ter uma das conversas mais pesadas de seu relacionamento e..."
show dev h sunset with dis
"{i}...Bem, talvez seja{/i} por isso."
"Se Cameron estava se sentindo mais confortável sendo honesto e aberto com Dev, então isso só poderia ser uma coisa boa na mente do urso."
hide dev with dissolve
"Depois de devolver um tapa muito mais forte que faz Cameron gritar, o urso se junta a ele para explorar a área."
"Considerando que o motel é supostamente o prédio mais assombrado de Echo, Dev achou que seria uma boa ideia montar a base lá."
"Especificamente no quarto 12, mas a maioria dos números está faltando, e a maioria das portas metálicas pesadas está trancada."
"Mesmo que todas estejam amassadas pelo que parece ser o resultado de literalmente aríetes."
show dev upset h sunset at left with dissolve
d "\"Bem, eles parecem se importar muito em fechar o lugar.\""
show cam smile a l sunset at right with dissolve
c "\"Eles provavelmente se cansaram de idiotas entrando e se machucando.\""
show dev grin h sunset with dis
d "\"Sim, mas por sorte eu não sou um idiota.\""
show cam smile c l sunset with dis
c "\"Ei, e eu?\""
show dev smirk p sunset with dis
d "\"Bem, não acho que um diploma em música vai nos ajudar nessa situação, mas você ainda é bem inteligente.\""
show cam unamused c sunset with dis
".{cps=2}..{w=0.7}{nw}"
show cam confused c sunset with dis
c "\"Ah merda, {w=0.3}é verdade! {w=0.4}Você se formou em engenharia mecânica e trabalha na empresa de automação industrial mais valiosa do país.\""
show dev worried h sunset with dis
d "\"Heh, sim.\""
"Devon fica um pouco surpreso com o quão fria foi a resposta de Cameron."
show cam unamused c sunset with dis
c "\"Bem, {w=0.3}vai lá. {w=0.3}Suas aulas de dinâmica e física baseada em cálculo devem resolver isso para nós.\""
"A voz de Cameron está cheia de sarcasmo, e Dev só pode assumir que ele está tirando sarro do jeito que o urso tentou impressioná-lo com seu curso durante seus primeiros encontros."
"Mas Devon tenta salvar o clima anterior, de boa vontade."
show dev grin h sunset with dis
d "\"Bem, eu provavelmente poderia quebrar essas tábuas desde que eu mova meu punho em alta velocidade. Veja, a quantidade de energia cinética--\""
window hide
stop music2
stop music fadeout 10.0
pause 0.5
$ renpy.music.set_volume(1.0, delay=10, channel=u'background')
hide cam with dissolve
pause 1.0
show dev disappointed sunset with dis
window hide
pause 0.5
window show
play background desertmorning fadein 10.0
"O meio coração de Devon em provocar diminui."
"Ele nunca gostou muito do desdém que seus colegas de STEM tinham pelas artes e ciências sociais."
"É só que isso deixava Cameron irritado, e isso era engraçado--"
"--na faculdade."
"Agora Devon só se sente um idiota."
"Além disso, a habilidade de Cameron de entender e tocar música é basicamente mágica para o urso. O entendimento de Devon sobre música é superficial, e ele é um pouco surdo para tons também."
"Cameron nunca apontaria isso, ele só cantaria junto e tentaria harmonizar."
"E enquanto Devon foi oferecido seu emprego de seis dígitos antes mesmo de se formar, ele viu os sonhos de Cameron de trabalhar na indústria da música evaporarem lentamente nos últimos três anos."
"Agora Cameron está trabalhando em um call center que ele odeia."
show dev embarrassed sunset with dis
"O urso pensou que era tão inteligente na faculdade, e sim, ele se saiu bem--"
"--mas agora ele está se tornando mais consciente do quão idiota ele é quando se trata de se comunicar com {i}pessoas{/i} de verdade, com seu próprio namorado."
"Ele precisa se desculpar por essa."
"O urso limpa a garganta."
show dev grin p sunset with dis
d "\"Ei, Cam.\""
"Dev se aproxima do coiote, mas antes que ele possa dizer qualquer coisa, Cameron apenas aponta para uma porta."
show cam smile a sunset at right with dissolve
c "\"Viu? Número 8. E a porta ali é o número 3.\""
c "\"Então, contando nessa direção--\""
"A postura fria de Cameron desapareceu completamente."
show dev skeptical p sunset with dis
c "\"Dez, onze, e quarto número 12. E olha só, está aberto!\""
show dev happy sunset at left with dis
d "\"Ah, legal!\""
show cam grinning c l sunset with dis
c "\"Obrigado, eu fui para a faculdade.\""
show dev smirk p sunset with dis
d "\"Ha-ha.\""
show dev skeptical p sunset with dis
d "\"Agora, eu vou entrar primeiro para ter certeza de que está tudo limpo.\""
show cam unamused a sunset with dis
c "\"De quê?\""
d "\"Sei lá, {w=0.3}ocupantes ilegais?\""
show cam serious c l sunset with dis
c "\"Bem, prepare-se para encontrar um ocupante ilegal morto porque como diabos eles sobreviveriam?\""
show dev surprised h sunset with dis
d "\"Na verdade, você me lembrou que há alguns creeps que moram aqui, como moradores teimosos que não vão embora. Pelo menos foi o que um post disse de uns dois anos atrás.\""
show cam worried a sunset with dis
c "\"O quê? Eu não gosto disso. Eles são perigosos?\""
d "\"Pelo que eu entendi, eles são mais do tipo 'saia do meu quintal' de creeps.\""
c "\"Esse tipo ainda pode ser perigoso.\""
show dev p sunset with dis
d "\"Se ninguém foi morto por eles ainda, então acho que estamos bem, mas como eu disse: eu vou cuidar de você.\""
"Dev solta um rosnado falso."
show dev angry sunset with dis
d "\"Vou torná-los residentes PERMANENTES de Echo... e com isso quero dizer mortos!\""
c "\"Devon...\""
"Agora Devon pode dizer que o coiote realmente está chateado."
show dev surprised h sunset with dis
d "\"O que foi, amor?\""
show cam sad sunset with dis
c "\"Você me disse que ninguém morava aqui. Você disse isso várias vezes.\""
show dev shocked h sunset with dis
d "\"Cameron, apareceu tão poucas vezes no fórum, e as postagens que eu lembro eram bem mundanas. Eu honestamente só esqueci.\""
show cam disappointed sunset with dis
c "\"Tá bom.\""
"Devon olha para o coiote, esperando, mas ele não diz nada."
show dev surprised p sunset with dis
d "\"Cameron.{cps=3}..{/cps}{w=0.4} Tem algo que você quer me dizer?{w=0.3} Se tiver, eu ainda espero que você seja aberto como você disse--\""
show cam frustrated sunset with dis
c "\"Aff! {w=0.3}Eu sei.\""
show dev scared sunset with dis
d "\"Ei, está tudo bem, cara! Não é como se eu estivesse esperando que você compartilhasse tudo em sua mente agora, mas eu estou aqui para ouvir se você quiser falar.\""
show cam sad sunset with dis
c "\"É só.{cps=3}..{/cps}{w=0.4} difícil de explicar.\""
c "\"Acho que o fato de que há pessoas reais ainda morando aqui deixa um pouco mais assustador.\""
show dev worried p sunset with dis
d "\"Tem a ver com os sonhos que você estava tendo?\""
"Dev observa Cameron de perto, mas ele parece genuinamente confuso."
show cam worried a sunset with dis
c "\"Mais ou menos, mas eles eram estranhos. Eu não acho que eles realmente significavam alguma coisa.\""
show cam smile sunset with dis
c "\"Sim, eu só estou exagerando. Eu só realmente não quero ter a experiência de {i}Deliverance{/i} além dos fantasmas, sabe?\""
show dev p sunset with dis
d "\"Eu entendo, e não há nada de errado em ser vigilante.\""
d "\"Meu amigo de Southland, aquele da cidade ainda mais assombrada que Echo--\""
d "\"--ele diz que algo horrível acontece entre um mochileiro e um caipira do interior a cada dois anos, mais ou menos.\""
show cam serious c sunset with dis
c "\"Que confortante.\""
d "\"Mas enquanto eu estava meio brincando antes, se alguém tentar alguma coisa, eu {i}vou{/i} fazer o que for preciso para impedi-los.\""
"Dev não conta a Cameron que naquele momento, ele meio que deseja ter ido em frente e comprado uma arma para proteção."
"Se esses homens ainda estão por aí, o urso não tem dúvidas de que eles têm muitas armas."
c "\"Bem, não vamos pensar nisso porque não vai acontecer.\""
show cam smirk c l sunset with dis
c "\"A menos que eles estejam ocupando aquele quarto.\""
show dev angry sunset with dis
d "\"Não por muito tempo!\""
window hide
pause 0.5
stop background fadeout 5.0
play sound doorsqueak
scene bg motel_room_disarray with medium_dissolve
pause 1.0
window show
"O exagero de bravata do urso se torna genuinamente cauteloso quando ele abre a porta."
"O quarto está mais quente do que lá fora, como se estivesse ampliando e prendendo o calor."
show dev h dark3 at left with dissolve
play music roadsideintro fadein 3.0 volume 0.3
queue music roadsideloop volume 0.3
d "\"Ok.{cps=3}..{/cps}{w=0.4} Ok, {w=0.3}sim, {w=0.3}isso é viável.\""
d "\"Ei, Cam! {w=0.3}Tudo limpo!\""
show cam happy eyes dark3 at right with dissolve
c "\"Ah, nenhum caipira assassino no--\""
show cam shocked dark3 at jumping
c "\"Ah, {w=0.3}que nojo!\""
show dev surprised h dark3 with dis
d "\"O que você esperava? Só precisamos arrumar um pouco. Olha, até tem um colchão ali.\""
show cam scared dark3 with dis
c "\"Espera, não vamos usar isso para dormir, ou algo assim, vamos?\""
show dev smirk p dark3 with dis
d "\"Por que você acha que eu trouxe lençóis?\""
show cam disgusted dark3 with dis
c "\"Ah, eu NÃO vou dormir em--\""
d "\"Brincadeira, brincadeira. Isso é só para cobrirmos os lugares nojentos onde podemos sentar. Eu já te disse que reservei um quarto em Payton.\""
c "\"E é melhor usarmos, não importa o quão animado você fique.\""
show dev h dark3 with dis
d "\"Claro, mas podemos pelo menos deixar esse lugar o mais confortável possível.\""
"Cameron fica quieto e Dev vira para vê-lo olhando para uma série de pregos enferrujados no chão ao redor da janela e do colchão."
show cam serious c dark3 with dis
c "\"Sua vacina antitetânica está em dia, né?\""
show dev surprised h dark3 with dis
d "\"Ótima pergunta.\""
show cam disgusted dark3 with dis
stop music fadeout 7.0
c "\"Sim, ótimo. Só não se fure em nada. Vou tentar limpar pelo menos isso, junto com todas as outras coisas afiadas e enferrujadas nesse chão.\""
window hide
pause 0.5
scene black with medium_dissolve
play background crickets fadein 3.0
scene bg motel_room_night_light with medium_dissolve
pause 0.5
window show
"Cameron observa Dev recuar, esfregando as patas uma na outra ruidosamente."
show dev p lamp at left with dissolve
d "\"Bem, eu diria que está bem aconchegante, não acha?\""
show cam smile a lamp at right with dissolve
c "\"Já vi casas reais que parecem piores, então sim, eu diria que sim.\""
show cam worried a lamp with dis
"Cameron olha para o sofá e senta devagar na borda, não confiando muito nele apesar do lençol."
show dev happy lamp with dis
d "\"Então! {w=0.4}O que você sabe sobre investigação paranormal? Você disse que pesquisou?\""
show cam smile talking c lamp with dis
c "\"Acontece que você só corre por aí com uma lanterna e chama o fantasma de filho da puta.\""
show dev serious h lamp with dis
d "\"Boa.\""
show cam grinning c lamp with dis
c "\"Poxa, desculpa. Não sabia que as caças fantasmas da TV eram um ponto tão sensível para você.\""
show dev worried p lamp with dis
d "\"Elas arruinaram sozinhas a credibilidade de investigações {i}de verdade{/i}.\""
show cam smile a lamp with dis
c "\"Bem, elas trouxeram mais atenção, certo? Enfim, tudo o que eu realmente sei é o que você faz: coisas de EVP, tirar fotos, só sentar e esperar. Coisas assim.\""
show dev h lamp with dis
d "\"É um começo.\""
show cam surprised c lamp with dis
c "\"Na verdade, eu estava pensando que você lidaria com a maior parte disso, então o que eu pesquisei principalmente tinha a ver com aqueles que são... dotados.\""
"É quase fisicamente impossível para o coiote usar essa palavra para descrever pessoas como ele."
show dev grin h lamp with dis
d "\"Ah sim! Eu queria dizer antes como fiquei feliz que você olhou aquele fórum.\""
d "\"Deve ser irritante só me ouvir falar sobre isso quando eu nem mesmo experimento.\""
show cam worried a lamp with dis
c "\"Não, você está bem, Dev.\""
"Na verdade, Cameron preferia muito mais ouvir de Dev."
"Metade das pessoas nos fóruns eram claramente mentirosas com um complexo de salvador--"
"--e a outra metade estava entrando em contato com esses idiotas para se comunicar com um ente querido morto."
"Cameron não conseguia suportar e acabou olhando um blog que parecia um pouco mais legítimo."
show dev happy lamp with dis
d "\"Então o que você descobriu?\""
"O jeito que o urso está animado agora que estão falando sobre investigação lembra Cameron que ele precisa pelo menos tentar."
show cam confused a lamp with dis
c "\"Bem, de acordo com esses psíquicos, é bem simples se você tem o sentido extra.\""
c "\"Primeiro, aproxime-se do local com intenções claras. Eu estou aqui para ver ou ouvir algo do passado.\""
c "\"Segundo, mantenha a mente aberta, o que é algo que eu prometo fazer.\""
show cam serious a l lamp with dis
c "\"E finalmente, se você sentir que a presença é hostil, lembre-se sempre que ela {i}pode{/I} te machucar. Nesses casos, pode nem ter sido uma pessoa de verdade.\""
show dev annoyed p lamp with dis
d "\"Eh, eu não me preocuparia com coisas demoníacas. Até eu tenho dificuldade em acreditar nisso.\""
show cam smile a l lamp with dis
c "\"Ei, há algo em que podemos concordar! Agora, vou chutar aqui e assumir que algo terrível aconteceu nesse quarto?\""
show dev worried h lamp with dis
d "\"Hmm...\""
show cam smile c l lamp with dis
c "\"Por que mais procurar um quarto específico, né? Eu não quero que você me diga o que aconteceu, mas também acho que isso é meio que um teste?\""
d "\"Bem, eu não quero chamar de teste. Eu vou estar gravando e procurando por... a coisa que aconteceu nesse quarto também.\""
show dev surprised h lamp with dis
d "\"Só pensei que você poderia querer ver se sente algo e comparar com o que realmente aconteceu.\""
c "\"Acho que é uma boa ideia. Eu só vou fazer um 'toque leve', acho que chamam assim. Então eu não vou ver nada, mas só sentir o que pode ter acontecido.\""
show dev confused talking p lamp with dis
d "\"Mas me avise se você sentir que as coisas não estão certas, claro.\""
show cam smile c l lamp with dis
c "\"Eu vou ficar bem.\""
show dev happy eyes lamp with dis
d "\"Tá bom, vou começar. Não vamos ficar até muito tarde hoje. Só queremos sentir o clima.\""
show cam surprised a lamp with dis
c "\"Claro. Eu vou, uh, começar abrindo minha mente e deixando minhas intenções claras.\""
show dev grin h lamp with dis
d "\"Ok, amor. Eu te amo.\""
hide cam
hide dev
with dissolve
"Devon se inclina e beija Cameron na cabeça."
"Então Cameron observa enquanto Dev desliga a lanterna, mergulhando-os na escuridão."
window hide
pause 0.5
scene black with medium_dissolve
scene bg motel_room_night with medium_dissolve
pause 0.5
window show
"Carregar equipamentos enquanto tenta ficar quieto rapidamente deixa Devon suando através da camisa."
"Ele nem tinha pensado no calor, mesmo quando Cameron estava reclamando, mas sua camisa estava colada em seu pelo, e ele teve que tirá-la."
"Ele está fazendo um esforço extra para não perturbar o coiote porque Cameron parece estar realmente tentando, seus olhos fechados e orelhas erguidas."
"Devon nem precisou pedir para ele tirar o telefone para gravar o áudio."
"Ele simplesmente fez, e para Devon, isso só prova o quanto Cameron quer fazer isso."
"Enquanto Devon mexe em seus equipamentos, Cameron se mexe e murmura algo."
"Dev se anima."
show dev surprised s dark at left with dissolve
d "\"Ei, querido, estou aqui. Você está bem?\""
c "\"Eu preciso... ficar mais confortável.\""
"Ao mesmo tempo que se ajusta para que seus pés fiquem na mala à sua frente."
d "\"T--Tá bom...\""
show dev embarrassed s dark with dis
"Algo no comportamento de Cameron está incomodando Devon."
"E as palavras de Cameron estavam um pouco arrastadas, e ele parece meio que... não muito presente."
"Ele deveria tirá-lo disso?"
"Devon nunca tinha visto um psíquico em ação antes, então talvez isso seja normal, como um transe."
"Ele espera que seja normal, porque mesmo que Devon possa encontrar suas respostas, ele as abandonaria para Cameron descobrir que não é \"psicótico\"."
"Enquanto mexe com seu sensor EMF, um pavor repentino agarra seu peito."
show dev disappointed s dark with dis
"E se o oposto acontecesse, e Cam realmente... perdesse a cabeça?"
"Como quando sua mãe teve psicose?"
"SE isso acontecer, Devon só agora está percebendo que ele seria responsável, e como Cameron poderia perdoá-lo por isso?"
"Como ele poderia se perdoar?"
show dev frustrated s dark with dis
d "\"Merda...\""
"Dev resmunga baixinho."
"Que {i}porra{/i} ele está fazendo, trazendo seu namorado para esse quarto, onde {i}aquilo{/i} aconteceu?"
"Ele geralmente estava sozinho, ou com amigos quando fazia essas investigações, e seu desejo de ver algo sempre superava o medo."
"Ele só assumiu que Cam estaria acostumado com coisas assustadoras, especialmente depois que descreveu aquela criatura de rosto achatado em uma capa de chuva que ele via desde criança."
"Ele apenas assumiu."
show dev disappointed s dark with dis
"Por que só agora ele está percebendo quais podem ser as consequências?"
"Bem, é porque as coisas que Cameron lhe contou no lago mudaram muitas coisas na mente do urso."
"Isso não é algo que um parceiro amoroso faz com outro parceiro."
"Ele está {i}usando{/i} Cameron por seus próprios motivos egoístas."
"Devon sabe que o coiote tem algum tipo de habilidades ESP, mas isso não significa que ele também não tenha outros problemas que possam ferrar com ele."
"Isso não significa que possivelmente ver essas coisas horríveis não {i}causaria{/i} ele a desenvolver mais problemas."
hide dev with dissolve
stop background fadeout 5.0
"Todo o vento tirado de suas velas, Devon olha para o chão, pensando."
"Então ele se levanta e anda um pouco, começando a se decidir, decidindo que logo depois disso, eles terminam, não importa o quê."
"O urso olha para o armário, aquele onde um lobo do conselho tribal Meseta se enforcou no início dos anos 90."
"Se ele pudesse ver uma coisa, apenas um vislumbre de prova de que ela está bem do outro lado, ele ficaria em paz com tudo isso."
"Realmente, o maior obstáculo à frente dele é a vergonha de abandonar seus planos e descobrir como dizer a Cameron o porquê."
"Dev solta um suspiro trêmulo, parado no armário, olhando para aquela barra, se perguntando se é a mesma que o lobo usou..."
play music2 looming volume 0
play music loomingintro fadein 10.0 volume 0.3
queue music loomingloop volume 0.3
"Devon sente algo."
"Não algo bom."
"Um calafrio sobe por sua espinha, e de repente ele está tremendo."
d "\"{cps=20}Não é possível.\""
"É.{cps=3}..{/cps}{w=0.5} Está realmente acontecendo."
d "\"{cps=20}Caralho... {w=0.5}Caralho...\""
"É tudo o que ele consegue dizer."
"Está acontecendo, {w=0.4}mas parece tão.{cps=3}..{/cps}{w=0.4} {i}errado{/i}."
"Então um medo que ele nunca conheceu antes toma conta."
"Ele quer se virar."
"Ele quer chamar por Cameron, mas é como se algo estivesse em volta de seu pescoço, mantendo-o no lugar."
"E então ele ouve um som terrível atrás dele..."
window hide
pause 0.5
scene bg black with medium_dissolve
pause 0.5
window show
"Cameron sabe que algo está acontecendo com certeza."
"É assustador, mas ao mesmo tempo, está fazendo ele questionar o que sempre acreditou."
"Devon estava certo sobre essas coisas?"
"Ele simplesmente se entendeu mal por tanto tempo?"
"Ele podia sentir {i}alguém{/i}, nada como os monstros que ele tinha visto no passado."
"Em vez disso, era um homem, de terno com uma gravata bolo."
"Ele estava triste, {w=0.5}estava com raiva, {w=0.5}e estava aterrorizado."
"Cameron sabia que isso era frequentemente o que psíquicos descreviam quando falavam sobre \"sentir\" pessoas do passado."
"Você sente o momento mais intenso delas na vida, esse homem, esse lobo, ele vai fazer algo terrível."
"E enquanto Cameron está maravilhado com isso, o lobo de repente... muda."
"Ao mesmo tempo, Cameron sente seu foco virar para ele."
"Isso faz o coiote pausar, porque agora essa presença estava tentando interagir com {i}ele{/i}."
"Isso está certo?"
"Cameron acha que pode estar, mas algo não parece certo sobre isso, como se isso não fosse o que ele pensa que é."
"Mas ele supõe que qualquer pessoa fazendo isso pela primeira vez se sentiria estranha."
"Talvez ele estivesse fazendo o \"toque leve\" errado; o ponto é ouvir o passado, como uma gravação."
"Essa comunicação direta está assustando o coiote, mas essa poderia ser sua chance de responder a pergunta de Dev, e sua própria pergunta também."
pause 1.0
centertext "{i}{cps=60}Desculpe incomodá-lo. {w=0.6}O que há após a morte?\n {w=0.4}Para onde vamos?{/i}"
pause 1.0
stop music2
stop music fadeout 5.0
play ambient wind2 fadein 3.0
"Parece estúpido e desajeitado, mas é tudo que vem à sua mente, então Cameron pergunta isso repetidamente."
"Há uma longa pausa vazia."
play sound cackle volume 0.4
"E então algo como uma gargalhada."
play sound2 cackle volume 0.4
"Quase parece falsa, como um brinquedo de Halloween, mas é sombria, maldosa e está tirando sarro dele."
play sound cackleloud volume 0.4
"Todos os sentimentos de maravilha e esperança por um avanço são esvaziados instantaneamente."
"Ele precisa de Dev, ele precisa abrir os olhos..."
window hide
scene closet_blurry with medium_dissolve
pause 1.0
window show
"Os olhos de Cameron estão pesados, e ele mal consegue focar."
"Algo deu terrivelmente errado."
"Essa presença é má, {w=0.4}maliciosa, {w=0.4}isso não é uma pessoa."
"Agora, tudo o que o coiote pode sentir é que uma tragédia profunda acabou de acontecer."
"Ele precisa de Devon, e acha que o vê quando sua visão começa a focar lentamente."
window hide
pause 1.0
scene closet_1 with medium_dissolve
pause 1.0
play music2 closet volume 0
play music closetintro fadein 3.0 volume 0.3
queue music closetloop volume 0.3
pause 1.0
window show
".{cps=1}..{/cps}{w=1.0}{nw}"
"A princípio, Cameron não entende o que está vendo."
"Como Dev está em pé daquele jeito?"
"Por que ele não está se mexendo?"
"Ele percebe o porquê nos próximos segundos."
"A forma não natural como o peso de Dev parece puxar para cima em seu pescoço diz tudo."
"Cameron começa a gritar, mas é fraco, abafado, mal um sussurro de sua garganta... e ele não consegue se mover."
"Paralisia."
"Isso não é real!"
"Isso é paralisia do sono... mas algo sobre isso é tão fodido, tão real, e ele não podia ter adormecido, ele está quase certo disso."
"Mas mesmo que ele tivesse, seu namorado poderia realmente estar se enforcando enquanto o coiote fica inutilmente no sofá."
"O terror começa a engoli-lo."
"Como isso pôde acontecer?"
stop music2
stop music fadeout 5.0
"Como ele pôde fazer isso!?"
scene closet_2 with dis
play background mobile
".{cps=1}..{/cps}{w=1.0}{nw}"
"Como?"
"Cameron tenta gritar de novo, mas novamente é apenas um sussurro de respiração."
"Ele olha para a foto de contato de Devon, em vez de Devon morto no armário."
"Eles tiraram essa foto na faculdade, cinco anos atrás e apenas um mês em seu relacionamento."
"Na época, era um símbolo para mostrar a seus outros amigos gays, para provar que ele tinha um namorado, e que ele era um urso bonito."
"E ele nunca mudou, mesmo que não tivesse mais ninguém para mostrar."
"Como diabos eles acabaram aqui?"
scene closet_3 with dis
stop background
"O telefone atende e muda para o viva-voz automaticamente."
"Cameron sabe no fundo que isso deve ser um sonho, mas Devon ainda está pendurado no armário."
"E ele é dominado pelo horror de que isso pode ser apenas um sonho parcial, e que a pior parte dele é real."
"Isso faz Cameron tentar e falhar em gritar novamente."
play background radiostatic fadein 3.0
unk "\”{cps=20}...Você{w=0.3}...queria...{w=0.4}saber...{w=0.5}como?\""
"Cameron olha para o telefone, incapaz de entender através do estático, mas capaz de reconhecer a voz."
d "\"Você disse.{cps=4}..{/cps} {w=0.5}que queria saber como.{cps=4}..{/cps} {w=0.5}é morrer?\""
d "\"Eu diria.{cps=3}..{/cps}{w=0.4} que é como afogar para sempre.\""
d "\"Consciente para sempre enquanto você sufoca pelo que te fez feliz quando estava vivo.\""
d "\"Mas então, {w=0.4}VOCÊ não acredita em nada,{w=0.4} então o que você realmente quer saber é como é desaparecer.\""
d "\"Porque você está com medo.\""
d "\"Você diz a si mesmo que quer morrer, que deseja que sua mãe não tivesse salvado sua vida inútil, que você mereceria.\""
d "\"Agora você diz a si mesmo que se não fosse por mim, você teria acabado com tudo na faculdade.\""
d "\"Nós dois sabemos que isso é mentira, porque você é um covarde.\""
d "\"Você vai ficar vivo o máximo que puder estar com alguém que pode te manter vivo.\""
d "\"Eu poderia ter te tratado como um lixo absoluto nos últimos cinco anos e você ainda estaria por aí hoje.\""
d "\"Você {i}implorou{/i} para Dylan não te deixar, apenas semanas depois que ele te deu um soco e deixou aquela cicatriz. Aquela que você disse que ganhou caindo em um armário. Você está doente.\""
d "\"Enquanto isso, você {i}deixou{/i} eu te colocar nessa situação. Você disse que {i}queria{/i}. Você ainda quer?\""
"{i}Não, {w=0.2}não, {w=0.2}não, {w=0.3}por favor Deus, {w=0.3}NÃO!{/i}"
"Cameron não consegue nem mover os lábios."
d "\"Enfim, estou me desviando um pouco, não estou? Você queria saber como é a vida após a morte? Vou te dar uma ideia.\""
"A voz de Devon fica mais abafada."
d "\"Ei, {w=0.3}Lupita! {w=0.3}Diga ao meu namorado como é.\""
stop background fadeout 5.0
"Fica quieto por um momento, e Cameron apenas senta em miséria atordoada, apenas esperando."
play sound staticscream
stop ambient
show bs
"Um grito terrível e demoníaco ecoa pelo telefone e o pelo de Cameron se eriça por todo o corpo, e ele luta contra essa prisão em que está com tudo o que tem." with vpunch
"E finalmente se liberta."
window hide
#ADD AMBIENCE?
pause 1.0
scene bg motel_room_night with medium_dissolve:
    zoom 1.02
    xalign 0.5
    yalign 0.5
pause 1.0
window show
"Leva um momento para Devon perceber que o som terrível está vindo de Cameron."
"Ele nunca o ouviu fazer um som assim antes."
"Naquele momento, o que quer que esteja segurando o urso se dissolve e Devon se vira, ofegando."
"Quando Dev olha para ele, vê que os olhos de Cameron estão bem abertos."
show dev scared s dark at left with dissolve
d "\"Cameron!?\""
"Cameron faz aquele som novamente."
"Embora Devon não tenha ideia do que Cameron está vendo, ele sabe que é algo terrível."
"Devon sente que está começando a entrar em pânico."
show dev angry s dark with dis
d "\"Amor, {w=0.3}por favor! {w=0.4}O que está acontecendo!?\""
"Cameron apenas olha de volta e Devon finalmente surta."
show dev angry yelling s dark
show cam horror dark at right
d "\"CAMERON!\"" with vpunch
"Devon está saindo do armário quando de repente Cameron pula do sofá, fazendo um som feral."
play music2 solace volume 0
play music solaceintro fadein 10.0 volume 0.3
queue music solaceloop volume 0.3
"O olhar nos olhos do coiote é tão intensamente diferente dele que Devon recua com medo."
show dev scared s dark with dis
d "\"Amor, {w=0.3}sou eu!\""
window hide None
hide dev
hide cam
play sound thud5
with vpunch
pause 0.5
window show
"Para o choque de Dev, as patas de Cameron voam para o pescoço do urso, mas em vez de apertar como ele acha que vai, elas arranham o pelo grosso lá."
show dev scared s dark at left with dissolve
d "\"Espera! {w=0.3}Pára!\""
"Devon consegue pegar as patas de Cameron em suas próprias patas muito maiores, facilmente contendo o macho menor."
show cam horror dark at right with dissolve
"Cameron continua olhando para o pescoço de Devon, parecendo procurar intensamente, então ele olha para o rosto de Dev."
show cam terror dark with dis
c "\"Eu vi você morto. Você me ligou e gritou comigo.\""
"Embora Devon não entenda, ele pode dizer que isso não foi um dos típicos terrores noturnos de Cameron."
"A expressão em seu rosto diz tudo."
show dev frustrated s dark with dis
d "\"Merda!\""
show dev tears s dark with dis
d "\"Eu sinto muito, muito mesmo. Estou te levando para Payton agora, ou para qualquer lugar que você quiser ir.\""
"Mas quando Devon tenta puxá-lo para a porta, Cameron resiste."
show cam horror dark with dis
c "\"Espera, {w=0.3}espera. {w=0.5}Só me deixa recuperar o fôlego, {w=0.3}ok?\""
d "\"Ok, ok. Só respira fundo, ok?\""
show cam crying dark:
    choice:
        pause 0.1
    choice:
        easeout_back 0.1 xoffset -5
        easein_bounce 0.1 xoffset 0
    choice:
        pass
    pause 0.5
    repeat
with dis
hide dev with dis
"Devon mexe com a lanterna até ligá-la."
window hide
pause 0.5
scene motel_room_night_light:
    zoom 1.02
    xalign 0.5
    yalign 0.5
show cam crying lamp at right:
    yalign 0.0
    choice:
        pause 0.1
    choice:
        easeout_back 0.1 xoffset -5
        easein_bounce 0.1 xoffset 0
    choice:
        pass
    pause 0.5
    repeat
with dis
pause 1.0
show dev disappointed s lamp at left behind cam with dis
pause 0.5
window show
"Então ele fica ao lado de Cameron por alguns momentos, ouvindo-o soluçar."
show dev embarrassed s lamp with dis
d "\"Posso pelo menos te abraçar.{cps=3}..{/cps}{w=0.4} por favor?\""
hide cam with dissolve
show cam crying lamp at center:
    yalign 0.0
    choice:
        pause 0.1
    choice:
        easeout_back 0.1 xoffset -5
        easein_bounce 0.1 xoffset 0
    choice:
        pass
    pause 0.5
    repeat
with dis
"Cameron se inclina para ele como resposta."
"Enquanto Dev acaricia sua cabeça, Cameron começa a esfregar suas costas, como se soubesse que Dev também estava aterrorizado."
show cam heartbreak lamp at center with dis
c "\"Estou bem. {w=0.5}Foi só uma.{cps=3}..{/cps}{w=0.3} visão muito intensa.\""
show dev disappointed s lamp with dis
d "\"Sinto muito. Nunca te vi assim antes. Você me assustou pra caramba.\""
d "\"Você.{cps=3}..{/cps}{w=0.4} achou que eu estava te atacando?\""
c "\"Hã?\""
d "\"Você estava indo atrás do meu pescoço, meio que.\""
c "\"Ah, não, eu uh, eu vi você pendurado no armário--\""
show cam crying lamp with dis
"A respiração de Cameron engasga em seu peito."
c "\"Tipo, pelo pescoço.\""
show dev surprised s lamp with dis
d "\"Ah merda...\""
c "\"Sim, e foi tão real pra caralho.\""
show dev embarrassed s lamp with dis
"Eles se abraçam em silêncio por um tempo, Devon refletindo sobre o que Cameron acabou de dizer."
show dev disappointed s lamp with dis
"Devon não tem mais dúvidas de que Cameron é psíquico, mas agora isso não importa."
"Ele só quer que o coiote se sinta seguro novamente."
show cam heartbreak lamp with dis
c "\"Devon?\""
show dev embarrassed s lamp with dis
d "\"Sim, amor?\""
c "\"Eu acho que você está certo.\""
d "\"Sobre o quê?\""
c "\"Algo aconteceu. Eu não sei se são fantasmas, ou--ou, qualquer outra coisa que poderia ter sido, mas isso não foi só eu.\""
c "\"Eu nunca senti ou vi coisas assim antes. Há mais nisso do que eu sendo louco.\""
c "\"Tem que haver...\""
show dev smirk h s lamp with dis
d "\"Podemos falar sobre isso quando estivermos em Payton, ok?\""
show cam terror lamp with dis
stop music2
stop music fadeout 10.0
c "\"Dev, eu prometi ser honesto com você, e preciso te contar algo agora senão provavelmente nunca vou.\""
show dev surprised s lamp with dis
d "\"O que é?\""
"O coração de Dev começa a bater mais forte quando ele vê a expressão no rosto de Cameron."
show cam heartbreak lamp with dis
c "\"Lupita estava nessa visão, Dev... Mas por favor acredite em mim quando digo que não acho que era realmente ela, mas...\""
show dev scared s lamp with dis
d "\"O quê!?\""
"Cameron hesita."
show dev surprised s lamp at left with dis
d "\"Cameron, {w=0.3}{i}por favor{/i} me diga.\""
show cam crying lamp with dis
c "\"Eu sinto muito, mas eu ouvi ela, e foi horrível e... Eu não sei, foi só um grito. Foi horrível.\""
scene black
show dev surprised s dark4 at left
with dis6
"O chão parece desaparecer sob Devon, e ele sente como se estivesse caindo em um abismo."
window hide
pause 1.0

jump a1s2