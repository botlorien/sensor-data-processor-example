from queue import Queue
from array import array
import numpy as np

class SensorDataProcessor():

    def __init__(self) -> None:
        self.queue = Queue()
        self.processed_data = array('B')

    def __repr__(self) -> str:
        return f'SensorDataProcessor({self.processed_data!r})'

    def add_data(self,data)-> None:
        if isinstance(data,(tuple,list)):
            for d in data:
                if isinstance(d,int):
                    self.queue.put(d)
                else:
                    raise ValueError(
                        f'Invalid type for sensor value: {d}. Expected "int" or list/tuple of "int"'
                    )
        elif isinstance(data,int):
            self.queue.put(d)
        else:
            raise ValueError(
                f'Invalid type for sensor value: {d}. Expected "int" or list/tuple of "int"'
            )
        print('Tamanho da fila: ',self.queue.qsize())

    def process_queue(self)->None:
        while not self.queue.empty():
            data = self.queue.get()
            self.processed_data.append(data)
            print(f'Processing sensor data value: {data}')
        print('Tamanho da fila: ',self.queue.qsize())

    def calculate_statistics(self) -> dict:
        array = np.array(self.processed_data)
        mean = np.mean(array)
        sum = array.sum()
        std = np.std(array)
        return{'mean': mean,'sum':sum, 'std':std}


    def get_memoryview(self) -> memoryview:
        return memoryview(self.processed_data)
    

if __name__=='__main__':
    # Criando uma instância da classe SensorDataProcessor
    processor = SensorDataProcessor()

    # Adicionando dados recebidos dos sensores
    processor.add_data([10, 20, 30])
    processor.add_data([40, 50, 60])

    # Processando todos os dados da fila
    processor.process_queue()

    # Calculando estatísticas
    print(processor.calculate_statistics())  # Saída: {'mean': 35.0, 'sum': 210.0, 'std': 17.078}

    # Obtendo um memoryview dos dados processados
    mv = processor.get_memoryview()
    print(mv.tolist())  # Saída: [10, 20, 30, 40, 50, 60]
    print(processor)