import word_count_pb2
import word_count_pb2_grpc
import grpc
from concurrent import futures
import time

def get_words_from_a_file():
    file_name = input('Digite o path do arquivo que quer abrir:\n')
    f = open(file_name)
    words = f.read().split()
    f.close()
    return words

def run():
    workes_ports = []
    words_count = 0
    search_word_count = 0
    words = get_words_from_a_file()
    words_size = len(words)
    searched_word = input('Digite qual palavra você quer descobrir a quantidade de ocorrência:\n')
    workes_qtt = int(input('Digite a quantidade de workers disponíveis:\n'))

    for i in range(0, workes_qtt):
        workes_ports.append(input(f'Digite a porta do worker {i+1}:\n'))

    for i, port in enumerate(workes_ports):
        with(grpc.insecure_channel(f"localhost:{port}")) as channel:
            init_pos = int((words_size / workes_qtt ) * i)
            final_pos = init_pos + workes_qtt
            stub = word_count_pb2_grpc.WordCountStub(channel)
            worker_request = word_count_pb2.WordsRequest(words=' '.join(words[init_pos:final_pos]), searched_word=searched_word)
            worker_reply = stub.CountWords(worker_request)
            words_count+= worker_reply.count
            search_word_count+= worker_reply.ocurrency

    print(f'Existem {words_count} palavras no arquivo e a palavra {searched_word} aparece {search_word_count} vezes')


if __name__ == "__main__":
    run()