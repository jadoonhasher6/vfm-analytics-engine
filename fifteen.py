transactions=[500,400,900,670,678,800]
high_value=[amt for amt in transactions if(amt>500)]
with open('high_value_report.txt','w') as report:
    for amt in high_value:
        report.write(str(amt)+'\n')

print('high value repotrt generated successfully')