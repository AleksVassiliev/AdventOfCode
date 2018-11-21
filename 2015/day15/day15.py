def main():
    A = (5, -1, 0, 0, 5)
    B = (-1, 3, 0, 0, 1)
    C = (0, -1, 4, 0, 6)
    D = (-1, 0, 0, 2, 8)

    max_score = 0
    cal_score = 0
    for a in range(1, 98):
        for b in range(98-a, 0, -1):
            for c in range(98-(a+b), 0, -1):
                d = 100 - (a + b + c)
                cap = a*A[0] + b*B[0] + c*C[0] + d*D[0]
                dur = a*A[1] + b*B[1] + c*C[1] + d*D[1]
                flv = a*A[2] + b*B[2] + c*C[2] + d*D[2]
                tex = a*A[3] + b*B[3] + c*C[3] + d*D[3]
                score = max(0, cap) * max(0, dur) * max(0, flv) * max(0, tex)
                max_score = max(score, max_score)

                cal = a*A[4] + b*B[4] + c*C[4] + d*D[4]
                if cal == 500:
                    cal_score = max(cal_score, score)
    
    print(max_score)
    print(cal_score)


if __name__ == "__main__":
    main()