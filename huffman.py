import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_dict(text):
    """文字の出現頻度を計算する"""
    return Counter(text)

def build_huffman_tree(freq_dict):
    """ハフマン木を構築する"""
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_huffman_codes(root, current_code='', huffman_codes=None):
    """ハフマン符号を生成する"""
    if huffman_codes is None:
        huffman_codes = {}
    
    if root is None:
        return huffman_codes
    
    if root.char is not None:
        huffman_codes[root.char] = current_code
    
    generate_huffman_codes(root.left, current_code + '0', huffman_codes)
    generate_huffman_codes(root.right, current_code + '1', huffman_codes)
    
    return huffman_codes

def huffman_encode(text):
    """テキストをハフマン符号化する"""
    # 文字の出現頻度を計算
    freq_dict = build_frequency_dict(text)
    
    # ハフマン木を構築
    huffman_tree = build_huffman_tree(freq_dict)
    
    # ハフマン符号を生成
    huffman_codes = generate_huffman_codes(huffman_tree)
    
    # テキストをハフマン符号に変換
    encoded_text = ''.join(huffman_codes[char] for char in text)
    
    return {
        'encoded_text': encoded_text,
        'huffman_codes': huffman_codes,
        'frequency': freq_dict
    }

def main():
    # 使用例
    text = input("ハフマン符号化するテキストを入力してください: ")
    
    result = huffman_encode(text)
    
    print("\n文字の出現頻度:")
    for char, freq in result['frequency'].items():
        print(f"'{char}': {freq}")
    
    print("\nハフマン符号:")
    for char, code in result['huffman_codes'].items():
        print(f"'{char}': {code}")
    
    print("\nエンコードされたテキスト:")
    print(result['encoded_text'])
    
    # 圧縮率の計算
    original_bits = len(text) * 8  # 各文字を8ビットと仮定
    compressed_bits = len(result['encoded_text'])
    compression_ratio = (1 - compressed_bits / original_bits) * 100
    print(f"\n圧縮率: {compression_ratio:.2f}%")

if __name__ == "__main__":
    main()