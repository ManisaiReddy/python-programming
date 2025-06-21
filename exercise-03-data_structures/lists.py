company_details = [101,"Wells Fargo", "Gachibowli",89000.756]
print(company_details)
print(len(company_details))
print(company_details[0])
print(company_details[-1])
print(company_details[:-1])
company_details.append('manisai')
company_details.pop(3)
print(company_details)
# print(company_details[100])
# company_details[100]="Reddy"
print(company_details)

matrixes = [[1,2,3],[3,4,5],[6,7,8]]
print(matrixes, type(matrixes))
print(matrixes[0][0])

col2 = [x[1] for x in matrixes]
print(col2)

print(list(range(-4,4,2)))
data = (sum(r) for r in matrixes)
next(data)
print(data)