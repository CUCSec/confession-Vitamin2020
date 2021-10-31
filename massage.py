message = "437962657270756e6b20323037372c20486579204a7564792e"

# 初始化一个空字符串保存编码结果
confession = ""

for i in range( 0,( len(message)-1 ),2 ):
    # 将16进制转换为10进制，输出对应ASCII码
    dec_string = chr( int(message[i:i+2],base=16) )
    # 追加到结果字符串尾部
    confession += dec_string

print(confession)