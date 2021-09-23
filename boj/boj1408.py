cur = list(map(int, input().split(':')))
start = list(map(int, input().split(":")))
# print(cur);
# print(start);
cur_time = cur[0]*3600 + cur[1]*60 + cur[2];
start_time = start[0]*3600 + start[1]*60 + start[2];
# print(cur_time);
# print(start_time);
diff = start_time - cur_time
diff = diff if diff > 0 else diff+24*3600
# print(diff);
print(str(diff//3600).zfill(2),":",str(diff//60%60).zfill(2),":",str(diff%60).zfill(2), sep='')