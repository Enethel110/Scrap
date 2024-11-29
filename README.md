# Scrap
Automatización de carga de datos desde CSV a Google Forms mediante Scraping

## Pasos de instalación

1. **Descargar el ChromeDriver**  
   Ve a [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/) y descarga la versión correspondiente a tu navegador (Brave o el que prefieras). Asegúrate de que coincida con la versión de tu navegador.

2. **Mover el ChromeDriver a una ruta conveniente**  
   Una vez descargado, coloca el `chromedriver` en la ruta que más te convenga. En mi caso, lo guardé en `C:/chrome`.

3. **Instalar las librerías necesarias**  
   Abre tu terminal y ejecuta los siguientes comandos para instalar las librerías requeridas:

   ```bash
   pip install pandas
   pip install time
   pip install selenium
