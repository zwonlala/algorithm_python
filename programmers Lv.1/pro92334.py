# 220418  23:44 ~ 
# 220425 23:08 ~ (준희님 만나고 집 가면서) ~ 23:48 1 try
#        23:48 ~ 24:01 2 try(solve)


def solution(id_list, report, k):
    
    ansArr = [];
    ansDict = {};
    reportDict = {};
    
    for id in id_list:
        ansDict[id] = 0;
        reportDict[id] = [];
        
    # reportDict = new Dict();

    # for rItem of report:
    for rItem in report:
        # print(rItem);
        x, y = rItem.split()
        # print(x, y);
        # reportDict[x].add(y) if (x in reportDict) else reportDict[x] = []
        
        # if y in reportDict:
        reportDict[y].append(x)
        # else :
            # reportDict[y] = [];
            
        # if y in reportCntDict:
        # else :
            # reportCntDict[y] = 1;
    
    for reportKey, reportValue in reportDict.items():
        reportCnt = len(list(set(reportValue)));
        print(reportKey, reportValue, reportCnt);
        if (reportCnt >= k):
            for reporter in reportValue:
                ansDict[reporter] += 1
    
    for id in id_list:
        ansArr.append(ansDict[id]);
    return ansArr



#  2nd try

def solution(id_list, report, k):
    ansArr = [];
    ansDict = {};
    reportDict = {};
    
    for id in id_list:
        ansDict[id] = 0;
        reportDict[id] = [];

    for rItem in report:
        x, y = rItem.split()
        reportDict[y].append(x)
    
    for reportKey, reportValue in reportDict.items():
        distintValues = list(set(reportValue));
        reportCnt = len(distintValues);
        if (reportCnt >= k):
            for reporter in distintValues:
                ansDict[reporter] += 1
    
    for id in id_list:
        ansArr.append(ansDict[id]);
    return ansArr