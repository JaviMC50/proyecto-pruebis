#!/usr/bin/env python3
"""
Script para ejecutar tests con mocks
"""
import subprocess
import sys

def run_tests():
    """Ejecuta los tests con mocks"""
    cmd = [sys.executable, "-m", "pytest", "tests/", "-v", "-m", "mock"]

    print(f"Comando: {' '.join(cmd)}")
    print("-" * 50)

    try:
        result = subprocess.run(cmd)
        return result.returncode
    except KeyboardInterrupt:
        print("\n Test interrumpidos")
        return 1

if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)