# 220724 19:22 ~ 중간에 다른거.. ~ 21:21

# 1try... 정확성 13/14 -> 실패(시간 초과) 

'''
from collections import deque

def solution(bridge_length, weight, truck_weights):
    CNT = 0
    
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    while True:
        
        if sum(bridge) == 0 and len(trucks) == 0:
            break;
            
        bridge.popleft();
        
        top = trucks.popleft() if len(trucks) > 0 else 0
        isOver = sum(bridge) + top > weight
        
        if isOver:
            # if len(bridge) > 0:
            bridge.append(0)
            trucks.appendleft(top);
        else :
            # if len(bridge) > 0:
            bridge.append(top)
        CNT += 1
        
        # print(CNT, bridge, trucks)            
            
    return CNT
'''


# 2 try SOL!. 원인 모르겠어서 질문 보고 풀음

from collections import deque

def solution(bridge_length, weight, truck_weights):
    CNT = 0
    
    bridge = deque([0] * bridge_length)
    bridgeSum = 0
    trucks = deque(truck_weights)
    
    while True:
        
        if bridgeSum == 0 and len(trucks) == 0:
            break;
            
        left = bridge.popleft();
        bridgeSum -= left
        
        top = trucks.popleft() if len(trucks) > 0 else 0
        isOver = bridgeSum + top > weight
        
        if isOver:
            bridge.append(0)
            trucks.appendleft(top);
        else :
            bridge.append(top)
            bridgeSum += top
        CNT += 1          
            
    return CNT