import numpy as np
import sys

def test_limpiar_datos():
    from vectorizacion import limpiar_datos
    test_arr = np.array([-10, 50, 150])
    res = limpiar_datos(test_arr)
    assert np.all(res >= 0) and np.all(res <= 100), "limpiar_datos falló: hay valores fuera de [0, 100]"
    print("  ✓ Test Limpieza: PASADO")

def test_vectorizacion_pura():
    # Este test es clave: verifica que no usen 'for' inspeccionando el código
    with open('vectorizacion.py', 'r') as f:
        content = f.read()
        if "for " in content.lower() and "range" in content.lower():
            print("  ⚠ ALERTA: Se detectaron bucles 'for'. El objetivo es usar VECTORIZACIÓN.")
            return False
    print("  ✓ Test Vectorización (Sin bucles): PASADO")

def test_estres_hidrico():
    from vectorizacion import calcular_estres_hidrico
    test_arr = np.array([10, 50, 15])
    res = calcular_estres_hidrico(test_arr, 20)
    expected = np.array([True, False, True])
    assert np.array_equal(res, expected), "calcular_estres_hidrico falló en la lógica booleana"
    print("  ✓ Test Estrés Hídrico: PASADO")

def main():
    print("--- INICIANDO VALIDACIÓN SEMANA 03 ---")
    try:
        test_limpiar_datos()
        test_estres_hidrico()
        test_vectorizacion_pura()
        print("\n¡FELICIDADES! Tu lógica de ingeniería es eficiente.")
    except Exception as e:
        print(f"\n✗ Error en la validación: {e}")

if __name__ == "__main__":
    main()
