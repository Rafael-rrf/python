times = ('América-MG', 'Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo', 'Vasco da Gama')
print(f'Os 5 primeiros colocados: {times[:5]}')
print(f'Os últimos 4 últimos colocados da tabela: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
posicaoFortaleza = times.index('Fortaleza') + 1
print(f' O fortaleza está na {posicaoFortaleza}ª posicao')
