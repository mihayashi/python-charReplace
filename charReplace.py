import os,sys, csv

#引数が３つであることを確認
if len(sys.argv)!=3:
    print("使い方：charReplace.py file1 file2")
    sys.exit()
#変換元のファイルが存在することを確認する
in_file = sys.argv[1]
if not os.path.exists(in_file):
    print("ファイルが存在しません")
    sys.exit()

#変換先のファイルが存在していた場合に上書きするかを確認する
out_file = sys.argv[2]
if os.path.exists(out_file):
    if input("上書きしますか？(y/n):")!="y":
        sys.exit()

#列番号
#i = 28
i = 26
findKeyword1 = "G Suiteユーザ メール"
findKeyword2 = "- Chat"
replaceWord1 = '"G Suiteユーザ メール"'
replaceWord2 = '"Chat"'


with open(in_file,"r", newline="", encoding="utf_16") as in_f:
    with open(out_file, "w", encoding="utf_8") as out_f:
        #reader = csv.reader(in_f)
        for line in in_f:
            #line = line.rstrip("\n")
            col = line.split("\t")
            print(col[i])


            if findKeyword1 in col[i]:
                col[i] = replaceWord1
            if findKeyword2 in col[i]:
                col[i] = replaceWord2

            # 変換後のタブ区切りの雛形を作り、変換処理した値を入れ込む
            row = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
                col[0],
                col[1],
                col[2],
                col[3],
                col[4],
                col[5],
                col[6],
                col[7],
                col[8],
                col[9],
                col[10],
                col[11],
                col[12],
                col[13],
                col[14],
                col[15],
                col[16],
                col[17],
                col[18],
                col[19],
                col[20],
                col[21],
                col[22],
                col[23],
                col[24],
                col[25],
                col[26],
                col[27],
                col[28],
                col[29],
                col[30],
                col[31],
                col[32],
                col[33],
                col[34],
                col[35],
                col[36],
                col[37],
                col[38],
                col[39],
                col[40],
                col[41],
                col[42],
                col[43],
                col[44],
                col[45],
                col[46],
                col[47],
                col[48],
                col[49],
                col[50],
                col[51],
                col[52],
                col[53]
                )
            row = row.rstrip("\n")
            # 書き出し用のファイルに出力
            out_f.write(row)

            #out_f.writecols(col)


