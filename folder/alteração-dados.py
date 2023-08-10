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
        # pesquisa de satisfação
    if texto in ['A pesquisa voltou para o ramal da agente', 'Falha no envio Pesquisa Satisfação',
                 'Ao encaminhar para a pesquisa, a mesma retornou (fluxo pesquisa de satisfação)',
                 'Retorno da pesquisa de satisfação', 'Ligação presa após transferência para pesquisa e caiu',
                 'Falha(*): ura de pesquisa satisfaçao', 'A pesquisa voltou para o ramal da agente',
                 'Ligação presa na pesquisa ']:
        return 'Fluxo falha pesquisa de satisfação'
        # queda de ligação
    elif texto in ['QUEDA NA LIGAÇÃO', 'Queda de ligação', 'Queda na ligação ', 
                   'Falha(*): queda na ligação', 'ligação caiu', 'Falha(*): ligação caiu ',
                   'Falha(*): Queda na ligação ', 'Falha(*): queda na linha ',
                   'Falha(*):queda na ligação', 'motivo: Queda de ligação',
                   'Falha(*): ligação caiu enquanto solicitava informações de contato  ',
                   'Falha(*): ligação caiu enquanto finalizava att',
                   'Motivo: Ligação caiu', 'Ligaçao caiu durante o atendimento  ',
                   'Falha(*): queda na ligação, durante att 16672171', 'Queda na ligação (falha)',
                   'Falha(*):ligaçao caiu ', 'Falha(*): queda ligação', 'Falha(*): queda na ligação 16670834',
                   'Ligação caiu antes de formalizar att', 'Ligação caiu durante a coleta dos dados',
                   'Falha(*): Queda de ligação', 'Falha(*): queda na ligação queda na ligação',
                   'Ligação caiu na finalização', 'Falha(*): ligação caiu', 'Queda na ligação (robotizada)',
                   'Falha(*):  Queda de Ligação']:
        return 'Ligações que tiveram queda'
        # ligação muda/sem retorno de voz
    elif texto in ['LIGAÇÃO MUDA', 'LIGAÇÃO MUDA - SEM RETORNO DE VOZ', 
                   'Ligação muda sem retorno de voz', 'Ligação caiu/sem retorno de voz',
                   'Ligação entrou muda', 'ligação sem retorno de voz',
                   'Ligação desconectada por falta de retorno de voz', 'Falha(*): ligação muda',
                   'Falha(*): sem retorno de voz ', 'Sem retorno de voz',
                   'Falha(*): sem retorno de voz']:
        return 'Ligações mudas e/ou sem retorno de voz'
        # durante atendimento
    elif texto in ['Ligação caiu durante o atendimento', 'Ligação muda (ficou muda durante o atendimento)', 
                   'Ligação muda (entrou muda no início do atendimento)',
                   'Ligação ficou muda e caiu durante o atendimento',
                   'Ligação ficou muda e caiu durante atendimento.', 
                   'Durante o atendimento: Ligação caiu/Sem retorno de voz',
                   'Ligação desconectada por falta de comunicação',
                   'Ligação caiu durante o atendimento;', 'Ligação caiu/sem retorno de voz durante o atendimento',
                   'ligação muda no script final ', 'Queda na ligação durante o atendimento']:
        return 'Falha nas ligações que ocorreram durante o atendimento'
        # cliente
    elif texto in ['Abandono em linha pelo cliente', 'cliente desconectou', 'Falha(*): seg desconectou ',
                   'Segurado desligou', 'Falha(*):corr desligou ', 'Segurado desconectou', 
                   'Falha(*): corr desligou', 'Falha(*): seg desconectou', 'Falha(*): seg desligou',
                   'Corretor desligou', 'Falha(*): segurado desligou', 'Segurado com dificuldade de desconectar',
                   'Falha(*):corr desligou 16337395', 'Falha(*): crr desconectou antes de enviar para pesquisa']:
        return 'Abandono ou desconexão realizada em linha pelo cliente'
        # aplicação e demais
    elif texto in ['Erro no Venus', 'Erro na transferência/tabulação', 'Erro StartPhone', 
                   'Vênus encerrou e desconectou o STARTPHONE', 'Erro no Horizon', 
                   'Erro no vênus', 'Não foi possível tabular a chamada', 'Sistema deslogou durante o almoço',
                   'Falha transferência para pesquisa de satisfação e tabulação - erro startphone',
                   'Sistema deslogou durante almoço', 'Falha no startphone', 'Erro para tabular e mandar para pesquisa',
                   'Falha(*): start desconectou', 'Falha na aplicação após encerrar chamada, seguiu com  o script de desconexão']:
        return 'Fluxo de sistemas ou telefonia'
        # falhas aparelhos e home
    elif texto in ['Queda na internet', 'Queda de energia', 'Reiniciou a máquina',
                   'Travou o computador e a agente teve que reiniciar', 'Problema físico no ramal (ex: ligação presa)',
                   'Falha Avaya - problema ramal (ex: ligação presa)']:
        return 'Falhas nos itens físicos ou HomeBased'
        # URA
    elif texto in ['Ligação entrou muda na URA e caiu', 'Ligação entrou muda na URA', 
                   'ligação caiu ao entrar na URA', 'ura caiu, falou porto e desligou',
                   'Ligação caiu ao entrar na URA (seguiu script de desconexão)', 'Queda da ligação ainda na URA',
                   'Queda na ligação após entrar na URA', 'ligação muda após ura ', 'Caiu na Ura',
                   'ura caiu muda, chamei 4 a 5x e fiz script de desconexão', 'Retorno da URA',
                   'Ligação com música gravada', 'Ligação entrou muda no ramal (feito script de desconexão)',
                   'Ligação entrou muda;', 'Falha(*): ligacao caiu na ura e caiu a chamafa ',
                   'Falha(*): ligação entrou muda', 'Falha(*): ligação entrou muda ']:
        return 'Falha nas ligações ao entrar na URA - Comportamento'
    else:
        return 'vazias-verificar'

# alterações= o valor que está na Coluna 'descrição' para a coluna 'Descrição Dados'
df['Desc-dados'] = df['Descrição'].apply(substituir_valor)

# carregar o arquivo atualizado e baixar nova planilha
df.to_excel('InfoNovo.xlsx')
