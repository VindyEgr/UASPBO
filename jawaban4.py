def get_umur():
    
    try:
        umur = int(input('Berapa umur anda?\n'))
    
    except:
        print('hah?')
    return umur

umur = get_umur()
print(f'terimakasih atas informasinya')
