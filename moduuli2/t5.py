le = float(input('Montako leiviskää?\n'))
na = float(input('Montako naulaa?\n'))
lu = float(input('Montako luotia?\n'))

massa = (13.3*(lu + na*32 + le*32*20))

print(f'Näiden massa on {massa/1000:.0f}kg ja {massa%1000:.0f}mg')