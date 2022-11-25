import word_count_pb2
import word_count_pb2_grpc
import grpc
from concurrent import futures
import time

class WordCountServicer(word_count_pb2_grpc.WordCountServicer):

    def CountWords(self, request, context):
        print(request)
        response = word_count_pb2.WordsResponse()
        response.count = len(request.words.split())
        response.ocurrency = find_word(request)
        return response

def find_word(request):
    words = request.words.split()
    count = 0
    for word in words:
        if word ==  request.searched_word:
            count+=1
    return count

def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    word_count_pb2_grpc.add_WordCountServicer_to_server(WordCountServicer(), server)
    server.add_insecure_port(f"localhost:{port}")
    server.start()
    print(f'Servidor rodando na porta {port}')
    server.wait_for_termination()

if __name__ == "__main__":
    port = input("Qual porta você deseja que esse servidor esteja rodando?\n")
    serve(port)