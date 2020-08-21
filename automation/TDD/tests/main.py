def nitro_salt(m):
    # 1000 : 10 = m : 
    try:
        m = int(m)
    except:
        m = 0
    return int(10 * m / 1000)