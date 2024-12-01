import itertools

key = [83, 67, 78, 85]  # 'SCNU' in ASCII
r = [1] * 53 + [0] + [1] * 47 + [0] + [1] * 47 + [0] + [1] * 50
target_length = len(r)  # r数组的长度

# 生成s数组的前缀，与r的前缀进行部分匹配
def generate_s_prefix(flag, length):
    s = []
    for idx, char in enumerate(flag):
        v7 = key[idx % 4] ^ ord(char)
        while v7 > 0:
            s.append(1)
            v7 -= 1
            if len(s) >= length:  # 达到所需前缀长度就退出
                return s
        s.append(0)
        if len(s) >= length:
            return s
    return s

# 尝试找出符合r前缀的flag
def find_flag():
    prefix_len = 100  # 只匹配r的前100个元素作为前缀
    max_len = 20  # 假设flag的最大长度为20
    for length in range(1, max_len + 1):
        for possible_flag in itertools.product(range(32, 127), repeat=length):
            flag = ''.join(map(chr, possible_flag))
            s_prefix = generate_s_prefix(flag, prefix_len)
            if s_prefix == r[:prefix_len]:  # 前缀匹配时才生成完整s数组
                s = generate_s_prefix(flag, target_length)
                if s == r:
                    return flag
    return None

print("The flag is:", find_flag())
