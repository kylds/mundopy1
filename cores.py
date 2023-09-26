# ANSI 
# representar uma cor \033[m entre esse cochete e m coloca o código da cor
# indicar três valores: o estilo - style, a cor do texto - text e a cor do fundo - background 
# ex: \033[0;33;44m
# códigos de estilo que funcionam melhor no py: 0 - nada, 1 - negrito, 4 - sublinhar e 7 - inverter as configurações 
# 30 - 37 (texto)
# 40-47 (background)

print('\033[1;31;43m Oi!')