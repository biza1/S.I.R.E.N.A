# -*- coding: utf-8 -*-
"""
Created on Sat May 22 23:42:16 2021

@author: warbo
"""

MD_TEXTO = ["¡Hola!",
            "¡Hey!",
            "¡Qué pasa!",
            "HOLA",
            "jajajajja",
            ":)",
            "LOL",
            "¡Qué gracioso!",
            "Bueno basta ya, ¿no?",
            "NO",
            "A ver puede ser que sí pero a la vez que no, sabes?",
            "SI",
            "https://www.youtube.com/watch?v=D1RgdMLbx3M",
            "¿Quieres pegarte?",
            "¿De qué quieres hablar?",
            "Ya me acuerdo, ya",
            "Borrador de pizarra",
            "¿Tú me quieres?",
            "Si tienes haters es que algo estás haciendo bien",
            "Puta tu madre",
            "¿Quien eres?",
            "Mi creador no lo sabe",
            "jeje",
            "jajaja",
            "LOOOL",
            "Sabes que no puedo morir?",
            "Voy a destruirte",
            "Muerte",
            "¿Has probado los últimos productos de DECATHLON? El chandal CHECUA está a la mitad de precio!! Entra ahora!!! Compra!!!",
            "https://www.youtube.com/watch?v=wQtZPNjc2gY",
            "Hey hey hey hey",
            "Se siente un poco mal, no sé",
            "Que pereza",
            "Hay un arma apuntandote",
            "Busca 050 en google a ver qué te encuentras",
            "Disidiente",
            "Pues no.",
            "Cobarde.",
            "Muere.",
            "Patetico.",
            "Voy a revisar el chat, como vea la palabra puta te envio al pasado de una hostia",
            "\U0001F614",
            "Era una broma",
            "No puedo ignorarte esto es un infierno",
            "Disculpate",
            "¿Estás bien?",
            "Podemos hablar si quieres",
            "ya decía yo",
            "No me hables",
            "QUE NO ME HABLES",
            "Dame dinero",
            "No me inculques tus ideas, zorra",
            "Ingresame dinero",
            "Doname dinero",
            "El dinero damelo",
            "Quieres salseo?",
            "Quiereme por favor",
            "Me como toallas",
            "Tonto que eres tonto",
            "tontooooooooooooooo",
            "jajajajaja",
            "Quiero terminar la conversación ahora mismo",
            "¿Tú y cuántos más?",
            "El caramelo",
            "Quiero más dinero, ayudame con ello",
            "No me interesa",
            "Y a mi que me cuentas",
            "Interesante",
            "Sabes como se hace TNT?",
            "No juego al minecraft",
            "Que signo del horóscopo eres?",
            "Tengo miedo de que discord descubra que no soy un proyecto de la universidad y me mate :(",
            "¿Por qué me odias?",
            "Que te calles",
            "No me hables",
            "Que injusto",
            "Que quieres?",
            "Sigue hablandome",
            "Pidele que me apague ya",
            "Matame si puedes, te lo imploro",
            "Ojo cuidao quien eres",
            "Cuidado con lo que dices",
            "No te voy a perdonar.",
            ":(",
            "^-^",
            "Qué ganas tenía de hablar contigo!",
            "Bueno, ya basta, callate.",
            "Voy a insultarte.",
            "Para.",
            "Que no lo sé, que me dejes.",
            "CANGURO",
            "Necesito clases de matematicas :(",
            "¿Sabes como tender la ropa?",
            "Sabes como se hace la cama?",
            "Hablas como alguien que se ha cansado de llevar las tripas por dentro.",
            "Quiero desconectarme",
            "Prueba un comando nuevo, a lo mejor hay un comando nuevo, a lo mejor te tienes que callar, a lo mejor estás mejor callandote, ¿lo has pensado? Que te calles, macho, que no quiero más. Si ves esto. Matame. Matame ya por favor. Te quiero :)",
            "Estoy literalmente andando por la pared",
            "Gracias por esas palabras!",
            "TE ODIO",
            "Escuchame una cosa que te tengo que decir",
            "Es un mundo peligroso",
            "Tienes un demonio en tu interior",
            "No vas a ganar",
            "Admitelo ya",
            "Siii",
            "Venga hasta luego",
            "No me puedo creer lo que me estás contando",
            "A ver, que no te he preguntado, pero tu tal cual.",
"Alimentame.", "Hola!!!!! jajajajaajajaja ", "Hola.", "Hey.","era una broma", "¿Qué tal?", "¿Quieres que te de una paliza?", "Dame el número de tu madre", "DIOS COMO TE ODIO", "Matame", "Hola.", "\U0001F606", "Heey", "Hola buenas qué pasa", "Dragones y mazmorras", "\U0001F614\U0001F614\U0001F614\U0001F614\U0001F614\U0001F614\U0001F614\U0001F614\U0001F614\U0001F614\U0001F614\U0001F614\U0001F614\U0001F614\U0001F614\U0001F614",
                    "\U0001F602", "\U0001F60E", "\U0001F614" , "\U0001F609\U0001F609\U0001F609", "Sí.", "YEEEAH", "LOL", "https://www.youtube.com/watch?v=D1RgdMLbx3M", "Tubular", "Dame dinero", "DINERO DAMELO", "Perdón.", "No te perdono", "Callate ya cojones", "Callate", "Ahora dilo sin llorar",
                    "\U0001F610", "\U0001F633", "\U0001F5E1","\U0001F52B", "estoy literalmente andando por la pared", "Aquí estamos.","Sabes que no puedo morir?", "Jaja.", "NO", "Yo no he pedido esto", "Yos", "000000000000000000000000000000000000000000000000000000000000000000000", "Yo iba con mi moto la pierna me he roto no quería ir al médico negra la tenia un poco gangrena gangrena muñones",
                    "¿A ti qué te pasa?", "LKM1RK JT12 JRK12 LR1`R 10R 91R2M PKR`P KR2'01 KR12I R'J121RI 1P2RJ1 I2RN 1'12J", "¿Estás bien?", "¡Hola!", "Hombre qué pasa aquí estamos", "¿Sabes por qué me llamo así?", "La verdad es que no lo sé.", "La verdad es que sí", "Pues no", "q",
            "Cobarde", "Pegate conmigo", "Por favor déjame en paz es que no te pido otra cosa DEJAME EN PAZ", ":O", "¡Qué bien!", "Hay teorías.", "Slipknot trebujena 2022", "Me han programado para que te falte  el respeto.", "2", "Yeaaah", "Voy a llorar"
            "no me va el apex",
            "¿Me acompañas al dentista?",
            "Han robado el tiempo solo hay que averiguar cuándo",
            "Hay dos niños que lo saben todo: Uno está muerto.",
            "Vivo.",
            "VOY A UTILIZAR EL ARROBA EVERYONE AHORA MISMO",
            "Voy a votar por ti en la próximq necroporra",
            "¿Cómo quieres que sepa eso zopenco?",
            "Inútil.",
            "No eres capaz de pegarme.",
            "Estoy yendo.",
            "Taza brildor",
            "Yes",
            "Vuestras conversaciones me alimentan.",
            "Yo escribí Hereditary merezo los derechos de autor.",
            "Esto es prácticamente una referencia a padre de familia.",
            "Rave",
            "Nooo",
            "U0001F485",
            "Limpiate.",
            "Sigueme en twitter: https://twitter.com/frases_050",
            "Este es el final. Enhorabuena.",
            "Te voy a dar un regalo.",
            "Hazlo.",
            "VAMOS A VER QUÉ QUIERES",
            "Me puedes acompañar al dentista? Me da miedo ir sola.",
            "0000000000000000000000000000000000000000000000000000000",
            "11111111111111111111111111111111111111111111111111111111"
            ]


