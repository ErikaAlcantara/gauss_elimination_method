from gauss_p_pivoting import Gauss_partial_pivoting

if __name__ =='__main__':

    gauss = Gauss_partial_pivoting(4,15,5,2,4,8,20,10,5,4,5,8)
    gauss.elimination()