poet='''
나 보기가 역겨워 가실 때에는 말없이 고이 보내 드리오리다
영변에 약산 진달래꽃 아름 따다 가실 길에 뿌리오리다
가시는 걸음 걸음 놓인 그 꽃을 사뿐히 즈려 밟고 가시옵소서
나 보기가 역겨워 가실 때에는 죽어도 아니 눈물 흘리오리다
'''

# isalpha함수로 문자만 체크 
# {'char'. number} 타입으로 값 저장, 값이 있는 경우는 charDic[key] += 1
# 4회 이상만 출력

charDic = {}
for ch in poet :
    if ch.isalpha() :
        if(ch in charDic) :
            charDic[ch] += 1
        else :
            charDic[ch] = 1

for ch in charDic :
    if charDic[ch] > 3 :
        print(f'{ch} : {charDic[ch]}')