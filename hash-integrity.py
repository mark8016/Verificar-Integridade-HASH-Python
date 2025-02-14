import hashlib
import os

def calculate_hash(file_path):
    """
    Função para calcular o hash de um arquivo.
    :param file_path: Caminho do arquivo a ser verificado
    :return: Hash do arquivo
    """
    hash_sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(8192):
            hash_sha256.update(chunk)
    
    return hash_sha256.hexdigest()

def verify_integrity(file_path, original_hash):
    """
    Função para verificar a integridade de um arquivo comparando com o hash original.
    :param file_path: Caminho do arquivo a ser verificado
    :param original_hash: Hash original do arquivo
    :return: None
    """
    current_hash = calculate_hash(file_path)
    if current_hash == original_hash:
        print("Arquivo está íntegro.")
    else:
        print("ALERTA: O arquivo foi alterado!")
        
# Exemplo de uso
file_path = "/path/to/important_file.txt"
original_hash = "c9e1074f5b9d5b4f4dce19b9b77fd44c"  # Substitua pelo hash original

verify_integrity(file_path, original_hash)
