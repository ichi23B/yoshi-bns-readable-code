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
        self.words = {}


    def read_dict_file(self):
        """辞書ファイルを読み込み、keyがid・valueが単語の辞書を作成する

        Raises:
            FileNotFoundError: 辞書ファイルが見つからない

        Returns:
            {id: 単語}: id・単語辞書
        """
        self.words = {} # id・単語辞書初期化
        if self.dict_path.exists():
            with self.dict_path.open(encoding='utf-8') as f:
                word_row = f.readlines()
                for id, word in enumerate(word_row):
                    self.words[id] = word.rstrip()
            return self.words    
        else:
            raise FileNotFoundError()


    def print_words(self):
        """id・単語辞書を表示
        """
        for id, word in self.words.items():
            print(f'{id}: {word}')


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
