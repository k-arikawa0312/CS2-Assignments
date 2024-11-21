import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def validate_percentages(percentages):
    """入力されたパーセンテージの合計が100%になるかチェック"""
    total = sum(percentages.values())
    if not (99.99 <= total <= 100.01):
        raise ValueError(f"パーセンテージの合計が100%になっていません。現在の合計: {total}%")

def build_huffman_tree(frequencies):
    """ハフマン木を構築する"""
    heap = [[weight, Node(char, weight)] for char, weight in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        new_node = Node(None, lo[0] + hi[0])
        new_node.left = lo[1]
        new_node.right = hi[1]
        heapq.heappush(heap, [new_node.freq, new_node])
    
    return heap[0][1]

def generate_codes(node, prefix="", codebook={}):
    """ハフマン符号を生成する"""
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

def adjust_code_for_char(codebook, char, desired_code):
    if char in codebook:
        codebook[char] = desired_code
        # Adjust other codes to ensure no conflicts
        # This part can be complex and may require rebalancing the tree
        # For simplicity, we assume no conflicts in this example
    return codebook

def huffman_encode_from_percentages(percentages):
    """出現割合からハフマン符号を生成"""
    # 入力のバリデーション
    validate_percentages(percentages)
    
    # ハフマン木の構築
    huffman_tree = build_huffman_tree(percentages)
    
    # ハフマン符号の生成
    huffman_codes = generate_codes(huffman_tree)
    
    return {
        'huffman_codes': huffman_codes,
        'frequencies': percentages
    }

def main():
    while True:
        print("\n--- パーセンテージからのハフマン符号化 ---")
        print("1. パーセンテージ入力")
        print("2. 終了")
        
        choice = input("選択してください (1/2): ")
        
        if choice == '2':
            break
        
        if choice == '1':
            try:
                # パーセンテージの入力
                percentages = {}
                while True:
                    char = input("文字を入力 (終了する場合は空白): ").strip()
                    if not char:
                        break
                    
                    try:
                        percentage = float(input(f"'{char}'のパーセンテージを入力: "))
                        percentages[char] = percentage
                    except ValueError:
                        print("数値を正確に入力してください。")
                
                # ハフマン符号化の実行
                result = huffman_encode_from_percentages(percentages)
                
                # 結果の表示
                print("\n入力されたパーセンテージ:")
                for char, percentage in result['frequencies'].items():
                    print(f"'{char}': {percentage}%")
                
                print("\nハフマン符号:")
                for char, code in sorted(result['huffman_codes'].items()):
                    print(f"'{char}': {code}")
            
            except ValueError as e:
                print(f"エラー: {e}")
        
        else:
            print("無効な選択です。1または2を選択してください。")

if __name__ == "__main__":
    main()