#!/usr/bin/env python3
"""
Script de Validación - Taller 02.3
Verifica funciones de vectorización con NumPy
"""

import sys
import os
import numpy as np


def test_dataset_existe():
    """Verifica que el archivo .npy existe"""
    if os.path.exists("humedad_finca.npy"):
        humedad = np.load("humedad_finca.npy")
        assert humedad.shape == (
            365,
            100,
        ), f"Shape incorrecto: {humedad.shape}, esperado (365, 100)"
        print("✓ Dataset humedad_finca.npy encontrado y válido")
        return True
    else:
        print("✗ No se encontró humedad_finca.npy")
        print(
            "  Ejecuta: python -c \"import numpy as np; np.save('humedad_finca.npy', np.random.rand(365, 100) * 100)\""
        )
        return False


def test_detectar_sequia():
    """Verifica la función detectar_sequia"""
    try:
        from vectorizacion import detectar_sequia

        # Caso de prueba: 30% en sequía
        humedad_test = np.full((10, 10), 50.0)
        humedad_test[:3, :] = 20.0  # 30 celdas en sequía

        resultado = detectar_sequia(humedad_test, umbral=30)

        assert isinstance(resultado, dict), "Debe retornar un diccionario"
        assert "celdas_sequia" in resultado, "Falta clave 'celdas_sequia'"
        assert "porcentaje" in resultado, "Falta clave 'porcentaje'"
        assert (
            resultado["celdas_sequia"] == 30
        ), f"Esperado 30 celdas, obtuvo {resultado['celdas_sequia']}"
        assert (
            abs(resultado["porcentaje"] - 30.0) < 0.1
        ), f"Esperado 30%, obtuvo {resultado['porcentaje']:.2f}%"

        print("✓ detectar_sequia() funciona correctamente")
        return True
    except ImportError:
        print("✗ No se pudo importar detectar_sequia")
        return False
    except AssertionError as e:
        print(f"✗ Error en detectar_sequia: {e}")
        return False
    except Exception as e:
        print(f"✗ Error inesperado en detectar_sequia: {e}")
        return False


def test_aplicar_riego():
    """Verifica la función aplicar_riego"""
    try:
        from vectorizacion import aplicar_riego

        # Caso de prueba
        humedad_test = np.array([[20.0, 40.0], [25.0, 60.0]])
        resultado = aplicar_riego(humedad_test, umbral=30, cantidad=20)

        assert isinstance(resultado, np.ndarray), "Debe retornar un ndarray"
        assert resultado.shape == humedad_test.shape, "El shape debe mantenerse"
        assert resultado[0, 0] == 40.0, "Debe aplicar riego donde humedad < 30"
        assert resultado[0, 1] == 40.0, "No debe modificar donde humedad >= 30"
        assert np.all(resultado <= 100), "La humedad no debe superar 100"

        print("✓ aplicar_riego() funciona correctamente")
        return True
    except ImportError:
        print("✗ No se pudo importar aplicar_riego")
        return False
    except AssertionError as e:
        print(f"✗ Error en aplicar_riego: {e}")
        return False
    except Exception as e:
        print(f"✗ Error inesperado en aplicar_riego: {e}")
        return False


def test_clasificar_zonas():
    """Verifica la función clasificar_zonas"""
    try:
        from vectorizacion import clasificar_zonas

        # Caso de prueba
        humedad_test = np.array([[20.0, 50.0, 85.0]])
        resultado = clasificar_zonas(humedad_test)

        assert isinstance(resultado, np.ndarray), "Debe retornar un ndarray"
        assert resultado.shape == humedad_test.shape, "El shape debe mantenerse"
        assert "SEQUIA" in resultado[0, 0].upper(), "Debe clasificar < 30 como SEQUIA"
        assert (
            "NORMAL" in resultado[0, 1].upper()
        ), "Debe clasificar [30-80] como NORMAL"
        assert "EXCESO" in resultado[0, 2].upper(), "Debe clasificar > 80 como EXCESO"

        print("✓ clasificar_zonas() funciona correctamente")
        return True
    except ImportError:
        print("✗ No se pudo importar clasificar_zonas")
        return False
    except AssertionError as e:
        print(f"✗ Error en clasificar_zonas: {e}")
        return False
    except Exception as e:
        print(f"✗ Error inesperado en clasificar_zonas: {e}")
        return False


def main():
    print("=" * 70)
    print("VALIDACIÓN AUTOMÁTICA - TALLER 02.3")
    print("=" * 70)
    print()

    resultados = []

    # Ejecutar tests
    resultados.append(test_dataset_existe())
    resultados.append(test_detectar_sequia())
    resultados.append(test_aplicar_riego())
    resultados.append(test_clasificar_zonas())

    # Resumen
    print()
    print("=" * 70)
    total = len(resultados)
    aprobados = sum(resultados)

    if aprobados == total:
        print(f"✓ APROBADO: {aprobados}/{total} pruebas exitosas")
        print()
        print("Siguiente paso:")
        print("  cd reporte")
        print("  bash compile.sh")
        print("  cd ..")
        print()
        print("Para entregar:")
        print("  git add talleres_semana_02/workspace3/")
        print("  git commit -m 'feat: completar taller 02.3 NumPy y vectorización'")
        print("  git push")
        sys.exit(0)
    else:
        print(f"✗ PENDIENTE: {aprobados}/{total} pruebas exitosas")
        print()
        print("Revisa los errores arriba y corrige tu código.")
        sys.exit(1)


if __name__ == "__main__":
    main()
