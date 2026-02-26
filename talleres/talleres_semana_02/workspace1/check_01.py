#!/usr/bin/env python3
"""
Script de Validación - Taller 01
Verifica que el estudiante completó correctamente las funciones.
"""

import sys
import os

def test_evaluar_riego():
    """Verifica la función evaluar_riego"""
    try:
        from riego_automatico import evaluar_riego

        # Casos de prueba
        assert "RIEGO" in evaluar_riego(35).upper(), "Error: humedad 35% debe indicar RIEGO"
        assert "DRENAJE" in evaluar_riego(80).upper(), "Error: humedad 80% debe indicar DRENAJE"
        assert "ÓPTIMO" in evaluar_riego(55).upper() or "OK" in evaluar_riego(55).upper(), "Error: humedad 55% debe ser ÓPTIMO"

        print("✓ evaluar_riego() funciona correctamente")
        return True
    except ImportError:
        print("✗ No se pudo importar evaluar_riego. ¿Está definida la función?")
        return False
    except AssertionError as e:
        print(f"✗ {e}")
        return False
    except Exception as e:
        print(f"✗ Error en evaluar_riego: {e}")
        return False


def test_evaluar_ph():
    """Verifica la función evaluar_ph"""
    try:
        from riego_automatico import evaluar_ph

        # Casos de prueba
        resultado_bajo = evaluar_ph(5.0).upper()
        resultado_alto = evaluar_ph(7.8).upper()
        resultado_optimo = evaluar_ph(6.5).upper()

        assert "CAL" in resultado_bajo, f"Error: pH 5.0 debe recomendar CAL, pero devolvió: {resultado_bajo}"
        assert "AZUFRE" in resultado_alto, f"Error: pH 7.8 debe recomendar AZUFRE, pero devolvió: {resultado_alto}"
        assert "ÓPTIMO" in resultado_optimo or "OK" in resultado_optimo, f"Error: pH 6.5 debe ser ÓPTIMO, pero devolvió: {resultado_optimo}"

        print("✓ evaluar_ph() funciona correctamente")
        return True
    except ImportError:
        print("✗ No se pudo importar evaluar_ph. ¿Está definida la función?")
        return False
    except AssertionError as e:
        print(f"✗ {e}")
        return False
    except Exception as e:
        print(f"✗ Error en evaluar_ph: {e}")
        return False


def test_procesar_parcela():
    """Verifica la función procesar_parcela"""
    try:
        from riego_automatico import procesar_parcela

        resultado = procesar_parcela("P999", "Norte", "Café", 32.0, 35, 5.2)

        # Verificar estructura del diccionario
        assert isinstance(resultado, dict), "Error: procesar_parcela debe retornar un diccionario"
        assert "parcela_id" in resultado, "Error: falta clave 'parcela_id' en el resultado"
        assert "riego" in resultado, "Error: falta clave 'riego' en el resultado"
        assert "alerta_termica" in resultado, "Error: falta clave 'alerta_termica' en el resultado"

        # Verificar lógica
        assert resultado["alerta_termica"] == True, "Error: temperatura 32°C debe generar alerta térmica"

        print("✓ procesar_parcela() funciona correctamente")
        return True
    except ImportError:
        print("✗ No se pudo importar procesar_parcela. ¿Está definida la función?")
        return False
    except AssertionError as e:
        print(f"✗ {e}")
        return False
    except Exception as e:
        print(f"✗ Error en procesar_parcela: {e}")
        return False


def test_archivo_csv():
    """Verifica que el archivo CSV existe"""
    if os.path.exists("parcelas.csv"):
        print("✓ Archivo parcelas.csv encontrado")
        return True
    else:
        print("✗ No se encontró el archivo parcelas.csv")
        return False


def main():
    print("="*60)
    print("VALIDACIÓN AUTOMÁTICA - TALLER 01")
    print("="*60)
    print()

    resultados = []

    # Ejecutar tests
    resultados.append(test_archivo_csv())
    resultados.append(test_evaluar_riego())
    resultados.append(test_evaluar_ph())
    resultados.append(test_procesar_parcela())

    # Resumen
    print()
    print("="*60)
    total = len(resultados)
    aprobados = sum(resultados)

    if aprobados == total:
        print(f"✓ APROBADO: {aprobados}/{total} pruebas exitosas")
        print()
        print("Siguiente paso:")
        print("  git add riego_automatico.py")
        print("  git commit -m 'Completar taller 01: automatización de riego'")
        print("  git push")
        sys.exit(0)
    else:
        print(f"✗ PENDIENTE: {aprobados}/{total} pruebas exitosas")
        print()
        print("Revisa los errores arriba y corrige tu código.")
        sys.exit(1)


if __name__ == "__main__":
    main()
