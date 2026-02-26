#!/usr/bin/env python3
"""
Script de Validación - Taller 02
Verifica funciones de análisis de sensores IoT
"""

import sys
import os

def test_agrupar_por_sensor():
    """Verifica la función agrupar_por_sensor"""
    try:
        from analisis_sensores import agrupar_por_sensor

        # Datos de prueba
        lecturas_test = [
            {'sensor_id': 'S001', 'temperatura_c': '25.0'},
            {'sensor_id': 'S002', 'temperatura_c': '26.0'},
            {'sensor_id': 'S001', 'temperatura_c': '27.0'}
        ]

        resultado = agrupar_por_sensor(lecturas_test)

        # Verificaciones
        assert isinstance(resultado, dict), "Debe retornar un diccionario"
        assert 'S001' in resultado, "Debe incluir sensor S001"
        assert 'S002' in resultado, "Debe incluir sensor S002"
        assert len(resultado['S001']) == 2, "S001 debe tener 2 lecturas"
        assert len(resultado['S002']) == 1, "S002 debe tener 1 lectura"

        print("✓ agrupar_por_sensor() funciona correctamente")
        return True
    except ImportError:
        print("✗ No se pudo importar agrupar_por_sensor")
        return False
    except AssertionError as e:
        print(f"✗ Error en agrupar_por_sensor: {e}")
        return False
    except Exception as e:
        print(f"✗ Error inesperado en agrupar_por_sensor: {e}")
        return False


def test_calcular_estadisticas():
    """Verifica la función calcular_estadisticas"""
    try:
        from analisis_sensores import calcular_estadisticas

        # Datos de prueba
        lecturas_test = [
            {'temperatura_c': '20.0', 'humedad_pct': '60.0', 'luz_lux': '10000'},
            {'temperatura_c': '25.0', 'humedad_pct': '55.0', 'luz_lux': '15000'},
            {'temperatura_c': '30.0', 'humedad_pct': '50.0', 'luz_lux': '2000'}
        ]

        resultado = calcular_estadisticas(lecturas_test)

        # Verificaciones
        assert isinstance(resultado, dict), "Debe retornar un diccionario"
        assert 'total_lecturas' in resultado, "Debe tener clave 'total_lecturas'"
        assert 'temp_promedio' in resultado, "Debe tener clave 'temp_promedio'"
        assert 'temp_maxima' in resultado, "Debe tener clave 'temp_maxima'"
        assert 'temp_minima' in resultado, "Debe tener clave 'temp_minima'"
        assert 'humedad_promedio' in resultado, "Debe tener clave 'humedad_promedio'"
        assert 'horas_luz' in resultado, "Debe tener clave 'horas_luz'"

        assert resultado['total_lecturas'] == 3, "Total debe ser 3"
        assert resultado['temp_maxima'] == 30.0, "Temperatura máxima debe ser 30.0"
        assert resultado['temp_minima'] == 20.0, "Temperatura mínima debe ser 20.0"
        assert resultado['horas_luz'] == 2, "Debe contar 2 lecturas con luz > 5000"

        print("✓ calcular_estadisticas() funciona correctamente")
        return True
    except ImportError:
        print("✗ No se pudo importar calcular_estadisticas")
        return False
    except AssertionError as e:
        print(f"✗ Error en calcular_estadisticas: {e}")
        return False
    except Exception as e:
        print(f"✗ Error inesperado en calcular_estadisticas: {e}")
        return False


def test_detectar_periodos_criticos():
    """Verifica la función detectar_periodos_criticos"""
    try:
        from analisis_sensores import detectar_periodos_criticos

        # Crear 15 lecturas con temp > 30 (más de 1 hora = 12 lecturas)
        lecturas_criticas = [{'temperatura_c': '31.0'} for _ in range(15)]

        resultado = detectar_periodos_criticos(lecturas_criticas, 'S999')

        assert isinstance(resultado, list), "Debe retornar una lista"
        assert len(resultado) > 0, "Debe detectar al menos una alerta con 15 lecturas críticas"

        # Caso sin alertas
        lecturas_normales = [{'temperatura_c': '25.0'} for _ in range(20)]
        resultado_normal = detectar_periodos_criticos(lecturas_normales, 'S999')
        assert len(resultado_normal) == 0, "No debe generar alertas con temperatura normal"

        print("✓ detectar_periodos_criticos() funciona correctamente")
        return True
    except ImportError:
        print("✗ No se pudo importar detectar_periodos_criticos")
        return False
    except AssertionError as e:
        print(f"✗ Error en detectar_periodos_criticos: {e}")
        return False
    except Exception as e:
        print(f"✗ Error inesperado en detectar_periodos_criticos: {e}")
        return False


def test_archivo_csv():
    """Verifica que el archivo CSV existe"""
    if os.path.exists("sensores_24h.csv"):
        print("✓ Archivo sensores_24h.csv encontrado")
        return True
    else:
        print("✗ No se encontró sensores_24h.csv")
        return False


def main():
    print("="*70)
    print("VALIDACIÓN AUTOMÁTICA - TALLER 02")
    print("="*70)
    print()

    resultados = []

    # Ejecutar tests
    resultados.append(test_archivo_csv())
    resultados.append(test_agrupar_por_sensor())
    resultados.append(test_calcular_estadisticas())
    resultados.append(test_detectar_periodos_criticos())

    # Resumen
    print()
    print("="*70)
    total = len(resultados)
    aprobados = sum(resultados)

    if aprobados == total:
        print(f"✓ APROBADO: {aprobados}/{total} pruebas exitosas")
        print()
        print("Siguiente paso:")
        print("  Ejecuta: python analisis_sensores.py")
        print("  Verifica que se genere resumen_sensores.csv")
        print()
        print("Para entregar:")
        print("  git add analisis_sensores.py")
        print("  git commit -m 'Completar taller 02: análisis de sensores IoT'")
        print("  git push")
        sys.exit(0)
    else:
        print(f"✗ PENDIENTE: {aprobados}/{total} pruebas exitosas")
        print()
        print("Revisa los errores arriba y corrige tu código.")
        sys.exit(1)


if __name__ == "__main__":
    main()
