import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    # Для работы с heapq
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    freq = Counter(data)
    heap = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        l = heapq.heappop(heap)
        r = heapq.heappop(heap)
        merged = Node(freq=l.freq + r.freq, left=l, right=r)
        heapq.heappush(heap, merged)
    
    return heap[0]

def build_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = dict()
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)
    return codebook

def compress(data):
    tree = build_huffman_tree(data)
    codebook = build_codes(tree)
    encoded_data = ''.join(codebook[char] for char in data)
    return encoded_data, codebook, tree

def decompress(encoded_data, tree):
    result = []
    node = tree
    for bit in encoded_data:
        node = node.left if bit == '0' else node.right
        if node.char is not None:
            result.append(node.char)
            node = tree
    return ''.join(result)


def print_tree(node, indent=""):
    if node is None:
        return
    if node.char is not None:
        print(f"{indent}🔹 '{node.char}' ({node.freq})")
    else:
        print(f"{indent}◼️ Node ({node.freq})")
        print_tree(node.left, indent + "  ")
        print_tree(node.right, indent + "  ")


# Пример использования
text = "hello huffman"
encoded, codes, tree = compress(text)
print("Коды:", codes)
print_tree(tree)
print("Сжатое:", encoded)
print("Восстановлено:", decompress(encoded, tree))

# Размер исходных данных (в байтах и битах)
original_size_bytes = len(text.encode('utf-8'))
original_size_bits = original_size_bytes * 8

# Размер сжатых данных (в битах)
compressed_size_bits = len(encoded)
compressed_size_bytes = (compressed_size_bits + 7) // 8  # округление вверх

# Коэффициент сжатия
compression_ratio = compressed_size_bits / original_size_bits

print(f"Исходный размер: {original_size_bytes} байт ({original_size_bits} бит)")
print(f"Сжатый размер: {compressed_size_bytes} байт ({compressed_size_bits} бит)")
print(f"Коэффициент сжатия: {compression_ratio:.2f}")