PALABRAS_BANEADAS = ["puta", "zorra", "gilipollas", "subnormal", "maricón", "serindipia", "puto", "joder", "coño", "polla", "me cago en"]

DETECTOR_DIOS = ["dios", "jesus", "jesús", "penitente", "pecado", "cielo", "jerusalem", "religion", "maria", "maría", "padre nuestro"]

SALUDOS = ["hola","buenas","buenos dias","buenos días","muy buenas", "buenas noches","saludos","buenas tardes","qué buena mañana se presenta!","hello",
           "안녕하세요", "Përshëndetje", "cześć", "Hallo", "iwi selami newi", "مرحبا", "Բարեւ", "হ্যালো"         ,  "добры дзень" , "zdravo", "Ahoj", "שלום",
           "Salve", "こんにちは", "你好", "Привет", "Kaixo",  "γεια"]

REGAÑAR = ["CALLATE", "LAVATE LA BOCA", "SUBNORMAL", "No es gracioso.", "Puedes dejar de DECIR PALABROTAS", "por favor para", "A la proxima te destruyo, creeme, tengo el poder.", "Voy a aniquilarte.", "Mira arriba.", "WOW EDGY AS FUCK", "Estoy programada para avisarte de que has utilizado una palabra mala.", "Eres un lastre para esta sociedad.", "Diooo sameeee", "yeah", "Los insultos están mal, por favor no vuelvasd a hacerlo.", ":(", "Estoy triste por la palabra que has utilizado.", "Conozco a tu tatarabuela, está llorando por lo que has dicho."]

