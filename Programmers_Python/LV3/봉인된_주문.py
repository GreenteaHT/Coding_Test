# https://school.programmers.co.kr/learn/courses/30/lessons/389481

spell_counts = [1]
cumulative_counts = [1]
alphabet_count = 1

for i in range(1, 11):
    alphabet_count *= 26
    spell_counts.append(alphabet_count)
    cumulative_counts.append(cumulative_counts[-1] + alphabet_count)

def solution(n, bans):
    bans = sorted([spell_to_idx(ban) for ban in bans])
    
    for ban in bans:
        if n < ban: break
        n += 1

    return idx_to_spell(n)


def spell_to_idx(spell):
    spell_length = len(spell)
    idx = 0
    
    for position, character in enumerate(spell):
        idx += (ord(character) - 96) * (spell_counts[spell_length - position  - 1])

    return idx


def idx_to_spell(idx):
    spell = ""
    position = 11
    
    while position >= 0:
        position -= 1
        if idx >= cumulative_counts[position]:
            idx -= cumulative_counts[position]
            break
    
    while position >= 0:
        share, idx = divmod(idx, spell_counts[position])
        spell += chr(share + 96 + 1)
        position -= 1
        
    return spell

# 입출력 예시
print(solution(30, ["d", "e", "bb", "aa", "ae"]))
print(solution(7388, ["gqk", "kdn", "jxj", "jxi", "fug", "jxg", "ewq", "len", "bhc"]))
