
import sqlite3
from paquete import Paquete


class BaseDatos:

    def __init__(self):
        self.conexion = sqlite3.connect("recargas.db")
        self.crear_tablas()
        self.registrar_paquetes_iniciales()

    def crear_tablas(self):

        cursor = self.conexion.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS paquetes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                viajes INTEGER NOT NULL UNIQUE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS resultados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                algoritmo TEXT NOT NULL,
                viajes_solicitados INTEGER NOT NULL,
                cantidad_paquetes INTEGER NOT NULL,
                combinacion TEXT NOT NULL
            )
        """)

        self.conexion.commit()

    def registrar_paquetes_iniciales(self):

        cursor = self.conexion.cursor()

        for viajes in [1, 3, 4]:

            cursor.execute(
                "INSERT OR IGNORE INTO paquetes (viajes) VALUES (?)",
                (viajes,)
            )

        self.conexion.commit()

    def obtener_paquetes(self):

        cursor = self.conexion.cursor()

        cursor.execute("SELECT id, viajes FROM paquetes ORDER BY viajes")

        registros = cursor.fetchall()

        return [
            Paquete(id_paquete, viajes)
            for id_paquete, viajes in registros
        ]

    def guardar_resultado(self, algoritmo, n, cantidad, combinacion):

        cursor = self.conexion.cursor()

        cursor.execute("""
            INSERT INTO resultados
            (algoritmo, viajes_solicitados, cantidad_paquetes, combinacion)
            VALUES (?, ?, ?, ?)
        """, (algoritmo, n, cantidad, combinacion))

        self.conexion.commit()

    def mostrar_resultados(self):

        cursor = self.conexion.cursor()

        cursor.execute("SELECT * FROM resultados")

        registros = cursor.fetchall()

        for registro in registros:
            print(registro)

    def cerrar(self):
        self.conexion.close()
