# Documentación del Pipeline de CI/CD

## Introducción
Este archivo describe la configuración del pipeline de integración continua para el proyecto X. El pipeline se implementa usando GitHub Actions y realiza las siguientes tareas:
- Compilación del código.
- Ejecución de pruebas automatizadas.
- Análisis estático de calidad de código.

## Configuración
### Herramientas utilizadas
- **GitHub Actions**: Para gestionar el pipeline.
- **Node.js**: Lenguaje base del proyecto.
- **SonarQube**: Para análisis estático del código.

### Estructura del workflow
El archivo `.github/workflows/ci.yml` contiene la configuración del pipeline. Sus pasos son:
1. **Checkout del repositorio:** Descarga el código fuente.
2. **Configuración del entorno:** Instala Node.js versión 16.
3. **Ejecución de pruebas:** Corre los tests definidos en el proyecto usando `npm test`.
4. **Análisis estático:** Ejecuta SonarQube para analizar la calidad del código.

### Resultados
- **Compilación:** Exitosa en todos los commits recientes.
- **Pruebas:** Todas las pruebas pasan sin errores.
- **Análisis estático:** Detectó mejoras sugeridas en [ArchivoSonarQube].

## Conclusión
El pipeline asegura que cada cambio en el proyecto mantenga la calidad y funcionalidad esperadas.
