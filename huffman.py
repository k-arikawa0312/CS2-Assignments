import heapq
from collections import defaultdict, Counter
import math

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_dict(text, use_percentage=False):
    """文字の出現頻度または出現割合を計算する"""
    freq_dict = Counter(text)
    
    if use_percentage:
        total = len(text)
        freq_dict = {char: (count / total) * 100 for char, count in freq_dict.items()}
    
    return freq_dict

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

def generate_huffman_codes(root, current_code='', huffman_codes=None, prefix='', prefix_length=0):
    """ハフマン符号を生成する（プレフィックス指定に対応）"""
    if huffman_codes is None:
        huffman_codes = {}
    
    if root is None:
        return huffman_codes
    
    if root.char is not None:
        # プレフィックスを追加
        final_code = prefix.zfill(prefix_length) + current_code
        huffman_codes[root.char] = final_code
    
    generate_huffman_codes(root.left, current_code + '0', huffman_codes, prefix, prefix_length)
    generate_huffman_codes(root.right, current_code + '1', huffman_codes, prefix, prefix_length)
    
    return huffman_codes

def huffman_encode(text, use_percentage=False, prefix_char=None, prefix_length=0):
    """テキストをハフマン符号化する"""
    # 文字の出現頻度または出現割合を計算
    freq_dict = build_frequency_dict(text, use_percentage)
    
    # ハフマン木を構築
    huffman_tree = build_huffman_tree(freq_dict)
    
    # ハフマン符号を生成（プレフィックス指定に対応）
    huffman_codes = generate_huffman_codes(
        huffman_tree, 
        prefix=prefix_char if prefix_char is not None else '', 
        prefix_length=prefix_length
    )
    
    # テキストをハフマン符号に変換
    encoded_text = ''.join(huffman_codes[char] for char in text)
    
    return {
        'encoded_text': encoded_text,
        'huffman_codes': huffman_codes,
        'frequency': freq_dict
    }

def main():
    while True:
        print("\n--- ハフマン符号化プログラム ---")
        print("1. 出現回数ベースでエンコード")
        print("2. 出現割合ベースでエンコード")
        print("3. 終了")
        
        choice = input("選択してください (1/2/3): ")
        
        if choice == '3':
            break
        
        text = input("エンコードするテキストを入力してください: ")
        
        # プレフィックスの設定
        use_prefix = input("特定の文字にプレフィックスを付けますか？ (y/n): ").lower() == 'y'
        prefix_char = None
        prefix_length = 0
        
        if use_prefix:
            prefix_char = input("プレフィックスを付けたい文字を入力: ")
            prefix_length = int(input("プレフィックスの長さを入力 (ビット数): "))
        
        try:
            # エンコード実行
            result = huffman_encode(
                text, 
                use_percentage=(choice == '2'),
                prefix_char=prefix_char,
                prefix_length=prefix_length
            )
            
            # 結果の表示
            print("\n文字の出現情報:")
            if choice == '2':
                for char, percentage in result['frequency'].items():
                    print(f"'{char}': {percentage:.2f}%")
            else:
                for char, count in result['frequency'].items():
                    print(f"'{char}': {count}")
            
            print("\nハフマン符号:")
            for char, code in sorted(result['huffman_codes'].items()):
                print(f"'{char}': {code}")
            
            print("\nエンコードされたテキスト:")
            print(result['encoded_text'])
            
            # 圧縮率の計算
            original_bits = len(text) * 8  # 各文字を8ビットと仮定
            compressed_bits = len(result['encoded_text'])
            compression_ratio = (1 - compressed_bits / original_bits) * 100
            print(f"\n圧縮率: {compression_ratio:.2f}%")
        
        except Exception as e:
            print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()