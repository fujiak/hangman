# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io. 
import random

def hangman(word): 
    ## 初期化
    wrong = 0 ## 誤った回数
    stages = ["", ## 出力画面 8行=8回まで間違えられる
              "________        ", 
              "|               ", 
              "|        |      ", 
              "|        0      ", 
              "|       /|\     ", 
              "|       / \     ", 
              "|               " 
              ] 
    rletters = list(word) ## 正解の単語を1文字ずつ配列に退避
    board = ["_"] * len(word) ## 伏字(正解した文字は後ほど設定)
    win = False ## 勝敗の状態
    ng_word=[] ## 間違ったアルファベットを退避
    print("Welcome to Hangman") ## タイトル画面
    ## メイン処理
    while wrong < len(stages) - 1:
        ## 入力画面 
        print("\nNG word = %s"%(" ".join(ng_word)))  ## これまで間違えた文字を出力 
        msg = "Guess a letter : "
        char = input(msg) ## 入力文字を退避 (文字列長が2文字以上の場合先頭1文字としたい)
        if char in rletters: ## 正解に含まれる文字の場合
            cind = rletters.index(char) 
            board[cind] = char ## 伏字→正解した文字
            rletters[cind] = '$'  ## 正解の単語のうち正解した文字は $ に変更 
        else:
            ng_word.append(char) ## 間違った字を NGに追加
            wrong += 1 ## 間違った回数を加算
        print((" ".join(board))) ## 伏字を出力
        ##e = wrong + 1 
        print("\n".join(stages[0:wrong+1])) ## ハングマン出力 
        if "_" not in board: ## 全部正解した
            print("\nYou win!") 
            ## print(" ".join(board)) 
            print(" ")
            win = True 
            break 
    if not win: ## 負け
        ## print("\n".join(stages[0:wrong])) 
        print("You lose! It was '{}'.".format(word)) 
        print(" ")

words=["food","apple","orange","rice","bread","egg","soup","meat","fish","mushroom",
       "family","mother","father","brother","sister","friend","animal","dog","cat",
	   "duck","elephant","bird","dinosaur","tiger","lion","giraffe","turtle","car",
	   "bicycle","train","bus","ambulance","tv","color","black","white","red","blue",
	   "yellow","green","purple","brown","pink","orange"]
hangman(words[random.randint(0,len(words)-1)])