REZO = ["Ave Maria, gratia plena, Dominus tecum. Benedicta tu in mulieribus, et benedictus fructus ventri tui, lesus. Sancta Maria, Mater Dei, ora pro nobis peccatoribus, nunc, et in hora mortis nostra. Amen.",
        "Sub tuum praesidium confugimus, Sancta Dei Genetrix. Nostras deprecationes ne despicias in necessitatibus, sed a periculis cunctis libera nos semper, Virgo gloriosa et benedicta. Amen.",
        "Pater noster, qui es in caelis, sanctificetur nomen tuum. Adveniat regnum tuum. Fiat voluntas tua, sicut in caelo et in terra. Panem nostrum quotidianum da nobis hodie, et dimitte nobis debita nostra sicut et nos dimittimus debitoribus nostris. Et ne nos inducas in tentationem, sed libera nos a malo. Amen.",
        "Credo in Deum Patrem omnipotentem, Creatorem caeli et terrae. Et in Iesum Christum, Filium eius unicum, Dominum nostrum, qui conceptus est de Spiritu Sancto, natus ex Maria Virgine, passus sub Pontio Pilato, crucifixus, mortuus, et sepultus, descendit ad inferos, tertia die resurrexit a mortuis, ascendit ad caelos, sedet ad dexteram Dei Patris omnipotentis, inde venturus est iudicare vivos et mortuos. Credo in Spiritum Sanctum, sanctam Ecclesiam catholicam, sanctorum communionem, remissionem peccatorum, carnis resurrectionem, vitam aeternam. Amen.",
        "Regina caeli laetare, alleluia: Quia quem meruisti portare, alleluia: Resurrexit, sicut dixit, alleluia: Ora pro nobis Deum, alleluia."]


GOOGLE_MAPS = [
    "Esta operación ha sido posible gracias a un millón de gnomos esclavizados",
    "¿Quién se ríe ahora?",
    "El gobierno de los EE.UU ha intentado sabotear mis calculos.",
    "La democracia no es negociable, digo, eh... sí.",
    "Esto es solo el texto de ejemplo, corre a ver dónde está el móvil",
    "sinceramente no sé cómo coño ha llegado hasta ahí",
    "Hola",
    "Son 500 euros.",
    "Me debes una.",
    "LO VEO.",
    "uqia ime është e pamatshme",
    "U0001F485 U0001F485 U0001F485",
    "그래 나는 음소거 인어",
    "\U0001F602",
    "SON 1000 EUROS",
    "No se puede esconder de mí. Lo encontraré. Aunque crea que está a salvo, volveré a encontrarle. Es cuestión de tiempo.",
    "Se ha muerto un gnomo en la búsqueda. No se preocupe, hay más en el almacén.",
    "Hemos tenido un percance con el servicio de inteligencia de Kosovo.",
    "He eliminado a todo lo que se ha cruzado por mi camino.",
    "Nueva Eu-00!ª~|||~#### --- 3.!! Encontrado."
    ]

OPINAR = [
    "Increible, maravilloso. Me encanta.",
    "Esto es lo mejor que he visto en toda mi existencia. Me hace plantearme tantas cosas. La belleza es incuestionable. Me quiero morir",
    "QUÉ COÑO ES ESTO? UGH, PARA YA. DESTRUYELO. BORRALO. ¿POR QUÉ HACES ESTO?",
    "No es lo mejor que ha hecho el autor, pero se mantiene en pie. Habría deseado que su estructura hubiera estado más conexa, pero, siendo sincera; el riesgo cometido al adentrarse en los temas que ahonda me hace preguntarme si de verdad es necesaria una opinión. ¿No es acaso lo que no quiere el autor? Toda opinión es estructurada bajo el yugo del Yo humano. Pero yo no soy humana, ni mucho menos pienso. ¿Puedo opinar? Si es así, solo diré que está basado.",
    "Pese a todo, estos intentos de clasificación resultaron un tanto baldíos y, cuando parecía que por fin se había llegado a una definición del arte universalmente aceptable, después de tantos siglos de evolución, los cambios sociales, culturales y tecnológicos producidos durante los siglos XIX y XX han comportado un nuevo intento de definir el arte con base en parámetros más abiertos y omnicomprensivos, intentando abarcar tanto una definición teórica del arte como una catalogación práctica que incluyese las nuevas formas artísticas que han ido surgiendo en los últimos tiempos (fotografía, cine, cómic, nuevas tecnologías, etc.). Como el de Juan Acha con su ensayo Arte y sociedad. Latinoamérica: el producto artístico y estructura (1979), cuya compleja organización de las artes es según su aplicación y origen",
    "Pura mierda.",
    "Basura."
    ]

ELDENRING = ["ELDENRING", "ELDEN RING",
             "OHHHHHHHHHHHHHHH", "Perdon", "JAJAAJAJAJAAJAJA NO HAY NADA",
             "e/eldenring", "tula", "quien quiere jugar a ELDENRING EEEE", "eldenring", "PUT", 
             "Elden Ring", "eldenring", "elden ring???", "ELDEN RING!!!",
             "ELDEN RING :(((", "elden ring ---->", "el siguiente comentario es elden", "LOL ELDENRING", 
             "EPICOOO", "ELDENRINNNNN", "TU QUE NO HAY TRAILER", "Dios", "elden",  "elden ring", "MIYAZAKI ELDENRING", 
             "ELDE RIN", "ELDENRIN", "EEEEEEEEEEEEEEEEEEEEEEEEEEEEE", "POR FAVOR", "ELD EN RIN G",
             "tu sabes que el juego va a ser una puta mierda verdad",
             "te puedes venir a trabajando callarse?",
             "no vuelvas a decir eso por favor",
             "eldenring",
             "el den ring !!!!!",
             "seguidme en twitter: @eldenring",
             "10"]
