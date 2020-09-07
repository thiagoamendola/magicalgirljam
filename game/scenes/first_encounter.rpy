
define haikou = Character("Haikou", color="#ccc")
define sister = Character("Irmã de Haikou", color="#f00")
define teacher = Character("Professor", color="#00f")
define student = Character("Aluno", color="#888")
define zero = Character("Zero", color="#0f0")
define kyuren = Character("Kyuren", color="#ff0")
define shimei = Character("Shimei", color="#0ff")
define niven = Character("Niven", color="#f0f")
define surai = Character("Surai", color="#c7c")



label first_encounter:

    transform centerflip:
        xzoom -1
        xalign 0.5
        yalign 1.0
    
    transform rightflip:
        xzoom -1
        xalign 0.8
        yalign 1.0
    
    transform leftflip:
        xzoom -1
        xalign 0.2
        yalign 1.0
    
    transform farrightflip:
        xzoom -1
        xalign 0.95
        yalign 1.0

    transform closerrightflip:
        xzoom -1
        xalign 0.65
        yalign 1.0

    transform farright:
        xalign 0.95
        yalign 1.0

    transform closerright:
        xalign 0.65
        yalign 1.0

    scene bg quarto with fade

    "Céu azul, sol brilhando lá fora. Quarto escuro, bagunçado. Som de despertador tocando." # Cenario
    
    "Haikou encara o teto e esfrega os olhos."
    
    "Haikou suspira."

    show haikou infeliz with dissolve

    haikou "Eu vou me atrasar se eu não levantar logo, ai ai..." # resmungando

    "Haikou encara a pilha de roupas."

    "Haikou levanta, vai ao banheiro, lava o rosto, escova os dentes."

    "Haikou volta para o quarto e coloca seu uniforme escolar."

    scene bg cozinha with dissolve

    "Haikou desce às escadas, chegando na cozinha. Ele anda direto pra porta, pra sair da casa."

    show haikou infeliz at centerflip with dissolve

    sister "Você não quer comer nada?"

    show haikou irritado

    haikou "Não."

    sister "Tem certeza?"

    haikou "Sim."

    sister "Mas..."

    show haikou bravo

    haikou "{b}Estou atrasado, tenho que ir.{/b}" # Curto e grosso

    "Haikou abre a porta e sai da casa."

    scene bg escola with dissolve
    
    show haikou irritado at centerflip with dissolve

    "rua, calçada, pouco trânsito, o céu ainda azul e brilhante. Som de pássaros cantando." # Cenario

    haikou "Que droga..." # resmungando

    scene bg saladeaula with dissolve

    "portões da escola, corredor, sala de aula." #Cenario

    "sala de aula, com lousa, cadeiras, professor dando aula e alunos nas cadeiras." # Cenario

    show haikou pensativo at centerflip with dissolve

    "Haikou joga no celular com uma mão embaixo de sua mesa e copia umas poucas frases no caderno com a outra mão. Ele faz isso a aula toda."

    teacher "Então, quem pode me dizer as figuras de linguagem usadas pelo eu-lírico nesse poema?"

    student "Metáfora, hipérbole e comparação."

    teacher "E qual a diferença entre uma comparação e uma metáfora?"

    "Haikou solta um suspiro inaudível."

    show haikou infeliz at centerflip with dissolve

    "Haikou encara a lousa com olhos sonolentos e tediosos."

    "Algumas horas passam, finalmente é hora do almoço." # Sugestão: mostrar relógio da sala, mostrar alunos saindo da sala, para indicar passagem do tempo

    # "Dois colegas (Zero e Kyuren) vêm em direção a Haikou."

    show haikou infeliz at leftflip with dissolve

    show zero normal at closerright with dissolve
    
    show kyuren normal at farrightflip with dissolve

    zero "Haikou, vamos comer? O que você trouxe hoje?"

    show haikou preocupado at leftflip

    haikou "Ah… Eu esqueci de preparar, acordei atrasado."

    show kyuren infeliz at farrightflip
    show zero pensativo at closerright

    kyuren "De novo?! Olha, você não pode sempre contar com amigos que te dêem o almoço!"

    haikou "Eu sei, eu sei… Desculpa, Kyuren."

    kyuren "Eu vou te dar parte do meu almoço hoje, mas você realmente precisa resolver isso."

    show zero surpreso at closerright

    zero "Eu posso dar também, mas é como ele disse… Você tem que dar um jeito."

    show haikou pensativo at leftflip

    "Haikou suspira e balança a cabeça."

    "Os três saem da sala."

    scene bg escola with dissolve

    "pátio da escola, com bancos, uma fonte e árvores." # Cenario

    show haikou infeliz at leftflip
    show zero normal at closerright
    show kyuren normal at farrightflip
    with dissolve

    "Zero e Kyuren abrem seus almoços."

    "Zero e Kyuren colocam parte de seus almoços num pote para Haikou."

    "Os três sentam no banco, cada um começa a comer."

    "várias meninas e meninos andando pelo pátio e conversando." # Cenario

    # Obs: essa pequena conversa acontece mais ou menos do lado dos meninos, mas eles não participam dela

    hide haikou
    hide zero
    hide kyuren
    with dissolve

    show shimei normal at closerright with dissolve
    
    show niven normal at farrightflip with dissolve

    shimei "O céu hoje de madrugada tava diferente, eu juro!"

    niven "Mas isso não faz sentido, Shimei. Tem certeza que não tá precisando trocar seu óculos? "

    shimei "Eu sei o que eu vi! Eu vi as estrelas ficarem vermelhas! Eu tenho certeza!"

    hide shimei
    hide niven
    with dissolve

    show haikou pensativo at leftflip
    show zero normal at closerright
    show kyuren normal at farrightflip
    with dissolve

    "Haikou revira os olhos."

    show zero feliz at closerright
    show haikou infeliz at leftflip

    zero "Vocês estão sabendo da festa na casa da Irisha? É hoje à noite."
    
    show zero sorrindo at closerright
    show kyuren sorrindo at farrightflip

    kyuren "Sim, eu vou!"

    show haikou surpreso at leftflip 
    show kyuren normal at farrightflip
    
    haikou "Que horas vai ser?"

    show zero normal at closerright 

    zero "Começa às oito."

    haikou "E acaba...?"

    zero "Não sei... Essas festas costumam ir até de madrugada."

    show haikou maldoso at leftflip 

    haikou "Haja saco para ficar tanto tempo assim... O que as pessoas têm na cabeça?"

    show haikou infeliz at leftflip
    show zero triste at closerright
    
    zero "Você devia sair um pouco mais, Haikou. Você ia perceber que pode ser bem divertido."
    
    show haikou pensativo at leftflip
    show zero corado at closerright
    
    zero "Especialmente com as meninas… As amigas da Irisha são bem bonitas…" # expressão meio maliciosa

    show kyuren infeliz at farrightflip
    show haikou preocupado at leftflip
    show zero triste at closerright
    
    haikou "Não vejo graça nisso. Nenhuma delas falaria comigo, e eu não teria saco de falar com elas mesmo…"

    show haikou infeliz at leftflip
    show zero surpreso at closerright

    zero "O que tem de errado com você hoje?!" # irritado

    # kyuren, erguendo a mão e apontando com o indicador

    show kyuren bravo at farrightflip
    show zero triste at closerright

    kyuren "A pergunta certa não é \"o que tem de errado com o Haikou hoje\", Zero."
    kyuren "A pergunta certa é \"o que tem de errado com o Haikou\"."
    
    show haikou irritado at leftflip
    
    kyuren "Ele sempre foi assim. Um saco de pessoa."

    show haikou maldoso at leftflip

    haikou "E com quem você acha que eu aprendi?!" # irritado

    show haikou feliz at leftflip
    show zero sorrindo at closerright
    show kyuren sorrindo at farrightflip

    "Os três riem."

    # Indicar passagem do tempo de novo

    "corredor." # Cenario

    haikou "Ah, eu vou no banheiro. Podem ir na frente."

    zero "Beleza."
    kyuren "Beleza."

    "Zero e Kyuren andam até a sala."

    "Haikou vai até o banheiro. Entra numa das divisões, depois sai e vai para a pia lavar as mãos. Passa um pouco de água no rosto."

    "Mostrar espelho com ele e uma garota ao lado."

    "Haikou arregala os olhos."

    "Haikou vira a cabeça pro lado."

    haikou "Estranho, não ouvi passos." # pensamento

    haikou "O que você tá fazendo aqui?" # áspero

    surai "Procurando meninos, é claro!" # animada

    haikou "Eu não faço ideia do que você quer dizer com isso, mas enfim…"
    haikou "Meninas não devem entrar aqui, está indicado claramente na porta que esse banheiro é para os \"meninos\", você não viu?"

    surai "E por que você acha que um mero símbolo na porta significaria algo para mim?" # sorrindo

    haikou "Você tem algum problema? É mais do que óbvio que os banheiros são separados. Em que mundo você vive?!" # confuso e bravo

    surai "Alguém como eu certamente tem uma gama de problemas para lidar."

    haikou "Se algum professor ver, você vai levar bronca. Eu avisei…"

    "Haikou anda em direção à porta."

    surai "Quanta consideração… Tentar me poupar de broncas dos mortais." # rindo

    "Haikou revira os olhos e continua andando."

    "Ao tentar sair do banheiro, bate numa parede invisível."

    haikou "Ai!"

    surai "Não vá se machucar..." # rindo

    "Haikou toca no ar com cuidado, sentindo como se houvesse um vidro bem fino, mas bem resistente, ali."

    "Uma bola de fogo aparece ao lado da mão dele."

    surai "Nem se queimar..." # sussurrando provocativamente

    "A bola de fogo some."

    "Haikou vira de volta para Surai, surpreso."

    surai "Ora, não precisa ficar tão chocado assim! Eu sou capaz de fazer coisas muito mais grandiosas do que bolas de fogo, você quer ver?"

    surai "Bom, você não me deixa escolha… Vou ter que fazer o contrato com você mesmo!" # bufando

    haikou "Contrato? Quê?"

    surai "Sim! É isso que eu faço. Eu escolho jovens para conceder-lhes poderes e acompanhá-los em uma jornada de luta contra o mal."

    haikou "Isso parece coisa de videogame… Talvez minha família esteja certa, afinal." # sarcástico
    haikou "Jogar demais talvez seja ruim. Eu não fazia ideia de que jogar tanto poderia me dar alucinações desse nível…"

    surai "Ei, ei, você tá me escutando?!"

    surai "Você precisa aceitar o contrato."

    haikou "Que contrato?"

    surai "Eu acabei de falar! Você ganha poderes e, em troca, precisa lutar contra o mal."
    surai "Derrotar monstros, investigar… Vocês humanos são cheios de histórias e fantasias a respeito disso, isso devia ser familiar pra você, não?!"

    haikou "Eu não sou obrigado a aceitar, eu não quero me envolver com isso, agora pode por favor tirar a parede invisível pra eu voltar pra aula?"

    surai "E se eu disser que não? E se eu chamuscar seu cabelo?" # ameaçando

    "Surai conjura uma chama no dedo indicador e avança o dedo na direção do cabelo dele."

    haikou "Isso é medonho, pára!"

    surai "Então aceita o contrato!" # brava

    haikou "Não! Eu nem te conheço! Eu ainda nem me convenci de que você é real!" # bravo

    surai "Ok, eu vou parar com as ameaças e brincadeiras… A verdade é que eu realmente preciso de você." # suspirando triste
    surai "Vocês não vêem isso, porque nós mantemos isso oculto de vocês para a sua própria segurança, mas esse mundo está desmoronando." 
    surai "Damos nosso máximo para lidar com esses problemas sozinhos e não envolver pessoas não-mágicas nisso, mas precisamos de reforços…"

    surai "É por isso que eu estou aqui: eu preciso escolher alguém para substituir companheiros que se foram, porque não temos mais pessoas o suficiente para proteger esse mundo." # com lágrimas nos olhos

    haikou "Eu sinto muito, mas eu preciso ir pra aula. E eu nem sequer seria qualificado para algo desse tipo." # mais calmo e tentando ser mais delicado
    haikou "Você eventualmente vai encontrar alguém melhor pra essa, uh… Tarefa? É, tarefa parece bom."
    haikou "Então não desista! Mas agora, por favor, pode me deixar ir para a aula?"

    "Surai enxuga as lágrimas." 

    surai "Infelizmente não posso. Você já viu minha magia, e humanos que presenciam isso podem ficar loucos." # novamente enérgica e travessa, sorrindo
    surai "Eles ficam, a não ser que se envolvam o suficiente na situação para aceitar a nova realidade e tomá-la como parte de si mesmos."
    surai "Além disso… Corro o risco de você sair espalhando por aí. Ninguém acreditaria, mas até mesmo boatos podem ser perigosos."
    surai "E, agora que você viu meus poderes, pode se tornar alvo de monstros. A opção mais segura aqui é aceitar o contrato…"

    haikou "Mais segura para você, né?!"

    surai "Mais segura para você! Eu estou falando sério! Monstros podem estar nos observando nesse instante!"
    surai "E mesmo que você recuse o contrato, eles não vão levar isso em conta!"

    "Haikou respira fundo."

    haikou "Eu realmente acho melhor eu não me envolver nisso. Eu posso ir agora? Por favor?"

    surai "Tudo bem. Obrigada pelo seu tempo!" # triste

    "Surai desaparece."

    "A parede invisível desaparece."

    "Haikou anda para fora do banheiro e volta para a sala de aula."

