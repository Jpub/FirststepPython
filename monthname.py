def getMonthName(month):
    month_name = {
        1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June",
        7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"
    }
    try:
        response = month_name[month]
    except:
        response = 'Please Input Month Between 1~12'
    return response

    if __name__ == '__main__':
        print('This is a Module. Please use after import')  