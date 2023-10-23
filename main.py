def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    female = int(input('Enter the number of female students:'))
    male = int(input('Enter the number of male students:'))
    total = female + male 
    f_per = female * 100 / total 
    m_per = male * 100 / total

    print(f'Female Percentage is: {f_per:.2f}')
    print(f'Male Percentage is: {m_per:.2f} ')

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_per, f_per


if __name__ == '__main__':
    main()
