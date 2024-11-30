

# Use of if ... elseif in Python

opt = input('Enter the choice,like square : 1 and rectangular : 2, so opt=')
# %%
if opt == '1':

    print('you selected to find the area for square shape')
    a = float(input('enter one side of square :'))

    print('your square area is:', a*a)
elif opt == '2':
    print('you selected to find the area for rectangale shape')
    a = int(input('enter one side of rec. :'))
    b = int(input('enter second side of rec. :'))
    print('your rectangle area is:', a*b)


# %%
