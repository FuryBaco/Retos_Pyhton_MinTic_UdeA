
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
mensaje = "U DE A"
b = 7

def 𝑒𝑛𝑐𝑟𝑖𝑝𝑡𝑎𝑟_𝑐𝑎𝑟𝑎𝑐𝑡𝑒𝑟(𝑐𝑎𝑟𝑎𝑐𝑡𝑒𝑟,  𝑏):
    a = abc.index(caracter)
    caracter_encriptado = abc[(𝑎 + 𝑏)%27]
    return caracter_encriptado

def 𝑒𝑛𝑐𝑟𝑖𝑝𝑡𝑎𝑟(𝑚𝑒𝑛𝑠𝑎𝑗𝑒,  𝑏):
    ec,m = encriptar_caracter, mensaje
    mensaje_encriptado = ''.join(ec(char,b) if char in abc else char for char in m)
    return mensaje_encriptado

def 𝑑𝑒𝑠𝑒𝑛𝑐𝑟𝑖𝑝𝑡𝑎𝑟_𝑐𝑎𝑟𝑎𝑐𝑡𝑒𝑟(𝑐𝑎𝑟𝑎𝑐𝑡𝑒𝑟_𝑒𝑛𝑐𝑟𝑖𝑝𝑡𝑎𝑑𝑜,  b):
    ϕ = abc.index(caracter_encriptado)
    caracter_desencriptado = abc[(ϕ - b)%27]
    return caracter_desencriptado

def 𝑑𝑒𝑠𝑒𝑛𝑐𝑟𝑖𝑝𝑡𝑎𝑟(𝑚𝑒𝑛𝑠𝑎𝑗𝑒_𝑒𝑛𝑐𝑟𝑖𝑝𝑡𝑎𝑑𝑜,  𝑏):
    dc,me = desencriptar_caracter, mensaje_encriptado
    mensaje_desencriptado = ''.join(dc(char,b) if char in abc else char for char in me)
    return mensaje_desencriptado

solucion = desencriptar(encriptar(mensaje,b),b)
print(solucion)



