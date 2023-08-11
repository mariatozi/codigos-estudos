# importando bibliotecas
import pandas as pd
import numpy as np
import openpyxl

# declarando dataframe e carregando o arquivo
df = pd.read_excel('chamados.xlsx')

# as primeiras informações
df.head()

# mostrar as informações do arquivo carregado
df

# colocando as informações nas funções para alterar os dados na planilha
def substituir_valor(texto):
        # ligações caindo
    if texto in ['QUEDA NA LIGAÇÃO', 'Queda de ligação', 'Ligação caiu durante o atendimento',
                 'Queda na ligação ', 'Falha(*): queda na ligação', 'ligação caiu',
                 'Ligação ficou muda e caiu durante o atendimento', 
                 'Ligação ficou muda e caiu durante atendimento.',
                 'Ligação caiu/sem retorno de voz', 'Falha(*): ligação caiu ', 
                 'Ligação entrou muda na URA e caiu',
                 'Durante o atendimento: Ligação caiu/Sem retorno de voz',
                 'Ligação caiu/sem retorno de voz durante o atendimento', 
                 'Ligação caiu durante o atendimento;',
                 'Falha(*): Queda na ligação ', 'Falha(*): queda na linha ', 
                 'Falha(*):queda na ligação',
                 'Falha(*): ligação caiu enquanto solicitava informações de contato  ',
                 'motivo: Queda de ligação', 'Motivo: Ligação caiu', 
                 'Queda na ligação durante o atendimento',
                 'Falha(*): ligação caiu enquanto finalizava att', 
                 'Ligaçao caiu durante o atendimento  ',
                 'Falha(*): queda na ligação durante abertura do atendimento', 
                 'Motivo: Queda de ligação (15997032083)',
                 'Falha(*): Queda de ligação', 
                 'Falha(*):ligação ficou muda e teve queda na ligação',
                 'Ligação caiu enquanto iniciava o atendimento', 
                 'Falha(*):ligação muda/queda na ligação',
                 'Ligação com falha e sem retorno de voz', 'Falha(*): ligação caiu', 
                 'Falha(*): queda na ligação, durante att 16672171',
                 'Falha(*):  Queda de Ligação', 'Ligação caiu durante o direcionamento', 
                 'Ligação caiu antes de formalizar att',
                 'Ligação caiu na finalização', 'Ligação caiu durante a coleta dos dados', 
                 'Falha(*): ligação caiu enquanto solicitava data do dano ',
                 'Falha(*): ligação caiu durante o atendimento ', 
                 'Falha(*): queda na ligação queda na ligação',
                 'Falha(*): caiu na hr de coletar o dano', 'Falha(*): queda ligação', 
                 'Falha(*): Durante a coleta dos numeros de ctt, a ligação ficou muda e caiu',
                 'Falha(*): Durante a coleta dos numeros de ctt, a ligação ficou muda e nao consegui mais retorno, seg desligou.',
                 'Queda na ligação (falha)', 'Falha(*):ligaçao caiu ', 
                 'Falha(*): queda na ligação 16670834',
                 'Falha(*): queda na ligação 16665068', 
                 'Ligação caiu durante o atendimento, sem retorno',
                 'Queda na ligação (robotizada)', 
                 'Falha(*): ligação caiu enquanto finalizava atendimento  ',
                 'Falha(*): queda na ligação 16668908', 'Ligação caiu durante o atendimento; ',
                 'Ligação no início do att']:
        return 'Ligações caindo no decorredor do atendimento'

        # ligações mudas ou sem retorno de voz
    elif texto in ['LIGAÇÃO MUDA', 'Ligação muda (ficou muda durante o atendimento)',
                   'Ligação muda (entrou muda no início do atendimento)',
                   'LIGAÇÃO MUDA - SEM RETORNO DE VOZ',
                   'Ligação muda sem retorno de voz', 'Ligação entrou muda',
                   'Ligação desconectada por falta de retorno de voz',
                   'Ligação entrou muda na URA', 'Falha(*): ligação muda',
                   'Ligação desconectada por falta de comunicação',
                   'ligação muda no script final ', 
                   'ura caiu muda, chamei 4 a 5x e fiz script de desconexão',
                   'Ligação muda/sem retorno de voz', 'Ligação muda (ficou durante o atendimento)',
                   'LIGAÇÃO MUDA / QUEDA DE LIGAÇÃO', 'Ligação ficou muda durante o atendimento',
                   'Ligação entrou normal, corretor se apresentou, e no meio a ligação ficou muda (feito script de desconexão)',
                   'Ligação muda durante atendimento', 'Ligação entrou muda;',
                   'Falha(*)ligação muda/ sem retorno de voz', 'Ligação muda e script de desconexão feito',
                   'Ligação ficou muda e seguiu com o script de desconexão',
                   'Ligação ficou muda com falha', 'Ligação ficou muda. Feito desconexão por falta de retorno de voz.',
                   'ligação muda após ura ', 'Falha(*): ligação entrou sem retorno de voz',
                   'Ligação Muda e Queda de ligação', 'Falha(*): ligação entrou muda ',
                   'Ligação muda no final do atendimento', 'Falha(*): ligação sem retorno de voz',
                   'Ligação muda seguida de queda', 'Falha(*): ligacao sem retorno de voz 16673884 ',
                   'Falha(*):ligação muda', 'Ligação entrou muda no ramal (feito script de desconexão)',
                   'Falha(*): ligação entrou muda', 'Ligação ficou muda durante o atendimento.',
                   'ligação sem retorno de voz', 'Sem retorno de voz',
                   'Falha(*): sem retorno de voz ', 'Falha(*): sem retorno de voz']:
        return 'Ligações mudas ao entrar na URA ou durante atendimento'

        # falha na URA
    elif texto in ['ura caiu, falou porto e desligou', 
                   'Caiu na Ura', 
                   'Retorno da URA',
                   'Falha(*): ligacao caiu na ura e caiu a chamafa ', 
                   'Ligação com música gravada',
                   'ligação caiu ao entrar na URA']:
        return 'Chamadas com falha na URA e retorno URA'

        # falha equipamento
    elif texto in ['Problema físico no ramal (ex: ligação presa)',
                   'Falha Avaya - problema ramal (ex: ligação presa)']:
        return 'Falha nos aparelhos físicos'

        # quedas (energia etc)
    elif texto in ['Queda na internet', 
                   'Queda de energia',
                   'Falha(*): Cabo do telefone deu mal contato , atendi a ligação com atraso ']:
        return 'Problemas com internet/luz/cabo de rede'

        # Aplicação, sistemas e demais
    elif texto in ['Erro StartPhone', 
                   'Vênus encerrou e desconectou o STARTPHONE',
                   'Erro no vênus', 
                   'Sistema deslogou durante almoço',
                   'Sistema deslogou durante o almoço',
                   'Falha no startphone', 
                   'Travou o computador e a agente teve que reiniciar',
                   'Falha(*): start desconectou', 
                   'Erro no Venus',
                   'Reiniciou a máquina', 
                   'Erro no Horizon']:
        return 'Falhas nos sitemas (outro fluxo)'

        # Pesquisa de satisfação e tabulador
    elif texto in ['Erro na transferência/tabulação', 
                   'Falha no envio Pesquisa Satisfação', 
                   'Ligação presa após transferência para pesquisa e caiu',
                   'Não foi possível tabular a chamada', 
                   'Ligação presa na pesquisa ',
                   'Falha transferência para pesquisa de satisfação e tabulação - erro startphone',
                   'Ao encaminhar para a pesquisa, a mesma retornou (fluxo pesquisa de satisfação)',
                   'Retorno da pesquisa de satisfação', 
                   'A pesquisa voltou para o ramal da agente',
                   'Erro para tabular e mandar para pesquisa', 
                   'Falha(*): ura de pesquisa satisfaçao',
                   'ligação presa em transferencia seguida de queda.']:
        return 'Falha na transferência ou tabulação'
      
        # cliente
    elif texto in ['Abandono em linha pelo cliente', 
                   'cliente desconectou', 
                   'Segurado desligou',
                   'Falha(*): seg desconectou ', 
                   'Falha(*):corr desligou ', 
                   'Segurado desconectou',
                   'Falha(*):corr desligou 16337395', 
                   'Falha(*): crr desconectou antes de enviar para pesquisa',
                   'Falha(*): Corr ligou, porem nao conseguiu me ouvir e desligou',
                   'Falha(*): seg desconectou', 
                   'Segurado com dificuldade de desconectar',
                   'Corretor desligou', 
                   'Falha(*): corr desligou', 
                   'Falha(*): seg desligou',
                   'Falha(*): segurado desligou']:
        return 'Ações cliente'
    else:
        return 'vazias-verificar'

# alterações= o valor que está na Coluna 'descrição' para a coluna 'Descrição Dados'
df['Desc-dados'] = df['Descrição'].apply(substituir_valor)

# carregar o arquivo atualizado e baixar nova planilha
df.to_excel('InfoNovo.xlsx')
