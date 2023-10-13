# coding: utf-8
import argparse
from pathlib import Path

class Dictionary():
    """辞書クラス
    """
    
    def __init__(self, dict_path:Path):
        """辞書クラスのイニシャライザ

        Args:
            dict_path (Path): 辞書ファイルのパスオブジェクト
        """
        self.dict_path = dict_path
        self.words = []


    def read_dict_file(self):
        """辞書ファイルを読み込み単語リストを作成する

        Raises:
            FileNotFoundError: 辞書ファイルが見つからない

        Returns:
            list[str]: 単語リスト
        """
        self.words = [] # 単語リスト初期化
        if self.dict_path.exists():
            with self.dict_path.open(encoding='utf-8') as f:
                self.words.append(f.read())
            return self.words    
        else:
            raise FileNotFoundError()


    def print_words(self):
        """単語リストを表示
        """
        for word in self.words:
            print(word)


if __name__ == '__main__':
    # 実行時パラメータの取得
    parser = argparse.ArgumentParser(description='辞書管理プログラム')
    parser.add_argument('--dict_path', type=str, help='辞書ファイルのパス', default='./dictionary-data.txt')
    args = parser.parse_args()
    dict_path = Path(args.dict_path)

    # 辞書オブジェクト作成
    dictionary = Dictionary(dict_path)
    dictionary.read_dict_file()
    dictionary.print_words()
