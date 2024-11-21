import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def validate_percentages(percentages):
    """入力されたパーセンテージの合計が100%になるかチェック"""
    total = sum(percentages.values())
    if not (99.99 <= total <= 100.01):
        raise ValueError(f"パーセンテージの合計が100%になっていません。現在の合計: {total}%")

def build_frequency_dict(percentages):
    """カスタム文字とその頻度のディクショナリを作成"""
    return {char: freq for char, freq in percentages.items()}

def build_huffman_tree(freq_dict, fixed_codes=None):
    """
    ハフマン木を構築する
    fixed_codesは特定の文字に特定のコードを割り当てるための辞書
    """
    # 固定コードの文字を除外
    variable_chars = {char: freq for char, freq in freq_dict.items() 
                      if fixed_codes is None or char not in fixed_codes}
    
    # 固定コード以外の文字のノードを作成
    heap = [HuffmanNode(char, freq) for char, freq in variable_chars.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_huffman_codes(root, current_code='', huffman_codes=None, fixed_codes=None):
    """
    ハフマン符号を生成する
    特定の文字に固定のコードを割り当てるオプションを追加
    """
    if huffman_codes is None:
        huffman_codes = {}
    
    # 固定コードがある場合は、先に追加
    if fixed_codes:
        huffman_codes.update(fixed_codes)
    
    if root is None:
        return huffman_codes
    
    if root.char is not None and (fixed_codes is None or root.char not in fixed_codes):
        huffman_codes[root.char] = current_code
    
    generate_huffman_codes(root.left, current_code + '0', huffman_codes, fixed_codes)
    generate_huffman_codes(root.right, current_code + '1', huffman_codes, fixed_codes)
    
    return huffman_codes

def huffman_encode_from_percentages(percentages, fixed_codes=None):
    """出現割合とオプションの固定コードからハフマン符号を生成"""
    # 入力のバリデーション
    validate_percentages(percentages)
    
    # ハフマン木の構築
    huffman_tree = build_huffman_tree(percentages, fixed_codes)
    
    # ハフマン符号の生成
    huffman_codes = generate_huffman_codes(huffman_tree, fixed_codes=fixed_codes)
    
    return {
        'huffman_codes': huffman_codes,
        'frequencies': percentages
    }

def main():
    while True:
        print("\n--- カスタムハフマン符号化 ---")
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
                
                # 特定の文字に固定のコードを割り当てるかの確認
                use_fixed_codes = input("特定の文字に固定のコードを割り当てますか？ (y/n): ").lower() == 'y'
                fixed_codes = {}
                
                if use_fixed_codes:
                    while True:
                        fixed_char = input("固定コードを割り当てる文字を入力 (終了する場合は空白): ").strip()
                        if not fixed_char:
                            break
                        
                        if fixed_char not in percentages:
                            print(f"エラー: '{fixed_char}'は入力されたパーセンテージに存在しません。")
                            continue
                        
                        fixed_code = input(f"'{fixed_char}'の固定コードを入力: ").strip()
                        fixed_codes[fixed_char] = fixed_code
                
                # ハフマン符号化の実行
                result = huffman_encode_from_percentages(percentages, fixed_codes)
                
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