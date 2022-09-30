import sys
sys.path.insert(0, './src')

import modulo_divisores as md

print(md.divisores(4))
print(md.divisores(0))
print(md.divisores(-3))
print(md.divisores("string"))
