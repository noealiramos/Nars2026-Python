edad = int(input('¿Cuántos años tienes? '))
dinero = float(input('¿Cuánto dinero tienes? '))

acceso_concedido = edad >= 18 and dinero >= 500

print(f'¿Puedes entrar? {acceso_concedido}')