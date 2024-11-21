class NotationConverter:
    def __init__(self):
        self.operators = {'+', '-', '*', '/', '^'}
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def is_operator(self, char):
        return char in self.operators

    def get_precedence(self, op):
        return self.precedence.get(op, 0)

    def infix_to_postfix(self, expression):
        """中置記法から後置記法への変換"""
        tokens = expression.split()
        stack = []
        result = []

        for token in tokens:
            if not self.is_operator(token) and token not in '()':
                result.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()  # '('を削除
            else:
                while (stack and stack[-1] != '(' and 
                       self.get_precedence(stack[-1]) >= self.get_precedence(token)):
                    result.append(stack.pop())
                stack.append(token)

        while stack:
            if stack[-1] != '(':
                result.append(stack.pop())
            else:
                stack.pop()

        return ' '.join(result)

    def infix_to_prefix(self, expression):
        """中置記法から前置記法への変換"""
        tokens = expression.split()
        # 式を逆順にし、括弧を入れ替える
        reversed_exp = []
        for token in reversed(tokens):
            if token == '(':
                reversed_exp.append(')')
            elif token == ')':
                reversed_exp.append('(')
            else:
                reversed_exp.append(token)
        
        # 後置記法に変換
        stack = []
        result = []
        
        for token in reversed_exp:
            if not self.is_operator(token) and token not in '()':
                result.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()  # '('を削除
            else:
                while (stack and stack[-1] != '(' and 
                    self.get_precedence(stack[-1]) > self.get_precedence(token)):
                    result.append(stack.pop())
                stack.append(token)

        while stack:
            if stack[-1] != '(':
                result.append(stack.pop())
            else:
                stack.pop()

        # 結果を逆順にして前置記法にする
        return ' '.join(reversed(result))

    def postfix_to_infix(self, expression):
        """後置記法から中置記法への変換"""
        tokens = expression.split()
        stack = []

        for token in tokens:
            if not self.is_operator(token):
                stack.append(token)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(f"( {operand1} {token} {operand2} )")

        return stack[0]

    def prefix_to_infix(self, expression):
        """前置記法から中置記法への変換"""
        tokens = expression.split()
        stack = []

        for token in reversed(tokens):
            if not self.is_operator(token):
                stack.append(token)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(f"( {operand1} {token} {operand2} )")

        return stack[0]

    def postfix_to_prefix(self, expression):
        """後置記法から前置記法への変換"""
        infix = self.postfix_to_infix(expression)
        return self.infix_to_prefix(infix)

    def prefix_to_postfix(self, expression):
        """前置記法から後置記法への変換"""
        infix = self.prefix_to_infix(expression)
        return self.infix_to_postfix(infix)

def main():
    converter = NotationConverter()
    
    while True:
        print("\n=== 記法変換プログラム ===")
        print("1: 中置記法からの変換")
        print("2: 前置記法からの変換")
        print("3: 後置記法からの変換")
        print("4: 終了")
        
        choice = input("\n選択してください (1-4): ")
        
        if choice == '4':
            print("プログラムを終了します。")
            break
            
        if choice not in ['1', '2', '3']:
            print("無効な選択です。1-4の数字を入力してください。")
            continue
            
        print("\n式を入力してください（要素はスペースで区切ってください）")
        print("例: A + B * C または + A * B C または A B C * +")
        expression = input("式: ")
        
        try:
            if choice == '1':  # 中置記法からの変換
                print("\n=== 変換結果 ===")
                print(f"前置記法: {converter.infix_to_prefix(expression)}")
                print(f"後置記法: {converter.infix_to_postfix(expression)}")
                
            elif choice == '2':  # 前置記法からの変換
                print("\n=== 変換結果 ===")
                print(f"中置記法: {converter.prefix_to_infix(expression)}")
                print(f"後置記法: {converter.prefix_to_postfix(expression)}")
                
            elif choice == '3':  # 後置記法からの変換
                print("\n=== 変換結果 ===")
                print(f"中置記法: {converter.postfix_to_infix(expression)}")
                print(f"前置記法: {converter.postfix_to_prefix(expression)}")
                
        except Exception as e:
            print(f"\nエラーが発生しました: {str(e)}")
            print("式の形式を確認してください。")

if __name__ == "__main__":
    main()
# 重要な注意点：

# 式の入力形式：

# すべての要素（演算子、オペランド）はスペースで区切る必要があります
# 正しい例: "A + B * C"
# 間違った例: "A+B*C"


# 使用可能な演算子：

# 基本演算子: +, -, *, /
# べき乗: ^


# 括弧の使用：

# 中置記法では括弧 ( ) が使用可能
# 括弧も前後にスペースが必要: "( A + B )"
# 中置記法: 2 + ( 5 - 3 ) * 2
# 前置記法: + 2 * - 5 3 2
# 後置記法: 2 5 3 - 2 * +