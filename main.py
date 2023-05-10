from typing import Dict, Any
import json

class AnalizadorEventos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
        self.total_eventos = 0
        self.eventos_por_tipo: Dict[str, int] = {}
        self.eventos_por_servidor: Dict[str, int] = {}

    def procesar_eventos(self) -> Dict[str, Any]:
        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                if 'Tipo de evento:' in linea:
                    tipo_evento = linea.split(': ')[1].strip()
                    self.total_eventos += 1
                    if tipo_evento in self.eventos_por_tipo:
                        self.eventos_por_tipo[tipo_evento] += 1
                    else:
                        self.eventos_por_tipo[tipo_evento] = 1
                elif 'Servidor:' in linea:
                    servidor = linea.split(': ')[1].strip()
                    if servidor in self.eventos_por_servidor:
                        self.eventos_por_servidor[servidor] += 1
                    else:
                        self.eventos_por_servidor[servidor] = 1

        return {
            'total_eventos': self.total_eventos,
            'eventos_por_tipo': self.eventos_por_tipo,
            'eventos_por_servidor': self.eventos_por_servidor
        }


analizador = AnalizadorEventos('eventos.txt')
resultados = analizador.procesar_eventos()

print(json.dumps(resultados, indent=4))