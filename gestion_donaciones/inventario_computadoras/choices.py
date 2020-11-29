class OpcionesArquitectura:
    X64 = "X64"
    X86 = "X86"

    OPCIONES_ARQUITECTURA = [
        (X64, 'x64'),
        (X86, 'x86')
    ]

class OpcionesComputadora:
    GABINETE = "GABINETE"
    NOTEBOOK = "NOTEBOOK"
    NETBOOK = "NETBOOK"
    ALL_IN_ONE = "ALL_IN_ONE"

    OPCIONES_FORMATO = [
        (GABINETE, 'Gabinete'),
        (NOTEBOOK, 'Notebook'),
        (NETBOOK, 'Netbook'),
        (ALL_IN_ONE, 'All in one')
    ]
    
    A_REVISAR = "A_REVISAR"
    EN_PROGRESO = "EN_PROGRESO"
    EN_PAUSA = "EN_PAUSA"
    LISTA = "LISTA"

    OPCIONES_ESTADO = [
        (A_REVISAR, 'A revisar'),
        (EN_PROGRESO, 'En progreso'),
        (EN_PAUSA, 'En pausa'),
        (LISTA, 'Lista')
    ]

    NO_FUNCIONA = "NO_FUNCIONA"
    FUNCIONA = "FUNCIONA"

    OPCIONES_FUNCIONAMIENTO = [
        (FUNCIONA, 'Funciona'),
        (NO_FUNCIONA, 'No funciona')
    ]

    SI = "SI"
    NO = "NO"

    OPCION_SI_NO = [
        (SI, 'Si'),
        (NO, 'No')
    ]
