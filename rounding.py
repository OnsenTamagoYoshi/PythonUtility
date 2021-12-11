def rounding(num, round):
    # 切り捨て
    if num % round < round / 2:
        after_rounding = num - (num % round)
    # 切り上げ
    else:
        after_rounding = num - (num % round) + round
    
    return after_rounding