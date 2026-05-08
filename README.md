# Ramdon numbers and numerical aproximations

*Uso de números aleatorios para aproximaciones numéricas*

## Descripción

Este proyecto implementa un **Generador Lineal Congruencial (GLC)** para producir números pseudoaleatorios y los aplica a problemas de aproximación numérica mediante métodos de Monte Carlo.

## Contenido

| Archivo | Descripción |
|---------|-------------|
| `glc.py` | Generador Lineal Congruencial con pruebas de uniformidad |
| `estimate_pi.py` | Estimación de π usando muestreo aleatorio |
| `integral_methods.py` | Comparación de dos métodos de integración Monte Carlo |

## Resultados

### Estimación de π

| n (muestras) | π estimado | Error | Tiempo (s) |
|--------------|------------|-------|-------------|
|      100     |   3.2000   | 0.0584|   0.0001    |
|     1,000    |   3.1960   | 0.0544|    0.002    |
|    10,000    |   3.1560   | 0.0144|    0.019    |
|   100,000    |   3.1502   | 0.0086|    0.163    |
|   1,000,000  |   3.1504   | 0.0088|    1.519    |

### Integración de ∫₀³ e^(x/2) dx (valor exacto ≈ 6.9634)

- **Método 1 (conteo de puntos)**: convergencia más lenta
- **Método 2 (esperanza)**: convergencia más rápida y eficiente

## Cómo ejecutar

```bash
# Requisitos
pip install numpy matplotlib

# Ejecutar cada script
python glc.py
python estimate_pi.py
python integral_methods.py
